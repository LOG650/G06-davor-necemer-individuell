# Prosjektstatus - Integrert volumprognose og kapasitetsanalyse

**Dato:** 2026-05-31
**Prosjektleder:** Davor Necemer
**Dager til innlevering:** frist 2026-06-01 kl. 14:00 (utvidet fra 31.05)
**Aktiv branch:** `Fase_4_report`
**Sluttvask 2026-05-31:** Forside + obligatoriske erklæringer fylt ut og verifisert (adversarisk Explore-sjekk: tall/dato/struktur OK); endelig PDF rebygd til 35 sider. Gjenstår: menneskelig korrektur, deretter merge `Fase_4_report` → `main`.

---

## Sammendrag

| Fase | Status |
|------|--------|
| Fase 1: Initiering | Fullfort |
| Fase 2: Prosjektplan | Fullfort |
| Fase 3: Gjennomforing | Fullfort (peer-to-peer levert og mottatt) |
| Fase 4: Sluttrapport | Pagar; G05 "MA"-funn integrert (ea25e47); "BOR" #5/#6/#10/#11 + #7/#8/#9 + #13 (teoretisk hull §2.3) integrert; menneskelig korrektur + merge til main gjenstaar |

Fase 3 er fullfort: hovedutkastet ble klart innen Eriks frist 30.04, og
peer-to-peer-utveksling med G05 (kontaktperson Birgitte) ble gjennomfort
04.-08.05 (Davor sendte hovedutkast 04.05, leverte review til G05 06.05,
mottok G05s review 08.05). G05s skriftlige tilbakemelding (datert 2026-05-07) ligger
i `013 fase 3 - review/peer review Integrert volumprognose og kapasitetsanalyse_G05_G06.md`
(.md og .docx). Var egen review til G05 ligger samme sted som `Peer-review_G06_G05.md`
og `.pdf`. Hovedutkast-PDF-en som G05 reviewet ligger i samme mappe.

Strukturert integrasjonsplan for G05s 19 funn er na i
`014 fase 4 - report/G05_INTEGRATION_PLAN.md`. En selvstendig hand-off for nye
chat-sesjoner ligger i `014 fase 4 - report/Fase_4_kickoff.md`.

Teknisk grunnlag fra fase 3 staar fortsatt: SNaive-baseline,
SARIMAX/ARIMA-kandidatgrid og LP smoke-test paa publiserbar indeks-skala.
Reell-skala LP, kalibrering av sonevise fristkapasiteter og full sensitivitetsanalyse
er fortsatt aktivt arbeidsomraade for fase 4 (men bare delvis realistisk innen
en dag - se G05_INTEGRATION_PLAN.md for ærlig scoping).

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
| 3.6 | Gjennomfore peer-to-peer review | 2026-05-08 | Completed | Hovedutkast sendt til G05 (Birgitte) 04.05; var review til G05 levert 06.05; G05s review mottatt 08.05 (dokumentet internt datert 07.05). Erik bekreftet "bestatt arbeidskravet" 30.05. |
| 3.7 | Milepael: Godkjent hovedutkast | 2026-05-08 | Completed | Arbeidskravet for peer-to-peer review er bestatt per Eriks bekreftelse 30.05. |

### Fase 4: Sluttrapport

| ID | Aktivitet | Planlagt slutt | Status | Merknad |
|----|-----------|----------------|--------|---------|
| 4.1 | Ferdigstille introduksjon | 2026-05-14 | In progress | Hovedutkast finnes. G05 ber om (a) tydeligere ramme om rammeverk+smoke-test og (b) at faglig bidrag fra 9.4 trekkes inn allerede her. Se G05_INTEGRATION_PLAN.md. |
| 4.2 | Skrive diskusjon og konklusjon | 2026-05-22 | In progress | Hovedutkast finnes. G05 ber om gap-erkjennelse (uke vs dag/sone), tydeligere implikasjoner og bedre skille mellom utviklet/dokumentert/gjenstaar. |
| 4.3 | Finpuss, kvalitetssikring og APA 7th | 2026-05-29 | MA-del fullfort | MA-lista ferdig (commit ea25e47): APA-bibliografi + Vedlegg J, forkortelsesliste, tabell-layout (0 Overfull \hbox verifisert), figurtekst-skille Figur 1-6. Endelig PDF: `014 fase 4 - report/Sluttrapport_..._endelig.pdf`. Gjenstaar: BOR-finpuss (#6 modellvalg S, #10 LP-framing, #11 sensitivitet-metode). |
| 4.4 | Milepael: Innlevering av rapport og kode | 2026-06-01 14:00 | Not started | Frist utvidet til mandag 01.06 kl. 14:00 (skiftet fra 31.05, opprinnelig 29.05). |
| 4.5 | Forberede og gjennomfore muntlig presentasjon | 2026-06-05 | Not started |  |

---

## Kritiske risikoer akkurat na

1. **Tidsbudsjett:** Bare en dag til frist. G05s top-3 (real-skala LP, kalibrere
   sonevise fristkapasiteter, full sensitivitetsanalyse) er ikke realistisk
   fullskala innen tidsrommet. Realistisk fokus: skriveflyt, APA, layout, og
   tydeligere smoke-test-ramme.
2. **Publiserbarhet vs. real-skala:** Rapporten bruker publiserbar indeks. LP
   smoke-testen kan ikke tolkes som faktisk mann-timebehov uten lokal
   `weekly_volume.csv`. G05 ber om at dette tydeliggjores enda mer i 1.1, 7.2, 8.4.
3. **Sonevise frister:** Soneandeler er etablert, men faktisk `CAP_deadline`
   for 00:00, 01:00 og 02:00 ma kalibreres for operativ bruk.
4. **Sluttvask:** Bibliografi (APA 7), tabell-/figurtekster, forkortelses-
   forklaringer (FPK/P1/P2/DD/ED/PD/LP), layout-fix av brutte tabeller paa
   side 19/23/29/30, og menneskelig korrektur.

## Prioriterte tiltak (fase 4, fra G05-review)

| Prioritet | Tiltak | Estimat | Status |
|-----------|--------|---------|--------|
| Ma | APA 7: fjern "Bruk:"-kommentarer i bibliografi (§11). | 15 min | Done (ea25e47) |
| Ma | Forkortelser introduseres ved forste forekomst (FPK, P1, P2, DD, ED, PD, LP). | 30 min | Done (ea25e47) |
| Ma | Layout-fix: tabell-tekstbrekking i §7.2, §8.4, §12 (+ §7.1, §8.3 funnet). | 30 min | Done (ea25e47) |
| Ma | Figurtekst-skille: kort figurtekst, tolkning til brodtekst med kryssreferanse. | 45 min | Done (ea25e47) |
| Bor | Innledning: rammeverk+smoke-test eksplisitt, faglig bidrag fra 9.4 hentes opp. | 30 min | Done |
| Bor | Modellvalg S (§7.2, §8.4): begrunn hvorfor RMSE prioriteres over MAE/MAPE. | 30 min | Done |
| Bor | Diskusjon: dag/sone vs uke-gap eksplisitt, implikasjoner-avsnitt utvides. | 45 min | Done (a1a726d) |
| Bor | Konklusjon: tydeligere skille utviklet vs dokumentert vs gjenstar. | 30 min | Done (a1a726d) |
| Bor | Metode §1.3: "praktisk forenkling med kjent kostnad"-formulering. | 15 min | Done (a1a726d) |
| Bor | LP smoke-test-framing §8.4 (styrk overskrift/forste setning). | 10 min | Done |
| Bor | Sensitivitetsanalyse-metode (§5.1.2 + §8.4) justert mot faktisk arbeid. | 25 min | Done |
| Kan | Reell sensitivitetsanalyse paa indeks-skala med varierte parametre. | 1-2 t | Pending |

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

## Restart checkpoint 2026-05-30 (oppdatert etter MA-okt)

**Status:** Hele MA-lista er ferdig, committet (ea25e47) og pushet til origin.
Endelig PDF bygd til `014 fase 4 - report/Sluttrapport_..._endelig.pdf` med 0 Overfull \hbox.

Ved neste arbeidsokt (ny chat for tokens) - **start rett pa BOR-lista**:

1. **Les forst** `014 fase 4 - report/Fase_4_kickoff.md`, deretter
   `014 fase 4 - report/G05_INTEGRATION_PLAN.md` (per-funn status er oppdatert der).
2. **Start arbeidet** med "Bor"-listen i tiltakstabellen over. Foreslatt forste gruppe:
   #5 innledning (ramme + faglig bidrag) + #6 modellvalg S (RMSE-begrunnelse).
3. Bruk `python "005 report/scripts/build_report_pdf_latex.py" --output "014 fase 4 - report/Sluttrapport_..._endelig.pdf"`
   (--output peker bevisst til fase 4 sa peer-review-PDF-en i `013 fase 3 - review/` ikke overskrives).
4. Hovedrapporten er `005 report/Sluttrapport_Volumprognose-Kapasitetsanalyse_DavorNecemer.md` -
   eneste innholdsfil som endres.
5. Ikke skann `000 templates/`. Ikke endre `013 fase 3 - review/` (frosset).
   Hold sensitive `004 data/`-filer lokalt/ignorert.
6. Aktiv branch `Fase_4_report`. Commit etter logiske grupper, push hyppig.

**Layout-teknikk (ikke-apenbar, fra MA-okt):** pandoc respekterer antall bindestreker
i pipe-tabellens separatorlinje som relativ kolonnebredde. Det er spaken for a hindre
at lange tokens (modellnavn, filstier) flyter inn i nabokolonner - kombinert med
`\allowbreak` i navn, `\footnotesize`-wrap og preamble `\usepackage[htt]{hyphenat}` +
`\sloppy` + `\emergencystretch` (NB: `xurl` finnes ikke i denne TinyTeX). Verifiser
alltid med xelatex-loggen: tell "Overfull \hbox"-advarsler (skal vaere 0).
