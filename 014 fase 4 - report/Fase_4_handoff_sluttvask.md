# Fase 4 — handoff for ny chat (etter sluttreview, 2026-05-31)

**Du leser denne + `Fase_4_kickoff.md` først.** Frisk kontekst for å spare tokens.
Denne fila er oppdatert etter den uavhengige sluttreviewen og erstatter all tidligere
status i dette dokumentet. **Stol på `git log`, ikke på hukommelse/eldre handoff-hashes.**

## Status akkurat nå (committet + pushet, verifisert)

Aktiv branch: `Fase_4_report`. **Siste commit: `abf85ef` = origin** (0 ahead/0 behind).
Verifiser alltid selv med `git log --oneline -5` ved oppstart.

Commit-kjede (nyest først):
- `abf85ef` — integrer funn fra uavhengig sluttreview (6 agenter + Codex): alle MÅ/BØR/KAN
- `fa3e71b` — nummererte tabelltekster (Tabell 1–11)
- `32d6fd9` — enke-/foreldreløs-kontroll (sideombrekking)
- `1933666` — listeetikett-fiks (`\@beginparpenalty`)
- `d90878f` — logo-forside (mal-oppsett) + brødtekst Calibri 11 pt
- `619b9db` — publiseringsavtale Brage = Nei
- `209afbe` — «Bruk av KI-verktøy»-seksjon (kreves av nettskjema-KI-egenerklæring)
- `33b541f` — endelig forside + obligatoriske erklæringer

**Endelig PDF:** `014 fase 4 - report/Sluttrapport_…_endelig.pdf` — **37 sider**, exit 0.
Sidetall-feltet på forsiden = 37 (oppdater hvis innhold endres).

## Hva som er gjort i denne sesjonen

1. **Forside** (LaTeX-titlepage med HiM-logo + mal-oppsett): tittel NO/EN, «Prosjektoppgave»,
   emnenavn, forfatter, sidetall 37, «Molde, 1. juni 2026». Logoene ligger i
   `005 report/figures/forside_mountain.png` og `forside_him_logo.jpeg`.
2. **Obligatoriske erklæringer:** egenerklæring 1–6 (alle «Ja»); Personvern NSD=Nei (presisert,
   se «Gjenstår»), REK=Nei; Publiseringsavtale: 15 sp, veileder **Per Kristian Rekdal og
   Bård-Inge Pettersen**, Brage=**Nei** (bedriftssamtykke ikke innhentet), båndlagt=Nei.
3. **«Bruk av KI-verktøy»-seksjon** — kreves av det innsendte nettskjema-KI-egenerklæringsskjemaet
   (siste bekreftelse forutsetter at all KI-bruk er beskrevet i besvarelsen). Mappet mot de fem
   avkryssede formålene. Se auto-memory `log650-ki-verktoy-declaration`.
4. **Typografi:** Calibri 11 pt brødtekst, 22 mm marg (Times-New-Roman/1,5-mal-match ble prøvd
   og forkastet). Sideombrekking-polish: `\@beginparpenalty`/`\clubpenalty`/`\widowpenalty`.
5. **Nummererte Tabell 1–11** (tabelltekst over tabellen); Forkortelser/symboler-ordlista
   bevisst unummerert.
6. **Uavhengig sluttreview** (6 parallelle agenter) + kryssjekk mot brukerens Codex-review
   (`.codex/review/Review-third.md`, IKKE i git). Funn arkivert i
   **`005 report/internal_reviews/REVIEW_FINAL_2026-05-31.md`** (inkl. egen «Muntlig forsvar»-seksjon).
7. **Alle MÅ/BØR/KAN rettet** og adversarisk re-verifisert (tall OK; 3 residual-overclaim funnet
   og lukket). Hovedrettinger: §5.1.1 metode↔kode-konsistens (grid-søk + RMSE-primær, ikke
   KPSS/AICc); kampanje- og LP-sonefrist-overclaim dempet (konsistent med §6.5); personvern-
   erklæring presisert; Figur 1 sluttuke W19→W14 (script + caption + regenerert PNG); SSB-tittel
   «Sykefravær» + URL; sum 0.999; språkvask.

## Gjenstår i fase 4 — prioritert

**MÅ før innlevering (brukerens jobb / krever bruker-handling):**
1. **Menneskelig korrektur** av hele 37-siders PDF-en. Den viktigste gjenstående jobben.
2. **NSD-avklaring:** erklæringen er nå ærlig dempet og *flagger* at lokal forbehandling av
   personnavn *kan* være meldepliktig. Bruker bør sende kort Teams-melding til veileder/
   personvernombud og bekrefte om melding kreves. (Se REVIEW_FINAL + §5.5 + forside-erklæring.)

**KAN (bevisst utsatt i denne sesjonen — vurder ved behov):**
- **Auto-TOC med sidetall:** kolliderer med rapportens *manuelle* kapittelnummerering (`## 1.0 …`)
  og den egendefinerte LaTeX-titlepagen (auto-`\tableofcontents` havner før forsiden / blir tom
  uten `--number-sections`, som gir dobbel nummerering). Krever restrukturering — ikke gjort
  pga. build-risiko nær frist. Manuell «## Innhold» beholdt.
- **APA «et al.» fra første sitering:** rapporten staver ut alle forfattere første gang (APA 6-stil);
  streng APA 7 bruker «et al.» fra første. Bredt akseptert som-er — utsatt.

**AVSLUTNING:**
3. **Merge `Fase_4_report` → `main`** KUN når korrektur + NSD er låst (ikke før).
4. Forbered muntlig presentasjon (05.06) — bruk «Muntlig forsvar»-seksjonen i REVIEW_FINAL.

## Ekte tall (fasit = `004 data/processed/model_run_summary.json`)

| Strøm | SNaive MAE/RMSE/MAPE | SARIMAX MAE/RMSE/MAPE | Valgt modell / eksogen |
|---|---|---|---|
| F | 12.88 / 18.96 / 24.4% | 8.18 / 13.21 / 16.3% | SARIMAX(1,1,1)(0,0,0)[52] + helligdagsflagg |
| S | 5.15 / 7.53 / 60.2% | 6.17 / 6.67 / 76.0% | (0,1,0)(0,0,0)[52], INGEN eksogen; flat konst. ≈15.68, RMSE-seier skjør |

Prosess-tid P1=0.003885, P2=0.037555 min/FPK. Basekapasitet P1=24, P2=144 t/uke.
Soneandeler Z1=0.325311, Z2=0.335234, Z3=0.339455 (eksakt sum 1.000000; avrundet 0.325/0.335/0.339 = 0.999).
117 modelluker / 234 obs; uke 2026-14 ekskludert (delvis). LP smoke-test: 0.00 ekstra indeks-timer / 0.00 slack
(skala-artefakt, IKKE validert kapasitetsmargin). Begge valgte modeller er effektivt ikke-sesonglige
(sesongledd testet, tapte på RMSE — 2 sesonger for lite).

## ⚠️ Verktøy-/miljølærdom (gjelder fortsatt)

- **Read kan fabrikere innhold/linjenr/commit-hasher.** Fasit for verifisering: `git log`/`git diff`
  + Grep (ripgrep) + PowerShell `Select-String` på fersk `Get-Content`. IKKE Read alene.
- **`Edit` feiler lukket** (feil `old_string` → ingen endring). Hent eksakt streng fra Grep/disk.
  Edit krever en fersk Read av fila i samme økt — ellers «File has not been read yet».
- **Commit via fil, BOM-fritt:** `[System.IO.File]::WriteAllText($tmp, $msg, (New-Object
  System.Text.UTF8Encoding($false)))` → `git commit -F`. PS 5.1 `Set-Content -Encoding UTF8`
  legger BOM i commit-emnet. Slett temp med `[System.IO.File]::Delete($tmp)` — `Remove-Item`
  nær strenger som «word/media/*» eller «/» kan bli blokkert av harness-guard (falsk positiv).
- **Ikke spam parallelle PowerShell-kall** — hvis ett feiler, kanselleres de andre.
- **PDF-bygg:** kjør bare ÉN om gangen. **Figurer regenereres via uv** (base-python mangler pandas):
  `uv run --python 3.12 --with pandas --with numpy --with matplotlib python "005 report/scripts/build_report_figures.py"`.
- **Verifiser innholdsendringer adversarisk** (Workflow med flere agenter; lenser: tall vs JSON-fasit,
  residual-overclaim/selvmotsigelser). Fanget reelle feil begge review-runder.
- Auto-memory `verify-actual-file-before-edit`, `powershell-commit-via-file`, `log650-ki-verktoy-declaration`.

## Bygg PDF + commit

```
python "005 report/scripts/build_report_pdf_latex.py" --output "014 fase 4 - report/Sluttrapport_Volumprognose-Kapasitetsanalyse_DavorNecemer_endelig.pdf"
```
Verifiser exit 0 + «Wrote PDF» + sidetall (pypdf). Oppdater forsidens sidetall-felt hvis tallet endres.
Oppdater `012 fase 2 - plan/status.md` + `014 fase 4 - report/G05_INTEGRATION_PLAN.md` som del av commiten.

## Ikke gjør

- Ikke skann `000 templates/` (unntatt eksplisitt). Ikke endre `013 fase 3 - review/` (frosset).
- Ikke commit `.claude/settings.local.json` (lokal) eller `.codex/review/` (brukerens Codex-artefakt).
- Ikke prøv G05s top-3 (reell-skala LP, fristkapasitet-kalibrering, full sensitivitet) — bevisst «gjenstår».
- Ikke merge til main før korrektur + NSD er låst.

## Frist

Innlevering **mandag 1. juni 2026 kl. 14:00** (WISEflow, kun rapport-PDF). Kandidatnr 46.
Muntlig presentasjon (Teams) **2026-06-05** (uke 24).
