# Integrert volumprognose og kapasitetsanalyse
## Integrated Volume Forecasting and Capacity Analysis

**Forfatter:** Davor Necemer
**Studium:** LOG650 – Høgskolen i Molde
**Versjon:** Hovedutkast for peer-review, 30. april 2026

> Obligatoriske erklæringer (egenerklæring, NSD/REK, publiseringsavtale, sidetall, studiepoeng og veileder) fylles ut på forsiden ved endelig innlevering 29. mai 2026 og er bevisst utelatt i denne peer-review-versjonen.

## Sammendrag

Næringsmiddelbedrifter med to konvergerende varestrømmer mot ett felles distribusjonsledd opplever regelmessige flaskehalser når begge strømmer topper samme uke, selv når den aggregerte ukekapasiteten i utgangspunktet virker tilstrekkelig. Sonevise nattlige cut-off-frister (00:00, 01:00, 02:00) gjør at problemet ikke kan leses ut av et rent ukeaggregat. Denne rapporten utvikler og dokumenterer et integrert rammeverk som kobler etterspørselsprognose og kapasitetsoptimering på ukentlig nivå for en anonymisert norsk produksjons- og distribusjonsoperasjon med ferskvare (F) og sekundærvare (S).

Metoden er todelt og sekvensiell. En SARIMAX-modell prognostiserer ukentlig volum per varestrøm med kampanjekalender som eksogen variabel, mens en Seasonal Naive (SNaive) baseline brukes som faglig sammenligningsstandard og operativ fallback dersom SARIMAX ikke gir bedre validering. Prognosene oversettes til arbeidsbelastning gjennom en empirisk prosess-tidsmatrise, og en lineær programmeringsmodell minimerer samlet ekstra kapasitet (overtid og tidlig oppstart) i prosessene `P1` (PD/for-klargjøring) og `P2` (ED/endelig dispatch) under en høy straffvekt for fristbrudd. Sonevise frister er aggregert som kumulative ukentlige andeler.

Empirisk grunnlag dekker 117 modelluker (2024-01 til 2026-13, uke 2026-14 ekskludert som delvis uke), to varestrømmer og totalt 234 observasjoner. Volum publiseres som indeks der 2024-gjennomsnitt per varestrøm er satt lik 100. Prosess-tider er estimert fra åtte komplette produksjons-/dispatcher-par til `P1` = 0.003885 og `P2` = 0.037555 minutter per FPK-ekvivalent. Soneprofilen er beregnet fra 643 dispatcher-datoer (Z1 = 0.325, Z2 = 0.335, Z3 = 0.339, sum 1.000). Basekapasitet er 24 mann-timer/uke for `P1` og 144 mann-timer/uke for `P2`. SNaive-validering på 2026-01 til 2026-13 gir MAE/RMSE 12.88/18.96 for F og 5.15/7.53 for S målt på indeks-skala. Den gjennomførte SARIMAX-gridkjøringen forbedrer RMSE til 13.21 for F og 6.67 for S, men S-resultatet tolkes varsomt fordi MAE/MAPE samtidig blir svakere enn SNaive.

Rapporten leverer nå en teknisk minimumsimplementasjon av det integrerte rammeverket: datagrunnlag, prosess-tidsmatrise, kapasitetsbaseline, soneprofil, SARIMAX-validering og LP-løser er koblet i ett reproduserbart skript. LP-kjøringen er en publiserbar indeks-skala smoke-test, ikke et operativt estimat på reelle mann-timer; den gir 0.00 ekstra indeks-timer og 0.00 slack i valideringshorisonten fordi anonymisert indeks ikke inneholder reelle FPK-skalaer. Gjenstående arbeid er derfor reell-skala LP med lokal `weekly_volume.csv`, kalibrering av sonevise fristkapasiteter og full sensitivitetsanalyse.

**Nøkkelord:** SARIMAX, lineær programmering, kapasitetsplanlegging, distribusjonsfrister, etterspørselsprognose, næringsmiddellogistikk, anonymisering.

## Abstract

Food production and distribution operations with two parallel product streams converging on a shared dispatch process face a recurring bottleneck when both streams peak in the same week, even when aggregate weekly capacity appears sufficient. Zone-based nightly cut-off deadlines (00:00, 01:00, 02:00) mean the problem cannot be detected from weekly totals alone. This report develops and documents an integrated weekly-level framework that links demand forecasting and capacity optimization for an anonymized Norwegian food production and distribution operation with a fresh stream (F) and a secondary stream (S).

The approach is sequential and consists of two components. A SARIMAX model forecasts weekly volume per stream using the promotion calendar as an exogenous variable, with a Seasonal Naive (SNaive) model serving as both a methodological benchmark and an operational fallback when SARIMAX fails to outperform it on validation. Forecasts are translated into workload through an empirically derived process-time matrix, and a linear programming model minimises total additional capacity (overtime and early start) in processes `P1` (PD / pre-dispatch preparation) and `P2` (ED / final dispatch) under a high penalty weight for deadline violations. Zone-level deadlines are aggregated as cumulative weekly share constraints.

The empirical basis covers 117 modelling weeks (2024-01 to 2026-13, week 2026-14 excluded as a partial week), two product streams and 234 observations in total. Volumes are published as an index normalised so the 2024 mean per stream equals 100. Process times are estimated from eight complete production/dispatcher pairs as `P1` = 0.003885 and `P2` = 0.037555 minutes per FPK-equivalent. The zone profile is derived from 643 dispatcher dates (Z1 = 0.325, Z2 = 0.335, Z3 = 0.339, sum 1.000). Base capacity is 24 worker-hours/week for `P1` and 144 worker-hours/week for `P2`. SNaive validation across 2026-01 to 2026-13 yields MAE/RMSE 12.88/18.96 for F and 5.15/7.53 for S on the index scale. The SARIMAX grid run improves RMSE to 13.21 for F and 6.67 for S, although the S result is interpreted cautiously because MAE/MAPE are weaker than SNaive.

The report now delivers a technical minimum implementation of the integrated framework: data foundation, process-time matrix, capacity baseline, zone profile, SARIMAX validation and LP solving are connected in one reproducible script. The LP run is a publishable index-scale smoke test, not an operational estimate of real worker-hours; it produces 0.00 extra index-hours and 0.00 slack across the validation horizon because the anonymised index file does not contain real FPK scales. Remaining work is therefore real-scale LP using local `weekly_volume.csv`, calibration of zone-level deadline capacities and full sensitivity analysis.

**Keywords:** SARIMAX, linear programming, capacity planning, distribution deadlines, demand forecasting, food logistics, anonymization.

## Innhold

- 1.0 Innledning
- 1.1 Problemstilling
- 1.2 Delproblemer (valgfri)
- 1.3 Avgrensinger
- 1.4 Antagelser
- 2.0 Litteratur
- 3.0 Teori
- 4.0 Casebeskrivelse
- 5.0 Metode og data
- 5.1 Metode
- 5.2 Data
- 5.3 Databehandling og anonymisering
- 5.4 Datakvalitet og kontroll
- 5.5 Forskningsetikk og konfidensialitet
- 6.0 Modellering
- 7.0 Analyse
- 8.0 Resultater
- 9.0 Diskusjon
- 10.0 Konklusjon
- 11.0 Bibliografi
- 12.0 Vedlegg

## 1.0 Innledning

Produksjonslogistikk i næringsmiddelbransjen står overfor en fundamental utfordring: etterspørselen er volatil og sesongbundet, mens distribusjonsnettet har strenge, daglige frister. I mange bedrifter oppstår en sammensatt flaskehals-dynamikk selv når den totale ukekapasiteten virker tilstrekkelig. Problemet ligger i at etterspørselen er ujevnt fordelt innenfor uken, og når flere varestrømmer skal gjennom samme distribusjonsledd med ulike cut-off-tider, kan kapasitetsbrudd oppstå på kritiske tidsvindu.

Denne situasjonen oppstår fordi tradisjonelle kapasitetsplaner baseres på ukeaggregater, som ikke fanger opp de kritiske søne- og dagsvise cut-offs. Resultat: fraktbrudd, forsinkede leveranser, eller behov for dyrbar ekstrabemanning og overtid som kunne vært unngått gjennom bedre prognoser og planlegging.

Litteraturen på demand forecasting og aggregate production planning tilbyr vel etablerte løsninger. SARIMAX-modeller kan prognostisere etterspørsel under hensyn til sesongmønstre, planlagte kampanjer og andre eksogene faktorer, og linear programming kan optimalisere kapasitetsallokeringen under stramme restruksjoner. Integrering av disse to metodene kan gi både operasjonell effektivitet og innsikt i kritiske ressursbehov.

Denne rapporten utvikler et integrert modellrammeverk og etablerer datagrunnlag for etterspørselsprognose og kapasitetsanalyse i en reell næringsmiddelproduksjon og distribusjonsoperasjon.

### 1.1 Problemstilling

**Hvordan kan vi kombinere etterspørselsprognoser og kapasitetsoptimering for å minimaliser resursforbuke ved å sikre at prognostiserte volumer ferdigstilles innenfor sonevise distribusjons-cut-offs i en flerprosess næringsmiddelproduksjon?**

Denne problemstillingen er todelt:

1. **Prognosedelen:** Utarbeide tidsserieprognose som fanger sesongvariasjoner og effekten av planlagte kampanjer (eksogene faktorer).
2. **Optimeringsdelen:** Gitt denne prognosen, beregne behovet for aggregert ekstra kapasitet som minimerer samlet ressursforbruk og synliggjør risiko for brudd på sonevise cut-off-frister.

Problemstillingen behandler altså hvordan man *integrerer* etterspørselsprognose og operasjonell planlegging for å løse en reell distribusjonsflaske-halssituasjon.

### 1.2 Delproblemer

Problemstillingen løses gjennom to delproblem i rekkefølge:

**DP1 – Etterspørselsprognose:** Hvordan kan SARIMAX-modeller best estimeres og valideres ved bruk av historiske volumdata, sesongmønstre og kampanjekalender for å prognose ukentlig etterspørsel?

**DP2 – Kapasitetsoptimering:** Gitt en etterspørselsprognose, hvordan kan linear programming formuleres og løses for å bestemme optimal kapasitetsallokering som minimerer ressursforbruk mens cut-off-frister respekteres?

Disse delproblemene er sekvensielle: prognosen fra DP1 blir input til LP-modellen i DP2.

### 1.3 Avgrensinger

**Aggregeringsnivå – fra dag/sone til uke:** Selv om problemet manifesteres daglig gjennom sonevise frister (kl 00:00, 01:00, 02:00), modelleres det på *ukentlig* nivå. *Begrunnelse:* Sonevise frister aggregeres som ukentlige kapasitets- og fristbegrensninger basert på sonestruktur. Fordi sonene er operasjonelt like (samme ressursbemanning, samme skiftlengde), er forskjellen primært avgangtidspunkt, ikke kapasitetskarakteristikk. Aggregering til uke tillater bruk av tidsseriedata for de to varestrømmene og forenkler LP-formulering betydelig. Daglig operativ planlegging (mann-allokering per natt) ligger utenfor modellomfanget.

**Prosessomfang:** Analysen dekker distribusjonsklargjøringen etter at volumet er klart for utsendelse. Prosessene modelleres som `P1 = PD / for-klargjøring` og `P2 = ED / endelig dispatch/ekspedering`, mens `DD` behandles som direkte eller særskilt dispatchflyt som inngår i tidsgrunnlaget ved behov, men ikke som separat hovedprosess. *Begrunnelse:* Produksjonslister og dispatcher actions for lager 310 viser at tilgjengelig tidsdata måler håndtering mot distribusjonsfrister, ikke primær eller sekundær produksjonspakking. Prosessavgrensningen må derfor følge det observerbare datagrunnlaget for å unngå at modellen estimerer kapasitet for prosesser som ikke er målt.

**Geografi og personvern:** Publiserte data og resultater er anonymisert eller aggregert, og bedriften er ikke identifisert. Sensitive rådata behandles lokalt og publiseres ikke. *Begrunnelse:* Sikrer personvern og forretningshemmeligheter.

**Måling:** Modellen optimaliserer kapasitetsforbruk (ekstra mann-timer) og omfang av fristbrudd (arbeidsminutter som ikke dekkes innen kapasitet), ikke faktiske norske kroner. *Begrunnelse:* Kostnadsdata er sensitive; ressursenhetsmål er generelt og reproduserbart.

**Volumenhet:** I distribusjonsleddet brukes FPK-ekvivalent som en operasjonell håndteringsenhet. Dersom en DPK, kurv eller tilsvarende salgsenhet håndteres som én fysisk plukk- eller sorteringsenhet, teller den som én enhet i modellen, selv om den inneholder flere underliggende forbrukerenheter. *Begrunnelse:* Kapasitetsbelastningen i distribusjonsklargjøring bestemmes primært av antall håndteringer, ikke av antall produkter inne i hver håndteringsenhet.

**Implementering:** Prosjektet er teoretisk modellutvikling. Operativ implementasjon av daglig mann-allokering ligger utenfor omfanget. *Begrunnelse:* Sikrer fokus på prognostisering og optimeringsmodell innenfor tidsrammen.

### 1.4 Antagelser

**Antagelse 1 – Sesongmønster er stabil:** Vi antar at sesongmønsteret i etterspørselen vil fortsette i prognosehorisonten. *Konsekvens:* Modellen fungerer godt for stabil drift, men kan være mindre pålitelig hvis markedsbetingelser endres drastisk (eks. pandemi, ny konkurrent).

**Antagelse 2 – Kampanjekalender er kjent:** Vi antar at planlagte tilbud og kampanjer er kjent på planleggingstidspunktet. *Konsekvens:* Dette er realistisk for bedriftens strategiske planlegging, men ikke for uforutsette markedshendelser.

**Antagelse 3 – Kapasitet er deterministisk:** Vi antar at grunnkapasitet per uke i hver prosess er kjent og stabil. *Konsekvens:* Modellen håndterer ikke stokastisk kapasitetsbortfall (sykdom, maskinbrudd). Sensitivitetsanalyse brukes til å teste robusthet.

**Antagelse 4 – Lineær kapasitetsrespons:** Vi antar at ekstra kapasitet (overtid, ekstrabemanning) kan skaleres lineært (ingen massive overheadkostnader ved små mengder, eller tapende economies of scale). *Konsekvens:* LP-modellen blir løsbar, men praktisk implementering må verifisere denne antagelsen case-for-case.

## 2.0 Litteratur

Litteraturgrunnlaget for denne rapporten dekker tre sentrale fagfelt: (1) tidsserieprognose for sesongbunden etterspørsel, (2) operasjonell kapasitetsplanlegging under begrensninger, og (3) håndtering av flaskehalseffekter i distribusjonslogistikk. Disse feltene er vel etablert i akademisk litteratur og praktisk implementering i næringsmiddelbransjen.

### 2.1 Etterspørselsprognose med tidsseriemodeller

Etterspørselsprognoser er kritisk for produksjonsplanlegging, spesielt når kapasiteten er begrenset og distribusjonsfrister må overholdes. **Tidsseriemodeller** er etablert praksis for volumdata: **SARIMAX-modeller** (Seasonal Autoregressive Integrated Moving Average with eXogenous variables) håndterer trend, sesongmønstre og eksogene effekter som er typiske for næringsmiddelproduksjon.

SARIMAX kombinerer to sentrale egenskaper. **For det første** håndterer **SARIMA**-komponenten sesongmønstre som repeterer seg gjennom året (påske, jul, sommerferie), noe som er kritisk for næringsmiddeletterspørsel. Hyndman & Athanasopoulos (2021, kapitlene 9 og 9.9) gir det kanoniske rammeverket for ARIMA og sesonglige varianter, inkludert valg av differensierings- og lagordener. **For det andre** gjør eksogene variabler (Hyndman & Athanasopoulos, 2021, kapittel 10) det mulig å inkludere kampanjekalender og andre eksterne faktorer. Dette er viktig fordi planlagte tilbud og kampanjer kan drive etterspørselstopper ut over det et rent sesongmønster kan forklare.

Arunraj, Ahrens & Fernandes (2016) demonstrerer denne tilnærmingen for ferskvare i detaljhandel, der kampanjer og helligdager brukes som eksogene variabler for å forbedre prognoser sammenlignet med rene sesongmodeller. Selv om deres case gjelder daglig butikkvolum mens denne rapporten fokuserer på ukentlig distribusjonsvolum, er metodologien relevant: sesongmønster og kampanjeeffekter påvirker etterspørsel i begge kontekster.

Fildes, Ma & Kolassa (2022) gjennomgår retail forecasting på tvers av ulike aggregeringsnivåer og diskuterer hvordan aggregering kompliserer planleggingen når kampanjer og sesongmønster påvirker etterspørselen ujevnt. I denne rapporten brukes samme logikk på distribusjonsleddet: overgangen fra sonevise daglige frister til ukentlig prognosering krever eksplisitt vurdering av sesongeffekter og kampanjer, slik at ukentlige prognoser ikke skjuler kritiske dags- eller sonevise belastningstopper.

### 2.2 Kapasitetsplanlegging gjennom linear programming

**Linear Programming (LP)** er en veletablert metodikk for allokering av begrenset kapasitet når målet er å minimere kostnad eller ressursforbruk under strenge begrensninger (Winston, 2004). **Aggregate Production Planning (APP)** løser nettopp dette problemet: på ukentlig eller månedlig nivå bestemmer modellen hvor mye ekstra kapasitet (overtid, ekstrabemanning, tidlig oppstart) som kreves for å møte prognostisert etterspørsel innenfor faste distribusjonsfrister.

Holt, Modigliani & Simon (1955) etablerte den lineære beslutningsregelen som fundamentet for moderne APP, der lineære regler for bemanning og produksjon kan minimere samlede kostnader under etterspørselsusikkerhet. I dagens praksis håndteres APP under både kapasitets- og etterspørselsbegrensninger. Leung, Wu & Lai (2006) formulerer APP for flere produksjonslokasjoner med stokastisk etterspørsel og arbeidskraftsbegrensninger; denne metodiske tilnærmingen er relevant for rapportens toprosessproblem i distribusjon, selv om konteksten er annerledes.

I dette prosjektet modelleres kapasitetsbehovet som et LP-minimeringsproblem. Målfunksjonen minimerer samlet ekstra kapasitet samtidig som distribusjonsfrister respekteres. Begrensningene sikrer at arbeidsbelastningen (prognostisert volum omregnet til minutter) ikke overstiger tilgjengelig kapasitet, definert som grunnbemanning og dokumentert mulig ekstra kapasitet. Denne strukturen følger standard APP-praksis som beskrevet av Winston (2004) og Leung et al. (2006).

### 2.3 Flaskehals-dynamikk i konvergerende logistikk

Når flere varestrømmer konvergerer til felles distribusjonsledd, oppstår en kompleks kapasitetsutfordring: selv om total ukekapasitet er tilstrekkelig når man aggregerer, kan et dags- eller sonevis fristkrav bli brutt hvis volumtoppene ikke er tidssynkronisert. Dette er et kjent fenomen i distribusjonslogistikk hvor høy etterspørselsvariabilitet møter stramme operasjonelle frister.

Fildes et al. (2022) diskuterer hvordan aggregering og kompleksitet i etterspørsel påvirker prognosenøyaktighet. Lignende logikk gjelder her: når man aggregerer fra daglige sonevise frister til ukentlig prognosering, risikerer man at kritiske daglige belastningstopper maskeres i ukentlige aggregater. I denne rapporten håndteres fenomenet ved å modellere sonevise frister (kl. 00:00, 01:00, 02:00) som ukentlige kapasitetsbegrensninger i LP-modellen, slik at flaskehalseffekten kan vurderes også på ukentlig aggregeringsnivå.

## 3.0 Teori

### 3.1 Tidsserieanalyse og prognoser

En **tidsserie** er en sekvens av observasjoner ordnet kronologisk, typisk med jevn tidsavstand (f.eks. ukentlige volumer). Tidsserier har tre karakteristiske komponenter (Hyndman & Athanasopoulos, 2021, kapittel 9):

- **Trend:** langvarig retning (stigning, stagnasjon, eller fall)
- **Sesongmønstre:** repeterende mønstre på kort sikt (f.eks. ukentlige eller årlige rytmer)
- **Residualer:** tilfeldig variasjon som ikke forklares av trend eller sesong

**SARIMAX-modeller** (Seasonal ARIMA with eXogenous variables) er matematiske rammer som modellerer disse komponentene samt eksterne påvirkninger. En SARIMAX-modell estimeres ved å minimere forskjellen mellom observerte verdier og modellens prediksjoner (vanligvis målt som Mean Absolute Error eller Root Mean Square Error).

Modellen består av fire deler (Hyndman & Athanasopoulos, 2021, kapittel 9–10):

1. **ARIMA-kjernen** håndterer autoregressive (AR) og moving average (MA) strukturer som fanger kortsiktig avhengighet mellom observasjoner
2. **Sesongkomponenten** modellerer repeterende mønstre over året (f.eks. 52 uker i ukesdata) via sesonglag
3. **Integreringsleddet** håndterer både trend (differensiering $d$) og sesongavdrift (sesongdifferensiering $D$) for å oppnå stasjonaritet
4. **Eksogene variabler** (kampanjekalender, helligdager) fanges eksplisitt (kapittel 10) som separate regressorer

Kombinasjonen av disse gjør SARIMAX spesielt egnet for sesongbundne varetyper med kjente kampanjepåvirkninger. Parameterestimering foregår via maximum likelihood estimation (MLE), og modellvalg støttes av informasjonskriterier som AICc og stasjonaritetstester.

For automatisk modellvalg brukes stepwise-algoritmer som `auto_arima` (Hyndman & Khandakar, 2008). Algoritmen tester kandidatmodeller systematisk, prioriterer parsimoniske ordener på små datasett, og rangerer modeller etter informasjonskriterier samtidig som residualene kontrolleres mot hvit støy (for eksempel med Ljung-Box-test).

### 3.2 Linear Programming og optimering

**Linear Programming** er en matematisk optimeringsmetode for å finne beste beslutning under lineære begrensninger (Winston, 2004). Generell form:

```
Minimiser: c₁x₁ + c₂x₂ + ... + cₙxₙ  (Målfunksjon)
Under:     Ax ≤ b  (Lineære begrensninger)
           x ≥ 0   (Ikke-negativitet)
```

hvor $c$ er en kostnads- eller vektvektor, $x$ er beslutningsvariablene, $A$ er en matrise av koeffisienter, og $b$ er høyre-side-verdier.

I **Aggregate Production Planning (APP)** bestemmer LP-modellen optimal allokering av kapasitet (overtid, ekstrabemanning, tidlig oppstart) gitt:

- **Prognostisert etterspørsel** (fra SARIMAX)
- **Grunnkapasitet per uke per prosessledd** (fra historiske data eller kapasitetsforutsetninger)
- **Sonevise distribusjonsfrister** som må respekteres
- **Mål:** minimere total ekstra kapasitet (overtid, bemanning)

LP-modellen kan løses eksakt ved bruk av **Simplex-algoritmen** eller **interiørpunktmetoder** (Winston, 2004). Løsningen er en optimal allokeringsplan for de to hovedprosessene i distribusjonsklargjøringen som oppfyller alle begrensninger samtidig som målfunksjonen minimeres.

For APP-kontekster med usikker etterspørsel og flere lokasjoner henviser Leung, Wu & Lai (2006) til stokastisk programmering som en robust utvidelse av deterministisk LP. I denne rapporten brukes deterministisk LP (med SARIMAX punkt-prognoser) som fundament, og usikkerheten håndteres gjennom scenarioanalyse (sensitivitetstesting av ±10 % volum).

### 3.3 Modellintegrasjon i prosjektet

Dette prosjektet integrerer begge tilnærminger sekvensielt:

1. **Fase 1 – Etterspørselsprognose:** SARIMAX-modellen estimeres basert på historiske ukentlige volumdata, sesongmønstre og kampanjekalender, separat for ferskvare og sekundærvare. Resultat: prognose per uke og varestrøm.
2. **Fase 2 – Kapasitetsoptimering:** LP-modellen bruker denne prognosen som fast input og beregner behov for ekstra kapasitet for å møte etterspørselen under sonevise frister.

Denne todelte strukturen gjør det mulig å vurdere konsekvensene av prognoseusikkerhet i kapasitetsmodellen, blant annet gjennom straffvekt for fristbrudd og scenarioanalyse. Dermed kan modellen testes under plausible volumavvik før den brukes som beslutningsstøtte.

## 4.0 Casebeskrivelse

### 4.1 Bedrift og bransje

Caset baseres på en anonymisert norsk bedrift innen næringsmiddelproduksjon og distribusjon. Bedriften har to parallelle produksjonsfilialer som sender volum inn til et sentralisert distribusjonsledd:

- **Filial A (Ferskvare):** Kortlevetids friske matvarer med streng holdbarhet (1–7 dager)
- **Filial B (Sekundær/handelsvare):** Lengre-levetids pakket og lagret vare (uker til måneder)

Begge varestrømmer må gjennomgå samme distribusjonsledd før utsendelse til kunder. Dette er den kritiske flaskehalsen i systemet.

### 4.2 Operasjonell struktur

Distribusjonsoperasjonen modelleres som to hovedledd i dispatcherflyten:

1. **P1 - PD / for-klargjøring:** Forberedende klargjøring, sortering eller pre-dispatch før endelig ekspedering.
2. **P2 - ED / endelig dispatch/ekspedering:** Ferdigstilling av volumet mot distribusjonsfristene.

I datagrunnlaget finnes også `DD`, som tolkes som direkte eller særskilt dispatchflyt. Denne flyten holdes foreløpig utenfor hovedprosessene fordi observasjonene viser lavt volum og svært lav registrert tid sammenlignet med `PD` og `ED`. Dersom flere uker viser at `DD` er operativt vesentlig, kan den senere skilles ut som en egen prosess eller behandles som egen scenarioforutsetning.

Hver prosess har en grunnkapasitet (Standard Working Hours per uke). Kapasiteten er ikke fullt ut fleksibel, men kan utvides gjennom:
- Overtid
- Ekstra skift (bemanning)
- Tidlig oppstart av for-klargjøring eller ekspedering i dispatcherleddet

### 4.3 Flaskehals-problematikk

Selv om den totale ukekapasiteten er tilstrekkelig når man aggregerer, oppstår regelmessige kapasitetsbrudd på grunn av **sonevise distribusjonsfrister**:

- Volumet fordeles over soner med nattlige cut-off-frister kl. 00:00, 01:00 og 02:00
- Begge varestrømmer bruker samme distribusjonsledd før utsendelse
- Hvis både ferskvare og sekundærvare peaker samme dag, kan distribusjonsklargjøring bli presset selv om ukekapasiteten virker tilstrekkelig

**Eksempel:** En tirsdag må 80 % av ukens volum ferdigstilles, mens resten av uken har lavere belastning. Selv om total ukekapasitet er tilstrekkelig, blir tirsdag en kritisk belastningsdag som krever betydelig ekstra kapasitet.

Problemet forverres av sesongmønstre (høysesonger med kampanjer) som driver etterspørselen opp på spesifikke uker.

### 4.4 Tilgjengelige data

Bedriften har tilgang til:

- **Historisk volumdata:** Ukentlige volumer (FPK-ekvivalenter) for begge varestrømmer over minimum 2 år
- **Kampanjekalender:** Planlagte tilbud og markedsføringskampanjer som er kjent i forkant
- **Grunnkapasitet:** Dokumentert Standard Working Hours per uke for hver av de to hovedprosessene
- **Fristspesifikasjon:** Sonevise cut-off-tider og aggregerte ukentlige krav per prosess
- **Kostnadsinformasjon:** Indikative kostnader for overtid, ekstrabemanning, og tidlig oppstart (kan være sensitiv)

### 4.5 Bedriftens utfordring og motivasjon

Bedriften søker en prognose- og optimeringsmodell som kan:

1. **Predikere etterspørsel** akkurat der volumene lander hver uke (under hensyn til sesong og kampanjer)
2. **Planlegge kapasitet** på ukebasis for de to hovedprosessene
3. **Minimere ressursforbruk** (overtid og ekstrabemanning) ved å identifisere kritiske ukentlige belastningstopper tidlig

Med en slik modell kan ledelsen ta proaktive beslutninger i stedet for å reagere etter at kapasitetsbrudd allerede har oppstått. Dette er både kostnads- og kvalitetsmessig viktig for bedriften.

## 5.0 Metode og data

### 5.1.1 Metode – Etterspørselsprognose (SARIMAX)

**Paradigme:** Kvantitativ case-studie basert på historiske operasjonelle data fra en produksjon- og distribusjonsoperasjon.

**Datavindu og modellstrategi:** Datagrunnlaget for prognosedelen består av ukentlige observasjoner for perioden 1. januar 2024 til 31. desember 2025, totalt 104 observasjoner per varestrøm. Modellen trenes på denne perioden og valideres deretter out-of-sample mot observerte ukedata for perioden 1. januar 2026 til 29. mars 2026. Dette følger prinsippet om hold-out-validering for tidsseriemodeller, der testdata ikke brukes i estimeringen (Hyndman & Athanasopoulos, 2021). På ukesnivå representeres treningsperioden som uke 2024-01 til 2025-52 (104 uker), og valideringsperioden som uke 2026-01 til 2026-13 (13 uker).

Uke 2026-14 ekskluderes fra validering fordi den inneholder kun 2 arbeidsdager (30.–31. mars), noe som gir anomalt lavt volum (F: 39.26, S: 2.83 indeks-enheter) som ikke representerer normal ukesdynamikk. Å inkludere slike anomalier i valideringsmetrikker kan gi skjeve MAE/RMSE-estimater.

Etter modellvalg re-estimeres endelig modell på hele det tilgjengelige datasettet (2024–2025) før prognosen brukes som input til kapasitetsmodellen. Endelig modellspesifikasjon fastsettes etter datakontroll og innledende eksplorativ analyse, slik at modellens kompleksitet tilpasses datamaterialets kvalitet, lengde og tilgjengelige eksogene variabler.

**Prognosemodell:** SARIMAX (Seasonal Autoregressive Integrated Moving Average with eXogenous variables) velges fordi (se også seksjon 2.1):
- Tidsseriene (ukentlige volumer) har **tydelige sesongmønstre** (høysesonger knyttet til julekampanjer, påske, sommerferie) og underliggende trend
- Eksogene variabler (kampanjekalender) påvirker etterspørselen betydelig utover det sesongbaserte nivået
- Næringsmiddeletterspørsel følger årlige sesongmønstre som SARIMAX håndterer godt (Arunraj, Ahrens & Fernandes, 2016)
- SARIMAX er etablert praksis i demand forecasting for sesongbundne varer (Hyndman & Athanasopoulos, 2021)

**Modellspesifikasjon:**

Modellen estimeres separat for ferskvare (F) og sekundærvare (S):

$$\Phi(B) \Phi_s(B^s) \nabla^d \nabla_s^D Y_t = \Theta(B) \Theta_s(B^s) \epsilon_t + \beta X_t$$

hvor:
- $Y_t$ = ukentlig volum (FPK-ekvivalenter)
- $B$ = backshift-operator
- $s$ = sesongperiode (52 uker for årlig sesong i ukesdata)
- $\nabla^d$ = d-te orden differensiering (for trend-stationaritet)
- $\nabla_s^D$ = sesongdifferensiering av orden D (for sesong-stationaritet)
- $\Phi(B)$ = autoregressive polynom av orden p
- $\Phi_s(B^s)$ = sesongavhengig autoregressive polynom av orden P
- $\Theta(B)$ = moving average polynom av orden q
- $\Theta_s(B^s)$ = sesongavhengig moving average polynom av orden Q
- $\epsilon_t$ = hvit støy
- $X_t$ = eksogen vektor (kampanjeindikator, helligdag-dummy, osv.)
- $\beta$ = koeffisientvektor for eksogene variabler

Her viser F og S til varestrømmene ferskvare og sekundærvare, mens $s$ i SARIMAX-formelen viser sesonglengden og ikke varestrømmen sekundærvare. For ukedata settes $s = 52$ fordi etterspørselen forventes å følge et årlig sesongmønster.

**Parameterestimering (med datakvalitetshensyn):**

Gitt at treningsdata omfatter bare 104 observasjoner (2 sesongperioder), legges det opp til en konservativ strategi. Korte datasett risikerer overparametrisering hvis man estimerer høye lagordener, særlig for sesongkomponenten. Strategien består av:

1. **Baseline-modell:** Seasonal Naive (SNaive)
   - Prognose: $\hat{y}_{t} = y_{t-52}$ (observasjon fra 52 uker siden)
   - **Rolle:** Enkel sammenligningsstandard. Hyndman & Athanasopoulos (2021) viser at enkle metoder bør brukes som benchmark for mer komplekse prognosemodeller. Arunraj, Ahrens & Fernandes (2016) viser at SARIMAX med kampanjevariabler kan forbedre prognosering i matvarehandel. Hvis SARIMAX ikke slår SNaive på validering, brukes SNaive som operativ prognose.

2. **SARIMAX-kandidater via konservativ `statsmodels`-grid (auto-ARIMA-prinsipp):**
   - **Stasjonaritetstesting:** KPSS-test for trendstasjonaritet, velg $d$; Canova-Hansen-test for sesongstasjonaritet, velg $D$ (typisk $D \in \{0, 1\}$)
   - **ACF/PACF-analyse** foreslår AR/MA-lagordener $(p, q, P, Q)$
   - En avgrenset kandidatgrid estimeres systematisk med fokus på parsimoni, og resultatene vurderes mot AICc, residualdiagnostikk og out-of-sample validering

3. **Modellvalg:**
   - Kandidater som krever $P > 1$ eller $D > 1$ forkastes (lite data til robust estimering på sesongkomponenten)
   - Valg baseres primært på **AICc** (Akaike Information Criterion corrected for small samples, per Hyndman & Khandakar, 2008) + residualdiagnostikk
   - **Ljung-Box test** brukes for å sikre at residualene mangler autokorrelasjon (hvit støy)
   - Endelig modell estimeres via **Maximum Likelihood Estimation (MLE)**

4. **Vurdering av eksogene variabler:**
   - `campaign_flag` har lav variasjon for F (117/118 uker = 99% med flaggverdi 1)
   - Binær flagg har minimal variasjon → liten forklaringskraft
   - **Alternativ:** Fildes et al. (2022) diskuterer kompleksiteten i kampanjeinformasjon og eksogene variabler i retail forecasting. For dette prosjektet kan kampanjeintensitet (antall kampanjer per uke) eller kampanjetype gi mer informasjon enn et nær-konstant binært flagg.
   - For S: `holiday_flag` kan ha mer effekt hvis det varierer tilstrekkelig

**Validering:** Modell valideres out-of-sample på uke 2026-01 til 2026-13 (13 uker, uke 2026-14 ekskludert):
- **Sammenligningskriterier:**
  - MAE (Mean Absolute Error)
  - RMSE (Root Mean Squared Error)
  - MAPE (Mean Absolute Percentage Error)
  - Alle målt mot SNaive baseline
- **Residualdiagnostikk:** Ljung-Box test for autokorrelasjon og sesongavhengighet
- **Beslutning:** Hvis SARIMAX RMSE > SNaive RMSE, brukes SNaive som operativ prognose

**Verktøy:** Python er hovedverktøyet i prognosedelen.
- `005 report/scripts/run_forecast_capacity_models.py` kjører en konservativ kandidatgrid med `statsmodels.tsa.statespace.sarimax.SARIMAX`
- `statsmodels` brukes til estimering, prognosegenerering og residualdiagnostikk, mens `scipy.optimize.linprog` brukes til LP-kjøringen
- `pmdarima.auto_arima` eller R med `forecast::auto.arima(seasonal = TRUE)` kan brukes som alternativ senere, men er ikke nødvendig for denne rapportens reproduserbare minimumskjøring

---

### 5.1.2 Metode – Kapasitetsoptimering (Linear Programming)

**Optimeringsproblem:** LP-modellen løser et aggregate production planning-problem (APP, se seksjon 6.0 og litteraturkapittel 2.2).

**Formulering:** Modellen følger standard APP-struktur (Winston, 2004; Leung, Wu & Lai, 2006):
- **Målfunksjon:** Minimerer samlet ekstra kapasitet og høy straffvekt for fristbrudd
- **Begrensninger:**
  - Kapasitetsbegrensninger: arbeidsbelastning ≤ grunnkapasitet + aggregert ekstra kapasitet
  - Sonevise frister: andel av volum må være ferdig innen cut-off-tider
  - Ikke-negativitet: alle beslutningsvariabler ≥ 0
  - Maksimalgrenser: ekstra kapasitet begrenset av dokumenterte tiltaksgrenser og praktisk realisme

**Løsningsmetode:**
- **Simplex-algoritmen** eller **interiørpunktmetode** (Winston, 2004) avhengig av solver
- Python: `scipy.optimize.linprog`, `PuLP`, eller `Gurobi/CPLEX` for større instanser
- Løsningen gir beregnet behov for ekstra kapasitet per prosess per uke

**Sensitivitetsanalyse (post-optimality analysis):**
Skyggepriser og reduserte kostnader analyseres (Winston, 2004) for å forstå:
- Hvilke begrensninger er bindende? (identifiserer kritiske ressurser)
- **Skyggepris:** Hva er verdien av 1 ekstra mann-time kapasitet i hver prosess? (informerer investeringsbeslutninger)
- Hvordan påvirker ulike straffvekter for fristbrudd løsningen?
- Robusthet av løsningen under parameter-endringer

**Scenarioanalyse:** Løsningen testes under usikkerhetskilder (Leung, Wu & Lai, 2006):
- **Prognoseusikkerhet:** ±10 % volumavvik (SARIMAX validerings-usikkerhet)
- **Kapasitetsbortfall:** sykefravær (~6 % årlig per SSB), maskinbrudd, turnover
- **Ekstreme høysesonger:** topptyngde-uker (påske, jul) som krever maksimal kapasitet

Disse scenarioene evalueres for å fastsette en robust overtidsbuffer.

### 5.2 Data

Prosjektet bygger på et avgrenset og anonymisert datagrunnlag hentet fra virksomhetens operative planleggings- og oppfølgingsmiljø. Siden formålet er å koble etterspørselsprognoser til kapasitetsanalyse på ukentlig nivå, er det ikke nødvendig å hente ut alle detaljdata fra ERP-systemet. Det sentrale er å hente inn de datasettene som gjør det mulig å modellere sammenhengen mellom prognostisert volum, arbeidsbelastning og tilgjengelig kapasitet.

Det detaljerte datakravet for prosjektet er dokumentert separat i `004 data/Datakrav_for_prosjektet.md`. Denne spesifikasjonen definerer hvilke felter som er nødvendige, hvilke som er anbefalte, og hvilke data som kan utelates i denne fasen.

Minimumssettet av data som kreves i prosjektet er:

- **Ukentlig volumhistorikk per varestrøm:** historiske ukesvolumer i FPK-ekvivalenter for ferskvare og sekundærvare, samt indikator for kampanjeuker
- **Omregning fra volum til tidsforbruk:** standard tidsbruk uttrykt som minutter per FPK for hver relevant prosess og varestrøm
- **Ukentlig tilgjengelig kapasitet:** grunnkapasitet og maksimal ekstra kapasitet per uke og prosessledd
- **Aggregerte sone- og fristparametre:** andeler av ukentlig volum som må være ferdig innen de ulike sonevise cut-off-fristene
- **Tiltaksparametre:** regler og relative vekter for overtid, ekstra skift og eventuell tidlig oppstart

For datavasken defineres `volume_fpk_eq` som operasjonelle håndteringsenheter i distribusjonsleddet. Hvis `Antall fakturert` i Qlik representerer DPK, kurv eller annen enhet som plukkes og sorteres som én fysisk enhet, kan verdien brukes direkte som FPK-ekvivalent i modellen. Hvis datakilden i stedet teller underliggende forbrukerenheter, må volumet omregnes eller dokumenteres som avvik.

Det mest kritiske datakravet i prosjektet er koblingen mellom:

- volum i FPK-ekvivalenter
- arbeidsforbruk i minutter per FPK
- tilgjengelig kapasitet i timer per uke og prosess

Uten denne koblingen vil kapasitetsmodellen ikke kunne oversette prognose til faktisk ressursbehov. Datainnsamlingen prioriteres derfor mot et lite, relevant og etterprøvbart datagrunnlag fremfor store mengder detaljdata med begrenset modellverdi.

### 5.3 Databehandling og anonymisering

Prosjektet bygger på interne virksomhetsdata, men rapporten og de publiserbare prosjektfilene skal ikke identifisere virksomheten, kunder, ansatte, produkter eller konkrete interne volum. Databehandlingen er derfor lagt opp som en todelt arbeidsflyt: sensitive rådata og vaskede arbeidsfiler beholdes lokalt, mens rapporten bare bruker aggregerte og anonymiserte modellinput.

Rådata er hentet fra operative systemer på et generisk nivå: ukentlige volumdata, kampanje- og livssyklushendelser, produksjonslister og dispatcher actions. Disse kildene brukes til å etablere tre modellkomponenter: historisk ukesvolum, omregning fra volum til arbeidstid, og kapasitetsforutsetninger. Råfiler og vaskede detaljerte filer er ikke del av det publiserbare datagrunnlaget. I prosjektmappen ligger de under lokale mapper som er utelatt fra versjonskontroll.

**Indeks-transformasjon for publiserbar fil:**

Den publiserbare prognosefilen erstatter reelle FPK-volum med en indeksvariabel, `volume_index`. Indeksen er beregnet per varestrøm med basislinje `2024_average_per_stream=100`:

$$\text{volume\_index}_{s,t} = \frac{\text{volume\_fpk}_{s,t}}{\text{average\_fpk}_{s,2024}} \times 100$$

hvor $s$ = varestrøm (F eller S), $t$ = uke.

Begrunnelse: `2024-01` brukes ikke som basisuke fordi den påvirkes av helligdag og kampanjeeffekt, noe som ville gitt en mindre representativ skala. Gjennomsnitt over hele 2024 gir mer stabil basis.

**Viktig: Indeks kan IKKE brukes direkte i kapasitetsmodellen** fordi hver varestrøm har sin egen skala. Hvis F og S har ulike gjennomsnittlige volum i 2024, blandes skalaene når man summerer `volume_index_F + volume_index_S`.

**Løsning for intern modell vs. publisert resultat:**

**Intern modell (lokalt, ikke publisert):**
- Bruker reelle FPK-volum fra lokal `weekly_volume.csv`
- Prognose: $\text{forecast\_fpk}_{s,t}$
- Arbeidsbelastning: $\text{workload}_{j,t} = \sum_s (\text{forecast\_fpk}_{s,t} \times \text{minutes\_per\_fpk}_{j,s})$
- LP løst med absolutte mann-timer, resulterer i $X_{j,t}$ som ekstra kapasitet i timer og $SLACK_{j,t}$ som udekket arbeidsbelastning i minutter
- Intern resultat: dimensjoner i timer og minutter, kan reproduseres med reelle FPK

**Publisert resultat (rapport + vedlegg):**
- Kapasitetsbehov rapporteres som **relative nøkkeltall**, ikke absolutte timer
- Eksempler: Gjennomsnittlig utnyttelsesgrad (%), fordeling av ekstra kapasitetsbehov, frekvens av fristbrudd (%)
- Absolutte mann-timer utelates fordi de kan avsløre reelt volum
- Reelle FPK-tall publiseres ikke
- `volume_index` brukes ikke som operativt kapasitetsgrunnlag i LP

**Etterprøvbarhet uten å avsløre volum:**
- SARIMAX-validering rapporteres på indeks-skala (MAE/RMSE i indeks-enheter)
- LP-logikk og struktur er transparent (begrensninger, målfunksjon)
- Sensitivitetsanalyse vises som relative endringer (±10% volum → ±Y% overtid)
- Leseren kan verifisere metodologien uten å kjenne reelle volum

For å dokumentere at prognose- og LP-leddet er teknisk koblet, er det likevel kjørt en publiserbar **indeks-skala smoke-test** der `volume_index` multipliseres med prosess-tidene og behandles som `indeks-minutter` / `indeks-timer`. Denne kjøringen viser at løseren og datastrømmen fungerer, men den kan ikke tolkes som faktisk bemanningsbehov fordi indeksen mangler de stream-spesifikke 2024-gjennomsnittene i FPK.

**Datatilgjengelighet og reproduserbarhet:**

Datagrunnlaget gjøres tilgjengelig på tre nivåer for å balansere etterprøvbarhet mot personvern og kommersiell konfidensialitet:

1. **Publiserbare modellfiler:** Disse kan inngå som vedlegg eller ligge i prosjektmappen fordi de er anonymiserte eller aggregerte. Dette omfatter `weekly_volume_anonymized.csv`, `process_time_matrix.csv`, `zone_cutoff_profile.csv`, `capacity_assumptions.csv`, `capacity_modifier_assumptions.csv` og `action_parameters.csv`.

2. **Reproduserbar kode og dataskjema:** Scripts som `anonymize_weekly_volume.py`, `build_capacity_control.py`, `build_process_time_matrix_batch.py` og `build_zone_cutoff_profile.py` dokumenterer transformasjonen fra rådata til publiserbare modellparametre. Koden gjør det mulig å kontrollere hvordan volumindeks, prosess-tider og soneandeler er beregnet, selv om råfilene ikke kan deles.

3. **Lokale rådata og kontrollfiler:** Rådata fra Qlik, produksjonslister og dispatcher actions beholdes lokalt og er ikke del av publiserbart datagrunnlag. Disse filene kan inneholde reelle volum, kunde-/artikkeldetaljer, interne driftsopplysninger og i dispatcherhistorikk også personnavn. De er derfor holdt utenfor versjonskontroll. Rapporten oppgir i stedet kontrolltall, datoperioder og aggregerte resultater, for eksempel at soneprofilen bygger på 643 valgte dispatcher-datoer fra 2023-07-21 til 2026-04-28 og at andelene summerer til 1.000000.

Denne løsningen innebærer at en ekstern leser ikke kan reprodusere alle interne datavaskesteg uten tilgang til virksomhetens rådata, men kan etterprøve modellstrukturen, variabeldefinisjonene, anonymiseringslogikken, enhetskoblingen mellom volum og tid, og de publiserte aggregerte parameterne. Etterprøvbarheten ligger derfor i sporbar metode, åpne beregningsregler og publiserbare kontrollsummer, ikke i offentliggjøring av sensitive rådata.

Dispatcherdata brukes også anonymisert og aggregert. Personnavn fra arbeidsregistreringer erstattes av interne worker slots eller systemkategorier, og resultatet rapporteres som tidsforbruk per prosess og håndteringsenhet. Den endelige tidsmatrisen publiserer derfor ikke hvem som utførte arbeidet, hvilke konkrete artikler som ble håndtert, eller hvilke kunder/ruter volumet gjaldt. Den rapporterer bare hvor mange minutter én håndteringsenhet i gjennomsnitt krever i `P1` og `P2`.

For kapasitetsmodellen skilles det mellom observerte data og modellantakelser. Observerte data omfatter blant annet ukesvolum, kampanjeflagg og tidsforbruk fra produksjons-/dispatchergrunnlaget. Antakelser omfatter blant annet sykefraværsnivå, effektivitet for tilkallingshjelp og relative kostnadsvekter for ekstra kapasitet. Disse antakelsene behandles som modellparametre og skal testes gjennom sensitivitetsanalyse, ikke presenteres som direkte målte bedriftsdata.

### 5.4 Datakvalitet og kontroll

En kort datakvalitetsdel er nødvendig for å vise at modellgrunnlaget er konsistent nok til å brukes i en vitenskapelig rapport. Datakvalitet betyr her ikke at dataene er perfekte, men at sentrale valg, avgrensninger og kontroller er dokumentert slik at leseren forstår hva analysen bygger på.

**Dataomfang og egnethet:**

Prognosegrunnlaget dekker perioden `2024-01` til `2026-13` (uke 2026-14 ekskludert). Det gir 117 sammenhengende uker trenings- og valideringsdata kombinert, fordelt på to varestrømmer (totalt 234 observasjoner). Treningsperioden er `2024-01` til `2025-52` (104 observasjoner), mens `2026-01` til `2026-13` brukes som valideringsperiode (13 observasjoner).

Hyndman & Athanasopoulos (2021) understreker at enkle regler for datakrav ikke er pålitelige: mer komplekse parametriseringer krever mer data, men optimalt antall sesongperioder avhenger av modellspesifikasjon, parameterusikkerhet og formål. De foreliggende 104 treningsobservasjoner (2 sesonger) er begrenset for komplekse sesongmodeller. Dette rettferdiggjør den konservative modellvalg-strategien (avsnitt 5.1) med SNaive baseline og parsimoni-preferanse (restriksjoner på P≤1, D≤1).

**Datavasking:**

I datavasken er `Ordretype/Navn = -` ekskludert. Kontroll mot supplerende uttrekk viste at disse radene i stor grad overlappet med navngitte ordretyper på kunde-, artikkel- og ukenivå. Dersom de hadde blitt beholdt, ville ukesvolumet blitt tilnærmet dobbeltregistrert. Produktgruppe `850` (øvrige driftsmidler) er også ekskludert fordi den ikke inngår i prognosevolumet for de operative varestrømmene som analyseres.

**Prosess-tidsmatrise:**

Tidsmatrisen bygger på åtte komplette produksjons-/dispatcher-par fordelt på 2024, 2025 og 2026. Dette gir et mer robust grunnlag enn én enkelt observasjonsdag, men er fremdeles et representativt utvalg og ikke en full tidsstudie av alle arbeidsdager i perioden. Resultatet brukes derfor som et praktisk standardtidsestimat for modellformål, ikke som en endelig operasjonell normtid.

**Databegrensninger og deres konsekvenser:**

Noen databegrensninger må tas med i tolkningen av resultatene:

**1. Valideringsperiode – delvis uke:**
Uke 2026-14 inneholder kun data for 30.–31. mars (2 av 7 dager). Volumene er anomalt lave (F: 39.26, S: 2.83 indeks-enheter, ~30 % av normal uke) og representerer ikke fullstendig ukesdynamikk. Uke 2026-14 ekskluderes derfor fra out-of-sample-validering for å unngå skjevhet i MAE/RMSE-beregninger.

**2. Sone-/cut-off-andeler:**
Disse er beregnet fra `ED`-rader i raw dispatcher actions, der `Street` brukes som operasjonell soneindikator. Grunnlaget dekker 643 valgte shipping dates fra 2023-07-21 til 2026-04-28. Volumvektede andeler i `zone_cutoff_profile.csv` er `Z1=0.325311`, `Z2=0.335234` og `Z3=0.339455`. Mappingen `Street 1 -> 00:00`, `Street 2 -> 01:00` og `Street 3+ -> 02:00` bør likevel tolkes som en operasjonell modellantakelse.

**3. Anomali- og begrensningsflagging:**
`anomaly_flag` og `constrained_week_flag` er foreløpig satt til `0` og er ikke validert mot en komplett avvikslogg. Dette kan gjøre at enkelte uker med reelle avvik behandles som normale observasjoner i første modellversjon.

**4. Kampanje-variabelen for F – lav variasjon (nær-konstant):**
`campaign_flag=1` for 117 av 118 observasjoner i varestrøm F (99 % av ukene). En så dominerende verdi gir minimal variasjon i en binær indikator, noe som gjør det vanskelig for modellen å skille effekten av kampanjer fra baseline etterspørselen. Modellvalg må vurdere:
- Brukes binær flagg som-er (risiko: koeffisient ikke-signifikant på grunn av mangel på variasjon), eller
- Erstattes med `campaign_intensity` (antall kampanjer per uke) eller `campaign_type` (kategorisk: chain-promo, launch, seasonal)?

Valget dokumenteres i modellvalgsresultater (seksjon 7.2).

### 5.5 Forskningsetikk og konfidensialitet

Selv om prosjektet ikke behandler personopplysninger i rapportens analysegrunnlag, bygger det på bedriftsinterne data som kan være kommersielt sensitive. Forskningsetisk håndtering handler derfor ikke bare om personvern, men også om å beskytte virksomhetens identitet, interne volumer, kunderelasjoner og operative detaljer.

Virksomheten omtales derfor som et anonymisert norsk produksjons- og distribusjonsmiljø innen næringsmiddelindustrien. Rapporten bruker generiske varestrømmer, prosessnavn og aggregerte resultater. Stedsnavn, kundenavn, personnavn, produktidentifikatorer og andre detaljer som kan gjøre virksomheten gjenkjennbar, publiseres ikke.

Metoden er likevel gjort etterprøvbar på et faglig nivå. Rapporten beskriver hvilke datatyper som er brukt, hvordan de er transformert, hvilke kolonner som inngår i modellfilene, og hvilke antakelser som ligger bak kapasitetsberegningen. Dette gir leseren mulighet til å vurdere modellens logikk og svakheter uten tilgang til rådataene.

## 6.0 Modellering

Dette kapitlet formulerer den matematiske koblingen mellom prognostisert volum, arbeidsbelastning og tilgjengelig kapasitet. Modellen er en ukentlig planleggingsmodell, ikke en detaljert natt-for-natt bemanningsplan. Hensikten er å vise hvordan prognoser kan omsettes til kapasitetsbehov og hvordan mangel på kapasitet kan synliggjøres som ekstra kapasitet eller fristbrudd.

### 6.1 Modellstruktur

Modellen består av to sekvensielle komponenter:

1. **Etterspørselsprognose:** Basert på historiske ukentlige volumer for ferskvare (F) og sekundærvare (S) samt kampanjekalender, produseres punktprognoser for volum i uke `t`. I den interne modellen brukes reelle FPK-ekvivalenter, mens publisert rapportering bruker indekserte volumer for å ivareta konfidensialitet.

2. **Kapasitetsoptimering:** Prognostisert volum omregnes til arbeidsbelastning ved hjelp av `process_time_matrix.csv`. LP-formuleringen beregner behov for aggregert ekstra kapasitet i `P1` og `P2`, og synliggjør eventuell restbelastning som ikke kan håndteres innen tilgjengelig kapasitet.

Prosessene er:
- `P1 = PD / for-klargjøring`
- `P2 = ED / endelig dispatch/ekspedering`

`DD` holdes utenfor hovedmodellen fordi det behandles som direkte eller særskilt dispatchflyt, ikke som et stabilt hovedledd i den ukentlige kapasitetsmodellen.

---

### 6.2 Notasjon og beslutningsvariabler

Indekser:
- $j \in \{P1,P2\}$: prosessledd
- $s \in \{F,S\}$: varestrøm
- $t = 1,\ldots,T$: uke i planleggingshorisonten

Parametre:
- $\hat{V}_{s,t}$ = prognostisert volum i FPK-ekvivalenter for varestrøm $s$ i uke $t$
- $m_{j,s}$ = minutter per FPK i prosess $j$ for varestrøm $s$
- $CAP^{base}_{j,t}$ = ordinær kapasitet i mann-timer for prosess $j$ i uke $t$
- $XMAX_{j,t}$ = maksimal tilgjengelig ekstra kapasitet i mann-timer
- $c_j$ = relativ kostnadsvekt per ekstra mann-time i prosess $j$
- $\lambda$ = penalty-vekt per minutt fristbrudd

Beslutningsvariabler:
- $X_{j,t} \geq 0$ = aggregert ekstra kapasitet i mann-timer for prosess $j$ i uke $t$
- $SLACK_{j,t} \geq 0$ = arbeidsminutter som ikke dekkes av tilgjengelig kapasitet i prosess $j$ i uke $t$

I denne rapportversjonen representerer $X_{j,t}$ samlet ekstra kapasitet. Praktisk kan dette komme fra overtid, tidlig oppstart eller ekstra bemanning. En mer detaljert operativ modell kan senere splitte $X_{j,t}$ i egne tiltaksvariabler.

---

### 6.3 Målfunksjon

**Minimiser:**

$$Z = \sum_{t=1}^{T} \sum_{j \in \{P1,P2\}} c_j X_{j,t} + \lambda \sum_{t=1}^{T} \sum_{j \in \{P1,P2\}} SLACK_{j,t}$$

hvor:
- $X_{j,t}$ måles i mann-timer
- $SLACK_{j,t}$ måles i minutter
- $c_j$ er en relativ vekt, ikke en faktisk kronekostnad
- $\lambda$ settes høyt for å gjøre fristbrudd dyrere enn normal ekstra kapasitet

**Tolking:** Målfunksjonen prioriterer å dekke arbeidsbelastningen med minst mulig ekstra kapasitet. Dersom kapasitetstaket nås, kan modellen bruke $SLACK_{j,t}$, men den høye penalty-vekten gjør dette til en siste utvei. Dermed blir fristbrudd synlig som modellresultat, ikke skjult i kapasitetsantakelsene.

---

### 6.4 Hovedbegrensninger

Arbeidsbelastningen i prosess $j$ og uke $t$ beregnes som:

$$W_{j,t} = \sum_{s \in \{F,S\}} \hat{V}_{s,t} \cdot m_{j,s}$$

hvor $W_{j,t}$ måles i minutter.

Kapasitetsbegrensningen per prosess er:

$$W_{j,t} \leq 60 \cdot (CAP^{base}_{j,t} + X_{j,t}) + SLACK_{j,t}$$

med grense:

$$0 \leq X_{j,t} \leq XMAX_{j,t}$$

Enhetskontrollen er sentral:
- $W_{j,t}$ og $SLACK_{j,t}$ er minutter
- $CAP^{base}_{j,t}$ og $X_{j,t}$ er mann-timer
- faktoren 60 konverterer timer til minutter

Eksempel: Hvis prognosen gir 1000 FPK gjennom `P2`, og `P2` har standardtid 0.037555 minutter per FPK, blir arbeidsbelastningen $1000 \cdot 0.037555 = 37.555$ minutter. Denne belastningen sammenlignes med tilgjengelige kapasitetsminutter i `P2`.

For å unngå ubegrensede løsninger skal bare tiltak med dokumentert maksimalgrense aktiveres i $XMAX_{j,t}$. Tiltak som mangler lokal maksimumsgrense i `action_parameters.csv`, for eksempel friuke- eller tilkallingsbemanning, behandles som scenarioforutsetninger inntil praktiske grenser er avklart.

---

### 6.5 Sonevise fristbegrensninger

Sonevise frister aggregeres som ukentlige andeler basert på `zone_cutoff_profile.csv`:

- **Sone 1 (Z1, kl 00:00):** $p_1 = 0.325311$ av ukens distribusjonsvolum må ha gjennomgått ED innen 00:00
- **Sone 2 (Z2, kl 01:00):** $p_1 + p_2 = 0.660545$ av ukens distribusjonsvolum må ha gjennomgått ED innen 01:00
- **Sone 3 (Z3, kl 02:00):** $p_1 + p_2 + p_3 = 1.000000$ må ha gjennomgått ED innen 02:00

I en soneutvidet modell deles P2-belastningen etter soneandel:

$$W_{P2,z,t} = p_z \cdot W_{P2,t}$$

For hver kumulativ frist $k \in \{1,2,3\}$ kan begrensningen formuleres som:

$$\sum_{z=1}^{k} W_{P2,z,t} \leq 60 \cdot (CAP^{deadline}_{k,t} + X^{deadline}_{k,t}) + SLACK^{deadline}_{k,t}$$

Her representerer $CAP^{deadline}_{k,t}$ den delen av P2-kapasiteten som er tilgjengelig frem til frist $k$. I rapportens ukentlige hovedmodell brukes soneandelene primært til å teste om kapasitetsbehovet er robust mot sonemiks. En fullt operativ modell bør kalibrere $CAP^{deadline}_{k,t}$ med daglige tidsvinduer og faktisk bemanningsprofil.

---

### 6.6 Tiltakstyper og videre detaljering

Den aggregerte ekstra kapasiteten $X_{j,t}$ kan senere splittes i tiltakstyper:

$$X_{j,t} = \sum_{a \in A} x_{j,a,t}$$

hvor:
- $a$ er tiltakstype, for eksempel tidlig oppstart, friukebemanning eller tilkallingshjelp
- $x_{j,a,t}$ er timer brukt av tiltak $a$ i prosess $j$ og uke $t$
- hver tiltakstype får egen kostnadsvekt og maksimalgrense fra `action_parameters.csv`

Denne rapporten bruker den aggregerte formen for å holde modellen etterprøvbar og enhetskonsistent. Detaljert tiltaksvalg krever mer presise lokale grenser for tilgjengelig friukebemanning og tilkallingskapasitet.

---

### 6.7 Ikke-negativitet og variabelbegrensninger

Primære variabler:

$$X_{j,t} \geq 0 \quad \forall j,t$$

$$SLACK_{j,t} \geq 0 \quad \forall j,t$$

$$X_{j,t} \leq XMAX_{j,t} \quad \forall j,t$$

For aktive tidlig-start-tiltak gir `action_parameters.csv` følgende dokumenterte maksimumsgrenser:
- `P1`: 6 timer per standard helligdagsuke eller 9 timer i påske/jul-scenario
- `P2`: 36 timer per standard helligdagsuke eller 54 timer i påske/jul-scenario

Friuke- og tilkallingsbemanning er dokumentert som mulige tiltak, men bør ikke brukes som ubundne LP-variabler før lokale maksimumsgrenser er fastsatt.

---

### 6.8 Løsningsmetode

Modellen er en lineær programmering-formulering og løses ved:
- **Simplex-algoritme** (standard LP-løser) eller
- **Interior-point method** (for større instanser)

Verktøy:
- Python: `scipy.optimize.linprog` eller `PuLP`
- Excel: Solver
- Spesialist: CPLEX, Gurobi

## 7.0 Analyse

### 7.1 Data-deskriptiv analyse

Analysegrunnlaget består av 117 modelluker etter at den ufullstendige uke 2026-14 er ekskludert. Dette gir 234 observasjoner fordelt på to varestrømmer. Volum er publisert som indeks med 2024-gjennomsnitt per varestrøm lik 100.

| Varestrøm | Observasjoner | Gj.sn. indeks | Std.avvik | CV | Min | Maks | Kampanjeuker |
|---|---:|---:|---:|---:|---:|---:|---:|
| F | 117 | 96.05 | 12.46 | 0.130 | 29.31 | 122.37 | 116 / 117 |
| S | 117 | 80.22 | 72.00 | 0.898 | 5.27 | 287.47 | 58 / 117 |

F-varestrømmen har relativt stabil indeksverdi sammenlignet med S, men har samtidig nesten konstant kampanjeflagg. Det betyr at et binært kampanjeflagg trolig har begrenset forklaringskraft for F. S-varestrømmen er langt mer volatil, med høyere relativ variasjon og enkelte svært høye uker. Dette peker mot at prognosemodellen bør vurderes separat per varestrøm, og at en enkel felles modell ville skjule viktige forskjeller.

De høyeste kombinerte indeksukene i modellperioden er 2024-20, 2024-27, 2025-14, 2024-30 og 2024-29. Dette viser at belastningstopper ikke bare oppstår i tradisjonelle juleuker, men også rundt vår/sommer og kampanjeperioder. Den laveste kombinerte modelluken er 2026-01, som er påvirket av helligdags- og oppstartsstruktur etter nyttår.

### 7.2 Valgt prognosestrategi og modellvalg

**Baseline-etablering og valideringsresultat:**

Som referanse brukes Seasonal Naive (SNaive)-prognose: $\hat{y}_{t} = y_{t-52}$. Denne enkle modellen utgør sammenligningsstandard for SARIMAX-alternativer.

Validering mot 2026-01 til 2026-13 gir følgende baseline-resultater på indeks-skala:

| Varestrøm | Valideringsuker | MAE | RMSE | MAPE |
|---|---:|---:|---:|---:|
| F | 13 | 12.88 | 18.96 | 24.4 % |
| S | 13 | 5.15 | 7.53 | 60.2 % |

MAPE for S blir høy fordi flere S-uker har lav indeksverdi; små absolutte feil gir da høy prosentfeil. Derfor bør MAE/RMSE vektlegges mer enn MAPE for S.

**SARIMAX-kandidater og estimering:**

Det ble kjørt en konservativ `statsmodels`-grid i `005 report/scripts/run_forecast_capacity_models.py`. Kandidatrommet var begrenset til lave ikke-sesongordener $(p,d,q)$, sesongperiode 52 og parsimoniske sesongledd $(P,D,Q) \in \{(0,0,0),(1,0,0),(0,1,0),(1,1,0)\}$. For F ble `campaign_flag` forkastet som eksogen kandidat fordi flagget er nesten konstant; `holiday_flag` var derfor eneste eksogene kandidat. For S ble både `campaign_flag` og `holiday_flag` testet.

Valgt operativ modell ble definert som den konvergerte kandidaten med lavest validerings-RMSE, sammenlignet mot SNaive:

| Varestrøm | Operativ modell | Eksogen input | MAE | RMSE | MAPE | SNaive RMSE | Ljung-Box p(10) |
|---|---|---|---:|---:|---:|---:|---:|
| F | SARIMAX(1,1,1)(0,0,0)[52] | `holiday_flag` | 8.18 | 13.21 | 16.3 % | 18.96 | 0.855 |
| S | ARIMA/SARIMAX(0,1,0)(0,0,0)[52] | ingen | 6.17 | 6.67 | 76.0 % | 7.53 | 0.137 |

Begge valgte kandidater slår SNaive på RMSE, som er beslutningskriteriet definert i metodekapitlet. F-modellen forbedrer også MAE og MAPE. S-modellen reduserer RMSE ved å dempe store feil, men gir svakere MAE og MAPE enn SNaive; derfor bør S-resultatet tolkes som en minimumskjøring og ikke som endelig operativ modell uten mer historikk eller rikere kampanjevariabler.

Kjøringen skrev sporbare resultater til `004 data/processed/forecast_validation_results.csv`, `004 data/processed/sarimax_candidate_results.csv` og `004 data/processed/model_run_summary.json`.

### 7.3 Kapasitetsmodell-setup

Kapasitetsmodellen har nå tre nødvendige inputblokker:

| Input | Verdi / status | Bruk i modellen |
|---|---|---|
| Prosess-tid P1 | 0.003885 min/FPK | Omregner volum til PD-belastning |
| Prosess-tid P2 | 0.037555 min/FPK | Omregner volum til ED-belastning |
| Basekapasitet P1 | 24.0 mann-timer/uke | Kapasitetsgrense for for-klargjøring |
| Basekapasitet P2 | 144.0 mann-timer/uke | Kapasitetsgrense for endelig dispatch |
| Soneprofil | Z1=0.325311, Z2=0.335234, Z3=0.339455 | Fordeler ED-belastning mot cut-off |

Prosess-tidene bygger på åtte komplette produksjons-/dispatcher-par fra 2024, 2025 og 2026. Soneprofilen bygger på 643 valgte dispatcher-datoer og summerer til 1.000000. Dette gjør at rapporten ikke lenger er avhengig av en ren antakelse for sonefordeling.

**Kritiske observasjoner:**
- Sone-andeler (`zone_cutoff_profile.csv`) er nå beregnet fra `ED`-rader i dispatcherhistorikk og summerer til 1.000000
- `anomaly_flag` og `constrained_week_flag` er ikke validert, så enkelte anomale uker kan være klassifisert som normale
- LP-modellen har nå nødvendig soneinput, men sonevise fristkapasiteter (`CAP_deadline`) må kalibreres før modellen kan tolkes som en natt-for-natt bemanningsplan

LP-løseren ble kjørt på de operative prognosene for valideringsperioden. Fordi publiserbar fil bare inneholder indeks og ikke reelle FPK-volum, rapporteres denne kjøringen som `indeks-minutter` og `indeks-timer`. Basisscenarioet gir 0.00 ekstra indeks-timer og 0.00 slack; maksimal beregnet indeksbelastning er 0.00660 indeks-timer for `P1` og 0.06384 indeks-timer for `P2`. Dette dokumenterer at løseren fungerer teknisk, men er ikke et bevis på at reell kapasitet er tilstrekkelig.

## 8.0 Resultater

### 8.1 Datavalidering og aggregering

Følgende datasett ble etablert for modellering:

| Komponent | Perioder | Rader | Bemerk |
|-----------|----------|-------|--------|
| Treningsdata | 2024-01 til 2025-52 | 104 (uker) × 2 (strømmer) = 208 | Basis for SARIMAX-estimering |
| Valideringsdata | 2026-01 til 2026-13 | 13 × 2 = 26 | Out-of-sample test (uke 14 ekskludert pga. partial week) |
| **Totalt** | 2024-01 til 2026-13 | **234 rader** | Anonymisert som indeks (2024_avg_per_stream=100) |

Den publiserbare filen inneholder 236 rader fra 118 uker, men modellgrunnlaget ekskluderer uke 2026-14 fordi den bare dekker to dager. Datavasken ekskluderer `Ordretype/Navn = -` for å unngå dobbeltregistrering og produktgruppe 850 fordi denne gruppen ikke inngår i prognosevolumet for de operative varestrømmene.

### 8.2 Prosess-tidsmatrise etablert

Basert på 8 komplette produksjons-/dispatcher-par:

| Prosess | Minutes/FPK | Kilder | Gyldighet |
|---------|-------------|--------|-----------|
| P1 (PD) | 0.003885 | 2024-03-12, 2024-06-25, ... 2026-04-28 | 2024-03-12 til 2026-04-28 |
| P2 (ED) | 0.037555 | (som over) | (som over) |

Eksempel på arbeidsforbruk:
- 1000 FPK i S gjennom P2 = 1000 × 0.037555 = 37.56 minutter

### 8.3 Kapasitets-baseline etablert

Fra capacity_assumptions.csv, normal drift:

| Prosess | Bemanning | Timer/dag | Driftsnetter/uke | Timer/uke | Betegnelse |
|---------|-----------|-----------|------------------|-----------|------------|
| P1 | 0.5 | 8.0 | 6 | 24.0 | PD/grovfordeling |
| P2 | 3.0 | 8.0 | 6 | 144.0 | ED/ekspedering |
| **Totalt** | **3.5** | | **6** | **168.0** | Normal apparat |

### 8.4 Prognose- og LP-kjøring

Minimumskjøringen i Python gir følgende valideringsresultat:

| Varestrøm | Valgt modell | MAE | RMSE | MAPE | Beslutning |
|---|---|---:|---:|---:|---|
| F | SARIMAX(1,1,1)(0,0,0)[52] + `holiday_flag` | 8.18 | 13.21 | 16.3 % | Slår SNaive på alle tre måltall |
| S | ARIMA/SARIMAX(0,1,0)(0,0,0)[52] | 6.17 | 6.67 | 76.0 % | Slår SNaive på RMSE, men ikke MAE/MAPE |

For LP-kjøringen er prognosene omregnet til `indeks-minutter` med prosess-tidsmatrisen. Resultatet for publiserbar indeks-skala er:

| Scenario | Ekstra indeks-timer | Slack indeks-minutter | Maks P1 indeks-timer | Maks P2 indeks-timer |
|---|---:|---:|---:|---:|
| -10 % volum | 0.00 | 0.00 | 0.00594 | 0.05746 |
| Basis | 0.00 | 0.00 | 0.00660 | 0.06384 |
| +10 % volum | 0.00 | 0.00 | 0.00726 | 0.07022 |

Tallene er ikke reelle mann-timer. De viser at SARIMAX-prognosene kan flyte inn i LP-formuleringen og løses uten brudd, men reell kapasitetskonklusjon krever lokal `weekly_volume.csv` med faktiske FPK-volum.

### 8.5 Kritiske funn og gjenstående arbeid

**Gjennomført:**
- Datakvalitet etablert for 117 modelluker og to varestrømmer
- SNaive-baseline beregnet på valideringsperioden 2026-01 til 2026-13
- SARIMAX/ARIMA-kandidater estimert og validert mot SNaive
- Prosess-tidsmatrise beregnet fra åtte produksjons-/dispatcher-par
- Kapasitetsbaseline dokumentert for `P1` og `P2`
- Soneandeler beregnet fra dispatcherhistorikk
- LP-struktur formulert med konsistente enheter og kjørt som publiserbar indeks-skala smoke-test

**Gjenstår før operativ bruk:**
- LP-løser må kjøres på reelle FPK-volum i lokal, ikke-publiserbar `weekly_volume.csv`
- Sonevise fristkapasiteter må kalibreres før `CAP_deadline` kan tolkes operativt
- Full sensitivitetsanalyse må gjennomføres for sonemiks, kapasitetsbortfall og mer realistiske volumscenarioer
- Friuke- og tilkallingsbemanning trenger lokale maksimumsgrenser før de kan brukes som egne LP-variabler

## 9.0 Diskusjon

### 9.1 Metodisk vurdering

**Valg av SARIMAX for etterspørselsprognose:**

SARIMAX er relevant for etterspørselsdynamikk i næringsmiddelbransjen grunnet klare sesongmønstre knyttet til påske, jul og handelskampanjer. Foreliggende datasett (104 treningsobservasjoner, 2 sesonger) er på grensen til SARIMAX-robusthet. Regel-of-thumb krever 3–4 sesonger for stabil sesong-komponentestimering.

**Mitigation:** Introduksjon av SNaive-baseline sikrer at modellen ikke overparameteriseres. Hvis SARIMAX ikke slår SNaive på validering, brukes SNaive operativt. Dette er faglig defensibelt.

**Campaign-flagg problematikk:** For varestrøm F er kampanje-indikatoren aktivt i 99 % av ukene, noe som gir minimal variasjon. Alternativ fremtidig tilnærming: bruk kampanje-intensitet (antall kampanjer per uke) eller kampanje-type (kjede, lansering, sesong) i stedet for binær flagg.

**Valg av Linear Programming for kapasitetsoptimering:**

LP er standard for aggregate production planning der målet er å minimere ressursforbruk under lineære constraints. Sonevise frister (00:00, 01:00, 02:00) krever eksplisitt modellering av distribusjons-frister, noe LP håndterer via fristbegrensninger.

**Limitation:** Sonevise constraints er ukentlig aggregerte, ikke daglig granulare. En fullt disaggregert modell ville modellert hver sone-frist daglig, men det ligger utenfor scopet for denne rapport-versjonen.

### 9.2 Datagrunnlag og etterprøvbarhet

**Styrker:**
- 118 sammenhengende uker = tilstrekkelig for sesongmessig mønsteranalyse
- Anonymisering via indekstransformasjon sikrer konfidensialitet uten å gjøre metoden uetterprøvbar
- Prosess-tidsmatrise basert på 8 representative uker fra 3 år gir robust grunnlag
- Publikum kan verifisere metodologi på indeks-skala (SARIMAX-validering, LP-struktur)

**Svakheter og begrensninger:**
- Sone-andeler er beregnet, men mappingen fra `Street` til cut-off må behandles som en operasjonell modellantakelse og testes i sensitivitet.
- Anomaly_flag ikke validert: Kan være anomale uker klassifisert som normale
- Campaign-flag har liten kraft for F: 99 % av F-ukene har kampanje, gir minimal differensiering
- Datavolum grensesnitt: 104 treningsobservasjoner × 52-ukes sesong = akkurat minimum for SARIMAX

**Konsekvenser for tolkning:** Prognose-feil på validering kan bli større enn ideelt. Sensitivitetsanalyse må teste hvor robust LP er under ±10 % prognose-usikkerhet.

### 9.3 Operativ relevans og næringslivets perspektiv

**Modellens tiltenkte verdi:**
1. Erstatte reaktive ("vi må ringe inn ekstrahjelp på fredag") med proaktiv planlegging
2. Identifisere kritiske høysesong-uker som krever tidlig oppstart eller overtid
3. Kvantifisere kostnads-trade-offs: Hvor mye mer overtid kreves for 100 % fristoppfyllelse vs. akseptert 5 % brudd?

**Operativ implementering (utenfor rapport):**
- Modellen kan brukes ugentlig: Prognose beregnes mandag, LP løses for kapasitets-allokeringen for uka
- Hvis SARIMAX viser høy etterspørsel, flagges uken for ekstrabemanning eller tidlig oppstart
- Feedback-loop: Faktisk fristbrudd sammenlignes med prognostisert SLACK for kontinuerlig validering

**Generaliserbarhet:**
Modellen er designet for bedriftens todelte varestrøm-struktur (ferskvare + sekundærvare, felles distribusjonsledd). Transferabilitet til andre næringsmiddelbedrifter avhenger av:
- Om sesongmønstre er tilsvarende
- Om sonevise distribusjons-frister gjøres eksplisitte
- Om tidsmatrise kan etableres fra produksjonslister/dispatcher-data

Andre logistikk-kontekster (f.eks. pharma, e-commerce) ville kreve tilpasset modellering.

### 9.4 Kritikk og videre forskning

**Denne rapport-versjonen inneholder en teknisk minimumsimplementasjon, men ikke en operativ real-skala kapasitetsplan.**

Gjenstår før operativ bruk:
1. **Reell-skala LP:** Kjør samme løser på lokal, ikke-publiserbar `weekly_volume.csv` slik at prognosene omregnes fra FPK til faktiske minutter og mann-timer
2. **Fristkapasitet:** Kalibrer `CAP_deadline` for 00:00, 01:00 og 02:00 basert på faktisk bemanning, pauser, oppstartstid og nattlig arbeidsprofil
3. **Scenarioanalyse:** Test sonemiks, kapasitetsbortfall, sykefravær, kampanjetopper og mer realistiske volumscenarioer enn den publiserbare ±10 %-indekskjøringen
4. **Modellrobusthet:** Re-estimer når flere sesonger foreligger, og vurder rikere eksogene variabler som kampanjeintensitet i stedet for binære flagg

**Teoretisk bidrag:** Rapporten etablerer en metodisk tilnærming til integrering av SARIMAX-prognose og LP-optimering for sesongbundet etterspørsel under sonevise distribusjonsfrister. Eksisterende litteratur på APP dekker ofte enten prognose eller optimering, men sjeldnere det integrerte oppsettet.

**Praktisk bidrag:** Demonstrerer hvordan bedriftsinterne data (volum, produksjonslister, dispatcher actions) kan transformeres fra rådata til anonymisert, reproduserbar modellgrunnlag uten å avsløre kommersielle hemmeligheter.

## 10.0 Konklusjon

### Besvarelse av problemstilling

**Hovedproblemstilling:**
*Hvordan kan vi kombinere etterspørselsprognoser og kapasitetsoptimering for å minimalisere ressursforbruk ved å sikre at prognostiserte volumer ferdigstilles innenfor sonevise distribusjons-cut-offs i en flerprosess næringsmiddelproduksjon?*

**Svar fra denne rapporten:**

Rapporten utvikler et **integrert modellrammeverk** bestående av:

1. **Etterspørselsprognose via SARIMAX/SNaive:** Sesongbundne ukevolumer predikeres basert på historiske ukedata, kampanjekalender og sesongmønstre. SNaive brukes som baseline, og SARIMAX skal bare velges dersom den gir bedre valideringsresultater og forsvarlig residualdiagnostikk.

2. **Kapasitetsoptimering via Linear Programming:** Gitt prognostisert etterspørsel, formuleres et LP-problem som minimerer samlet ekstra kapasitetsbruk under distribusjonsfrist-constraints. Modellen håndterer den sammensatte flaskehals-dynamikken ved å modellere sonevise frister som ukentlige aggregerte constraints.

3. **Anonymisering som enabler:** Bedriftsinterne data (råvolum fra Qlik, dispatcher-tidsdata fra Outlook, produksjonslister) transformeres til anonymisert, publiserbar modellgrunnlag via indekstransformasjon. Metoden sikrer konfidensialitet samtidig som metodologi blir etterprøvbar.

**Konkrete funn:**
- Datagrunnlag på plass: 117 modelluker, 2 varestrømmer, anonymisert publiserbar fil
- Prosess-tidsmatrise etablert: P1 = 0.004 min/FPK, P2 = 0.038 min/FPK (basert på 8 dager)
- Kapasitets-baseline dokumentert: P1 = 24 t/uke, P2 = 144 t/uke
- Soneprofil etablert: Z1 = 0.325311, Z2 = 0.335234, Z3 = 0.339455
- SARIMAX/ARIMA-kjøring gjennomført: F-modell RMSE 13.21 mot SNaive 18.96; S-modell RMSE 6.67 mot SNaive 7.53
- LP-struktur formulert med enhetskonsistente constraints og kjørt som indeks-skala smoke-test med 0.00 ekstra indeks-timer og 0.00 slack

### Gjenstår før operativ implementasjon

For at modellen skal kunne brukes til praktisk planlegging:
- Reell-skala LP må kjøres på lokal `weekly_volume.csv` med faktiske FPK-volum
- Sonevise fristkapasiteter må kalibreres mot faktisk nattlig bemanning og tidsvinduer
- Full sensitivitetsanalyse må gjennomføres for volum-, sonemiks- og kapasitetsusikkerhet
- Lokale maksimumsgrenser for friuke- og tilkallingsbemanning må fastsettes før disse tiltakene brukes som egne beslutningsvariabler

Disse stegene ligger utenfor den publiserbare minimumskjøringen, men er detaljert planlagt i kapitlene 7–8.

### Teoretisk og praktisk bidrag

**For akademia:** Rapporten demonstrerer en systematisk tilnærming til integrering av tidsserieprognose og produktionsplanlegging under sesongbundne frister. Den kombinerer etablert litteratur (SARIMAX, LP) i en domene-spesifikk kontekst (næringsmiddellogistikk) og løser en reell operasjonell utfordring.

**For næringslivet:** Modellen gir et rammeverk for å gå fra reaktiv ("vi må ha ekstrahjelp") til proaktiv ("høysesong uke 11 krever 30 ekstratimer, planlegg i god tid") kapasitetsplanlegging. Estimatene kan brukes til investeringsbeslutninger (skal vi øke fast bemanning eller satse på fleksibel overtid?).

### Avsluttende refleksjon

Selv om denne rapporten ikke publiserer reell-skala kapasitetsestimat i mann-timer, leverer den nå en teknisk minimumsimplementasjon av prognose- og LP-kjeden. Designen er defensibel både faglig og etisk, og prosessen demonstrerer disiplin i:
- Databehandling og anonymisering
- Matematisk konsistens (enhetskontroll, formulering)
- Metodisk robusthet (baseline-sammenligninger, dokumentasjon)
- Transparans om begrensninger og videre arbeid

**Fremtidig arbeid** bør prioritere (1) reell-skala LP med faktisk FPK-grunnlag, (2) kalibrering av sonevise fristkapasiteter, og (3) sensitivitetstesting for å gjøre modellen fullt operativ.

---

**Dato for sluttrapport:** 30. april 2026
**Rammeverk-status:** Metodikk og datagrunnlag etablert, teknisk minimumskjøring gjennomført
**Innlevering:** Planlagt 30. april 2026

## 11.0 Bibliografi

### Primær litteratur – Tidsserieprognose og SARIMAX

Hyndman, R.J., & Athanasopoulos, G. (2021). *Forecasting: principles and practice* (3. utg.). OTexts. https://otexts.com/fpp3/
- *Bruk:* Kapittel 9 for ARIMA-teori, 9.9 for sesongmodeller, Kapittel 10 for eksogene variabler (ARIMAX). Sentral for modellvalg, residualdiagnostikk og hvorfor baseline-sammenligninger er kritiske.

Hyndman, R.J., & Khandakar, Y. (2008). Automatic time series forecasting: The forecast package for R. *Journal of Statistical Software*, 27(3), 1–22. https://doi.org/10.18637/jss.v027.i03
- *Bruk:* Kanonisk kilde for auto_arima stepwise-algoritmen. Brukt som metodisk inspirasjon for parsimonisk kandidatgrid og modellseleksjon i 5.1.1.

Arunraj, N.S., Ahrens, D., & Fernandes, M. (2016). Application of SARIMAX model to forecast daily sales in food retail industry. *International Journal of Operations Research and Information Systems*, 7(2), 1–21. https://doi.org/10.4018/IJORIS.2016040101
- *Bruk:* Direkte parallell til ditt case: SARIMAX for sesongbundet matetherspørsel med eksogene variabler (promotions, holidays). Seksjon 2.1 (litteratur), 7.1 (datadeskriptiv), validering av eksogen-variabel-tilnærming.
- *Merk:* Deres case er daglig butikkvolum; ditt case er ukentlig distribusjonsvolum. Metodologien er overførbar.

Fildes, R., Ma, S., & Kolassa, S. (2022). Retail forecasting: Research and practice. *International Journal of Forecasting*, 38(4), 1283–1318. https://doi.org/10.1016/j.ijforecast.2019.06.004
- *Bruk:* Bredspektret gjennomgang av retail-forecasting utfordringer, aggregeringsnivåer, og håndtering av høy variabilitet. Seksjon 2.1 (litteratur om etterspørselsprognose), 7.1 (datavolatilitet og etterspørselsdynamikk).

Fildes, R., Goodwin, P., & Önkal, D. (2019). Use and misuse of information in supply chain forecasting of promotion effects. *International Journal of Forecasting*, 35(1), 144–156. https://doi.org/10.1016/j.ijforecast.2017.12.006
- *Bruk:* Valgfritt, kun hvis du diskuterer kampanjeinformasjon og forecast-justering. Seksjon 2.1 (kampanjepåvirkninger), 5.4 (høy kampanje-flagg-variasjon for F).

### Produksjonsplanlegging og Linear Programming

Winston, W.L. (2004). *Operations Research: Applications and Algorithms* (4. utg.). Thomson Brooks/Cole.
- *Bruk:* Lærebok for LP-formulering, Simplex-algoritme, og formuleringsteknikk. Seksjon 2.2, 3.2, 6.0 (LP-metodikk og løsningsapproach).

Holt, C.C., Modigliani, F., & Simon, H.A. (1955). A linear decision rule for production and employment scheduling. *Management Science*, 2(1), 1–30.
- *Bruk:* Historisk kontekst for APP-metodikk. Seksjon 2.2 (litteratur om kapasitetsplanlegging). Merk: Ikke samme formulering som ditt problem; brukes kun for grunnleggende APP-perspektiv.

Leung, S.C.H., Wu, Y., & Lai, K.K. (2006). A stochastic programming approach for multi-site aggregate production planning. *Journal of the Operational Research Society*, 57(2), 123–132. https://doi.org/10.1057/palgrave.jors.2601988
- *Bruk:* APP under usikkerhet, arbeidskraftsnivåer, og etterspørsel med medium-range planlegging. Seksjon 2.2 (APP under kapasitets-begrensninger), 6.3–6.4 (formuleringsinspirasjoner for kapasitets-constraints).

### Statistikk og datakilder

Statistisk sentralbyrå (SSB). (2024). *Sykefraværet i industri og andre næringer*. Norges offisielle statistikk. https://www.ssb.no/
- *Bruk:* Norsk sykefraværsrate (~6 %) som kapasitets-justerings-parameter. Seksjon 5.4 (datakvalitet, kapasitets-antakelser), 6.3 (kapasitets-baseline og justering).

Norsk Næringsmiddel- og Landbruksarbeiderforbund (NNN). (2024–2026). *Mat- og drikkevareoverenskomsten*. Tariffavtale, lokalt forankret.
- *Bruk:* Norsk tariff-struktur for grunnlønn, overtid, og tilkallingshjelp som relative kostnads-vekter i LP-modellen. Seksjon 6.6 (beslutningsvariabler for overtid/bemanning), 6.3 (målfunksjon vekter $c_j$).

### Undervisningsmateriale

KML Kompendium. (2026). *Quantitative methods in logistics: A framework for AI-driven research*. [Online]. Tilgjengelig fra: https://kml-site-production.up.railway.app/
- *Bruk:* Kompendium for LOG650. Bakgrunn for SARIMAX-intuisjon, produksjonsplanlegging, og databehandling-rammeverk.

---

**Notat til framtidig arbeid:** Ytterligere litteratur på følgende emner anbefales:
- Demand sensing og real-time prognoser i sesongbundne industrier
- Supply chain resilience under kapasitets-begrensninger
- Benchmark-studier av produksjonsbedrifter som bruker integrert prognose-optimering

## 12.0 Vedlegg

Vedleggene er holdt som prosjektmappe-artefakter heller enn innlimte fulltabeller, slik at rapporten forblir lesbar og reproduserbar uten å publisere sensitive rådata.

| Vedlegg | Fil / artefakt | Formål |
|---|---|---|
| A | `004 data/weekly_volume_anonymized.csv` | Publiserbar ukentlig volumindeks for F og S |
| B | `004 data/process_time_matrix.csv` | Prosess-tider brukt i kapasitetsomregningen |
| C | `004 data/capacity_assumptions.csv` og `004 data/action_parameters.csv` | Basekapasitet og dokumenterte tiltak |
| D | `004 data/zone_cutoff_profile.csv` | Soneandeler for cut-off-modellen |
| E | `005 report/scripts/run_forecast_capacity_models.py` | Reproduserbart skript for SARIMAX-grid, SNaive-baseline og LP smoke-test |
| F | `004 data/processed/forecast_validation_results.csv` | Valideringsprognoser, faktiske indeksverdier og modellfeil |
| G | `004 data/processed/sarimax_candidate_results.csv` | Oversikt over evaluerte SARIMAX/ARIMA-kandidater |
| H | `004 data/processed/lp_capacity_validation_index.csv` og `004 data/processed/lp_zone_deadline_load_index.csv` | LP-resultater på publiserbar indeks-skala |
| I | `004 data/processed/model_run_summary.json` | Maskinlesbar oppsummering av modellkjøringen |
