# Integrert volumprognose og kapasitetsanalyse
## Integrated Volume Forecasting and Capacity Analysis

**Forfatter(e):** Davor Necemer
**Totalt antall sider inkludert forsiden:** _[fyll inn etter ferdigstilling]_
**Sted og innleveringsdato:** Molde, 29. mai 2026

## Obligatorisk egenerklæring / gruppeerklæring

Den enkelte student er selv ansvarlig for å sette seg inn i hva som er lovlige hjelpemidler, retningslinjer for bruk av disse og regler om kildebruk. Erklæringen skal bevisstgjøre studentene på deres ansvar og hvilke konsekvenser fusk kan medføre. Manglende erklæring fritar ikke studentene fra sitt ansvar.

Fyll ut erklæringen ved å krysse av punktene under:

- [ ] 1. Jeg/vi erklærer herved at min/vår besvarelse er mitt/vårt eget arbeid, og at jeg/vi ikke har brukt andre kilder eller har mottatt annen hjelp enn det som er nevnt i besvarelsen.
- [ ] 2a. Besvarelsen har ikke vært brukt til annen eksamen ved annen avdeling/universitet/høgskole innenlands eller utenlands.
- [ ] 2b. Besvarelsen refererer ikke til andres arbeid uten at det er oppgitt.
- [ ] 2c. Besvarelsen refererer ikke til eget tidligere arbeid uten at det er oppgitt.
- [ ] 2d. Alle referanser er oppgitt i litteraturlisten.
- [ ] 2e. Besvarelsen er ikke en kopi, duplikat eller avskrift av andres arbeid eller besvarelse.
- [ ] 3. Jeg/vi er kjent med at brudd på ovennevnte er å betrakte som fusk og kan medføre annullering av eksamen og utestengelse fra universiteter og høgskoler i Norge, jf. Universitets- og høgskoleloven §§4-7 og 4-8 og Forskrift om eksamen §§14 og 15.
- [ ] 4. Jeg/vi er kjent med at alle innleverte oppgaver kan bli plagiatkontrollert i URKUND, se Retningslinjer for elektronisk innlevering og publisering av studiepoenggivende studentoppgaver.
- [ ] 5. Jeg/vi er kjent med at høgskolen vil behandle alle saker hvor det foreligger mistanke om fusk etter høgskolens retningslinjer for behandling av saker om fusk.
- [ ] 6. Jeg/vi har satt oss inn i regler og retningslinjer for bruk av kilder og referanser på bibliotekets nettsider.

## Personvern

### Personopplysningsloven

Forskningsprosjekt som innebærer behandling av personopplysninger iht. Personopplysningsloven skal meldes til Norsk senter for forskningsdata, NSD, for vurdering.

- Har oppgaven vært vurdert av NSD? [ ] Ja [ ] Nei
- Hvis ja, referansenummer: _[fyll inn]_
- Hvis nei: Jeg/vi erklærer at oppgaven ikke omfattes av Personopplysningsloven.

### Helseforskningsloven

Dersom prosjektet faller inn under Helseforskningsloven, skal det også søkes om forhåndsgodkjenning fra Regionale komiteer for medisinsk og helsefaglig forskningsetikk, REK, i din region.

- Har oppgaven vært til behandling hos REK? [ ] Ja [ ] Nei
- Hvis ja, referansenummer: _[fyll inn]_

## Publiseringsavtale

**Studiepoeng:** _[fyll inn]_
**Veileder:** _[fyll inn]_

### Fullmakt til elektronisk publisering av oppgaven

Forfatter(ne) har opphavsrett til oppgaven. Det betyr blant annet enerett til å gjøre verket tilgjengelig for allmennheten (Åndsverkloven §2).

Alle oppgaver som fyller kriteriene vil bli registrert og publisert i Brage HiM med forfatter(ne)s godkjennelse.

Oppgaver som er unntatt offentlighet eller båndlagt vil ikke bli publisert.

Jeg/vi gir herved Høgskolen i Molde en vederlagsfri rett til å:

- Gjøre oppgaven tilgjengelig for elektronisk publisering: [ ] Ja [ ] Nei
- Er oppgaven båndlagt (konfidensiell)? [ ] Ja [ ] Nei
- Hvis ja: Kan oppgaven publiseres når båndleggingsperioden er over? [ ] Ja [ ] Nei
- Dato: _[fyll inn]_

**Antall ord:** Oppgi antall ord dersom dette er et krav. Hvis ikke, slett denne linjen.

**Forfattererklæring:** Skriv inn forfattererklæring dersom det er et krav til oppgaven. Hvis ikke, slett dette avsnittet.

## Sammendrag

_Skriv sammendrag her._

## Abstract

_Write the abstract here._

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
- 8.0 Resultat
- 9.0 Diskusjon
- 10.0 Konklusjon
- 11.0 Bibliografi
- 12.0 Vedlegg

## 1.0 Innledning

Produksjonslogistikk i næringsmiddelbransjen står overfor en fundamental utfordring: etterspørselen er volatil og sesongbundet, mens distribusjonsnettet har strenge, daglige frister. I mange bedrifter oppstår en sammensatt flaskehals-dynamikk selv når den totale ukekapasiteten virker tilstrekkelig. Problemet ligger i at etterspørselen er ujevnt fordelt innenfor uken, og når flere varestrømmer skal gjennom samme distribusjonsledd med ulike cut-off-tider, kan kapasitetsbrudd oppstå på kritiske tidsvindu.

Denne situasjonen oppstår fordi tradisjonelle kapasitetsplaner baseres på ukeaggregater, som ikke fanger opp de kritiske søne- og dagsvise cut-offs. Resultat: fraktbrudd, forsinkede leveranser, eller behov for dyrbar ekstrabemanning og overtid som kunne vært unngått gjennom bedre prognoser og planlegging.

Litteraturen på demand forecasting og aggregate production planning tilbyr vel etablerte løsninger. SARIMAX-modeller kan prognostisere etterspørsel under hensyn til sesongmønstre, planlagte kampanjer og andre eksogene faktorer, og linear programming kan optimalisere kapasitetsallokeringen under stramme restruksjoner. Integrering av disse to metodene kan gi både operasjonell effektivitet og innsikt i kritiske ressursbehov.

Denne rapporten utvikler og tester en slik integrert modell på data fra en reell næringsmiddelproduksjon og distribusjonsoperasjon.

### 1.1 Problemstilling

**Hvordan kan vi kombinere etterspørselsprognoser og kapasitetsoptimering for å minimaliser resursforbuke ved å sikre at prognostiserte volumer ferdigstilles innenfor sonevise distribusjons-cut-offs i en flerprosess næringsmiddelproduksjon?**

Denne problemstillingen er todelt:

1. **Prognosedelen:** Utarbeide tidsserieprognose som fanger sesongvariasjoner og effekten av planlagte kampanjer (eksogene faktorer).
2. **Optimeringsdelen:** Gitt denne prognosen, bestemme optimal allokering av ekstra kapasitet (overtid, tidlig oppstart, ekstrabemanning) som minimerer samlet ressursforbruk mens alle sonevise cut-off-frister respekteres.

Problemstillingen behandler altså hvordan man *integrerer* etterspørselsprognose og operasjonell planlegging for å løse en reell distribusjonsflaske-halssituasjon.

### 1.2 Delproblemer

Problemstillingen løses gjennom to delproblem i rekkefølge:

**DP1 – Etterspørselsprognose:** Hvordan kan SARIMAX-modeller best estimeres og valideres ved bruk av historiske volumdata, sesongmønstre og kampanjekalender for å prognose ukentlig etterspørsel?

**DP2 – Kapasitetsoptimering:** Gitt en etterspørselsprognose, hvordan kan linear programming formuleres og løses for å bestemme optimal kapasitetsallokering som minimerer ressursforbruk mens cut-off-frister respekteres?

Disse delproblemene er sekvensielle: prognosen fra DP1 blir input til LP-modellen i DP2.

### 1.3 Avgrensinger

**Aggregeringsnivå – fra dag/sone til uke:** Selv om problemet manifesteres daglig gjennom sonevise frister (kl 00:00, 01:00, 02:00), modelleres det på *ukentlig* nivå. *Begrunnelse:* Sonevise frister aggregeres som ukentlige kapasitets- og fristbegrensninger basert på sonestruktur. Fordi sonene er operasjonelt like (samme ressursbemanning, samme skiftlengde), er forskjellen primært avgangtidspunkt, ikke kapasitetskarakteristikk. Aggregering til uke tillater bruk av tidsseriedata for de to varestrømmene og forenkler LP-formulering betydelig. Daglig operativ planlegging (mann-allokering per natt) ligger utenfor modellomfanget.

**Prosessomfang:** Analysen dekker distribusjonsklargjøringen etter at volumet er klart for utsendelse. Prosessene modelleres som `P1 = PD / for-klargjøring` og `P2 = ED / endelig dispatch/ekspedering`, mens `DD` behandles som direkte eller særskilt dispatchflyt som inngår i tidsgrunnlaget ved behov, men ikke som separat hovedprosess. *Begrunnelse:* Produksjonslister og dispatcher actions for lager 310 viser at tilgjengelig tidsdata måler håndtering mot distribusjonsfrister, ikke primær eller sekundær produksjonspakking. Prosessavgrensningen må derfor følge det observerbare datagrunnlaget for å unngå at modellen estimerer kapasitet for prosesser som ikke er målt.

**Geografi og personvern:** Data behandles fullt anonymisert uten personopplysninger. Bedriften er ikke identifisert. *Begrunnelse:* Sikrer personvern og forretningshemmeligheter.

**Måling:** Modellen optimaliserer kapasitetsforbruk (mann-timer, overtimebehov) og omfang av fristbrudd (FPK-enheter over kapasitet), ikke faktiske norske kroner. *Begrunnelse:* Kostnadsdata er sensitive; ressursenhetsmål er generelt og reproduserbart.

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

I dette prosjektet modelleres kapasitetsallokeringen som et LP-minimeringsproblem. Målfunksjonen minimerer totalt ressursforbruk (overtid, ekstrabemanning) samtidig som distribusjonsfrister respekteres. Begrensningene sikrer at arbeidsbelastningen (prognostisert volum omregnet til minutter) ikke overstiger tilgjengelig kapasitet, definert som grunnbemanning og mulig overtid. Denne strukturen følger standard APP-praksis som beskrevet av Winston (2004) og Leung et al. (2006).

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
2. **Fase 2 – Kapasitetsoptimering:** LP-modellen bruker denne prognosen som fast input og bestemmer optimal kapasitetsallokering for å møte etterspørselen under sonevise frister.

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

- Filial A har daglige frister (f.eks. kl. 14:00) for hver kundesone
- Filial B har også daglige frister, men senere på dagen
- Hvis både ferskvare og sekundærvare peaker samme dag, kan distribusjonsklargjøring ikke strekke til

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

### 5.1 Metode – Etterspørselsprognose (SARIMAX)

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

2. **SARIMAX-kandidater via `auto_arima` (Hyndman & Khandakar, 2008):**
   - **Stasjonaritetstesting:** KPSS-test for trendstasjonaritet, velg $d$; Canova-Hansen-test for sesongstasjonaritet, velg $D$ (typisk $D \in \{0, 1\}$)
   - **ACF/PACF-analyse** foreslår AR/MA-lagordener $(p, q, P, Q)$
   - **auto_arima-algoritmen** genererer kandidatmodeller systematisk med fokus på parsimoni, rangert etter AICc (Akaike Information Criterion corrected for small samples)

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
- `auto_arima` (fra `pmdarima`, implementert basert på Hyndman & Khandakar, 2008) brukes til modellseleksjon
- `statsmodels.tsa.statespace.sarimax.SARIMAX` brukes til endelig estimering, tolkning av koeffisienter, residualdiagnostikk og prognosegenerering
- R med `forecast::auto.arima(seasonal = TRUE)` kan brukes som alternativ ved behov

---

### 5.1b Metode – Kapasitetsoptimering (Linear Programming)

**Optimeringsproblem:** LP-modellen løser et aggregate production planning-problem (APP, se seksjon 6.0 og litteraturkapittel 2.2).

**Formulering:** Modellen følger standard APP-struktur (Winston, 2004; Leung, Wu & Lai, 2006):
- **Målfunksjon:** Minimerer totalt ressursforbruk (overtid, ekstrabemanning) og høy straffvekt for fristbrudd
- **Begrensninger:**
  - Kapasitetsbegrensninger: arbeidsbelastning ≤ grunnkapasitet + overtid
  - Sonevise frister: andel av volum må være ferdig innen cut-off-tider
  - Ikke-negativitet: alle beslutningsvariabler ≥ 0
  - Maksimalgrenser: overtid begrenset av arbeidstidslover og realisme

**Løsningsmetode:**
- **Simplex-algoritmen** eller **interiørpunktmetode** (Winston, 2004) avhengig av solver
- Python: `scipy.optimize.linprog`, `PuLP`, eller `Gurobi/CPLEX` for større instanser
- Løsningen gir optimal allokering av overtidsbehov per prosess per uke

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
- LP løst med absolutte mann-timer, resulterer i $OT_{j,t}$ i timer, $SLACK_t$ i minutter
- Intern resultat: dimensjoner i timer og minutter, kan reproduseres med reelle FPK

**Publisert resultat (rapport + vedlegg):**
- Kapasitetsbehov rapporteres som **relative nøkkeltall**, ikke absolutte timer
- Eksempler: Gjennomsnittlig utnyttelsesgrad (%), fordelinghistogram for overtidsbehov, frekvens av fristbrudd (%)
- Absolutte mann-timer utelates fordi de kan avsløre reelt volum
- Reelle FPK-tall publiseres ikke
- `volume_index` brukes ikke direkte som input til LP

**Etterprøvbarhet uten å avsløre volum:**
- SARIMAX-validering rapporteres på indeks-skala (MAE/RMSE i indeks-enheter)
- LP-logikk og struktur er transparent (begrensninger, målfunksjon)
- Sensitivitetsanalyse vises som relative endringer (±10% volum → ±Y% overtid)
- Leseren kan verifisere metodologien uten å kjenne reelle volum

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

### 6.1 Modellstruktur

Modellen består av to sekvensielle komponenter:

1. **Etterspørselsprognose (SARIMAX):** Basert på historiske ukentlige volumer for ferskvare (F) og sekundærvare (S) samt kampanjekalender, produseres punkt-prognoser for volumene i hver uke. Prognosen fanger sesongmønstre, eksogene effekter (kampanjer), og genererer prediktert volum `V_F,t` og `V_S,t` for uke `t`.

2. **Kapasitetsoptimering (LP):** Gitt prognostisert volum, bestemmes optimal kapasitetsallokering (overtimebehov, tidlig oppstart) for `P1` og `P2` i distribusjonsklargjøringen for å møte sonevise frister med minimalt ressursforbruk.

---

### 6.2 Beslutningsvariabler

La `OT_j,t` = overtimebehov (mann-timer) i prosess j, uke t

Prosesser:
- j = 1: `P1 = PD / for-klargjøring`
- j = 2: `P2 = ED / endelig dispatch/ekspedering`

Tidsperiode:
- t = 1, 2, ..., T (planningshorisonten, f.eks. T=52 uker)

---

### 6.3 Målfunksjon

**Minimiser:**

$$Z = \sum_{t=1}^{T} \sum_{j \in \{P1,P2\}} c_j \cdot OT_{j,t} + \sum_{t=1}^{T} \lambda \cdot SLACK_t$$

hvor:
- $c_j$ = kostnads-/vektvektor per overtimetime i prosess j (ressursenhet eller relativ vekt)
- $OT_{j,t}$ = overtimebehov (mann-timer, beslutningsvariabel)
- $SLACK_t$ = arbeidsminutter som ikke klargjøres innen den aggregerte soneslutten (late_minutes, beslutningsvariabel)
- $\lambda$ = penalty-vekt for sen arbeid (settes høyt slik at fristbrudd prioriteres sterkt, typisk $\lambda = 100$)

**Tolking:** Målfunksjonen minimerer totalt overtimebehov over planningshorisonten, samtidig som fristbrudd (SLACK i minutter) penaliseres høyt. Siden $\lambda \gg c_j$, vil modellen normalt unngå slack og velge overtid heller. Slack tillates bare hvis overtid er umulig innenfor maksimalgrenser.

---

### 6.4 Hovedkonstrants

**Kapasitetsrestriksjon per prosess (ENHETSKONSISTENT):**

For hver prosess j ∈ {P1, P2} og uke t:

$$W_{j,t} \leq 60 \cdot (CAP_{j,\text{base}} + OT_{j,t})$$

hvor:
- $W_{j,t}$ = arbeidsbelastning i **minutter** i prosess j, uke t
  - Beregnet som: $\sum_{\text{streams}} (\text{forecast}_{s,t} \times \text{minutes\_per\_fpk}_{j,s})$
  - Eksempel: Hvis forecast_F = 1000 FPK, minutes_per_fpk_F_P2 = 0.0376 min/FPK, da får vi 1000 × 0.0376 = 37.6 minutter

- $CAP_{j,\text{base}}$ = grunnkapasitet i **mann-timer** per uke, prosess j
  - Fra `capacity_assumptions.csv`: P1 = 24.0 timer/uke, P2 = 144.0 timer/uke
  - Konvertering til minutter: 24.0 × 60 = 1440 minutter

- $OT_{j,t}$ = overtimebehov i **mann-timer** (beslutningsvariabel)
  - Konvertering: $OT_{j,t}$ multipliseres med 60 for å få minutter

**Tolking:** Totalt arbeid (prognostisert volum × tidsstandard) må kunne utføres innenfor tilgjengelig kapasitet (base + overtid). Hvis $W_{j,t}$ > kapasitet, må modellen øke $OT_{j,t}$ eller akseptere SLACK.

---

### 6.5 Sonevise fristbegrensninger

Sonevise frister aggregeres som ukentlige andeler basert på `zone_cutoff_profile.csv`:

- **Sone 1 (Z1, kl 00:00):** $p_1 = 0.325311$ av ukens distribusjonsvolum må ha gjennomgått ED innen 00:00
- **Sone 2 (Z2, kl 01:00):** $p_1 + p_2 = 0.660545$ av ukens distribusjonsvolum må ha gjennomgått ED innen 01:00
- **Sone 3 (Z3, kl 02:00):** $p_1 + p_2 + p_3 = 1.000000$ må ha gjennomgått ED innen 02:00

**Enkel formalisering (når alle prosesser aggregeres):**

$$W_{P2,t} - SLACK_t \leq 60 \cdot (CAP_{P2,\text{base}} + OT_{P2,t})$$

hvor:
- $W_{P2,t}$ = totalt arbeidsforbruk i **minutter** for endelig dispatch/ekspedering (P2) i uke t
- $SLACK_t$ = arbeidsminutter som ikke klargjøres innen sone 3 sin 02:00 frist (late_minutes i minutter)
- $60 \cdot CAP_{P2,\text{base}}$ = grunnkapasitet konvertert til minutter
- $60 \cdot OT_{P2,t}$ = tilgjengelig overtid konvertert til minutter

**Tolking:** Hvis $W_{P2,t} > 60 \cdot (CAP + OT)$, kan ikke alt arbeidsvolum utføres, og $SLACK_t$ vil være positiv i løsningen. Høy penalty-vekt $\lambda$ sikrer at dette unngås hvis mulig.

**Videre detaljering (oppnådd via scenarioanalyse):** Siden sone-andelene nå er kjente, kan modellen splitte arbeidsbelastningen per sone og teste sensitiviteter rundt sonemiksen, for eksempel ±10 % relativ endring i `Z1`, `Z2` og `Z3`.

---

### 6.6 Tidlig oppstart og ekstra bemanning (VALG FOR SENERE UTVIKLING)

I senere versjon av modellen kan tidlig oppstart (ES) eller ekstra bemanning (OFFWEEK, ONCALL) modelleres eksplisitt som beslutningsvariabler:

$$W_{j,t} \leq 60 \cdot (CAP_{j,\text{base}} + OT_{j,t} + ES_{j,t} + OFFWEEK_{j,t} + ONCALL_{j,t})$$

hvor:
- $ES_{j,t}$ = ekstra timer fra tidlig oppstart (mann-timer)
- $OFFWEEK_{j,t}$ = ekstra timer fra bemanning på friuke (mann-timer)
- $ONCALL_{j,t}$ = ekstra timer fra tilkallingshjelp (mann-timer)

Hver variabel har maksimalgrenser fra `action_parameters.csv` og relative kostnads-vekter som reflekterer tariff-forhold.

**Notat for implementasjon:** For denne rapport-versjonen inkluderes tidlig oppstart/bemanning som forutsetninger i grunnkapasiteten (f.eks. via scenario-anta telser), ikke som eksplisitte beslutningsvariabler. Modellutvikling kan senere splitte disse ut hvis LP skal løses for å velge mellom tiltakene.

---

### 6.7 Ikke-negativitet og variabelbegrensninger

**Primære beslutningsvariabler:**
$$OT_{j,t} \geq 0 \quad \forall j \in \{P1, P2\}, t \in [1, T]$$
$$SLACK_t \geq 0 \quad \forall t \in [1, T]$$

**Maksimalgrenser (fra `action_parameters.csv` og kapasitetsforutsetninger):**
$$OT_{j,t} \leq OT\text{\_}MAX_{j,t} \quad \text{(tidlig oppstart + normal overtid)}$$
$$SLACK_t \text{ tillatt hvis andre tiltak ikke strekker}$$

**Eksempler:**
- P1 early_start standard holiday: maks 6 timer/uke
- P1 early_start Easter/Christmas: maks 9 timer/uke
- P2 early_start standard holiday: maks 36 timer/uke
- P2 early_start Easter/Christmas: maks 54 timer/uke

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

**Sesongmønster og etterspørselsdynamikk:**

Forecastgrunnlaget for begge varestrømmer (F og S) dekker 118 sammenhengende uker (2024-01 til 2026-13, uke 2026-14 ekskludert). Ukedataene viser et klart sesongmønster knyttet til årlige høysesongperioder:

- **Høysesong F (ferskvare):** Rundt påske (uke 13–14) og jul (uke 50–52) viser F-volumet tydelige topper
- **Høysesong S (sekundærvare):** Mindre utpreget sesongvariasjoner, men markant topp omkring jul
- **Kampanjepåvirkning:** F har kampanje-flag aktivt 117 av 118 uker, noe som gjenspeiler kontinuerlig markedsføring. S har kampanjer på ~50 % av ukene

**Volatilitet og stabilitet:**

Volumene viser moderat volatilitet innenfor hver sesong. En full tidsserien-dekomponering (trend, sesong, residualer) er påkrevd for å identifisere stabiliteten av sesongmønsteret over tidsperioden. Denne analysen gjennomføres som del av SARIMAX-estimering.

### 7.2 Valgt prognosestrategi og modellvalg

**Baseline-etablering:**

Som referanse brukes Seasonal Naive (SNaive)-prognose: $\hat{y}_{t} = y_{t-52}$. Denne enkle modellen utgør sammenligningsstandard for SARIMAX-alternativer.

**SARIMAX-kandidater og estimering:**

Auto-ARIMA-algoritmen identifiserer kandidatmodeller basert på AIC/BIC-kriterier. For hver varestrøm vurderes (p,d,q)(P,D,Q,52)-kombinasjoner med fokus på parsimoniske modeller gitt det begrensede datasettet (104 treningsobservasjoner):

- Trend-orden $d$: Bestemt via ADF-test for stationaritet
- Sesong-orden $D$: Bestemt via sesong-differensiering og stasjonaritetskontroll
- AR/MA-ordener $(p,q,P,Q)$: Identifisert fra ACF/PACF-analyse, med preferanse for små verdier

Endelig modell estimeres via Maximum Likelihood Estimation (MLE) og valideres på out-of-sample data (2026-01 til 2026-13, 13 uker).

### 7.3 Kapasitetsmodell-setup (foreløpig)

**Prosess-tidsmatrise:**

Grunnlag: Åtte komplette produksjons-/dispatcher-par fra 2024, 2025 og 2026.
- **P1 (PD / for-klargj.):** 0.003885 minutter per FPK
- **P2 (ED / endelig dispatch):** 0.037555 minutter per FPK

Disse standardtider brukes til å konvertere prognostisert volum til arbeidsbelastning (minutter).

**Kapasitets-baseline:**

Fra `capacity_assumptions.csv`:
- P1: 24.0 mann-timer per uke (0.5 arbeider × 8 timer × 6 driftsnetter)
- P2: 144.0 mann-timer per uke (3.0 arbeidere × 8 timer × 6 driftsnetter)

**Kapasitets-kontroll:**

Høysesong-ukene (f.eks. uke 2024-11 med kombinert F+S-topp) analyseres:
- Prognostisert arbeidsbelastning i minutter beregnes
- Kapasitets-behov (mann-timer) estimeres
- Hvis behov > base-kapasitet, kreves ekstra tiltak (tidlig oppstart, overtid, bemanning)

**Kritiske observasjoner:**
- Sone-andeler (`zone_cutoff_profile.csv`) er nå beregnet fra `ED`-rader i dispatcherhistorikk og summerer til 1.000000
- `anomaly_flag` og `constrained_week_flag` er ikke validert, så enkelte anomale uker kan være klassifisert som normale
- LP-modellen har nå nødvendig soneinput, men bør fortsatt valideres med sensitivitetsanalyse for sonemiks og volumavvik

## 8.0 Resultater (FORELØPIG)

### 8.1 Datavalidering og aggregering

Følgende datasett ble etablert for modellering:

| Komponent | Perioder | Rader | Bemerk |
|-----------|----------|-------|--------|
| Treningsdata | 2024-01 til 2025-52 | 104 (uker) × 2 (strømmer) = 208 | Basis for SARIMAX-estimering |
| Valideringsdata | 2026-01 til 2026-13 | 13 × 2 = 26 | Out-of-sample test (uke 14 ekskludert pga. partial week) |
| **Totalt** | 2024-01 til 2026-13 | **234 rader** | Anonymisert som indeks (2024_avg_per_stream=100) |

**Datavasking:**
- Ordretype "-" ekskludert (dobbeltregistrering)
- Produktgruppe 850 (driftsmidler) ekskludert
- Resultat: 236 rader fra 118 sammenhengende uker

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

### 8.4 Kritiske funn og gjenstående arbeid

**Gjennomført:**
- ✅ Datakvalitet etablert (118 uker, 2 varestrømmer, anonymisert)
- ✅ Tidsmatrise beregnet (8-dags basis, robust)
- ✅ Kapasitets-baseline dokumentert
- ✅ SARIMAX-metodikk definert (med SNaive-baseline)
- ✅ LP-struktur formulert (enheter konsistente)

**Gjenstår (kart for implementasjon):**
- ❌ SARIMAX-kode implementering og validering
- ❌ SNaive baseline-resultat
- ❌ Sone-andeler beregnet eller dokumentert som antakelse
- ❌ LP-løser kjørt på test-scenarioer
- ❌ Sensitivitetsanalyse (±10 % volum, syk-fravær-variasjon)

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
- 118 sammenhengende uker = tilstrekkelig for sesongisk mønster-analyse
- Anonymisering via indekstransformasjon sikrer konfidensialitet uten å gjøre metoden uetterprøvbar
- Prosess-tidsmatrise basert på 8 representative uker fra 3 år gir robust grunnlag
- Publikum kan verifisere metodologi på indeks-skala (SARIMAX-validering, LP-struktur)

**Svakheter og begrensninger:**
- Sone-andeler er beregnet, men mappingen fra `Street` til cut-off må behandles som en operasjonell modellantakelse og testes i sensitivitet.
- Anomaly_flag ikke validert: Kan være anomale uker klassifisert som normale
- Campaign-flag har liten kraft for F: 99 % av F-ukene har kampanje, gir minimal differensiering
- Datavolum grensesnitt: 104 treningsobservasjoner × 52-ukes sesong = akkurat minimum for SARIMAX

**Konsekvenserfor tolkning:** Prognose-feil på validering kan bli større enn ideelt. Sensitivitetsanalyse må teste hvor robust LP er under ±10 % prognose-usikkerhet.

### 9.3 Operativ relevans og næringslivets perspektiv

**Modellens tiltenkte verdi:**
1. Erstatte reaktive ("vi må ringe inn ekstrahjelp på fredag") med proaktiv planlegging
2. Identifisere kritiske høysesong-uker som påkræver tidlig oppstart eller overtid
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

**Denne rapport-versjonen er et modellrammeverk, ikke full implementasjon.**

Gjenstår før operativ bruk:
1. **Full SARIMAX-implementering:** Python `statsmodels` eller R `forecast::auto.arima`
2. **Sone-andeler:** Beregn fra dispatcherhistorikk eller fastsett eksplisitte antakelser med sensitivitetsanalys
3. **LP-løsning:** Implementer i Python (PuLP, scipy.optimize) eller Excel Solver
4. **Validering:** Kjør på 2026-01 til 2026-13, sammenlign SARIMAX mot SNaive baseline
5. **Scenarioanalyse:** Test under ±10 % volum-usikkerhet, variabel sykefravær, kapasitetsbortfall

**Teoretisk bidrag:** Rapporten etablerer en metodisk tilnærming til integrering av SARIMAX-prognose og LP-optimering for sesongbundet etterspørsel under sonevise distribusjons-frister. Eksisterende litteratur på APP dekker ofte enten bare prognose ELLER optimer ing, sjeldent det integrerte oppsettet.

**Praktisk bidrag:** Demonstrerer hvordan bedriftsinterne data (volum, produksjonslister, dispatcher actions) kan transformeres fra rådata til anonymisert, reproduserbar modellgrunnlag uten å avsløre kommersielle hemmeligheter.

## 10.0 Konklusjon

### Besvarelse av problemstilling

**Hovedproblemstilling:**
*Hvordan kan vi kombinere etterspørselsprognoser og kapasitetsoptimering for å minimalisere ressursforbruk ved å sikre at prognostiserte volumer ferdigstilles innenfor sonevise distribusjons-cut-offs i en flerprosess næringsmiddelproduksjon?*

**Svar fra denne rapporten:**

Rapporten utvikler et **integrert modellrammeverk** bestående av:

1. **Etterspørselsprognose via SARIMAX:** Sesongbundne ukevolumer predikeres basert på 2 år med historiske data, kampanjekalender og sesongmønstre. SARIMAX-modellen handles som et first-class komponent i prognosemiksen, sammenlignet mot SNaive-baseline for robusthet.

2. **Kapasitetsoptimering via Linear Programming:** Gitt prognostisert etterspørsel, formuleres et LP-problem som minimerer totalt ressursforbruk (overtid, tidlig oppstart, ekstrabemanning) under distribusjonsfrist-constraints. Modellen håndterer den sammensatte flaskehals-dynamikken ved å eksplisitt modellere sonevise frister som ukentlige aggregerte constraints.

3. **Anonymisering som enabler:** Bedriftsinterne data (råvolum fra Qlik, dispatcher-tidsdata fra Outlook, produksjonslister) transformeres til anonymisert, publiserbar modellgrunnlag via indekstransformasjon. Metoden sikrer konfidensialitet samtidig som metodologi blir etterprøvbar.

**Konkrete funn:**
- Datagrunnlag på plass: 118 sammenhengende uker, 2 varestrømmer, anonymisert (weekly_volume_anonymized.csv)
- Prosess-tidsmatrise etablert: P1 = 0.004 min/FPK, P2 = 0.038 min/FPK (basert på 8 dager)
- Kapasitets-baseline dokumentert: P1 = 24 t/uke, P2 = 144 t/uke
- SARIMAX-metodikk definert med robusthet-sikringer (SNaive baseline, parsimoni, validering)
- LP-struktur formulert med enhetskonsistente constraints

### Gjenstår før operativ implementasjon

For at modellen skal kunne brukes til praktisk planlegging:
- ❌ SARIMAX-estimering og validering (Python implementering)
- ❌ Sone-andeler beregning (fra dispatcherhistorikk)
- ❌ LP-løsing på test-scenarioer
- ❌ Sensitivitetsanalyse under volum- og kapasitets-usikkerhet

Disse stegene ligger utenfor denne rapport-versjonen, men er detaljert planlagt i kapitlene 7–8.

### Teoretisk og praktisk bidrag

**For akademia:** Rapporten demonstrerer en systematisk tilnærming til integrering av tidsserieprognose og produktionsplanlegging under sesongbundne frister. Den kombinerer etablert litteratur (SARIMAX, LP) i en domene-spesifikk kontekst (næringsmiddellogistikk) og løser en reell operasjonell utfordring.

**For næringslivet:** Modellen gir et rammeverk for å gå fra reaktiv ("vi må ha ekstrahjelp") til proaktiv ("høysesong uke 11 krever 30 ekstratimer, planlegg i god tid") kapasitetsplanlegging. Estimatene kan brukes til investeringsbeslutninger (skal vi øke fast bemanning eller satse på fleksibel overtid?).

### Avsluttende refleksjon

Selv om denne rapporten ikke leverer fullt implementerte resultater (SARIMAX-valideringer, LP-løsninger), etablerer den et solid metodisk og datamessig fundament. Designen er defensibel både faglig og etisk, og prosessen demonstrerer disiplin i:
- Databehandling og anonymisering
- Matematisk konsistens (enhetskontroll, formulering)
- Metodisk robusthet (baseline-sammenligninger, dokumentasjon)
- Transparans om begrensninger og videre arbeid

**Fremtidig arbeid** bør prioritere (1) SARIMAX-implementering, (2) LP-validering med de beregnede soneandelene, og (3) sensitivitetstesting for å gjøre modellen fullt operativ.

---

**Dato for sluttrapport:** 29. april 2026
**Rammeverk-status:** Metodikk og datagrunnlag etablert, implementasjon påbegynt
**Innlevering:** Planlagt 30. april 2026

## 11.0 Bibliografi

### Primær litteratur – Tidsserieprognose og SARIMAX

Hyndman, R.J., & Athanasopoulos, G. (2021). *Forecasting: principles and practice* (3. utg.). OTexts. https://otexts.com/fpp3/
- *Bruk:* Kapittel 9 for ARIMA-teori, 9.9 for sesongmodeller, Kapittel 10 for eksogene variabler (ARIMAX). Sentral for modellvalg, residualdiagnostikk og hvorfor baseline-sammenligninger er kritiske.

Hyndman, R.J., & Khandakar, Y. (2008). Automatic time series forecasting: The forecast package for R. *Journal of Statistical Software*, 27(3), 1–22. https://doi.org/10.18637/jss.v027.i03
- *Bruk:* Kanonisk kilde for auto_arima stepwise-algoritmen. Sentral for 5.1b (modellseleksjon via AIC/BIC).

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
- Benchmark-studier av produksjonsbedrifter som bruker integrert prognose-optim isering

## 12.0 Vedlegg

_Legg inn vedlegg her ved behov._
