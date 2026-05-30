# Fase 4 — kickoff for ny chat-sesjon

**Du leser dette først.** Dette dokumentet gir all kontekst en frisk Claude-sesjon trenger for å fortsette fase 4-arbeidet uten å lese hele kurs-historikken.

## Prosjekt

- **Tittel:** Integrert volumprognose og kapasitetsanalyse (LOG650 individuell, HiMolde)
- **Student:** Davor Necemer
- **Kanonisk rapport:** [`005 report/Sluttrapport_Volumprognose-Kapasitetsanalyse_DavorNecemer.md`](../005%20report/Sluttrapport_Volumprognose-Kapasitetsanalyse_DavorNecemer.md)
- **Frist sluttrapport:** **2026-05-31** (Eriks senere kommunikasjon; original 29.05 ble utvidet)
- **Eksamensform etter innlevering:** muntlig presentasjon 2026-06-05

## Status akkurat nå (2026-05-30)

- Aktiv branch: **`Fase_4_report`** (skapt fra `main` 30.05; ingen rapport-innhold endret ennå)
- Fase 1, 2, 3 er fullført. Erik bekreftet "bestått arbeidskravet" 30.05.
- Hovedutkastet var klart innen Eriks frist 30.04. Direkte peer-to-peer-utveksling med G05 (Birgitte og Vera) skjedde 04.05–08.05: Davor sendte hovedutkast 04.05, leverte review til G05 06.05, mottok G05s review 08.05.
- G05s tilbakemelding (dokumentet internt datert 2026-05-07, mottatt 2026-05-08) inneholder 19 funn; **denne sesjonens jobb er å integrere dem innen 2026-05-31.**

## Filer å lese FØRST (i denne rekkefølgen)

1. **Denne fila** (kontekst)
2. [`014 fase 4 - report/G05_INTEGRATION_PLAN.md`](G05_INTEGRATION_PLAN.md) — strukturert plan med 19 G05-funn, lokasjon i rapport, tiltak, tidsestimat, status. Realisme-scoping helt øverst.
3. [`012 fase 2 - plan/status.md`](../012%20fase%202%20-%20plan/status.md) — overordnet status, prioritert tiltaksliste, restart-checkpoint
4. [`005 report/Sluttrapport_Volumprognose-Kapasitetsanalyse_DavorNecemer.md`](../005%20report/Sluttrapport_Volumprognose-Kapasitetsanalyse_DavorNecemer.md) — rapporten som skal endres

## Filer du IKKE skal lese

- **`000 templates/`** — store forelesnings-transcripts (auto-memory-regel `feedback_templates.md` sier hopp over). Bare les hvis brukeren eksplisitt ber om det.
- **`013 fase 3 - review/Peer-review_G06_G05.md` og `.pdf`** — vår review av G05. Bare *G05s* review av oss er relevant (peer review … G05_G06.md), og den er allerede oppsummert i G05_INTEGRATION_PLAN.md.
- **`004 data/raw/`, `004 data/processed/`, `004 data/weekly_volume.csv`** — sensitive lokale data, ikke i Git.

## Arbeidsmål for denne sesjonen

Implementere "MÅ"-listen (≈2 t) og deretter "BØR"-listen (≈2.5 t) fra G05_INTEGRATION_PLAN.md. Hold deg fra "Ikke realistisk innen frist"-listen (G05s top-3 om reell-skala LP, fristkapasitet, full sensitivitetsanalyse) — i stedet, erkjenn eksplisitt at de gjenstår i §10.

## Build-pipeline (PDF)

Når rapport-endringer er gjort, regenerer PDF med:

```
python "005 report/scripts/build_report_pdf_latex.py"
```

Den bruker Pandoc 3.9 (winget user-scope) + xelatex (TinyTeX), bygger til `013 fase 3 - review/Sluttrapport_…_DavorNecemer.pdf`. **For fase 4-sluttleveranse bør du endre `--output` i skriptet til `014 fase 4 - report/Sluttrapport_…_endelig.pdf`** for ikke å overskrive peer-review-versjonen.

Fallback: [`005 report/scripts/build_report_pdf.py`](../005%20report/scripts/build_report_pdf.py) (Edge headless + MathJax, dårligere formelrendering).

## Konvensjoner

- **Språk:** Norsk bokmål i rapport. Tekniske termer (SARIMAX, LP) er OK på engelsk.
- **Datafiler:** Publiserbart bruker indeks (2024-snitt per varestrøm = 100). Reelle FPK er ikke i Git.
- **Git:**
  - Branch: `Fase_4_report`
  - Commit hyppig med klare meldinger ("fase4: …")
  - Push fortløpende — branchen er allerede på origin etter denne kickoff-commit
  - IKKE merge til main før hele fase 4 er ferdig
- **Auto-memory:** Skip `000 templates/` med mindre eksplisitt bedt om. Brukeren er senior student med god kontroll, gi konsise svar.

## Hvordan ny chat starter

Anbefalt åpningsmelding fra brukeren til ny Claude-sesjon:

```
Les 014 fase 4 - report/Fase_4_kickoff.md først for kontekst.
Deretter 014 fase 4 - report/G05_INTEGRATION_PLAN.md. Vi skal starte
på "MÅ gjøre"-listen — begynn med APA-fix i §11 bibliografi.
```

## Hva som er gjort i denne (forrige) sesjonen

- Mottatt og lest G05s peer-review
- Strukturert integrasjonsplan med 19 funn + realisme-scoping skrevet til [`G05_INTEGRATION_PLAN.md`](G05_INTEGRATION_PLAN.md)
- `status.md` oppdatert med 2026-05-30-dato, fase 3 fullført, fase 4 in-progress, nye prioriterte tiltak basert på G05
- Denne hand-off-fila opprettet
- Branch `Fase_4_report` opprettet, pushet til origin

**Ingenting i `005 report/Sluttrapport_…_DavorNecemer.md` er endret av meg ennå.** Det arbeidet starter i din sesjon.

## Quick reference — viktige filer

| Sti | Hensikt |
|---|---|
| `005 report/Sluttrapport_…_DavorNecemer.md` | Kanonisk rapport (endres) |
| `005 report/scripts/build_report_pdf_latex.py` | PDF-build (pandoc+xelatex) |
| `005 report/internal_reviews/` | AI-baserte selv-reviews fra fase 3 (les for ekstra kontekst) |
| `014 fase 4 - report/G05_INTEGRATION_PLAN.md` | 19 G05-funn med tiltak |
| `012 fase 2 - plan/status.md` | Overordnet status |
| `013 fase 3 - review/peer review … G05_G06.md` | G05s originale review (kilde) |
| `004 data/processed/model_run_summary.json` | SARIMAX/LP-resultatfasit |
| `003 references/DOWNLOAD_STATUS.md` | Referanse-verifikasjon |

## Ved tvil

- Om frist: 31.05.2026 per Eriks senere kommunikasjon. Hvis brukeren tviler, foreslå å bekrefte med Erik i Teams.
- Om scope: hold deg til G05_INTEGRATION_PLAN.md prioritering. Ikke prøv top-3-gjenstår-listen i en enkelt sesjon.
- Om PDF ser rart ut: bygg på nytt med xelatex-pipelinen, ikke Edge.
