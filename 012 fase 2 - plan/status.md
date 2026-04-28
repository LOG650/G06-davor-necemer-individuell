# Prosjektstatus - Integrert volumprognose og kapasitetsanalyse

**Dato:** 2026-04-28
**Prosjektleder:** Davor Necemer  
**Dager til innlevering:** 33 (2026-05-29)

---

## Sammendrag

| Fase | Status |
|------|--------|
| Fase 1: Initiering | Fullfort |
| Fase 2: Prosjektplan | Fullfort |
| Fase 3: Gjennomforing | Pagar, men bak plan |
| Fase 4: Sluttrapport | Pabegynt i repo, men ikke ferdigstilt |

Prosjektet er fortsatt forsinket i forhold til Gantt-planen, men statusen er bedre enn tidligere repo-gjennomgang tilsa. Det finnes na et aktivt rapportutkast, et tydelig datakravsdokument, CSV-maler for datainnhenting, forste lokale vask av Qlik-volumdata, kapasitetsantakelser for dispatch og en oppdatert metodisk retning med SARIMAX for prognosedelen og LP for kapasitetsdelen.

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
| 3.2 | Datainnsamling og vask av bedriftsdata | 2026-03-26 | In progress, delayed | Qlik-volum, kampanjer og lansering/sanering er lastet lokalt og forste vask er gjennomfort. Outlook-script for produksjonslister/dispatcher er testet, men 2024-historikk venter paa videre Outlook-synk/arkivtilgang. Sensitive data ignoreres av Git inntil anonymisering er klar. |
| 3.3 | Utvikling og trening av prognosemodell | 2026-04-09 | Prepared, delayed | SARIMAX er valgt metodisk. Vasket ukentlig volum dekker trening 2024-2025 og validering 2026-01 til 2026-14. Ingen modellkode er implementert ennå. |
| 3.4 | Utvikling av kapasitetsoptimeringsmodell | 2026-04-24 | Prepared, delayed | LP-struktur og beslutningslogikk er beskrevet i rapportutkastet. Kapasitetsbaseline for P1/P2, tidlig oppstart, sykefravaersproxy og ekstra bemanning er dokumentert som dataantakelser. Ingen optimeringsimplementasjon er laget ennaa. |
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

1. **Datainnsamling:** Ukentlig volumgrunnlag er lastet og vasket lokalt, men data maa anonymiseres foer de kan pushes eller brukes som del av leveranse. Historiske Outlook-vedlegg foer 2025 er forelopig ikke tilgjengelige lokalt.
2. **Litteraturgrunnlag:** Strukturen er ryddet og kompendiene er pa plass, men ekstern litteratur utover kompendiet ma fortsatt bygges opp.
3. **Implementasjon:** Metodikken er definert, men prognosemodell og kapasitetsmodell er forelopig bare dokumentert konseptuelt.

## Prioriterte tiltak

| Prioritet | Tiltak |
|-----------|--------|
| Kritisk | Gjennomfoer review av datagrunnlag og antakelser foer anonymisering. Deretter anonymiser `weekly_volume.csv`, og oppdater `process_time_matrix.csv` naar flere Outlook-par er hentet. |
| Hoy | Fullfor et lite, relevant litteraturgrunnlag utover kompendiet |
| Hoy | Implementer en enkel baseline for SARIMAX sa snart de forste dataene er klare |
| Medium | Bygg den forste operative LP-modellen nar forecast-input og kapasitetsdata foreligger |

---

## Repo-basert statusbilde

Det viktigste som na faktisk finnes i repoet er:

- proposal i `011 fase 1 - proposal/`
- prosjektplan og styringsdokumenter i `012 fase 2 - plan/`
- referansestruktur med aktive kompendier i `003 references/`
- datakrav, CSV-maler, vaskeskript og lokal handover-note i `004 data/`
- aktiv sluttrapport i `005 report/Sluttrapport_Volumprognose-Kapasitetsanalyse_DavorNecemer.md`

Det viktigste som fortsatt mangler er:

- anonymisert datagrunnlag som kan committes/pushes trygt
- kode eller notebook for forecast og optimering
- gjennomfort analyse og review
