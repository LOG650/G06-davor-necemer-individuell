# Oppgave og status – Integrert volumprognose og kapasitetsanalyse

**Dato:** 26.04.2026  
**Status-revisjon:** Basert på repo-analyse og Gantt-plan fra MS Project  
**Prosjektleder:** Davor Necemer

---

## Sammendrag av forsinkelse

**Dager til innlevering:** 33 dager (29.05.2026)

Prosjektet er **betydelig forsinket**. Fase 1 og 2 er fullført, men **alle aktiviteter i fase 3 (Gjennomføring & Review)** ligger etter planen:

- **Litteraturarbeid (3.1):** ~31 dager forsinket
- **Datainnsamling (3.2):** ~31 dager forsinket ⚠️ **KRITISK – blokkerer alt videre arbeid**
- **Prognosemodell (3.3):** ~17 dager forsinket
- **Kapasitetsmodell (3.4):** 2 dager forsinket (skulle ende 24.04.26)

Fase 4 (Sluttrapport) har ennå ikke startet.

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
| 2.3 | Starte formelt litteratursøk | 10 d | 25.02.26 | 10.03.26 | ⚠️ Delvis | 1 ref. funnet, søk ikke fullført |
| 2.4 | **Milepæl: Godkjent prosjektplan** | 0 d | 16.03.26 | 16.03.26 | ✅ Fullført | Prosjektstyringsplan i `012 fase 2 - plan/` |

### **FASE 3: Gjennomføring & Review** ❌ FORSINKET

| ID | Aktivitet | Varighet | Start | Slutt (planlagt) | **Status** | **Dager forsinket** | Kommentar |
|----|-----------|----------|-------|------------------|-----------|---------------------|-----------|
| 3.1 | Utarbeide teoretisk rammeverk | 8 d | 17.03.26 | 26.03.26 | ⚠️ Forsinket | ~31 | Kun 1 metodologi-referanse i repo. Mangler litteratur i forecasting & capacity_planning mapper |
| 3.2 | **Datainnsamling og vask av bedriftsdata** | 8 d | 17.03.26 | 26.03.26 | 🔴 Ikke startet | ~31 | **KRITISK:** `004 data/` mappen er **HELT TOM** – ingen datafiler |
| 3.3 | Utvikling og trening av KI-prognosemodell | 10 d | 27.03.26 | 09.04.26 | 🔴 Ikke startet | ~17 | Ingen kode-filer i repo. Avhenger av 3.2 |
| 3.4 | Utvikling av kapasitetsoptimeringsmodell | 11 d | 10.04.26 | 24.04.26 | 🔴 Ikke startet | 2 | Skulle avsluttes IGÅR. Ingen implementasjon funnet. Avhenger av 3.2 |
| 3.5 | Analyse av resultater | 5 d | 27.04.26 | 01.05.26 | 🔴 Ikke startet | – | Starter MORGEN iht. plan, men forutsetninger (3.2–3.4) ikke oppfylt |
| 3.6 | Gjennomføre peer-to-peer review | 5 d | 04.05.26 | 08.05.26 | 🔴 Ikke startet | – | `013 fase 3 - review/` er tom |
| 3.7 | **Milepæl: Godkjent hovedutkast** | 0 d | 08.05.26 | 08.05.26 | 🔴 Ikke startet | – | 12 dager igjen. Kritisk milepæl – blokkert av 3.2–3.6 |

### **FASE 4: Sluttrapport** ❌ IKKE STARTET

| ID | Aktivitet | Varighet | Start | Slutt (planlagt) | Status | Kommentar |
|----|-----------|----------|-------|------------------|--------|-----------|
| 4.1 | Ferdigstille introduksjon | 4 d | 11.05.26 | 14.05.26 | 🔴 Ikke startet | Starter 15 dager fra nå |
| 4.2 | Skrive diskusjon og konklusjon | 6 d | 15.05.26 | 22.05.26 | 🔴 Ikke startet | `014 fase 4 - report/` er tom |
| 4.3 | Finpuss, kvalitetssikring og APA 7th | 5 d | 25.05.26 | 29.05.26 | 🔴 Ikke startet | Siste oppgave før innlevering |
| 4.4 | **Milepæl: Innlevering av rapport og kode** | 0 d | 29.05.26 | 29.05.26 | 🔴 Ikke startet | **ENDELIG FRIST:** 33 dager igjen |
| 4.5 | Forberede og gjennomføre muntlig presentasjon | 5 d | 01.06.26 | 05.06.26 | 🔴 Ikke startet | Etter innlevering |

---

## Status etter repo-analyse

### Eksisterende arbeidsprodukt

| Område | Status | Bevis |
|--------|--------|-------|
| **Fase 1: Proposal** | ✅ Fullført | `011 fase 1 - proposal/Proposal for integrert volumprognose og kapasitetsanalyse Revidert.md` |
| **Fase 2: Plan & Gantt** | ✅ Fullført | `012 fase 2 - plan/LOG650_Prosjektstyringsplan_Davor_Necemer_1.2.md` + MS Project-fil |
| **Litteraturgrunnlag** | ⚠️ Mangelfull | Kun 1 fil i `003 references/03 method/`. Mapper `01 forecasting/` og `02 capacity_planning/` er tomme |
| **Data** | 🔴 Mangler helt | `004 data/` mappen er tom. Ingen datafiler innlastet |
| **Kode/Modeller** | 🔴 Mangler helt | Ingen Python-, R-, Excel- eller modelleringsfiler i repo |
| **Analyse** | 🔴 Ikke startet | `013 fase 3 - review/` er tom |
| **Rapport** | 🔴 Ikke startet | `014 fase 4 - report/` er tom |
| **Report-mal** | ✅ Tilgjengelig | `005 report/Mal prosjekt LOG650 v2.md` (oppdatert 25.04.26) |

---

## Kritisk linje og avhengigheter

**Blokkert av:** Aktivitet 3.2 (Datainnsamling) – **URGENT START REQUIRED**

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

1. **Start datainnsamling (3.2) UMIDDELBART**
   - Hent bedriftsdata fra anonymisert næringsmiddelkilde
   - Gjennomfør datavask og normalisering til FPK-ekvivalenter
   - Mål: Fullføre innen 2–3 uker for å få modellering på skinner

2. **Komplettere litteraturgrunnlag (3.1)**
   - Søk etter referanser om:
     - Demand forecasting / volumprognoser
     - Capacity planning / kapasitetsplanlegging
     - Optimering under tidsfrister
   - Mål: Minimum 8–12 relevante kilder

### ⚠️ HØYT PRIORITET (Dager: 3–7)

3. **Starte KI-prognosemodell (3.3)** (parallelt med datavask)
   - Velg tidsseriemetode (ARIMA, eksponentiell utjevning, enkel ML)
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
| **3.7: Godkjent hovedutkast** | 08.05.26 | 12 | 🔴 Avhenger av 3.2–3.6 |
| **4.4: Innlevering rapport og kode** | 29.05.26 | 33 | 🔴 Avhenger av fase 3 & 4 |
| **4.5: Muntlig presentasjon** | 01–05.06.26 | 36–40 | 🔴 Etter innlevering |

---

## Konklusjon

**Prosjektet kan fullføres innen fristen dersom datainnsamling (3.2) starter umiddelbart og gjennomføres parallelt med litteratur- og modellarbeid.** Gjenværende 33 dager er tilstrekkelig hvis kritiske oppgaver gjennomføres effektivt og sekvensiell (ikke parallell) der det er planlagt.

**Største risiko:** Forsinkelse i datavask (3.2) vil kaskadeforsink alle påfølgende aktiviteter og truende milepælen på 08.05.26.
