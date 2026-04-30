# Prosjektstatus - Integrert volumprognose og kapasitetsanalyse

**Dato:** 2026-04-30
**Prosjektleder:** Davor Necemer
**Dager til innlevering:** 29 (2026-05-29)

---

## Sammendrag

| Fase | Status |
|------|--------|
| Fase 1: Initiering | Fullfort |
| Fase 2: Prosjektplan | Fullfort |
| Fase 3: Gjennomforing | Hovedutkast klart for peer-to-peer review |
| Fase 4: Sluttrapport | Pabegynt; finpuss etter peer review gjenstar |

Prosjektet har tatt igjen den viktigste fase 3-risikoen. Hovedutkastet av
rapporten er na lesbart nok til at en annen student/gruppe kan gi skriftlig
peer-to-peer review. Rapporten inneholder sammendrag/abstract, problemstilling,
teori/litteratur, case, metode, modellering, analyse, resultater, diskusjon,
konklusjon, bibliografi og vedleggsoversikt.

Det er ogsa gjennomfort en teknisk minimumskjoring: SNaive-baseline,
SARIMAX/ARIMA-kandidatgrid og en LP smoke-test paa publiserbar indeks-skala.
Kjoringen dokumenterer at prognose- og LP-leddet henger teknisk sammen. Reell
kapasitetskonklusjon i mann-timer krever fortsatt lokal `weekly_volume.csv`
med faktiske FPK-volum og kalibrerte sonevise fristkapasiteter.

---

## Aktivitetsoversikt

### Fase 1: Initiering

| ID | Aktivitet | Planlagt slutt | Status | Merknad |
|----|-----------|----------------|--------|---------|
| 1.1 | Utvikle forste utkast | 2026-02-19 | Completed |  |
| 1.2 | Levere forste utkast | 2026-02-19 | Completed |  |
| 1.3 | Vente pa tilbakemelding fra veileder | 2026-02-20 | Completed |  |
| 1.4 | Revidere proposal | 2026-02-23 | Completed |  |
| 1.5 | Levere revidert versjon | 2026-02-24 | Completed |  |
| 1.6 | Milepael: Godkjent prosjektbeskrivelse | 2026-02-24 | Completed |  |

### Fase 2: Prosjektplan

| ID | Aktivitet | Planlagt slutt | Status | Merknad |
|----|-----------|----------------|--------|---------|
| 2.1 | Utvikle styringsplan og risikoanalyse | 2026-03-09 | Completed |  |
| 2.2 | Bygge WBS og Gantt i MS Project | 2026-03-16 | Completed |  |
| 2.3 | Starte formelt litteratursok | 2026-03-10 | Partial | Kompendier for forecasting og capacity planning er lagt inn. Mer litteratur legges til fortlopende. |
| 2.4 | Milepael: Godkjent prosjektplan | 2026-03-16 | Completed |  |

### Fase 3: Gjennomforing og review

| ID | Aktivitet | Planlagt slutt | Status | Merknad |
|----|-----------|----------------|--------|---------|
| 3.1 | Utarbeide teoretisk rammeverk | 2026-03-26 | Completed for draft | Teori-, metode- og modelleringskapitler er skrevet. Litteraturgrunnlaget er tilstrekkelig for peer review, men kan strammes videre i fase 4. |
| 3.2 | Datainnsamling og vask av bedriftsdata | 2026-03-26 | Completed for draft | Publiserbare modellinput er etablert: `weekly_volume_anonymized.csv`, `process_time_matrix.csv`, `capacity_assumptions.csv`, `action_parameters.csv` og `zone_cutoff_profile.csv`. Sensitive raw/processed-data holdes fortsatt lokalt og ignorert av Git. |
| 3.3 | Utvikling og trening av prognosemodell | 2026-04-09 | Completed minimum run | `005 report/scripts/run_forecast_capacity_models.py` kjorer SNaive-baseline og konservativ `statsmodels` SARIMAX/ARIMA-grid. Validering ekskluderer delvis uke 2026-14 og bruker 2026-01 til 2026-13. |
| 3.4 | Utvikling av kapasitetsoptimeringsmodell | 2026-04-24 | Completed minimum run | LP-formulering er implementert med `scipy.optimize.linprog` som publiserbar indeks-skala smoke-test. Operativ real-skala LP gjenstar fordi reelle FPK-volum ikke publiseres. |
| 3.5 | Analyse av resultater | 2026-05-01 | Completed for draft | Kapittel 7-8 inneholder datadeskriptiv analyse, SARIMAX/SNaive-validering og LP-resultater paa indeks-skala. |
| 3.6 | Gjennomfore peer-to-peer review | 2026-05-08 | Next | Send hovedutkast til tildelt student/gruppe og skriv skriftlig review av en annen rapport. |
| 3.7 | Milepael: Godkjent hovedutkast | 2026-05-08 | Ready for review | Hovedutkastet er klart til peer-to-peer review, men formell godkjenning avhenger av review- og faglaererprosess. |

### Fase 4: Sluttrapport

| ID | Aktivitet | Planlagt slutt | Status | Merknad |
|----|-----------|----------------|--------|---------|
| 4.1 | Ferdigstille introduksjon | 2026-05-14 | Draft exists | Introduksjon og problemstilling finnes, men bor leses mot konklusjonen etter peer review. |
| 4.2 | Skrive diskusjon og konklusjon | 2026-05-22 | Draft exists | Diskusjon og konklusjon er skrevet for hovedutkastet. Revideres etter peer review. |
| 4.3 | Finpuss, kvalitetssikring og APA 7th | 2026-05-29 | Not started | Sluttvask, bibliografi, figurer/tabeller, eksportformat og menneskelig korrektur gjenstar. |
| 4.4 | Milepael: Innlevering av rapport og kode | 2026-05-29 | Not started |  |
| 4.5 | Forberede og gjennomfore muntlig presentasjon | 2026-06-05 | Not started |  |

---

## Kritiske risikoer akkurat na

1. **Peer-to-peer review:** Hovedutkastet er klart, men arbeidskravet er ikke
   fullfort for man ogsa har gitt skriftlig review til en annen gruppe/student.
2. **Publiserbarhet vs. real-skala:** Rapporten bruker publiserbar indeks. LP
   smoke-testen kan ikke tolkes som faktisk mann-timebehov uten lokal
   `weekly_volume.csv`.
3. **Sonevise frister:** Soneandeler er etablert, men faktisk `CAP_deadline`
   for 00:00, 01:00 og 02:00 ma kalibreres for operativ bruk.
4. **Sluttvask:** Bibliografi, tabell-/figurtekster, norsk/engelsk konsistens,
   PDF/Word-eksport og menneskelig korrektur gjenstar til fase 4.

## Prioriterte tiltak

| Prioritet | Tiltak |
|-----------|--------|
| Kritisk | Del hovedutkastet med tildelt peer-review partner og avklar format (Markdown/PDF/Word). |
| Kritisk | Skriv skriftlig peer-to-peer review av en annen rapport naar den mottas. |
| Hoy | Les gjennom hele egen rapport manuelt og noter konkrete fase 4-endringer. |
| Hoy | Stram bibliografi/APA, tabelltekster og begrepsbruk etter peer review. |
| Medium | Kjor real-skala LP lokalt dersom `weekly_volume.csv` skal brukes i endelig, ikke-publiserbar analyse. |

---

## Repo-basert statusbilde

Det viktigste som na faktisk finnes i repoet er:

- proposal i `011 fase 1 - proposal/`
- prosjektplan og styringsdokumenter i `012 fase 2 - plan/`
- referansestruktur med aktive kompendier i `003 references/`
- datakrav, CSV-maler, vaskeskript, anonymiseringsskript, publiserbar
  `weekly_volume_anonymized.csv` og lokal handover-note i `004 data/`
- prosess-tidsmatrise, kapasitetsantakelser, tiltaksparametre og soneprofil i
  `004 data/`
- modellskript for SARIMAX/SNaive og LP smoke-test i
  `005 report/scripts/run_forecast_capacity_models.py`
- aktiv sluttrapport i
  `005 report/Sluttrapport_Volumprognose-Kapasitetsanalyse_DavorNecemer.md`

Det viktigste som fortsatt mangler er:

- gjennomfort peer-to-peer review og skriftlig reviewrapport til annen gruppe
- sluttvask av rapport, bibliografi og eksportformat
- eventuell real-skala LP-kjoring lokalt dersom endelig rapport skal inneholde
  operative mann-timeestimater

## Restart checkpoint 2026-04-30

Ved neste arbeidsokt etter omstart:

1. Start fra hovedutkastet i `005 report/Sluttrapport_Volumprognose-Kapasitetsanalyse_DavorNecemer.md`.
2. Ikke skann `000 templates/` med mindre template- eller forelesningsmateriale eksplisitt ettersporres.
3. Bruk `005 report/scripts/run_forecast_capacity_models.py` for aa reprodusere minimumskjoringen.
4. Hold `004 data/weekly_volume.csv`, `004 data/raw/` og sensitive `004 data/processed/`-filer lokalt/ignorert.
5. Neste faglige steg er peer-to-peer review: send eget hovedutkast og skriv review av en annen rapport.
6. Etter review: prioriter sluttvask, bibliografi, rapportformat og eventuelle faglige justeringer.
