# Prosjektstatus – Integrert volumprognose og kapasitetsanalyse

**Dato:** 2026-04-26  
**Prosjektleder:** Davor Necemer  
**Dager til innlevering:** 33 (29.05.2026)

---

## Sammendrag

| Fase | Status |
|------|--------|
| Fase 1: Initiering | ✅ Fullført |
| Fase 2: Prosjektplan | ✅ Fullført |
| Fase 3: Gjennomføring | 🔴 Forsinket |
| Fase 4: Sluttrapport | 🔴 Ikke startet |

---

## Aktivitetsoversikt

### Fase 1: Initiering

| ID | Aktivitet | Planlagt slutt | Status | Merknad |
|----|-----------|----------------|--------|---------|
| 1.1 | Utvikle første utkast | 2026-02-19 | ✅ Completed |  |
| 1.2 | Levere første utkast | 2026-02-19 | ✅ Completed |  |
| 1.3 | Vente på tilbakemelding fra veileder | 2026-02-20 | ✅ Completed |  |
| 1.4 | Revidere proposal | 2026-02-23 | ✅ Completed |  |
| 1.5 | Levere revidert versjon | 2026-02-24 | ✅ Completed |  |
| 1.6 | Milepæl: Godkjent prosjektbeskrivelse | 2026-02-24 | ✅ Completed |  |

### Fase 2: Prosjektplan

| ID | Aktivitet | Planlagt slutt | Status | Merknad |
|----|-----------|----------------|--------|---------|
| 2.1 | Utvikle styringsplan og risikoanalyse | 2026-03-09 | ✅ Completed |  |
| 2.2 | Bygge WBS og Gantt i MS Project | 2026-03-16 | ✅ Completed |  |
| 2.3 | Starte formelt litteratursøk | 2026-03-10 | ⚠️ Partial | Kun 1 referanse funnet i repo |
| 2.4 | Milepæl: Godkjent prosjektplan | 2026-03-16 | ✅ Completed |  |

### Fase 3: Gjennomføring & Review

| ID | Aktivitet | Planlagt slutt | Status | Merknad |
|----|-----------|----------------|--------|---------|
| 3.1 | Utarbeide teoretisk rammeverk | 2026-03-26 | ⚠️ Delayed (31 d forsinket) | Kun 1 metodologi-ref. Mangler forecasting & capacity refs. |
| 3.2 | Datainnsamling og vask av bedriftsdata | 2026-03-26 | 🔴 Not started (31 d forsinket) | KRITISK: 004 data/ mappen er tom |
| 3.3 | Utvikling og trening av KI-prognosemodell | 2026-04-09 | 🔴 Not started (17 d forsinket) | Avhenger av 3.2 |
| 3.4 | Utvikling av kapasitetsoptimeringsmodell | 2026-04-24 | 🔴 Not started (2 d forsinket) | Avhenger av 3.2 og 3.3 |
| 3.5 | Analyse av resultater | 2026-05-01 | 🔴 Not started | Avhenger av 3.3 og 3.4 |
| 3.6 | Gjennomføre peer-to-peer review | 2026-05-08 | 🔴 Not started |  |
| 3.7 | Milepæl: Godkjent hovedutkast | 2026-05-08 | 🔴 Not started |  |

### Fase 4: Sluttrapport

| ID | Aktivitet | Planlagt slutt | Status | Merknad |
|----|-----------|----------------|--------|---------|
| 4.1 | Ferdigstille introduksjon | 2026-05-14 | 🔴 Not started |  |
| 4.2 | Skrive diskusjon og konklusjon | 2026-05-22 | 🔴 Not started |  |
| 4.3 | Finpuss, kvalitetssikring og APA 7th | 2026-05-29 | 🔴 Not started |  |
| 4.4 | Milepæl: Innlevering av rapport og kode | 2026-05-29 | 🔴 Not started |  |
| 4.5 | Forberede og gjennomføre muntlig presentasjon | 2026-06-05 | 🔴 Not started |  |

---

## Kritiske risikoer akkurat nå

1. **RK01 – Datainnsamling:** `004 data/` er tom. Blokkerer 3.3, 3.4, 3.5.
2. **RK05 – Modellkompleksitet:** 33 dager igjen – prioriter minimumsløsning.
3. **RK02 – Modellvalg:** Velg enkel baseline-modell raskt.

## Prioriterte tiltak

| Prioritet | Tiltak |
|-----------|--------|
| 🚨 Kritisk | Start datainnsamling (3.2) UMIDDELBART |
| ⚠️ Høy | Ferdigstill litteratursøk og rammeverk (3.1) |
| ⚠️ Høy | Start prognosemodell parallelt med datavask (3.3) |
| Medium | Kapasitetsmodell når data er klart (3.4) |
