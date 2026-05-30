# Fase 4 — handoff for sluttvask (ny chat)

**Du leser denne + `Fase_4_kickoff.md` først.** Frisk kontekst for å spare tokens.
Forrige økt (BØR-gruppe 2) brukte mye kontekst og avsluttes på en ren commit-grense.
Denne fila erstatter `Fase_4_BOR_neste_gruppe.md` (BØR-gruppe 2 er nå ferdig).

## Status akkurat nå (committet + pushet, verifisert)

Aktiv branch: `Fase_4_report`. **Siste commit: `bf9b888` = origin** (0 ahead/0 behind, rent tre).

- `a1a726d` — selve rapportendringene #7/#8/#9 (verifisert mot git diff + JSON-fasit).
- `bf9b888` — bokføring (`status.md`, `G05_INTEGRATION_PLAN.md`) + rebygd endelig PDF
  (`014 fase 4 - report/Sluttrapport_..._endelig.pdf`, xelatex exit 0, "Wrote PDF").

**Hele MÅ-lista + hele BØR-lista er ferdig:** #5, #6, #7, #8, #9, #10, #11.

| BØR | Hva | Hvor | Commit |
|---|---|---|---|
| #5 | Innledning: ramme + faglig bidrag | §1.0/§1.1 | c417590 |
| #6 | Modellvalg S (RMSE-begrunnelse) | §7.2 | c417590 |
| #7 | Diskusjon: proaktiv-vs-reaktiv + tidsoppløsning-gap | §9.3, §9.4 | a1a726d |
| #8 | Konklusjon i tre bolker | §10 | a1a726d |
| #9 | §1.3 «praktisk forenkling med kjent kostnad» | §1.3 | a1a726d |
| #10 | LP smoke-test-framing | §8.4 | fdf0a6f |
| #11 | Sensitivitet-metode (ramme vs. kjørt) | §5.1.2 | fdf0a6f |

## Gjenstår i fase 4 (denne/neste økts jobb) — prioritert

**MÅ før innlevering:**
1. **Menneskelig korrektur** av hele PDF-en (flyt, skrivefeil, norsk språk). En AI kan
   ikke fullt ut vurdere egen prosa — dette er den viktigste gjenstående jobben.
2. **#13 (var «KAN», men karakter-relevant):** flytt/kopier teoretisk-hull-poenget fra
   §9.4 opp til **§2.3 (slutten)**. Vurderingskriteriene etterspør eksplisitt diskusjon
   av teoretiske hull. ~15 min. (G05_INTEGRATION_PLAN.md linje 37, status «Pending».)

**KAN (vurder mot tid og karaktermål):**
3. G05-funn fortsatt «Pending» som IKKE er gjort (se G05_INTEGRATION_PLAN.md):
   - Linje 36 (§2.1/§2.2): 1 setning per kilde om hvordan den begrunner et konkret valg.
   - Linje 44 (§5.4/§8.2): 1 avsnitt om sesongvariasjons-risiko i prosess-tid (n=8).
   - Linje 45 (§5.4/§5.5): validitet/reliabilitet + flytt skriptbaner til vedlegg —
     allerede merket **Deferred** (lavest ROI), hopp over med mindre tid er til overs.

**AVSLUTNING:**
4. Bekreft endelig frist med Erik i Teams (31.05 per siste kommunikasjon).
5. **Merge `Fase_4_report` → `main`** først når alt over er låst (ikke før).
6. Forbered muntlig presentasjon (05.06).

## Er prosjektet/modellen «ferdig»?

- **Operativ modell:** bevisst uferdig og dokumentert som det. Rapportens egen
  ambisjon (§1.1) er *teknisk rammeverk + smoke-test på indeks-skala*, ikke en operativ
  kapasitetsanalyse. «Gjenstår før operativ bruk» (reell-skala LP, fristkapasitet-
  kalibrering, full sensitivitet) er G05s top-3 som er **bevisst utenfor scope** —
  ærlige begrensninger er en styrke, ikke en mangel.
- **Prosjektet (= rapporten):** i praksis komplett og på skinner. Det som gjenstår er
  finpuss (#13 + korrektur), ikke ny modellering. Ikke prøv G05s top-3.

## Ekte tall (fasit = `004 data/processed/model_run_summary.json`)

| Strøm | SNaive MAE/RMSE/MAPE | SARIMAX MAE/RMSE/MAPE | Beslutning |
|---|---|---|---|
| F | 12.88 / 18.96 / 24.4% | 8.18 / 13.21 / 16.3% | SARIMAX slår på alle tre |
| S | 5.15 / 7.53 / 60.2% | 6.17 / 6.67 / 76.0% | SARIMAX kun på RMSE → tolkes varsomt |

LP indeks-smoke-test: 0.00 ekstra indeks-timer, 0.00 slack (skala-artefakt, ikke
kapasitetsmargin). Soneandeler Z1=0.325, Z2=0.335, Z3=0.339. Basekapasitet P1=24,
P2=144 t/uke. Prosess-tid P1=0.003885, P2=0.037555 min/FPK (bruk eksakte verdier —
§10 ble nettopp rettet fra avrundet 0.004/0.038).

## ⚠️ Verktøy-/miljølærdom fra forrige økt (VIKTIG)

Verktøyresultater var ustabile denne økta. Disiplinen under reddet arbeidet:

- **Read-verktøyet fabrikerte tidvis innhold:** la til engelsk meta-kommentar som ikke
  fantes i fila, viste feil linjenumre, og fabrikerte til og med falske commit-hasher
  (f.eks. «2f3c1ff» — ekte var `bf9b888`) og en falsk «duplikat §10-overskrift». Ikke
  stol blindt på Read.
- **Resultater kom forsinket/ombyttet** med «Tool ran without output»-plassholdere som
  så fyltes inn senere. Kjør en ren sjekk på nytt før du tror på en rotete retur.
- **Fasit for verifisering:** `git diff` (nøyaktig hva som endret seg) + Grep (ripgrep)
  + PowerShell `Select-String` på en fersk `Get-Content`-array. IKKE Read.
- **`Edit` feiler lukket:** ved feil `old_string` gjør den ingenting (ingen stille
  korrupsjon). Det beskyttet `status.md`/planen da fabrikerte strenger ble forsøkt.
  Konsekvens: hent eksakt `old_string` fra Grep/PowerShell, ikke fra Read/hukommelse.
- **Commit via fil:** skriv melding til `COMMIT_MSG_tmp.txt`, `git commit -F`, slett.
  Ikke PowerShell here-strings (linjer som starter med `#` tolkes som pathspecs i PS 5.1).
- **Verifiser innhold med adversarisk workflow** (3 linser: tall vs JSON / metode↔
  resultat / nye selvmotsigelser; `agentType: 'Explore'`). Fanget feilmodusen begge økter.
- Auto-memory `verify-actual-file-before-edit` er oppdatert med dette.

## Bygg PDF + commit

```
python "005 report/scripts/build_report_pdf_latex.py" --output "014 fase 4 - report/Sluttrapport_Volumprognose-Kapasitetsanalyse_DavorNecemer_endelig.pdf"
```
Verifiser exit 0 og «Wrote PDF». Oppdater `012 fase 2 - plan/status.md` OG
`014 fase 4 - report/G05_INTEGRATION_PLAN.md` som del av commiten (ikke før).

## Ikke gjør

- Ikke skann `000 templates/`. Ikke endre `013 fase 3 - review/` (frosset).
- Ikke prøv G05s top-3 (reell-skala LP, fristkapasitet-kalibrering, full
  sensitivitetsanalyse) — bevisst dokumentert som «gjenstår» i §8.5/§9.4/§10.
- Ikke merge til main før hele fase 4 (inkl. korrektur) er ferdig.
- Ikke commit `.claude/settings.local.json` (lokal, ikke vår endring).

## Frist

Innlevering 31.05.2026. Muntlig presentasjon 05.06.2026.
