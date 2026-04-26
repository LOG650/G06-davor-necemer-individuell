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

**Prosessomfang:** Analysen dekker tre hovedprosessledd (primær pakkeprosess, sekundær pakkeprosess, distribusjonsklargjøring) og to varestrømmer (ferskvare og sekundær/handelsvare). *Begrunnelse:* Dette er de kritiske flaskehalsene identifisert i caset; andre prosesser har større fleksibilitet.

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

### 2.1 Etterspørselsprognose med tidsseriemodeller

Etterspørselsprognoser er kritisk for produksjonsplanlegging, spesielt når kapasiteten er begrenset og distribusjons-fristkrav må overholdes. **Tidsseriemodeller** er etablert praksis for volumdata: SARIMAX-modeller (Seasonal Autoregressive Integrated Moving Average with eXogenous variables) håndterer både trends, sesongmønstre og eksogene effekter typiske for næringsmiddelproduksjon.

**SARIMAX** kombinerer to sentrale egenskaper: (1) **SARIMA**-komponenten fanger sesongmønstre repetitive over året (påske, jul, sommerferie), som er kritisk for næringsmiddeletterspørsel; (2) **eXogenous variables**-delen inkorporerer kampanjekalender og andre eksterne faktorer. Dette er essensielt da bedriftens planlagte tilbud og kampanjer driver etterspørselstopperushet ut over det baseline sesongmønster kan forklare. (KML Kompendium, 2026, s. Demand Forecasting)

### 2.2 Kapasitetsplanlegging gjennom linear programming

**Linear Programming (LP)** er en veletablert metodikk for allokering av begrenset kapasitet når målet er å minimere kostnad eller ressursforbruk under strenge restruksjoner. **Aggregate Production Planning (APP)** løser nettopp dette: på ukentlig eller månedlig nivå bestemmer modellen hvor mye ekstra kapasitet (overtid, ekstrabemanning, tidlig oppstart) som kreves for å møte prognostisert etterspørsel innenfor faste distribusjons-cut-offs.

I dette prosjektet modelleres kapasitetsallokeringen som et LP-minimiseringsproblem. Målfunksjonen minimerer totalt ressursforbruk samtidig som distribusjonsfrister respekteres. (KML Kompendium, 2026, s. Production Planning)

### 2.3 Flaskehals-dynamikk i konvergerende logistikk

Når flere varestrømmer konvergerer til felles distribusjonsledd, oppstår kompleks kapasitetstilknytting: selv om total ukekapasitet er tilstrekkelig, kan et dags- eller sonesvis cut-off bli brutt hvis volumtoppingene ikke er tidssynkronisert. Litteraturen på nettverksdesign og produkt-distribusjon understreker at aggregering fra dag til uke kan maskere kritiske flaskehalser på sonenivå hvis ikke gjort carefully.

## 3.0 Teori

### 3.1 Tidsserieanalyse og prognoser

En **tidsserie** er en sekvens av observasjoner ordnet kronologisk, typisk med jevn tidsavstand (f.eks. ukentlige volumer). Tidsserier har tre karakteristiske komponenter:

- **Trend:** langvarig retning (stigning, stagnasjon, eller fall)
- **Sesongmønstre:** repeterende mønstre på kort sikt (f.eks. ukentlige eller årlige rytmer)
- **Residualer:** tilfeldig variasjon som ikke forklares av trend eller sesong

**SARIMAX-modeller** (Seasonal ARIMA with eXogenous variables) er matematiske rammer som modellerer disse komponentene samt eksterne påvirkninger. En SARIMAX-modell estimeres ved å minimere forskjellen mellom observerte verdier og modellens prediksjoner (vanligvis målt som Mean Absolute Error eller Root Mean Square Error).

Modellen består av fire deler: (1) **ARIMA-kjernen** håndterer autoregressive og moving average strukturer; (2) **Sesongkomponenten** modellerer repeterende mønstre over året (f.eks. 52 uker i ukesdata); (3) **Integreringsleddet** håndterer både trend (differensiering d) og sesongavdrift (sesongdifferensiering D); (4) **Eksogene variabler** (kampanjekalender, helligdager) fanges eksplisitt. Kombinasjonen av disse gjør SARIMAX spesielt egnet for sesongbundne varetyper med kjente kampanjepåvirkninger.

(KML Kompendium, 2026)

### 3.2 Linear Programming og optimering

**Linear Programming** er en matematisk optimeringsmetode for å finne beste beslutning under lineære begrensninger. Generell form:

```
Minimiser: c₁x₁ + c₂x₂ + ... + cₙxₙ  (Målfunksjon)
Under:     Ax ≤ b  (Lineære begrensninger)
           x ≥ 0   (Ikke-negativitet)
```

I **Aggregate Production Planning** bestemmer LP-modellen optimal allokering av kapasitet (overtid, ekstrabemanning, tidlig oppstart) gitt:
- Prognostisert etterspørsel (fra SARIMAX)
- Grunnkapasitet per uke per prosessledd
- Sonevise distribusjons-cut-offs som må respekteres
- Mål om å minimere total ekstra kapasitet

LP-modellen kan løses eksakt ved bruk av Simplex-algoritmen eller lignende. Løsningen er en optimal allokeringsplan for de tre hovedprosessene.

(KML Kompendium, 2026)

### 3.3 Modellintegrasjon i prosjektet

Dette prosjektet integrerer begge tilnærminger sekvensielt:

1. **Fase 1 – Etterspørselsprognose:** SARIMAX-modellen estimeres basert på historiske ukentlige volumdata, sesongmønstre og kampanjekalender, estimert separat for ferskvare og sekundærvare. Output: prognose per uke og varestrøm.
2. **Fase 2 – Kapasitetsoptimering:** LP-modellen bruker denne prognosen som fast input og bestemmer optimal kapasitetsallokering for å møte etterspørselen under sonevise frister.

Denne todelte strukturen sikrer at prognosefeil håndteres gjennom LP-modellens begrensninger (f.eks. penalty for fristbrudd) i stedet for å propagere usikkerhet direkte til operasjonelle beslutninger. Scenarioanalyse brukes til å teste modellrobusthet under prognoseusikkerhet.

## 4.0 Casebeskrivelse

### 4.1 Bedrift og bransje

Caset baseres på en anonymisert norsk bedrift innen næringsmiddelproduksjon og distribusjon. Bedriften har to parallelle produksjonsfilialer som feeder inn til et sentralisert distribusjonsledd:

- **Filial A (Ferskvare):** Kortlevetids friske matvarer med streng holdbarhet (1–7 dager)
- **Filial B (Sekundær/handelsvare):** Lengre-levetids pakket og lagret vare (uker til måneder)

Begge varestrømmer må gjennomgå samme distribusjonsledd før utsendelse til kunder. Dette er den kritiske flaskehalsen i systemet.

### 4.2 Operasjonell struktur

Distribusjonsoperasjonen består av tre hovedprosessledd:

1. **Primær pakkeprosess:** Pakking av ferskvare fra Filial A
2. **Sekundær pakkeprosess:** Håndtering og forberedelse av vare fra Filial B
3. **Distribusjonsklargjøring:** Sortering, palletisering, og lasting på utgående kjøretøy

Hver prosess har en grunnkapasitet (Standard Working Hours per uke). Kapasiteten er ikke fullt ut fleksibel, men kan utvides gjennom:
- Overtid
- Ekstra skift (bemanning)
- Tidlig oppstart av dagsproduksjonsteam (bare for sekundær vare)

### 4.3 Flaskehals-problematikk

Selv om den totale ukekapasiteten er tilstrekkelig når man aggregerer, oppstår regelmessige kapasitetsbrudd på grunn av **sonevise distribusjons-cut-offs**:

- Filial A har daglige cut-offs (f.eks. kl. 14:00) for hver kundesone
- Filial B har også daglige cut-offs, men senere på dagen
- Hvis både ferskvare og sekundærvare peaker samme dag, kan distribusjonsklargjøring ikke strekke til

**Eksempel:** En tirsdag må 80% av ukens volum ferdigstilles, mens resten av uken er underdimensjonert. Selv om total ukekapasitet = 100%, blir tirsdag en «crisis day» som krever massiv overtid.

Problemet forverres av sesongmønstre (høysesonger med kampanjer) som driver etterspørselen opp på spesifikke uker.

### 4.4 Tilgjengelige data

Bedriften har tilgang til:

- **Historisk volumdata:** Ukentlige volumer (FPK-ekvivalenter) for begge varestrømmer over minimum 2 år
- **Kampanjekalender:** Planlagte tilbud og markedsføringskampanjer som er kjent i forkant
- **Grunnkapasitet:** Dokumentert Standard Working Hours per uke for hver av de tre prosessene
- **Cut-off-spesifikasjon:** Sonevise cut-off-tider og aggregerte ukentlige krav per prosess
- **Kostnadsinformasjon:** Indikative kostnader for overtid, ekstrabemanning, og tidlig oppstart (kan være sensitiv)

### 4.5 Bedriftens utfordring og motivasjon

Bedriften søker en prognose- og optimeringsmodell som kan:

1. **Predikere etterspørsel** akkurat der volumene lander hver uke (under hensyn til sesong og kampanjer)
2. **Planlegge kapasitet** på ukebasis for de tre prosessene
3. **Minimere ressorsforbruk** (overtid og ekstrabemanning) ved å identifisere kritiske ukentlige topperusher tidlig

Med en slik modell kan ledelsen ta proaktive beslutninger i stedet for reaktive («vi må ringe inn ekstrahjelp på fredag fordi torsdag ble kaos»). Dette er både kostnad- og kvalitetsmessig viktig for bedriften.

## 5.0 Metode og data (kan splittes i to)

Litt avhengig av omfanget, kan det være lurt å vurdere om du skal splitte kapittelet i to eller ikke.

### 5.1 Metode – Etterspørselsprognose (SARIMAX)

**Paradigme:** Kvantitativ case-studie basert på historiske operasjonelle data fra en produksjon- og distribusjonsoperasjon.

**Datavindu og modellstrategi:** Datagrunnlaget for prognosedelen består av ukentlige observasjoner for perioden 1. januar 2024 til 31. desember 2025, totalt 104 observasjoner per varestrøm. Modellen trenes på denne perioden og valideres deretter out-of-sample mot observerte ukedata for perioden 1. januar 2026 til 31. mars 2026. På ukesnivå representeres dette som uke 2026-01 til 2026-14, der uke 14 starter 30. mars 2026 og dermed dekker 31. mars. Etter modellvalg re-estimeres endelig modell på hele det tilgjengelige datasettet før prognosen brukes som input til kapasitetsmodellen. Endelig modellspesifikasjon fastsettes etter datakontroll og innledende eksplorativ analyse, slik at modellens kompleksitet tilpasses datamaterialets kvalitet, lengde og tilgjengelige eksogene variabler.

**Prognosemodell:** SARIMAX (Seasonal Autoregressive Integrated Moving Average with eXogenous variables) velges fordi:
- Tidsseriene (ukentlige volumer) har **tydelige sesongmønstre** (høysesonger knyttet til julekampanjer, påske, sommerferie) og underliggende trend
- Eksogene variabler (kampanjekalender) påvirker etterspørselen betydelig utover sesongbasis-nivå
- Næringsmiddeletterspørsel er kjent for å følge årlige sesongmønstre som SARIMAX håndterer godt
- SARIMAX er etablert praksis i demand forecasting for sesongbundne varer (jf. Seksjon 2.0)

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

**Parameterestimering:** SARIMAX-parametere (p, d, q, P, D, Q, s) bestemmes via:
1. ADF-test (Augmented Dickey-Fuller) for å sjekke trend-stationaritet og velge d
2. Sesongdifferensiering og sjekk for sesong-stationaritet, velg D
3. ACF/PACF-plot for å identifisere p, q, P, Q
4. Auto-ARIMA med seasonal=True brukes som støtte til å identifisere rimelige kandidatmodeller for (p, d, q)(P, D, Q, s), siden manuell søking raskt blir vilkårlig når datamaterialet er begrenset
5. Endelig SARIMAX-modell estimeres med maximum likelihood estimation (MLE), og valg av modell støttes av informasjonskriterier og residualdiagnostikk

Siden hver varestrøm bare har 104 ukesobservasjoner i treningsperioden, estimeres parsimoniske modeller og sammenlignes mot enklere benchmark-modeller der det er relevant, for eksempel seasonal naive eller enklere SARIMA/SARIMAX-varianter.

**Validering:** Modellen evalueres out-of-sample mot observerte ukedata for perioden 1. januar 2026 til 31. mars 2026. Siden modellen bruker hele uker, behandles valideringsperioden som uke 2026-01 til 2026-14, etter at modellen først er estimert på data for 2024 og 2025:
- MAE (Mean Absolute Error)
- RMSE (Root Mean Squared Error)
- MAPE (Mean Absolute Percentage Error)
- Residual-diagnostikk (Ljung-Box test for autokorrelasjon og sesongavhengighet)

**Verktøy:** Python er hovedverktøyet i prognosedelen. `auto_arima` (for eksempel fra `pmdarima`) kan brukes som støtte til modellseleksjon, mens `statsmodels.tsa.statespace.sarimax.SARIMAX` brukes til endelig estimering, tolkning av koeffisienter for eksogene variabler, residualdiagnostikk og prognosegenerering. R med `forecast::auto.arima(seasonal = TRUE)` kan brukes som alternativ ved behov.

---

### 5.1b Metode – Kapasitetsoptimering (Linear Programming)

**Optimeringsproblem:** LP-modellen løser et aggregate production planning-problem (jf. Seksjon 6.0).

**Løsningsmetode:**
- Simplex-algoritmen eller interior-point method (avhengig av solver)
- Løsingen gir optimal allokering av overtimebehov per prosess per uke

**Sensitivitetsanalyse:** Shadow prices og reduced costs analyseres for å forstå:
- Hvor er de bindende constraints? (kritiske ressurser)
- Hva er verdien av 1 ekstra mann-time i hver prosess?
- Hvordan påvirker ulike penalty-vekter for fristbrudd løsningen?

**Scenarioanalyse:** Løsningen testes under:
- ±10% volumavvik (usikkerhet i prognose)
- Kapasitetsbortfall (f.eks. sykdom, maskinbrudd)
- Ekstreme høysesonger (topptyngde-uker)

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

Uten denne koblingen vil kapasitetsmodellen ikke kunne oversette forecast til faktisk ressursbehov. Datainnsamlingen prioriteres derfor mot et lite, relevant og etterprøvbart datagrunnlag fremfor store mengder detaljdata med begrenset modellverdi.

## 6.0 Modellering

### 6.1 Modellstruktur

Modellen består av to sekvensielle komponenter:

1. **Etterspørselsprognose (SARIMAX):** Basert på historiske ukentlige volumer for ferskvare (F) og sekundærvare (S) samt kampanjekalender, produseres punkt-prognoser for volumene i hver uke. Prognosen fanger sesongmønstre, eksogene effekter (kampanjer), og genererer prediktert volum `V_F,t` og `V_S,t` for uke `t`.

2. **Kapasitetsoptimering (LP):** Gitt prognostisert volum, bestemmes optimal kapasitetsallokering (overtimebehov, tidlig oppstart) per prosess for å møte sonevise frister med minimalt ressursforbruk.

---

### 6.2 Beslutningsvariabler

La `OT_j,t` = overtimebehov (mann-timer) i prosess j, uke t

Prosesser:
- j = 1: Primær pakkeprosess (ferskvare)
- j = 2: Sekundær pakkeprosess (sekundærvare)
- j = 3: Distribusjonsklargjøring (kombinert)

Tidsperiode:
- t = 1, 2, ..., T (planningshorisonten, f.eks. T=52 uker)

---

### 6.3 Målfunksjon

**Minimiser:**

$$Z = \sum_{t=1}^{T} \sum_{j=1}^{3} c_j \cdot OT_{j,t} + \sum_{t=1}^{T} \lambda \cdot SLACK_t$$

hvor:
- $c_j$ = kostnadsvektor per overtimetime i prosess j (ressursenhet eller relativ vekt)
- $SLACK_t$ = fristbrudd i uke t (FPK-enheter som ikke klargjøres innen sonevise cut-offs)
- $\lambda$ = penalty-vekt for fristbrudd (settes slik at fristbrudd prioriteres høyere enn overtimebehov)

**Tolking:** Målfunksjonen minimerer totalt overtimebehov over planningshorisonten, men tillater fristbrudd hvis det skulle være unavoidelig (testet gjennom scenarioanalyse).

---

### 6.4 Hovedkonstrants

**Kapasitetsrestriksjon per prosess:**

For hver prosess j og uke t:

$$V_{\text{eff}, j,t} \leq CAP_{j,\text{base}} + OT_{j,t}$$

hvor:
- $V_{\text{eff}, j,t}$ = effektivt volum (FPK-ekvivalenter) som krever behandling i prosess j, uke t
- $CAP_{j,\text{base}}$ = grunnkapasitet (mann-timer) i prosess j per uke
- $OT_{j,t}$ = overtimebehov (beslutningsvariabel)

Eksempel (grunnkapasitet):
- Primær pakking: 250 mann-timer/uke
- Sekundær pakking: 250 mann-timer/uke
- Distribusjonsklargjøring: 150 mann-timer/uke (3 mann × 10 timer × 5 netter)

---

### 6.5 Sonevise fristbegrensninger

Sonevise frister aggregeres som ukentlige andeler:

- **Sone 1 (kl 00:00):** Må ha **minst p₁ % av ukens distribusjonsvolum** ferdig innen denne fristen
- **Sone 2 (kl 01:00):** Må ha **minst p₁ + p₂ % av ukens distribusjonsvolum** ferdig innen denne fristen
- **Sone 3 (kl 02:00):** Må ha **minst p₁ + p₂ + p₃ = 100% ferdig innen denne fristen**

**Eksempel:** Hvis sone 1 normalt håndterer 30% av distribusjonsvolum:

$$V_{\text{dist}, t} \cdot 0.30 \leq CAP_{3,\text{base}} \cdot 0.30 + \text{(tilgjengelig overtid for sone 1)}$$

I enkel form (uten detaljert sone-fordeling):

$$V_{F,t} + V_{S,t} - SLACK_t \leq CAP_{3,\text{base}} + OT_{3,t}$$

hvor `SLACK_t` representerer volum som ikke klargjøres innen den samlede avgangsfristen.

---

### 6.6 Sekundærvare prioritering

Modellen prioriterer tidlig oppstart for sekundærvare når prognostisert volum krever det. Dette modelleres som en eksplisitt constraint:

$$V_{S,t} \leq CAP_{2,\text{base}} + OT_{2,t}$$

Hvis `OT_{2,t}` overstiger en terskelverdi, trigges en flagg som indikerer "tidlig oppstart anbefalt for uke t".

---

### 6.7 Ikke-negativitet

$$OT_{j,t} \geq 0 \quad \forall j, t$$
$$SLACK_t \geq 0 \quad \forall t$$

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

Hvordan skrive bacheloroppgave etter at metodedelen er laget? Jo, du lager en analyse.

Dette er siste bit før du kan presentere selve resultatene av studiene. Du kan velge mellom forskjellige metoder, nemlig:

- Kvalitativ metode (intervju eller lignende)
- Kvantitativ metode
- Dokumentanalyse

Prat gjerne med veilederen din om du er usikker på hvilken metode som er best for akkurat din problemstilling.

## 8.0 Resultat

Den kanskje viktigste delen når du skal skrive en bacheloroppgave, er resultatdelen. Her beskriver du alle funnene som er gjort i analyser og studier.

Det er viktig at du presenterer resultatene på en klar og tydelig måte, gjerne ved bruk av tabeller og figurer.

Noen viktige punkter:

- Dersom dette er et eget kapittel, skal dere her kun presentere resultatene i form av tabeller og/eller figurer.
- Tabeller: oppsummerte resultater.
- Resultatene skal være direkte linket til forskningsspørsmålet.
- Dersom de ikke er det, har du to alternativer: kjør analysene på nytt i henhold til forskningsspørsmålet, eller endre forskningsspørsmålet slik at det er samsvar med analysene.
- NB: Ha en forklarende tekst for hver tabell og hver figur.
- Som regel kommer teksten før tabellen/figuren, men noen ganger etter og noen ganger litt tekst både før og etter.
- Den forklarende teksten kan virke overflødig, men den må være med og skal være en objektiv presentasjon av det dere viser.

## 9.0 Diskusjon

I diskusjonsdelen skal du diskutere de forskjellige funnene du har gjort. Her skal du blant annet inkludere en kritisk metodediskusjon, der du vurderer om metoden din var riktig.

Diskuter hvor pålitelige funnene dine er, om de er generaliserbare og eventuelle svakheter. Forklar også hvorvidt studiet har gitt ny teoretisk innsikt, og om hypoteser kan avkreftes.

Noen viktige punkter:

- Her skal resultatene diskuteres.
- Studenter blander ofte sammen diskusjon og resultater.
- Her skal dere kommentere resultatene som dere har funnet.
- Er dette som forventet?
- Uventede funn? Hvis ja, hvordan kan dere forklare dette?
- Stemmer resultatene deres med forskningslitteraturen?
- Hvis ikke, hvorfor ikke? Det kan også være bra.
- Hvis ja, kan dere henvise til forskningslitteraturen for å understøtte resultatene.
- Resultatene skal diskuteres opp mot problemstillingen.
- Har dere fått svar på forskningsspørsmålet?
- Hvilken betydning har dette for næringslivet?
- Dette anbefales som eget punkt i diskusjonen.
- Hva medfører resultatene for næringslivet eller bedriften?
- Hvilke endringer bør bedriften eller næringslivet gjøre?
- Er det mulig å generalisere?
- Ta med begrensinger og svakheter i oppgaven.
- Ikke overfokuser på dette punktet, men vær ærlige.

## 10.0 Konklusjon

I oppgavens konklusjon oppsummerer du hovedfunn sett i forhold til problemstillingen.

Avslutt gjerne med spørsmål til videre forskning, og del personlige refleksjoner du eventuelt måtte ha.

Hva er det viktigste dere har funnet?

Konkluder i henhold til oppgavens problemstilling. Ofte begynner en konklusjon med å gjenta forskningsspørsmålet:

- "I denne oppgaven har vi analysert/redegjort for..."
- "Hovedfunnene i oppgaven viser at..."
- "På tross av de svakhetene som oppgaven har, er det indikasjoner på at..."

I konklusjonen blir det ofte litt gjentagelse fra diskusjon og resultat, men det er helt greit. Her skal dere dra frem de viktigste funnene og hvilken betydning de har for caset deres.

## 11.0 Bibliografi

KML Kompendium. (2026). *Quantitative methods in logistics: A framework for AI-driven research* [Online]. Tilgjengelig fra: https://kml-site-production.up.railway.app/

_Flere referanser vil legges til etter litteratursøk og analyse._

## 12.0 Vedlegg

_Legg inn vedlegg her ved behov._
