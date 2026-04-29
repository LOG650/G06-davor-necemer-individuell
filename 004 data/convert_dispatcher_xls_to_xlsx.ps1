<#
.SYNOPSIS
Converts legacy dispatcher-action .xls attachments to .xlsx for the parser.

.DESCRIPTION
Older Outlook dispatcher exports are stored as Excel 97-2003 .xls files. The
capacity parser reads .xlsx directly, so this helper converts matching legacy
dispatcher files in-place next to the original .xls files. Raw data remains
under 004 data/raw/ and is ignored by Git.
#>

[CmdletBinding(SupportsShouldProcess = $true)]
param(
    [string]$InputDir = "004 data/raw/outlook_exports",
    [switch]$Force,
    [int]$Limit = 0
)

Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

$root = Resolve-Path -LiteralPath $InputDir
$files = Get-ChildItem -LiteralPath $root -File |
    Where-Object {
        $_.Extension -ieq ".xls" -and
        $_.Name -like "*dispatcher actions*"
    } |
    Sort-Object Name

if ($Limit -gt 0) {
    $files = @($files | Select-Object -First $Limit)
}

if ($files.Count -eq 0) {
    Write-Host "No legacy dispatcher .xls files found in '$InputDir'."
    exit 0
}

$excel = New-Object -ComObject Excel.Application
$excel.Visible = $false
$excel.DisplayAlerts = $false
$xlsxFormat = 51
$converted = 0
$skipped = 0
$failed = 0

try {
    foreach ($file in $files) {
        $target = [IO.Path]::ChangeExtension($file.FullName, ".xlsx")
        if ((Test-Path -LiteralPath $target) -and -not $Force) {
            $skipped++
            continue
        }

        if (-not $PSCmdlet.ShouldProcess($target, "Convert $($file.Name) to xlsx")) {
            continue
        }

        $workbook = $null
        try {
            $workbook = $excel.Workbooks.Open($file.FullName)
            $workbook.SaveAs($target, $xlsxFormat)
            $converted++
        } catch {
            $failed++
            Write-Warning "Failed to convert '$($file.Name)': $($_.Exception.Message)"
        } finally {
            if ($null -ne $workbook) {
                $workbook.Close($false)
            }
        }
    }
} finally {
    $excel.Quit()
}

Write-Host "Converted $converted file(s), skipped $skipped existing file(s), failed $failed file(s)."
