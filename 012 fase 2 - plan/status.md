# Prosjektstatus - Integrert volumprognose og kapasitetsanalyse

**Dato:** 2026-04-25  
**Prosjektleder:** Davor Necemer  
**Dager til innlevering:** 34 (2026-05-29)

---

## Sammendrag

| Fase | Status |
|------|--------|
| Fase 1: Initiering | Fullfort |
| Fase 2: Prosjektplan | Fullfort |
| Fase 3: Gjennomforing | Pagar, men bak plan |
| Fase 4: Sluttrapport | Pabegynt i repo, men ikke ferdigstilt |

Prosjektet er fortsatt forsinket i forhold til Gantt-planen, men statusen er bedre enn tidligere repo-gjennomgang tilsa. Det finnes na et aktivt rapportutkast, et tydelig datakravsdokument, CSV-maler for datainnhenting og en oppdatert metodisk retning med SARIMAX for prognosedelen og LP for kapasitetsdelen.

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
| 3.1 | Utarbeide teoretisk rammeverk | 2026-03-26 | In progress, delayed | Teori-, metode- og modelleringsutkast finnes i rapporten, men litteraturgrunnlaget ma fortsatt utvides. |
| 3.2 | Datainnsamling og vask av bedriftsdata | 2026-03-26 | Prepared, delayed | Datakrav og CSV-maler er klare. Faktiske bedriftsdata fra Qlik Sense / Infor M3 er ikke lastet inn ennå. |
| 3.3 | Utvikling og trening av prognosemodell | 2026-04-09 | Prepared, delayed | SARIMAX er valgt metodisk, med treningsvindu 2024-2025 og valideringsplan for Q1 2026. Ingen modellkode er implementert ennå. |
| 3.4 | Utvikling av kapasitetsoptimeringsmodell | 2026-04-24 | Prepared, delayed | LP-struktur og beslutningslogikk er beskrevet i rapportutkastet, men ingen implementasjon er laget ennå. |
| 3.5 | Analyse av resultater | 2026-05-01 | Not started | Avhenger av 3.2 til 3.4. |
| 3.6 | Gjennomfore peer-to-peer review | 2026-05-08 | Not started |  |
| 3.7 | Milepael: Godkjent hovedutkast | 2026-05-08 | Not started | Avhenger av framdrift i 3.2 til 3.6. |

### Fase 4: Sluttrapport

| ID | Aktivitet | Planlagt slutt | Status | Merknad |
|----|-----------|----------------|--------|---------|
| 4.1 | Ferdigstille introduksjon | 2026-05-14 | Early draft exists | Rapportfilen er opprettet og har aktivt utkast, men kapitlene er ikke ferdigstilt. |
| 4.2 | Skrive diskusjon og konklusjon | 2026-05-22 | Not started |  |
| 4.3 | Finpuss, kvalitetssikring og APA 7th | 2026-05-29 | Not started |  |
| 4.4 | Milepael: Innlevering av rapport og kode | 2026-05-29 | Not started |  |
| 4.5 | Forberede og gjennomfore muntlig presentasjon | 2026-06-05 | Not started |  |

---

## Kritiske risikoer akkurat na

1. **Datainnsamling:** Faktiske bedriftsdata er ikke lastet inn enda. Dette blokkerer modellering og analyse.
2. **Litteraturgrunnlag:** Strukturen er ryddet og kompendiene er pa plass, men ekstern litteratur utover kompendiet ma fortsatt bygges opp.
3. **Implementasjon:** Metodikken er definert, men prognosemodell og kapasitetsmodell er forelopig bare dokumentert konseptuelt.

## Prioriterte tiltak

| Prioritet | Tiltak |
|-----------|--------|
| Kritisk | Hent inn og anonymiser `weekly_volume.csv`, `process_time_matrix.csv` og `capacity_weekly.csv` |
| Hoy | Fullfor et lite, relevant litteraturgrunnlag utover kompendiet |
| Hoy | Implementer en enkel baseline for SARIMAX sa snart de forste dataene er klare |
| Medium | Bygg den forste operative LP-modellen nar forecast-input og kapasitetsdata foreligger |

---

## Repo-basert statusbilde

Det viktigste som na faktisk finnes i repoet er:

- proposal i `011 fase 1 - proposal/`
- prosjektplan og styringsdokumenter i `012 fase 2 - plan/`
- referansestruktur med aktive kompendier i `003 references/`
- datakrav og CSV-maler i `004 data/`
- aktiv sluttrapport i `005 report/Sluttrapport_Volumprognose-Kapasitetsanalyse_DavorNecemer.md`

Det viktigste som fortsatt mangler er:

- faktiske bedriftsdata i `004 data/`
- kode eller notebook for forecast og optimering
- gjennomfort analyse og review
