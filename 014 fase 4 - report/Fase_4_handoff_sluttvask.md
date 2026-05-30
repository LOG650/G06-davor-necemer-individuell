# Fase 4 — handoff for sluttvask (ny chat)

**Du leser denne + `Fase_4_kickoff.md` først.** Frisk kontekst for å spare tokens.
Forrige økter avsluttes på rene commit-grenser. Denne fila erstatter
`Fase_4_BOR_neste_gruppe.md` (BØR-gruppe 2 er ferdig) og er oppdatert etter #13.

## Status akkurat nå (committet + pushet, verifisert)

Aktiv branch: `Fase_4_report`. **Siste commit: `3f2a9c1` = origin** (0 ahead/0 behind).
Verifiser alltid selv med `git log --oneline -5` ved oppstart.

- `a1a726d` — rapportendringene #7/#8/#9.
- `bf9b888` — bokføring + rebygd endelig PDF for #7/#8/#9.
- `95e30f4` — forrige versjon av denne handoff-fila.
- `3f2a9c1` — **#13 teoretisk hull (§2.3) + §9.4 heading-fix + bokføring + PDF**.

**Ferdig: hele MÅ-lista + hele BØR-lista + #13.** Funn #5, #6, #7, #8, #9, #10, #11, #13.

| BØR | Hva | Hvor | Commit |
|---|---|---|---|
| #5 | Innledning: ramme + faglig bidrag | §1.0/§1.1 | c417590 |
| #6 | Modellvalg S (RMSE-begrunnelse) | §7.2 | c417590 |
| #7 | Diskusjon: proaktiv-vs-reaktiv + tidsoppløsning-gap | §9.3, §9.4 | a1a726d |
| #8 | Konklusjon i tre bolker | §10 | a1a726d |
| #9 | §1.3 «praktisk forenkling med kjent kostnad» | §1.3 | a1a726d |
| #10 | LP smoke-test-framing | §8.4 | fdf0a6f |
| #11 | Sensitivitet-metode (ramme vs. kjørt) | §5.1.2 | fdf0a6f |
| #13 | Teoretisk hull eksplisitt + §9.4-callback + heading/TOC | §2.3, §9.4 | 3f2a9c1 |

## Gjenstår i fase 4 — prioritert

**MÅ før innlevering:**
1. **Menneskelig korrektur** av hele PDF-en (flyt, skrivefeil, norsk språk). En AI kan
   ikke fullt ut vurdere egen prosa — dette er den viktigste gjenstående jobben.

**KAN (vurder mot tid og karaktermål) — fortsatt «Pending»/«Deferred» i G05_INTEGRATION_PLAN.md:**
- Linje 36 (§2.1/§2.2): 1 setning per kilde om hvordan den begrunner et konkret valg.
- Linje 44 (§5.4/§8.2): 1 avsnitt om sesongvariasjons-risiko i prosess-tid (n=8).
- Linje 45 (§5.4/§5.5): validitet/reliabilitet + flytt skriptbaner til vedlegg —
  allerede **Deferred** (lavest ROI), hopp over med mindre tid er til overs.
- Linje 115 status.md (§8): reell sensitivitetsanalyse på indeks-skala — bevisst utenfor
  scope (se «Ikke gjør» under), ikke prøv i én økt.

**AVSLUTNING:**
2. Frist bekreftet utvidet til mandag 1. juni 2026 kl. 14:00.
3. **Merge `Fase_4_report` → `main`** først når korrektur er låst (ikke før).
4. Forbered muntlig presentasjon (05.06).

## Er prosjektet/modellen «ferdig»?

- **Operativ modell:** bevisst uferdig og dokumentert som det. Rapportens egen ambisjon
  (§1.1) er *teknisk rammeverk + smoke-test på indeks-skala*, ikke en operativ
  kapasitetsanalyse i mann-timer. «Gjenstår før operativ bruk» (reell-skala LP,
  fristkapasitet-kalibrering, full sensitivitet) er G05s top-3 som er **bevisst utenfor
  scope** — ærlige begrensninger er en styrke, ikke en mangel.
- **Prosjektet (= rapporten):** i praksis komplett. Det som gjenstår er korrektur, ikke
  ny modellering. Ikke prøv G05s top-3.

## Ekte tall (fasit = `004 data/processed/model_run_summary.json`)

| Strøm | SNaive MAE/RMSE/MAPE | SARIMAX MAE/RMSE/MAPE | Beslutning |
|---|---|---|---|
| F | 12.88 / 18.96 / 24.4% | 8.18 / 13.21 / 16.3% | SARIMAX slår på alle tre |
| S | 5.15 / 7.53 / 60.2% | 6.17 / 6.67 / 76.0% | SARIMAX kun på RMSE → tolkes varsomt |

LP indeks-smoke-test: 0.00 ekstra indeks-timer, 0.00 slack (skala-artefakt, ikke
kapasitetsmargin). Soneandeler Z1=0.325, Z2=0.335, Z3=0.339. Basekapasitet P1=24,
P2=144 t/uke. Prosess-tid P1=0.003885, P2=0.037555 min/FPK (bruk eksakte verdier).

## ⚠️ Verktøy-/miljølærdom (VIKTIG — gjelder fortsatt)

Verktøyresultater var ustabile begge BØR-økter. Disiplinen under reddet arbeidet:

- **Read-verktøyet fabrikerte tidvis innhold:** engelsk meta-kommentar som ikke fantes
  i fila, feil linjenumre, og til og med falske commit-hasher (f.eks. «2f3c1ff»,
  «2f3c1ff» — ekte hasher kommer fra `git log`). Ikke stol blindt på Read.
- **Resultater kom forsinket/ombyttet/svelget** (tomme returer, «Tool ran without
  output»-plassholdere fylt inn senere, og leakede fragmenter). Kjør en ren sjekk på
  nytt før du tror på en rotete retur; ikke spam parallelle kommandoer da de avbrytes.
- **Fasit for verifisering:** `git diff`/`git log` + Grep (ripgrep) + PowerShell
  `Select-String` på fersk `Get-Content`-array. IKKE Read.
- **`Edit` feiler lukket:** feil `old_string` → ingen endring (ingen stille korrupsjon).
  Brukt som diagnostikk: re-apply en allerede-gjort Edit → «String not found» bekrefter
  at den landet. Hent `old_string` fra Grep/PowerShell/diff, ikke fra Read/hukommelse.
- **Multi-line markdown:** oppdater forward-looking dokumenter med full `Write`-rewrite,
  ikke fragile fler-linjes exact-string-Edits.
- **Commit via fil:** skriv melding til `COMMIT_MSG_tmp.txt`, `git commit -F`, slett.
  Ikke PowerShell here-strings (linjer med `#` tolkes som pathspecs i PS 5.1).
- **Verifiser innhold med adversarisk workflow** (linser: tall/kilder vs JSON+bibliografi,
  metode↔resultat/kryssref, nye selvmotsigelser; `agentType: 'Explore'`). Fanget reelle
  feilmoduser begge økter (bl.a. §9.4 heading/TOC-avvik ved #13).
- Auto-memory `verify-actual-file-before-edit` er oppdatert med dette.

## Bygg PDF + commit

```
python "005 report/scripts/build_report_pdf_latex.py" --output "014 fase 4 - report/Sluttrapport_Volumprognose-Kapasitetsanalyse_DavorNecemer_endelig.pdf"
```
Verifiser exit 0 og «Wrote PDF». Kjør bare ÉN PDF-build om gangen (samtidige builds mot
samme fil kan låse/korruptere). Oppdater `012 fase 2 - plan/status.md` OG
`014 fase 4 - report/G05_INTEGRATION_PLAN.md` som del av commiten (ikke før).

## Ikke gjør

- Ikke skann `000 templates/`. Ikke endre `013 fase 3 - review/` (frosset).
- Ikke prøv G05s top-3 (reell-skala LP, fristkapasitet-kalibrering, full
  sensitivitetsanalyse) — bevisst dokumentert som «gjenstår» i §8.5/§9.4/§10.
- Ikke merge til main før korrektur er ferdig.
- Ikke commit `.claude/settings.local.json` (lokal, ikke vår endring).

## Frist

Innlevering **mandag 1. juni 2026 kl. 14:00** (utvidet fra 31.05). Muntlig presentasjon 05.06.2026.
