<#
.SYNOPSIS
Extracts Bakehuset production-list and dispatcher-action attachments from Outlook.

.DESCRIPTION
This script searches Outlook mail items for attachments from the project folders
`Utskrifter fra bakehuset` and `Dispatcher Actions/ Crates`. The expected
attachments are production-list PDFs such as `Utskrifter fra Bakehuset.pdf` and
dispatcher exports such as `Dispatcher actions (Production)` or `Crates`.

By default the script only previews matches. Add -Save to write the attachments
to disk.

The script does not parse mail bodies or attachment contents. It uses message
metadata only for filtering and output file naming.

.EXAMPLE
.\extract_outlook_attachments.ps1 -FolderPath 'Utskrifter fra bakehuset'

Preview matching production-list attachments for the last 30 days.

.EXAMPLE
.\extract_outlook_attachments.ps1 -FolderPath 'Dispatcher Actions/ Crates' -Since '2026-04-01' -Until '2026-04-30' -Save

Save matching dispatcher-action attachments for April 2026.

.EXAMPLE
.\extract_outlook_attachments.ps1 -FolderPath 'Utskrifter fra bakehuset' -Since '2026-04-27' -Until '2026-04-28' -Save

Save matching production-list attachments for one date.
#>

[CmdletBinding(SupportsShouldProcess = $true)]
param(
    [object]$Since = (Get-Date).AddDays(-30),
    [object]$Until = (Get-Date).AddDays(1),
    [string]$FolderPath = "",
    [switch]$IncludeSubfolders,
    [string]$SubjectContains = "",
    [string]$SenderContains = "",
    [string[]]$AttachmentPatterns = @(
        "*Dispatcher actions (Production)*",
        "*Dispatcher actions*.csv",
        "*Dispatcher actions*.xlsx",
        "*Crates*.csv",
        "*Crates*.xlsx",
        "*Utskrifter fra Bakehuset*.pdf",
        "*produksjonsliste*.pdf",
        "*produksjonsliste*.PDF"
    ),
    [string]$OutputDir = "004 data/raw/outlook_exports",
    [switch]$Save,
    [int]$Limit = 0
)

Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

function Convert-ToSafeFileName {
    param([Parameter(Mandatory = $true)][string]$Name)

    $invalid = [IO.Path]::GetInvalidFileNameChars()
    $safe = -join ($Name.ToCharArray() | ForEach-Object {
        if ($invalid -contains $_) { "_" } else { $_ }
    })
    return ($safe -replace "\s+", " ").Trim()
}

function Get-FolderDisplayPath {
    param([Parameter(Mandatory = $true)]$Folder)

    $parts = New-Object System.Collections.Generic.List[string]
    $current = $Folder
    while ($null -ne $current) {
        try {
            if ($current.Name) {
                $parts.Insert(0, [string]$current.Name)
            }
            $current = $current.Parent
        } catch {
            break
        }
    }
    return ($parts -join "\")
}

function Format-OutlookDate {
    param([Parameter(Mandatory = $true)][datetime]$Date)

    # Outlook Restrict parses dates using the local Outlook/Windows locale.
    # On this project machine, ISO and US-style dates are interpreted as dd/MM/yyyy.
    return $Date.ToString("dd/MM/yyyy HH:mm", [System.Globalization.CultureInfo]::InvariantCulture)
}

function Convert-ToDateTimeParameter {
    param([Parameter(Mandatory = $true)]$Value)

    if ($Value -is [datetime]) {
        return [datetime]$Value
    }

    $text = ([string]$Value).Trim()
    $formats = @(
        "yyyy-MM-dd HH:mm:ss",
        "yyyy-MM-dd HH:mm",
        "yyyy-MM-dd",
        "dd.MM.yyyy HH:mm:ss",
        "dd.MM.yyyy HH:mm",
        "dd.MM.yyyy",
        "dd.MM.yy HH:mm",
        "dd.MM.yy"
    )
    $culture = [System.Globalization.CultureInfo]::InvariantCulture
    $styles = [System.Globalization.DateTimeStyles]::AssumeLocal
    $parsed = [datetime]::MinValue

    foreach ($format in $formats) {
        if ([datetime]::TryParseExact($text, $format, $culture, $styles, [ref]$parsed)) {
            return $parsed
        }
    }

    return [datetime]::Parse($text, [System.Globalization.CultureInfo]::CurrentCulture)
}

function Get-ChildFolders {
    param([Parameter(Mandatory = $true)]$Folder)

    foreach ($child in $Folder.Folders) {
        $child
        Get-ChildFolders -Folder $child
    }
}

function Find-OutlookFolder {
    param(
        [Parameter(Mandatory = $true)]$Namespace,
        [Parameter(Mandatory = $true)][string]$Path
    )

    $normalized = ($Path -replace "/", "\").Trim("\")
    if (-not $normalized) {
        return $Namespace.GetDefaultFolder(6)
    }

    foreach ($store in $Namespace.Folders) {
        try {
            return $store.Folders.Item($Path)
        } catch {
            # Fall back to path/recursive matching below.
        }
    }

    foreach ($store in $Namespace.Folders) {
        $segments = $normalized -split "\\"
        if ($segments.Count -gt 1) {
            try {
                $folder = $store
                foreach ($segment in $segments) {
                    $folder = $folder.Folders.Item($segment)
                }
                return $folder
            } catch {
                # Fall back to recursive matching below.
            }
        }
    }

    foreach ($store in $Namespace.Folders) {
        $candidates = @($store) + @(Get-ChildFolders -Folder $store)
        foreach ($folder in $candidates) {
            $displayPath = Get-FolderDisplayPath -Folder $folder
            $displayPathNormalized = $displayPath -replace "/", "\"
            if (
                $displayPath.EndsWith($Path.Trim("\"), [StringComparison]::OrdinalIgnoreCase) -or
                $displayPathNormalized.EndsWith($normalized, [StringComparison]::OrdinalIgnoreCase)
            ) {
                return $folder
            }
        }
    }

    throw "Could not find Outlook folder ending with '$normalized'."
}

function Test-MatchesPattern {
    param(
        [Parameter(Mandatory = $true)][string]$Name,
        [Parameter(Mandatory = $true)][string[]]$Patterns
    )

    foreach ($pattern in $Patterns) {
        if ($Name -like $pattern) {
            return $true
        }
    }
    return $false
}

function Get-MailFolders {
    param(
        [Parameter(Mandatory = $true)]$RootFolder,
        [Parameter(Mandatory = $true)][bool]$Recursive
    )

    $RootFolder
    if ($Recursive) {
        Get-ChildFolders -Folder $RootFolder
    }
}

$outlook = New-Object -ComObject Outlook.Application
$namespace = $outlook.GetNamespace("MAPI")
$rootFolder = Find-OutlookFolder -Namespace $namespace -Path $FolderPath
$folders = @(Get-MailFolders -RootFolder $rootFolder -Recursive ([bool]$IncludeSubfolders))
$sinceDate = Convert-ToDateTimeParameter -Value $Since
$untilDate = Convert-ToDateTimeParameter -Value $Until

if ($Save) {
    New-Item -ItemType Directory -Force -Path $OutputDir | Out-Null
}

$matches = New-Object System.Collections.Generic.List[object]
$savedCount = 0

foreach ($folder in $folders) {
    $items = $folder.Items
    $items.Sort("[ReceivedTime]", $true)
    $filter = "[ReceivedTime] >= '$(Format-OutlookDate -Date $sinceDate)' AND [ReceivedTime] < '$(Format-OutlookDate -Date $untilDate)'"
    $dateItems = $items.Restrict($filter)

    foreach ($item in $dateItems) {
        if ($Limit -gt 0 -and $matches.Count -ge $Limit) {
            break
        }

        if (-not $item.ReceivedTime) {
            continue
        }
        if ($SubjectContains -and ([string]$item.Subject) -notlike "*$SubjectContains*") {
            continue
        }
        if ($SenderContains -and ([string]$item.SenderName) -notlike "*$SenderContains*") {
            continue
        }
        if ($item.Attachments.Count -lt 1) {
            continue
        }

        for ($i = 1; $i -le $item.Attachments.Count; $i++) {
            $attachment = $item.Attachments.Item($i)
            $attachmentName = [string]$attachment.FileName
            if (-not (Test-MatchesPattern -Name $attachmentName -Patterns $AttachmentPatterns)) {
                continue
            }

            $receivedStamp = ([datetime]$item.ReceivedTime).ToString("yyyyMMdd_HHmmss")
            $safeName = Convert-ToSafeFileName -Name $attachmentName
            $targetName = "$receivedStamp`_$safeName"
            $targetPath = Join-Path $OutputDir $targetName

            $match = [pscustomobject]@{
                Received = ([datetime]$item.ReceivedTime).ToString("yyyy-MM-dd HH:mm:ss")
                Folder = Get-FolderDisplayPath -Folder $folder
                Subject = [string]$item.Subject
                Attachment = $attachmentName
                TargetPath = $targetPath
            }
            $matches.Add($match)

            if ($Save -and $PSCmdlet.ShouldProcess($targetPath, "Save Outlook attachment")) {
                $attachment.SaveAsFile((Resolve-Path -LiteralPath $OutputDir).Path + "\" + $targetName)
                $savedCount++
            }
        }
    }
}

if ($matches.Count -eq 0) {
    Write-Host "No matching attachments found."
    Write-Host "Searched from $($sinceDate.ToString('yyyy-MM-dd')) to $($untilDate.ToString('yyyy-MM-dd')) in '$((Get-FolderDisplayPath -Folder $rootFolder))'."
    exit 0
}

$matches | Format-Table Received, Folder, Attachment, TargetPath -AutoSize

if ($Save) {
    Write-Host "Saved $savedCount attachment(s) to '$OutputDir'."
} else {
    Write-Host "Preview only. Re-run with -Save to write these attachments to disk."
}
