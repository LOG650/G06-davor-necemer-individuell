# Oppgave og status – Integrert volumprognose og kapasitetsanalyse

**Dato:** 25.04.2026  
**Status-revisjon:** Basert på repo-gjennomgang per 25.04.2026 og Gantt-plan fra MS Project  
**Prosjektleder:** Davor Necemer

---

## Sammendrag av forsinkelse

**Dager til innlevering:** 34 dager (29.05.2026)

Prosjektet er fortsatt **forsinket i forhold til planen**, men repoet viser tydelig framdrift sammenlignet med tidligere statusbilde:

- **Litteraturarbeid (3.1):** pågår, men trenger flere kilder utover kompendiet
- **Datainnsamling (3.2):** faktiske bedriftsdata mangler fortsatt ⚠️ **kritisk aktivitet**
- **Prognosemodell (3.3):** metodikk er oppdatert til SARIMAX, men implementasjon mangler
- **Kapasitetsmodell (3.4):** LP-struktur er beskrevet, men implementasjon mangler

Fase 4 er ikke ferdigstilt, men sluttrapportutkastet er nå opprettet og påbegynt i repoet.

---

## Aktivitetsoversikt (alle 26 oppgaver)

### **FASE 1: Initiering** ✅ FULLFØRT

| ID | Aktivitet | Varighet | Start | Slutt (planlagt) | Status | Kommentar |
|----|-----------|----------|-------|------------------|--------|-----------|
| 1.1 | Utvikle første utkast | 29 d | 12.01.26 | 19.02.26 | ✅ Fullført | Proposal-fil eksisterer |
| 1.2 | Levere første utkast | 0 d | 19.02.26 | 19.02.26 | ✅ Fullført | Milepæl nådd |
| 1.3 | Vente på tilbakemelding fra veileder | 1 d | 20.02.26 | 20.02.26 | ✅ Fullført | |
| 1.4 | Revidere proposal | 1 d | 23.02.26 | 23.02.26 | ✅ Fullført | |
| 1.5 | Levere revidert versjon | 1 d | 24.02.26 | 24.02.26 | ✅ Fullført | |
| 1.6 | **Milepæl: Godkjent prosjektbeskrivelse** | 0 d | 24.02.26 | 24.02.26 | ✅ Fullført | Proposal exists in `011 fase 1 - proposal/` |

### **FASE 2: Prosjektplan** ✅ FULLFØRT

| ID | Aktivitet | Varighet | Start | Slutt (planlagt) | Status | Kommentar |
|----|-----------|----------|-------|------------------|--------|-----------|
| 2.1 | Utvikle styringsplan og risikoanalyse | 9 d | 25.02.26 | 09.03.26 | ✅ Fullført | Plan finnes |
| 2.2 | Bygge WBS og Gantt i MS Project | 5 d | 10.03.26 | 16.03.26 | ✅ Fullført | MS Project fil eksisterer |
| 2.3 | Starte formelt litteratursøk | 10 d | 25.02.26 | 10.03.26 | ⚠️ Delvis | Kompendier for forecasting og capacity planning er lagt inn. Ekstern litteratur bygges videre fortløpende |
| 2.4 | **Milepæl: Godkjent prosjektplan** | 0 d | 16.03.26 | 16.03.26 | ✅ Fullført | Prosjektstyringsplan i `012 fase 2 - plan/` |

### **FASE 3: Gjennomføring & Review** ❌ FORSINKET

| ID | Aktivitet | Varighet | Start | Slutt (planlagt) | **Status** | **Dager forsinket** | Kommentar |
|----|-----------|----------|-------|------------------|-----------|---------------------|-----------|
| 3.1 | Utarbeide teoretisk rammeverk | 8 d | 17.03.26 | 26.03.26 | ⚠️ Pågår, men forsinket | - | Rapportutkast med teori, metode og modellstruktur finnes, men litteraturgrunnlaget må utvides |
| 3.2 | **Datainnsamling og vask av bedriftsdata** | 8 d | 17.03.26 | 26.03.26 | ⚠️ Forberedt, men forsinket | - | **KRITISK:** `004 data/` inneholder datakrav og CSV-maler, men ingen faktiske bedriftsdata ennå |
| 3.3 | Utvikling og trening av KI-prognosemodell | 10 d | 27.03.26 | 09.04.26 | ⚠️ Metodisk forberedt | - | SARIMAX er valgt og dokumentert, men ingen kode eller estimering er gjennomført ennå |
| 3.4 | Utvikling av kapasitetsoptimeringsmodell | 11 d | 10.04.26 | 24.04.26 | ⚠️ Konseptuelt forberedt | - | LP-logikk og modellstruktur er dokumentert, men ingen implementasjon finnes ennå |
| 3.5 | Analyse av resultater | 5 d | 27.04.26 | 01.05.26 | 🔴 Ikke startet | – | Forutsetter at 3.2–3.4 gir brukbare modellresultater |
| 3.6 | Gjennomføre peer-to-peer review | 5 d | 04.05.26 | 08.05.26 | 🔴 Ikke startet | – | `013 fase 3 - review/` er tom |
| 3.7 | **Milepæl: Godkjent hovedutkast** | 0 d | 08.05.26 | 08.05.26 | 🔴 Ikke startet | – | Kritisk milepæl – blokkert av 3.2–3.6 |

### **FASE 4: Sluttrapport** ⚠️ PÅBEGYNT, MEN IKKE FERDIGSTILT

| ID | Aktivitet | Varighet | Start | Slutt (planlagt) | Status | Kommentar |
|----|-----------|----------|-------|------------------|--------|-----------|
| 4.1 | Ferdigstille introduksjon | 4 d | 11.05.26 | 14.05.26 | ⚠️ Påbegynt | Rapportutkast finnes i `005 report/` |
| 4.2 | Skrive diskusjon og konklusjon | 6 d | 15.05.26 | 22.05.26 | 🔴 Ikke startet | Avhenger av analyse og ferdig modellgrunnlag |
| 4.3 | Finpuss, kvalitetssikring og APA 7th | 5 d | 25.05.26 | 29.05.26 | 🔴 Ikke startet | Siste oppgave før innlevering |
| 4.4 | **Milepæl: Innlevering av rapport og kode** | 0 d | 29.05.26 | 29.05.26 | 🔴 Ikke startet | **ENDELIG FRIST:** 34 dager igjen |
| 4.5 | Forberede og gjennomføre muntlig presentasjon | 5 d | 01.06.26 | 05.06.26 | 🔴 Ikke startet | Etter innlevering |

---

## Status etter repo-analyse

### Eksisterende arbeidsprodukt

| Område | Status | Bevis |
|--------|--------|-------|
| **Fase 1: Proposal** | ✅ Fullført | `011 fase 1 - proposal/Proposal for integrert volumprognose og kapasitetsanalyse Revidert.md` |
| **Fase 2: Plan & Gantt** | ✅ Fullført | `012 fase 2 - plan/LOG650_Prosjektstyringsplan_Davor_Necemer_1.2.md` + MS Project-fil |
| **Litteraturgrunnlag** | ⚠️ Under oppbygging | Kompendier i forecasting og capacity planning er lagt inn. Ekstern litteratur utover dette legges til fortløpende |
| **Data** | ⚠️ Forberedt, men ikke innlastet | `004 data/` inneholder datakrav og CSV-maler, men ingen faktiske bedriftsdata ennå |
| **Kode/Modeller** | 🔴 Mangler helt | Ingen Python-, R-, Excel- eller modelleringsfiler i repo |
| **Analyse** | 🔴 Ikke startet | `013 fase 3 - review/` er tom |
| **Rapport** | ⚠️ Påbegynt | Aktiv rapportfil finnes i `005 report/Sluttrapport_Volumprognose-Kapasitetsanalyse_DavorNecemer.md` |
| **Report-mal** | ✅ Tilgjengelig | `005 report/Mal prosjekt LOG650 v2.md` finnes fortsatt som grunnlag |

---

## Kritisk linje og avhengigheter

**Kritisk avhengighet:** Aktivitet 3.2 (Datainnsamling) – faktiske data må inn før modellene kan implementeres og testes

Kritisk sekvens som må gjennomføres serielt:

1. **3.2 Datainnsamling (17.03–26.03 i plan)** → Start UMIDDELBART
2. **3.1 Teoretisk rammeverk (17.03–26.03)** → Parallelt med 3.2
3. **3.3 KI-prognosemodell (27.03–09.04)** → Avhenger av 3.2
4. **3.4 Kapasitetsmodell (10.04–24.04)** → Avhenger av 3.2 og 3.3
5. **3.5 Analyse (27.04–01.05)** → Avhenger av 3.3 og 3.4
6. **3.6–3.7 Review & milepæl (04.05–08.05)** → Avhenger av 3.5
7. **Fase 4 (11.05–29.05)** → Avhenger av 3.7

---

## Tiltak – Prioritet

### 🚨 KRITISK (Dager: 0)

1. **Start innlasting av faktiske bedriftsdata (3.2) umiddelbart**
   - Hent data via Qlik Sense fra Infor M3
   - Prioriter `weekly_volume.csv`, `process_time_matrix.csv` og `capacity_weekly.csv`
   - Gjennomfør anonymisering og normalisering til FPK-ekvivalenter

2. **Komplettere litteraturgrunnlag (3.1)**
   - Søk etter referanser om:
     - Demand forecasting / volumprognoser
     - Capacity planning / kapasitetsplanlegging
     - Optimering under tidsfrister
   - Mål: Bygge et lite, relevant litteraturgrunnlag utover kompendiet

### ⚠️ HØYT PRIORITET (Dager: 3–7)

3. **Starte prognosemodell (3.3)** (parallelt med datavask)
   - Bruk SARIMAX som hovedretning, med enkel baseline ved behov
   - Implementer baseline-modell
   - Test med historiske data når 3.2 er delvis ferdig

4. **Starte kapasitetsoptimeringsmodell (3.4)** (uke 2–3 av fase 3)
   - Definer optimeringsmål (min. ekstra kapasitet + straff for fristbrudd)
   - Implementer lineær programmering eller heuristikk
   - Integrer med prognosemodulen fra 3.3

### MEDIUM PRIORITET (Dager: 8–12)

5. **Gjennomføre analyse (3.5)**
   - Kjør fullstendig modell på datagrunnlag
   - Tolking av resultater
   - Scenarioanalyse og sensitivitetstest

6. **Peer-to-peer review (3.6)**
   - Be medstudent om tilbakemelding
   - Gjør justeringer basert på feedback

### LAVT PRIORITET (Dager: 13+)

7. **Fase 4: Rapportskriving**
   - Ferdigstille alle kapitler (introduksjon, metode, resultater, diskusjon, konklusjon)
   - Finpuss av APA 7th stil
   - Innlevering 29.05.26

---

## Ressurser og verktøy

**Tilgjengelige:**
- Word / Markdown for dokumentasjon
- MS Project for Gantt-oppdateringer
- Python / R / Excel for modellering (må avklares)
- GitHub repo for versjonskontroll (allerede i bruk)

**Kritisk å ha klart:**
- Datafil(er) fra bedrift
- Python-miljø eller Excel for modellering
- Referansehåndtering (BibTeX, Zotero, eller manuell APA)

---

## Milepæler gjenværende

| Milepæl | Dato | Dager igjen | Status |
|---------|------|-------------|--------|
| **3.7: Godkjent hovedutkast** | 08.05.26 | 13 | 🔴 Avhenger av 3.2–3.6 |
| **4.4: Innlevering rapport og kode** | 29.05.26 | 34 | 🔴 Avhenger av fase 3 & 4 |
| **4.5: Muntlig presentasjon** | 01–05.06.26 | 37–41 | 🔴 Etter innlevering |

---

## Konklusjon

**Prosjektet kan fortsatt fullføres innen fristen dersom datainnsamling (3.2) starter nå og gjennomføres parallelt med målrettet litteraturarbeid og enkel modellimplementasjon.** Gjenværende 34 dager er knappe, men tilstrekkelige dersom omfanget holdes stramt og minimumsløsningen prioriteres først.

**Største risiko:** Forsinkelse i tilgang til faktiske data vil kaskadeforsinke modellering, analyse og hovedutkastet som skal være klart før 08.05.2026.
