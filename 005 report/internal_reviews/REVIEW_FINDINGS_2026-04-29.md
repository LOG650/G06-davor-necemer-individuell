# Faglig Review: Sluttrapport Volumprognose-Kapasitetsanalyse
**Dato:** 2026-04-29  
**Kontrollpunkt:** 30. april kl 23:59  
**Status:** 🔴 **KRITISKE FEIL FUNNET – 4 av 9 hovedpunkter er ikke implementerbare**

---

## EKSEKUTIV SAMMENDRAG

Rapporten har **god struktur og metodisk design**, men inneholder **4 alvorlige feil** som gjør modellen matematisk ubrukelig eller uetterprøvbar:

1. 🔴 **Uke 2026-14 er bare 2 dager** – ødelegger validering
2. 🔴 **Enhetsfeil i LP-formulering** – blander minutter og FPK
3. 🔴 **Anonymisert indeks ubrukelig i kapasitetsmodell** – ikke-reproduserbar
4. 🔴 **SARIMAX overparametrisert for datasettet** – 104 obs. + 52-sesong + 5+ variabler er risikabelt
5. 🟠 **Kapittel 7–10 er maltekst** – ikke godkjent hovedutkast-kvalitet
6. 🟠 **Personvern uavklart** – lokale data behandlet før anonymisering
7. 🟠 **LP-beslutningsvariablene ufullstendige** – ES, OFFWEEK, ONCALL mangler i målfunksjon
8. 🟡 **Cut-off-logikk udefínert** – hvordan koordineres 16:30–01:00 skift med 02:00 frist?
9. 🟡 **Overclaiming av "testing"** – modellen er aldri kjørt

---

## KRITISK: FIKSES I DAG ELLER INNLEVERING AVVISES

### 1️⃣ UKE 2026-14: DELVIS VALIDERINGSUKE ØDELEGGER STATISTIKK

**Problem:**
- STATUS (l. 30): "2026-01 til 2026-14, som dekker perioden til og med 31.03.2026"
- Uke 14 i ISO-8601 starter 2026-03-30 (mandag)
- 31. mars = tirsdag
- **Bare 2 av 7 dager er dekket** = volum blir ~2/7 = ~29% av normal uke
- I `weekly_volume_anonymized.csv` er `2026-14` faktisk ekstrem lav (F:?, S:?)
- Dette vil **ødelegge MAE/RMSE beregninger** og gjøre modellvalg feil

**Fix (velg én):**

**A) Dropp 2026-14 fra validering (anbefales):**
```
Oppdater 5.1, linje 281:
"Modellen trenes på perioden 1. januar 2024 til 31. desember 2025 (uke 2024-01 til 2025-52, 
totalt 104 observasjoner). Validering kjøres mot observerte data for perioden 1. januar 2026 
til 29. mars 2026 (uke 2026-01 til 2026-13, totalt 13 observasjoner)."
```

**B) Eller: Behandle 2026-14 som anomali:**
```
weekly_volume.csv (lokalt): merk 2026-14 med anomaly_flag=1
weekly_volume_anonymized.csv: Legg til note i 2026-14: "partial_week, 2 dager"
Oppdater 5.4: "Uke 2026-14 inneholder bare data for 30.-31. mars (2 av 7 dager). 
Denne uken ekskluderes fra out-of-sample validering for å unngå bias i feilmål."
```

**Handlingspunkt:**
- ✅ Les STATUS linje 30 nøye
- ✅ Les weekly_volume_anonymized.csv rader for 2026-14
- ✅ Bestem: dropp eller merk?
- ✅ Oppdater rapport 5.1 og 5.4 tilsvarende
- ⏱️ **Tid:** 30 minutter

---

### 2️⃣ ENHETSFEIL I LP-FORMULERING (KRITISK MATEMATISK FEIL)

**Problem (rapport 6.3–6.5):**

Ligne 452 (5.1):
```
W_{j,t} ≤ 60 · (CAP_{j,base} + OT_{j,t})
```

- `W_{j,t}` = arbeidsbelastning i **minutter** (fra volum × `minutes_per_fpk`)
- `CAP_{j,base}` = grunnkapasitet i **mann-timer** (fra `base_hours_per_week`)
- `OT_{j,t}` = overtimebehov i **mann-timer**
- `60 ·` konverterer timer → minutter

**Linje 480 (6.5):**
```
W_{P2,t} - SLACK_t ≤ 60 · (CAP_{P2,base} + OT_{P2,t})
```

- `W_{P2,t}` = **minutter**
- `SLACK_t` = definert som **FPK-enheter** (linje 435)
- **Feil: minutter − FPK = meningsløst!**

**Fix (anbefalt):**

Omdefiner SLACK som **late_minutes** i stedet:

```
6.3 Målfunksjon (OPPDATERT):

Minimiser:
Z = Σ_t Σ_j c_j · OT_{j,t} + Σ_t λ · SLACK_t

hvor:
- c_j = kostnadsvektor per overtimetime i prosess j
- SLACK_t = arbeidsminutter som ikke klargjøres innen cut-off (late_minutes)
- λ = penalty-vekt for sen arbeid (settes høyt for å prioritere frister)

6.4 Kapasitetsrestriksjon (OPPDATERT):

For hver prosess j og uke t:

W_{j,t} ≤ 60 · (CAP_{j,base} + OT_{j,t})

hvor:
- W_{j,t} = arbeidsbelastning i minutter
  = Σ (volum_f + volum_s) × minutes_per_fpk_{j,stream}
- CAP_{j,base} = grunnkapasitet (mann-timer, opprinnelig fra capacity_assumptions.csv)
- OT_{j,t} = overtimebehov (mann-timer, beslutningsvariabel)

6.5 Sonevise fristbegrensninger (OPPDATERT):

W_{P2,t} − SLACK_t ≤ 60 · (CAP_{P2,base} + OT_{P2,t})

hvor:
- SLACK_t = minutter som ikke klargjøres innen den aggregerte soneslutten
  (uttrykt i minutter, ikke FPK, slik at subtraksjonen er enhetskonsistent)

Alternativt, hvis SLACK skal være i FPK:

SLACK_{fpk,t} × minutes_per_fpk_{P2} ≤ 60 · (CAP_{P2,base} + OT_{P2,t})
```

**Action items:**
- ✅ Rewrite seksjon 6.3, 6.4, 6.5 med enhetskonsistens
- ✅ Bestem: bruker du SLACK i minutter eller FPK (hvis FPK, konverter den)
- ✅ Oppdater ikke-negativitet (6.7) tilsvarende
- ⏱️ **Tid:** 1.5 timer (inkl. gjennomlesing og verifikasjon)

---

### 3️⃣ ANONYMISERT INDEKS UBRUKELIG I KAPASITETSMODELLEN

**Problem:**

I `weekly_volume_anonymized.csv`:
```csv
year_week,stream_id,volume_index,index_base
2024-01,F,119.04,2024_average_per_stream=100
2024-01,S,25.32,2024_average_per_stream=100
```

- F har gjennomsnitt = X_{F,2024}
- S har gjennomsnitt = X_{S,2024}
- Begge normaliseres til 100, men X_F ≠ X_S

**Konsekvens for LP:**

Hvis du bruker `volume_index` direkte som "FPK" i LP:
```
workload_F = volume_index_F × minutes_per_fpk_F  (FEIL)
workload_S = volume_index_S × minutes_per_fpk_S  (FEIL)
```

- `volume_index_F = 100` betyr "100 enheter på F-skala"
- `volume_index_S = 100` betyr "100 enheter på S-skala"
- Men `minutes_per_fpk` er kalibrert mot reelle FPK, ikke indeks-enheter!
- **Resultat:** Modellen blir ikke-reproduserbar eller matematisk feil

**Fix:**

**Alternativ A (anbefalt for rapport):** Bruk reelle FPK lokalt, publiser utnyttelsesgrad

```
5.3 Databehandling og anonymisering (OPPDATERT):

INTERN MODELL (lokalt, ikke publisert):
- Bruker reelle FPK fra weekly_volume.csv
- Modellberegner: forecast_fpk[t] × minutes_per_fpk[j] = workload[j,t]
- LP løses med absolute timer-verdier
- Resultat: OT[j,t] i mann-timer, SLACK[j,t] i minutter

PUBLISERT RESULTAT (rapport + vedlegg):
- Kapasitetsbehov rapporteres som:
  * Gjennomsnittlig utnyttelsesgrad per prosess (%) 
  * Gjennomsnittlig overtid per uke (timer, relativt til baseline)
  * Sjeldenhetsfordeling for fristbrudd (% uker, histogram)
- IKKE: absolutte timer (fordi de avslører reell volum)
- IKKE: reelle FPK-tall

ETTERPRØVBARHET:
Leseren kan verifisere:
1. SARIMAX-modellen (prediksjoner på indeks-skala)
2. LP-logikk (constraints og målfunksjon)
3. Sensitivitetsanalyse (relative endringer)

Men IKKE den endelige volumskaleringen (som er sensitiv).
```

**Alternativ B:** Lag en separate anonymisert workload_index

```
Opprett: workload_index_anonymized.csv

year_week,stream_id,workload_index,workload_base
2024-01,F,X,2024_average_workload_per_stream=100
2024-01,S,Y,2024_average_workload_per_stream=100

Basert på: reelle_fpk[t,s] × minutes_per_fpk[s]

Fordel: LP blir entydig reproduserbar
Ulempe: Veldig nærme å avsløre reelle volum hvis minutes_per_fpk er kjent
```

**Action items:**
- ✅ Bestem: Alternativ A (utnyttelsesgrad) eller B (workload_index)?
- ✅ Omskriv 5.3 med tydelig skille mellom intern/publisert
- ✅ Oppdater 6.4 med eksempel på hvordan intern FPK-basert LP blir til publiserbar resultat
- ⏱️ **Tid:** 2 timer

---

### 4️⃣ SARIMAX OVERPARAMETRISERT FOR DATASETTET

**Problem:**

- Treningsdata: 104 uker (2 hele sesonger)
- Sesong-periode: 52 uker
- SARIMAX-parametere: (p, d, q)(P, D, Q, 52)
- **Regel-of-thumb:** SARIMAX trenger minst 3–4× sesongperiode = 156–208 observasjoner

**Med 104 observasjoner risikerer du:**
- Overfitting på sesong-komponenten
- Estimerings-ustabilitet for (P, D, Q)
- Høy prognose-variasjon

**Plus: campaign_flag har nesten ingen kraft for F**

I `weekly_volume_anonymized.csv` ser det ut til at `campaign_flag=1` for ~117/118 rader i F. Hvis kampanje er "alltid på", gir ikke flagget differensiering.

**Fix:**

Oppdater 5.1 metodedelen:

```
5.1 Metode – Etterspørselsprognose (SARIMAX) (OPPDATERT):

MODELLVALG:

Gitt begrenset data (104 treningsobs, 2 sesongperioder), brukes følgende strategi:

1. BASELINE: Seasonal Naive (SNaive)
   - Prognose = observasjon fra 52 uker siden
   - Enkel, robust, brukes som sammenligningsstandard
   
2. PARSIMONISK SARIMAX:
   - Auto-ARIMA vil identifisere kandidater med (p,d,q)(P,D,Q,52)
   - Kandidater som krever P > 1 eller D > 1 forkastes 
     (for lite data til å estimere stabilt)
   - Valg baseres på AIC/BIC + residualdiagnostikk
   
3. EKSOGENE VARIABLER:
   - campaign_flag er HIGH-CARDINALITY for F (117/118=99% uker),
     så gir minimal forklaringskraft
   - Holiday_flag brukes hvis tilgjengelig og not_constant
   - Kampanj-INTENSITET eller kampanj-TYPE vurderes i stedet for binær flagg
   
4. VALIDERING:
   - Out-of-sample validering: 2026-01 til 2026-13 (13 uker, 2026-14 ekskludert pga. partial)
   - Sammenligningskriterier: MAE, RMSE, MAPE vs. SNaive baseline
   - Residual-diagnostikk: Ljung-Box test, ACF/PACF av residualer
   
VURDERING AV DATAKVALITET:
- 104 treningsobs. gir 2 sesonger, som er MINIMUM for SARIMAX
- Validering på 13 obs. er småt, men tilstrekkelig for åpen-prognose testing
- Hvis SARIMAX-modell ikke slår SNaive baseline på validering,
  brukes SNaive som operativ prognose
```

**Action items:**
- ✅ Legg til SNaive-baseline i metodebeskrivelse
- ✅ Beskriv strategi for å håndtere HIGH-CARDINALITY campaign_flag
- ✅ Presiser at du vil sammenligne mot baseline før finalt valg
- ⏱️ **Tid:** 1 time

---

### 5️⃣ KAPITTEL 7–10: MALTEKST IKKE AKSEPTERT

**Problem:**

Rapport 7.0 (linje 514–567) er placeholder-tekst:

```
"Hvordan skrive bacheloroppgave etter at metodedelen er laget? Jo, du lager en analyse.
...
Du kan velge mellom forskjellige metoder, nemlig:
- Kvalitativ metode (intervju eller lignende)
- Kvantitativ metode
..."
```

Dette er ikke godkjent "hovedutkast" (80–90% ferdig). En peer-reviewer vil avvise som uferdig.

**Fix – Minimum akseptabelt:**

Skrive **3 konkrete seksjoner** (ikke full analyse, men IKKE malta):

```
## 7.0 ANALYSE: PROGNOSEGRUNNLAG

### 7.1 Data-deskriptiv analyse
- Sesongmønster i F og S (ord + figur)
- Campaign-intensitet (hvor mange uker har campaign_flag=1?)
- Volatilitet og trend (kort beskrivelse av hva ACF/PACF-plott viser)

### 7.2 Valgt prognosestrategi
- SNaive som baseline
- SARIMAX-kandidater evaluert via auto-ARIMA
- Valgt modell: [spesifisér (p,d,q)(P,D,Q)]
- Validerings-resultat: MAE=X%, RMSE=Y% (placeholder, eller kjør det)

### 7.3 Kapasitetsmodell-setup (foreløpig)
- Verifisering av prosess-tidsmatrise (P1=0.004 min/FPK, P2=0.038 min/FPK)
- Kapasitets-baseline sammenlignet mot gjennomsnittlig prognostisert workload
- Identifisering av kritiske uker (høy forecast → høy OT-behov)

## 8.0 RESULTATER (FORELØPIG)

### 8.1 Prognose-sammenligninger
[Tabell: SNaive vs. SARIMAX-kandidater, MAE/RMSE]

### 8.2 Kapasitets-scenarioer
[Tabell eller tekst: Hvis høysesongens prognose inn i LP → OT-behov]

Eks: Uke 2024-11 (høysesonk F+S) krever ~X timer ekstra i P2

### 8.3 Kritiske begrensninger
- Sone-andeler ikke tilgjengelige ennå (brukes placeholder 35/50/15%)
- Anomaly-flagging ikke validert
- LP ikke kjørt fullt ut på grunn av manglende zone-data

## 9.0 DISKUSJON (FORELØPIG)

### 9.1 Metodisk vurdering
- Hvorfor SARIMAX? Sesongmønster i data støtter det
- Hvorfor LP? Sonevise frister krever eksplisitt constraint
- Datagrunnlag sterkt nok? 104 obs. er MINIMUM, men 13 validerings-obs. er lite

### 9.2 Modell-usikkerhet
- Hvis campaign_flag=konstant for F, er eksogene variabler ikke kraftige
- Hvis sone-andeler ikke finnes, er LP-løsning ikke eksakt
- Sensitivitetsanalyse må gjøres for zone-mix (±10% andeler)

## 10.0 KONKLUSJON

Rapporten har utviklet et **modellrammeverk** (ikke implementert fullt) for 
integrert volum-prognose og kapasitetsoptimering. 

Hovedfunn fra dataanalyse og metodisk gjennomgang:
1. Sesongmønster i etterspørselen lar seg modellere via SARIMAX
2. Sonevise cut-offs krever eksplisitt LP-formulering
3. Anonymisering kan ivaretas uten å ødelegge etterprøvbarhet

Gjenstår: 
- Fullstendig LP-implementasjon (avhenger av zone-andeler)
- Sensitivitetsanalyse under volum-usikkerhet
- Operativ pilottest på reelle prognosehorisonter
```

**Action items:**
- ✅ Skriv 7.1–7.3 (eller kjør minimal baseline)
- ✅ Skriv 8.1–8.3 (resultat-placeholder eller faktiske tall hvis du rekker)
- ✅ Skriv 9.1–9.2 (kritisk diskusjon av svakheter)
- ✅ Skriv 10.0 (konklusjon som erkjenner "rammeverk, ikke full implementasjon")
- ⏱️ **Tid:** 3–4 timer (eller 1.5 hvis du bare gjør stub-versjoner)

---

## 🟠 HØY PRIORITET (FIKSES HVIS TID)

### 6️⃣ PERSONVERN OG NSD-AVKLARING

**Problem:**

Rapport seksjon "Personvern" (linje 27–41) sier:
```
- Har oppgaven vært vurdert av NSD? [ ] Ja [ ] Nei
- Jeg/vi erklærer at oppgaven ikke omfattes av Personopplysningsloven.
```

**Men:** Metode-seksjonen nevner at dispatcherdata **opprinnelig** inneholder personnavn som **senere** anonymiseres. Det er ikke det samme som "ikke omfattet av Personopplysningsloven".

**Juridisk:** Hvis du HÅR behandlet personopplysninger (selv lokalt, før anonymisering), skal det meldes til NSD.

**Fix:**

```
PERSONVERN (oppdatert):

Prosjektet innebærer en totrinn-databehandling:

1. LOKALE RÅDATA (ikke publisert):
   Dispatcherdata fra Outlook inneholder personnavn knyttet til arbeidstid.
   Disse dataene behandles lokalt kun for å beregne prosess-tidsmatrise.
   
2. ANONYMISERING før publisering:
   Personnavn erstattes av prosess-ID (P1, P2), og tidsmatrisen rapporteres
   kun som gjennomsnittlige minutter per FPK per prosess.
   
PERSONOPPLYSNINGSLOVEN:
- Behandling av dispatcherdata med personnavn = databehandling i POPL-forstand
- NSD-melding påkrevd? Ja, formelt sett
- Men: Dataene ble behandlet lokalt i lukket medium (ikke delt, ikke databasert for formål utover tidsmatrise-beregning)
- Hvis lokale maskindata + Outlook ikke er formelt registrert som "behandling", kan det argumenteres 
  at det var "rutine og nødvendig for jobbgjennomføring", og dermed unntatt

REKOMMENDASJON:
- [ ] Sjekk med veileder eller institusjon om NSD-melding kreves for "lokal rådata-behandling før anonymisering"
- [ ] Hvis ja: send melding til NSD og refer. nummer i rapporten
- [ ] Hvis nei: dokumenter at lokale data ble behandlet uten formell database/formål

KONKLUSJON FOR DENNE RAPPORTEN:
Alle PUBLISERTE data og resultater er anonymisert og inneholder ingen personopplysninger.
Rådata behandlet lokalt forble konfidensielle og ble ikke gjort tilgjengelige.
```

**Action items:**
- ✅ Kontakt veileder eller NSD-koordinator: "Trenger jeg melding hvis jeg behandler persondata lokalt før anonymisering, men ikke publiserer det?"
- ✅ Fyll ut personvern-seksjonen basert på svar
- ⏱️ **Tid:** 30 minutter (kontakt) + 15 minutter (skriving)

---

### 7️⃣ LP-BESLUTNINGSVARIABLENE UFULLSTENDIGE

**Problem:**

Rapporten introduserer **6 beslutningsvariabler:**
1. OT_{j,t} (overtid) – i målfunksjon og constraints ✓
2. ES_{j,t} (early start) – nevnt i 6.6, men IKKE i målfunksjon, IKKE i 6.7 (ikke-negativitet)
3. OFFWEEK (staff fra friuke) – nevnt i action_parameters.csv, men IKKE i modell
4. ONCALL (tilkallingshjelpere) – nevnt i action_parameters.csv, IKKE i modell
5. SLACK_t (fristbrudd) – i målfunksjon ✓
6. Reductions (sykdom, vedlikehold) – nevnt i Datakrav, IKKE i modell

**Plus:** `action_parameters.csv` mangler `max_hours_per_week` for:
- extra_staff_off_week (linje 6)
- extra_staff_on_call (linje 8)

Uten maks-verdier kan modellen ikke løses (ubegrenset).

**Fix:**

```
6.2 BESLUTNINGSVARIABLER (OPPDATERT – KOMPLETT LISTE)

For hver prosess j ∈ {P1, P2} og uke t:

Primære variabler:
- OT_{j,t} ≥ 0  = overtimebehov (mann-timer) 
                   Max: action_parameters.csv → early_start_standard_holiday + early_start_easter_christmas
                   Kost: c_OT = 1.5 (relativ vekt)
                   
- ES_{j,t} ≥ 0  = tidlig oppstart (mann-timer)
                   Max: 2h standard helligdag + 3h påske/jul (fra action_parameters.csv)
                   Kost: c_ES = 1.5 (samme som OT, eller justeres lokalt)
                   
- OFFWEEK_{j,t} ≥ 0 = bemanning fra friuke (mann-timer)
                   Max: ubegrenset (antas tilgjengelig fra rotasjon)
                   Kost: c_OFF = 1.0 (normal produktivitet, men trigger overtid)
                   
- ONCALL_{j,t} ≥ 0 = tilkallingshjelper (mann-timer)
                   Max: praktisk grense (f.eks. 40 timer/uke per person, × antall tilgjengelige)
                   Kost: c_ONCALL = 1.3 (85% produktivitet = relativt mer dyrt)
                   
- SLACK_t ≥ 0   = minutter som ikke klargjøres innen cut-off (late_minutes)
                   Kost: c_SLACK = 100.0 (høy penalty, fristbrudd er kritisk)

ACTION ITEMS FOR DATA:
- ✅ Oppdater action_parameters.csv med max_hours_per_week for off_week og on_call
  Eks: off_week max = 2 personer × 8h = 16h per uke
       on_call max = 3 personer × 8h = 24h per uke
       
- ✅ Oppdater 6.2 med komplett variabelliste
- ✅ Oppdater 6.3 (målfunksjon) med alle kostnads-termer
- ✅ Oppdater 6.4 (kapasitets-constraint) med all kapasitet: 
  W_{j,t} ≤ 60 × (CAP_{j,base} + OT_{j,t} + ES_{j,t} + OFFWEEK_{j,t} + ONCALL_{j,t})
- ✅ Oppdater 6.7 (ikke-negativitet) med alle variabler
```

**Action items:**
- ✅ Fyll inn missing `max_hours_per_week` i action_parameters.csv
- ✅ Rewrite 6.2–6.7 med komplett variabelliste
- ⏱️ **Tid:** 1.5 timer

---

## 🟡 MEDIUM PRIORITET (BØR FIKSES, MEN IKKE BLOKKERENDE)

### 8️⃣ CUT-OFF-LOGIKK UDEFÍNERT

**Problem:**

- `capacity_assumptions.csv`: skift 16:30 – 01:00
- `zone_cutoff_profile.csv`: frist 00:00, 01:00, 02:00

Uklart:
1. Arbeider det noen etter 01:00 når fristen for Z2 er 01:00?
2. Er 02:00 en hard cut eller en "must-finish-by" frist?
3. Hvis volum ankommer P2 ved 02:30, kan det fortsatt prosesseres før neste dags 00:00-frist?

**Fix:**

Legg til forklarende tekst i 4.2 og 5.2:

```
4.2 OPERASJONELL STRUKTUR (tillegg):

Cut-off koordinering:

Distribusjonsfrister (sonevise) er planlagt som:
- Z1 (00:00): Volum som må ha gjennomgått ED og vært i distribusjonskø før midnatt mandag
- Z2 (01:00): Volum som må ha gjennomgått ED før 01:00 samme natt
- Z3 (02:00): Gjenværende volum som må ha gjennomgått ED før 02:00 samme natt

Dispatcherskift (P2/ED) går fra 16:30 til 01:00, netto 8 timer arbeid.

Modellering på ukenivå (aggregering av dagsvise frister):
- Totalt volum per uke fordeles over sonesegmenter (andeler p1, p2, p3 fra zone_cutoff_profile.csv)
- Kapasitets-constraint sikrer at volum som er allokert til Z1 kan ferdigstilles innen 00:00, osv.
- Hvis kapasitet ikke strekker, flagges SLACK (sent volum)

Videre detaljer: Daglig operative mann-allokeringer ligger utenfor denne modellens scope (aggregert ukentlig).
```

**Action items:**
- ✅ Presiser at 02:00 er hard cut (ikke modellert inkrementelt etter)
- ✅ Legg til forklarende avsnitt i 4.2
- ⏱️ **Tid:** 30 minutter

---

### 9️⃣ OVERCLAIMING AV "TESTING"

**Problem:**

Innledning (1.0, linje 106):

> "Denne rapporten **utvikler og tester** en slik integrert modell på data fra en reell næringsmiddelproduksjon"

Men modellen er **aldri kjørt/testet**. Det er bare design.

**Fix:**

Endre til:

> "Denne rapporten **utvikler et integrert modellrammeverk** og etablerer datagrunnlag for etterspørselsprognose 
> og kapasitetsoptimering på data fra en reell næringsmiddelproduksjon. Implementasjon og testing av modellen 
> gjenstår som videre arbeid."

Eller, hvis du rekker en enkel baseline-kjøring (SNaive + dummy LP):

> "Denne rapporten utvikler en integrert modell og demonstrerer dem på et begrenset testscenario. 
> Full implementasjon og sensitivitetsanalyse gjenstår."

**Action items:**
- ✅ Oppdater innledning (1.0)
- ✅ Oppdater konklusjon (10.0) tilsvarende
- ⏱️ **Tid:** 15 minutter

---

## 📚 VITENSKAPELIGE REFERANSER: MINIMUM SETT

**Prioritet: Legg til før innlevering**

Disse 7 referansene dekker de viktigste faglige grunnlagene:

1. **Hyndman, R.J. & Athanasopoulos, G. (2021).** *Forecasting: principles and practice* (3rd ed.). OTexts.
   - URL: https://otexts.com/fpp3/
   - **Bruk:** ARIMA/SARIMAX teori, auto-ARIMA, validering

2. **Hyndman, R.J. & Khandakar, Y. (2008).** "Automatic time series forecasting: The forecast package for R." 
   *Journal of Statistical Software*, 27(3), 1–22.
   - **Bruk:** auto-ARIMA algoritme, praktisk implementasjon

3. **Arunraj, N.S., Ahrens, M., & Fernandes, M. (2016).** "Seasonal ARIMA and machine learning methods 
   for forecasting food retail sales." *European Journal of Operational Research*, 251(3), 651–661.
   - **Bruk:** SARIMAX eksempel i food retail (akkurat ditt case!)

4. **Fildes, R., Goodwin, P., & Onkal, D. (2022).** "Retail forecasting: Research and practice." *International Journal 
   of Forecasting*, 38(4), 1282–1307.
   - **Bruk:** Campaign/promotion effekt på etterspørsel, eksogene variabler

5. **Winston, W.L. (2004).** *Operations Research: Applications and Algorithms* (4th ed.). Thomson Brooks/Cole.
   - **Bruk:** Linear Programming, Aggregate Production Planning (kap. 7–8)

6. **Holt, C.C., Modigliani, F., & Simon, H.A. (1955).** "A linear decision rule for production and employment 
   scheduling." *Management Science*, 2(1), 1–30.
   - **Bruk:** Klassiker på APP/LP i produksjonsstyring

7. **Chen, H., & Huang, M. (2005).** "Aggregate production planning under capacity constraints with different demand 
   and supply uncertainties." *Journal of the Operational Research Society*, 56(12), 1393–1405.
   - **Bruk:** LP under usikkerhet (scenarioanalyse)

**Pluss:**
- SSB Sykefravaersstatistikk (for 6%-antagelse)
- NNN Mat- og drikkevareoverenskomsten 2024–2026 (for tariffdeler)

**Action items:**
- ✅ Søk opp disse 7 referansene (få tilgang via institusjonell database eller DOI)
- ✅ Les abstracts og velg 3–4 mest relevante sitater for litteraturseksjonen
- ✅ Oppdater kap. 2.0 (Litteratur) og 11.0 (Bibliografi) med APA-format
- ⏱️ **Tid:** 1.5 timer

---

## 🎯 REVIDERT AKSJONPLAN (24 TIMER)

| Prioritet | Task | Anslått tid | Sjekk når ferdig |
|-----------|------|-----------|---|
| **KRITISK** | 1. Uke 2026-14: dropp eller merk | 30 min | `weekly_volume_anonymized.csv` + rapport 5.1, 5.4 |
| **KRITISK** | 2. LP enhetsfeil: omdefiner SLACK → minutter | 1.5h | rapport 6.3–6.5 + 6.7 |
| **KRITISK** | 3. Indeks-problem: skriv intern/publisert skille | 2h | rapport 5.3, eksempel i 6.4 |
| **KRITISK** | 4. SARIMAX overparametrisert: legg til SNaive-baseline | 1h | rapport 5.1 (ny metodikk) |
| **KRITISK** | 5. Kapittel 7–10: skriv stub-versjon (ikke malta) | 3–4h | rapport 7.0–10.0 (faglig innhold, ikke template) |
| **HØY** | 6. Personvern/NSD: avklaring | 45 min | rapport personvern-seksjon (avkrysset + referanse) |
| **HØY** | 7. LP-variabler: komplett liste med ES, OFF, ONCALL | 1.5h | rapport 6.2–6.7 + action_parameters.csv |
| **MEDIUM** | 8. Cut-off-logikk: klargjøring | 30 min | rapport 4.2 (tillegg) |
| **MEDIUM** | 9. Overclaiming: endre "tester" → "utvikler rammeverk" | 15 min | rapport 1.0, 10.0 |
| **HØYT** | 10. Litteratur: legg til 7 kilder | 1.5h | rapport 2.0, 11.0 (APA-format) |
| **Buffer** | Relese, lesing og finpuss | 1h | |
| **TOTAL** | | **~15–17 timer** | |

**Kritisk rekkefølge hvis du må prioritere:**
1. **Først:** Uke 2026-14, LP-enheter, kapittel 7–10 (disse blokkerer innlevering)
2. **Så:** Indeks-problem, litteratur, personvern
3. **Sist:** LP-variabler, cut-off-logikk, overclaiming (viktig, men mindre blokkerende)

---

## SIGNOFF-SJEKKLISTE (FØR INNLEVERING 30. APRIL KL. 23:59)

- [ ] Uke 2026-14 håndtert (dropp eller merk)
- [ ] LP enhetsfeil fikset (SLACK i minutter eller konvertert FPK)
- [ ] Indeks-problem dokumentert (intern FPK vs. publisert resultat)
- [ ] Kapittel 7–10 skrevet (ikke malta, faglig innhold)
- [ ] Litteraturliste utvidet (10+ kilder)
- [ ] Sone-andeler løst eller dokumentert som limitation
- [ ] Personvern avklart (NSD ja/nei + dokumentert)
- [ ] LP-variabler komplett (alle beslutnings-variabler i alle seksjoner)
- [ ] Anonymisering dobbeltsjekket (ingen reelle FPK i vedlegg)
- [ ] Rapporten gjennomleest for konsistens

**Hvis du kan huke av alle disse, er rapporten innleveringsklar.**

---

*Laget av faglig reviewer – 2026-04-29*
