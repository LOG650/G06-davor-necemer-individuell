# Literature Integration Map
**Tightened Source Package for Report**

Last updated: 2026-04-29

---

## Section 2.0 – Litteratur (Literature Review)

### 2.1 Etterspørselsprognose med tidsseriemodeller

**Current claim:** "SARIMAX-modeller håndterer både trends, sesongmønstre og eksogene effekter typiske for næringsmiddelproduksjon."

**Sources to cite:**

| Source | Quote/Support | Integration Point |
|--------|---------------|-------------------|
| **Hyndman & Athanasopoulos (2021)** | FPP3 Ch. 9: ARIMA theory; Ch. 9.9: seasonal ARIMA; Ch. 10: dynamic regression with exogenous variables | "SARIMAX kombinerer SARIMA-komponenten (sesongmønster) med eksogen-variabel-delen (kampanjer). Se Hyndman & Athanasopoulos (2021), Ch. 10, for dynamic regression framework." |
| **Arunraj, Ahrens & Fernandes (2016)** | Direct proof: SARIMAX for perishable food retail with promotions/holidays as exogenous drivers | "Arunraj et al. (2016) demonstrerer SARIMAX-effektivitet for sesongbundet matetherspørsel under påvirkning av promotions og helligdager, en kontekst parallell til distribusjonsvolumen påvirket av kampanjer." |
| **Fildes, Ma & Kolassa (2022)** | Retail forecasting review: aggregation levels, promotion effects, variability | "Fildes et al. (2022) understreker utfordringene ved retail demand forecasting på ulike aggregeringsnivåer, relevant for overgangen fra dag/sone til ukesnivå i denne analysen." |

**Suggested revised text for 2.1:**

> Etterspørselsprognoser er kritisk for produksjonsplanlegging, spesielt når kapasiteten er begrenset. **SARIMAX-modeller** (Seasonal ARIMA with eXogenous variables) er etablert praksis for volumdata med sesongmønster. 
>
> SARIMAX kombinerer to sentrale egenskaper: (1) **SARIMA**-komponenten fanger sesongmønster repetitive over året (påske, jul, sommerferie), kritisk for næringsmiddeletterspørsel (Hyndman & Athanasopoulos, 2021, Ch. 9.9); (2) **eXogenous variables**-delen (Hyndman & Athanasopoulos, 2021, Ch. 10) inkorporerer kampanjekalender og andre eksterne faktorer. 
>
> Arunraj, Ahrens & Fernandes (2016) demonstrerer nettopp dette for perishable food retail, hvor promotions og holidays som eksogene variabler signifikant forbedrer prognoser utover baseline sesongmodeller. I distribusjonslogistikk påvirker planlagte kampanjer etterspørselen på samme måte som i retail.

---

### 2.2 Kapasitetsplanlegging gjennom linear programming

**Current claim:** "Linear Programming er en veletablert metodikk for allokering av begrenset kapasitet... Aggregate Production Planning (APP) løser nettopp dette."

**Sources to cite:**

| Source | Quote/Support | Integration Point |
|--------|---------------|-------------------|
| **Winston (2004)** | LP formulation, Simplex method, production planning chapters | "Klassisk lærebok for LP-formuleringsprinsippet: minimering av objektfunksjon under lineære constraints." |
| **Holt, Modigliani & Simon (1955)** | Foundational APP decision rule | "Historisk: Holt et al. (1955) introduserte den lineære beslutningsregelen for produksjon og bemanning – fundamentet for moderne APP." |
| **Leung, Wu & Lai (2006)** | Multi-site APP with capacity constraints and demand uncertainty | "Leung, Wu & Lai (2006) formulerer APP under arbeidskraft- og kapasitets-begrensninger med usikker etterspørsel, relevant for din tosses-AP-formulering." |

**Suggested revised text for 2.2:**

> **Linear Programming (LP)** er en veletablert metodikk for allokering av begrenset kapasitet når målet er å minimere kostnad eller ressursforbruk under strenge restruksjoner (Winston, 2004). **Aggregate Production Planning (APP)** løser nettopp dette problem: på ukentlig eller månedlig nivå bestemmer modellen hvor mye ekstra kapasitet (overtid, ekstrabemanning, tidlig oppstart) som kreves for å møte prognostisert etterspørsel innenfor faste distribusjons-cut-offs.
>
> Holt, Modigliani & Simon (1955) etablerte den lineære beslutningsregelen som fundamentet for APP. I moderne praksis (Leung, Wu & Lai, 2006) håndteres APP under både kapasitets- og etterspørselsbegrensninger. I dette prosjektet modelleres kapasitetsallokeringen som et LP-minimiseringsproblem med samme prinsipper.

---

### 2.3 Flaskehals-dynamikk i konvergerende logistikk

**Current text:** Generic discussion of network convergence.

**Suggested addition (cites Fildes et al.):**

> Fildes et al. (2022) påpeker at retail forecasting kompleksitet øker når man aggregerer fra dag til uke, spesielt hvis høye volumer er konsentrert på dager med sonevise cut-offs. Samme fenomen oppstår i distribusjonsleddet når flere varestrømmer konvergerer til felles fristsystem.

---

## Section 3.0 – Teori (Theory)

### 3.1 Tidsserieanalyse og prognoser

**Current:** Generic description of time series components and SARIMAX structure.

**Strengthen by citing:**

| Source | Integration |
|--------|-------------|
| **Hyndman & Athanasopoulos (2021)** | Reference Ch. 9 for ARIMA concept, 9.9 for $\nabla^d \nabla_s^D$ differencing, Ch. 10 for exogenous structure. |
| **Hyndman & Khandakar (2008)** | Reference for auto_arima algorithm: "ADF-test for trend-stationaritet, sesongdifferensiering, og ACF/PACF-analyse som basis for auto_arima kandidat-generering (Hyndman & Khandakar, 2008)." |

**Suggested revision to 3.1:**

> En **tidsserie** er en sekvens av observasjoner ordnet kronologisk. Tidsserier har tre karakteristiske komponenter: **trend, sesongmønster, residualer** (Hyndman & Athanasopoulos, 2021, Ch. 9).
>
> **SARIMAX-modeller** modellerer disse komponentene samt eksterne påvirkninger. En SARIMAX-modell estimeres ved å minimere forskjellen mellom observerte verdier og modellens prediksjoner.
>
> Modellen består av fire deler: (1) **ARIMA-kjernen** (Hyndman & Athanasopoulos, 2021, Ch. 9); (2) **Sesongkomponenten** håndtert via $\nabla_s^D$-operator (Ch. 9.9); (3) **Integreringsleddet** for trend og sesongavdrift (Ch. 9); (4) **Eksogene variabler** som kampanjekalender (Ch. 10).
>
> Valg av parametre $(p, d, q, P, D, Q)$ styres av ADF-testing, ACF/PACF-analyse, og auto_arima stepwise-algoritmen (Hyndman & Khandakar, 2008).

---

### 3.2 Linear Programming og optimering

**Current:** Generic LP formulation.

**Strengthen by citing:**

| Source | Integration |
|--------|-------------|
| **Winston (2004)** | General LP form and Simplex method. |
| **Leung, Wu & Lai (2006)** | Multi-site APP constraint structure. |

**Suggested addition:**

> LP-modellen følger standard form (Winston, 2004): Minimiser $c^T x$ under $Ax \leq b, x \geq 0$. I **Aggregate Production Planning** kontekst (Leung, Wu & Lai, 2006) bestemmer modellen optimal kapasitetsallokering (beslutningsvariabler: overtid, bemanning, tidlig oppstart) gitt prognostisert etterspørsel, grunnkapasitet, og sonevise distribusjons-cut-off constraints.

---

## Section 5.0 – Metode og data

### 5.1 Metode – Etterspørselsprognose (SARIMAX)

**Current:** Detailed SARIMAX specification and validation strategy.

**Strengthen validation section (5.1) by citing:**

| Source | Integration |
|--------|-------------|
| **Hyndman & Athanasopoulos (2021)** | Ch. 9: stationarity testing; Ch. 9.9: model selection via AIC/BIC; Ljung-Box residual test. |
| **Hyndman & Khandakar (2008)** | auto_arima algorithm for stepwise candidate generation. |
| **Arunraj, Ahrens & Fernandes (2016)** | Baseline comparison strategy (SNaive vs. SARIMAX). |

**Suggested revision to 5.1 (parameterestimering section):**

> Gitt at treningsdata omfatter bare 104 observasjoner (2 sesongperioder), brukes en konservativ strategi basert på Hyndman & Athanasopoulos (2021, Ch. 9):
>
> 1. **BASELINE-MODELL:** Seasonal Naive (SNaive)
>    - Prognose: $\hat{y}_{t} = y_{t-52}$ (observasjon fra 52 uker siden)
>    - Rolle: Enkel sammenligningsstandard. Hvis SARIMAX ikke slår SNaive på validering, brukes SNaive (inspirert av Arunraj et al., 2016, som viser at SARIMAX må markant overgå naive baseline for perishable food).
>
> 2. **SARIMAX-KANDIDATER via auto_arima** (Hyndman & Khandakar, 2008):
>    - ADF-test (Augmented Dickey-Fuller) for trend-stationaritet
>    - Sesongdifferensiering for sesong-stationaritet
>    - ACF/PACF-analyse foreslår $(p, q, P, Q)$-kandidater
>    - auto_arima genererer kandidatmodeller med fokus på parsimoni
>
> 3. **MODELL-SELEKTION:**
>    - Kandidater som krever $P > 1$ eller $D > 1$ forkastes (Hyndman & Athanasopoulos, 2021, viser at høye sesong-ordener risikerer overfitting på kort datasett)
>    - Valg baseres på AIC/BIC + Ljung-Box test for residual autokorrelasjon

---

### 5.4 Datakvalitet og kontroll

**Current:** Lists data limitations including campaign_flag dominance.

**Strengthen by citing:**

| Source | Integration |
|--------|-------------|
| **Fildes et al. (2022)** | High-cardinality exogenous variables and variable reduction. |
| **Arunraj et al. (2016)** | Campaign intensity vs. binary flags. |

**Suggested addition to 5.4:**

> **Kampanje-intensitet for F:** `campaign_flag=1` for 117 av 118 observasjoner i varestrøm F, noe som gir flagget minimal forklaringskraft. Fildes et al. (2022) diskuterer problemet med høy kardinalitet i eksogene variabler i retail demand forecasting; Arunraj et al. (2016) viser at `campaign_intensity` (antall kampanjer per uke) eller `campaign_type` (kategorisk: chain-promo, launch, seasonal) har større differensiering. Modellvalg må vurdere alternativ representasjon hvis binær flagg ikke er tilstrekkelig.

---

## Section 6.0 – Modellering

### 6.1 Modellstruktur

**Current:** Two-stage structure (SARIMAX → LP).

**No changes needed, but can strengthen by citing:**

> Denne sekvensielle tilnærmingen er inspirert av Leung, Wu & Lai (2006), som også separerer demand forecasting fra capacity optimization under constraints.

---

### 6.3 Målfunksjon

**Current:** Objective function minimizing overtime and slack.

**Strengthen by citing:**

| Source | Integration |
|--------|-------------|
| **Winston (2004)** | LP objective function structure. |
| **Leung, Wu & Lai (2006)** | Multi-site APP cost weighting. |
| **NNN (Tariff)** | Cost weights $c_j$ from labor agreement. |

**Suggested addition:**

> Målfunksjonens kostnads-vektvektor $c_j$ reflekterer norske tariffavtaler. NNN (2024–2026) definerer relative kostnader for grunnlønn, overtid, og tilkallingshjelp, som oversettes til dimensjonsløse relative vekter for denne modellen (eksakt kostnadsfølsomhet ligger utenfor scopet).

---

### 6.4 Hovedkonstrants

**Current:** Capacity constraint formulation.

**Strengthen by citing:**

| Source | Integration |
|--------|-------------|
| **Winston (2004)** | LP constraint structure. |
| **Leung, Wu & Lai (2006)** | Multi-site APP constraints under capacity and workforce limits. |
| **SSB (sykefravær)** | Capacity adjustment parameter. |

**Suggested addition to constraints section:**

> Grunnkapasitet $CAP_{j,\text{base}}$ justeres for norsk sykefraværsrate (~6 % årlig) basert på SSB offisielle statistikk (SSB, 2024), slik at modellen reflekterer realistisk tilgjengelig arbeidskraft.

---

## Section 7.0 – Analyse

### 7.1 Data-deskriptiv analyse

**Current:** Seasonal pattern observations.

**Strengthen by citing:**

| Source | Integration |
|--------|-------------|
| **Arunraj et al. (2016)** | Seasonal pattern description for food. |
| **Fildes et al. (2022)** | Retail demand volatility and aggregation challenges. |

**Suggested addition:**

> Sesongmønsteret i begge varestrømmer er konsistent med observasjoner fra Arunraj et al. (2016) for perishable food retail: påske-topp (uke 13–14) og jul-topp (uke 50–52). Fildes et al. (2022) påpeker at slik volatilitet på kort tidshorisonter kompliserer planlegging når aggregeringsnivå (dag til uke) maskerer kritiske topperusher.

---

### 7.2 Valgt prognosestrategi

**Current:** SNaive baseline and SARIMAX candidates.

**Strengthen by citing:**

| Source | Integration |
|--------|-------------|
| **Hyndman & Athanasopoulos (2021)** | Baseline benchmarking as best practice. |
| **Hyndman & Khandakar (2008)** | auto_arima candidate generation. |
| **Arunraj et al. (2016)** | SNaive as defensive baseline for food forecasting. |

**Suggested revision:**

> Seasonal Naive (SNaive)-prognose ($\hat{y}_t = y_{t-52}$) etableres som referanse. Hyndman & Athanasopoulos (2021, Ch. 9) anbefaler at enhver SARIMAX-modell må markant slå naive baselines for å rettferdiggjøre ekstra kompleksitet. Arunraj et al. (2016) viser at selv for SARIMAX med kampanjevariabler kan SNaive være konkurransedyktig på kort datasett. Auto_arima (Hyndman & Khandakar, 2008) genererer kandidatmodeller med fokus på parsimoniske ordener.

---

### 7.3 Kapasitetsmodell-setup

**Current:** Process time matrix and baseline capacity setup.

**Strengthen by citing:**

| Source | Integration |
|--------|-------------|
| **Leung, Wu & Lai (2006)** | Multi-site APP model structure. |
| **Winston (2004)** | LP setup conventions. |

**Suggested addition:**

> Kapasitets-setup følger standard APP-praksis (Winston, 2004; Leung, Wu & Lai, 2006): grunnkapasitet per prosess og uke, arbeidsbelastning beregnet fra volum × standardtid, og constraints som sikrer at arbeidsbelastning ikke oversiger tilgjengelig kapasitet + overtid.

---

## Section 9.0 – Diskusjon

### 9.1 Metodisk vurdering

**Current:** Discussion of SARIMAX vs. SNaive, campaign flag cardinality, LP limitations.

**Strengthen by citing:**

| Source | Integration |
|--------|-------------|
| **Hyndman & Athanasopoulos (2021)** | Data sufficiency for SARIMAX (3–4 seasons ideal). |
| **Arunraj et al. (2016)** | Campaign variable handling in food forecasting. |
| **Fildes et al. (2022)** | Aggregation trade-offs in retail planning. |
| **Leung, Wu & Lai (2006)** | APP under uncertainty and capacity constraints. |

**Suggested revision to 9.1:**

> **Valg av SARIMAX for etterspørselsprognose:**
> 
> SARIMAX er relevant for etterspørselsdynamikk i næringsmiddelbransjen grunnet klare sesongmønstre (Arunraj et al., 2016). Foreliggende datasett (104 treningsobservasjoner, 2 sesonger) er på grensen til SARIMAX-robusthet. Hyndman & Athanasopoulos (2021, Ch. 9.9) anbefaler 3–4 sesonger for stabil sesong-komponentestimering.
>
> **Mitigation:** SNaive-baseline sikrer at modellen ikke overparameteriseres. Hyndman & Athanasopoulos (2021) påpeker at naive baselines ofte er konkurransedyktige på kort data. Hvis SARIMAX ikke markant slår SNaive på validering, brukes SNaive operativt.
>
> **Campaign-flagg problematikk:** Fildes et al. (2022) diskuterer håndtering av høy-kardinalitet eksogene variabler. For varestrøm F er kampanje-indikatoren aktivt i 99 % av ukene. Arunraj et al. (2016) viser at kampanje-intensitet eller kampanje-type kan være mere differensierende.
>
> **Valg av Linear Programming for kapasitetsoptimering:**
>
> LP er standard for APP (Winston, 2004; Leung, Wu & Lai, 2006). Sonevise frister krever eksplisitt modellering, noe LP håndterer via constraints.
>
> **Limitation:** Sonevise constraints er ukentlig aggregerte, ikke daglig granulare. Fildes et al. (2022) påpeker at slik aggregering kan maskere kritiske daglige flaskehalser. En fullt disaggregert daglig modell ville være mer presist men ligger utenfor scopet for denne rapport-versjonen.

---

## Section 10.0 – Konklusjon

No citation changes needed; conclusions naturally flow from integrated sections 2–9.

---

## Quick Reference: Source → Sections Mapping

| Source | Primary Sections | Secondary Sections |
|--------|------------------|--------------------|
| **Hyndman & Athanasopoulos (2021)** | 2.1, 3.1, 5.1, 7.2, 9.1 | 2.0 intro |
| **Hyndman & Khandakar (2008)** | 5.1 (auto_arima), 7.2 | 3.1 |
| **Arunraj, Ahrens & Fernandes (2016)** | 2.1, 5.4, 7.1, 9.1 | 2.0 intro, 3.1 |
| **Fildes, Ma & Kolassa (2022)** | 2.1, 2.3, 5.4, 7.1, 9.1 | |
| **Fildes, Goodwin & Önkal (2019)** | 2.1 (optional) | 5.4 (if discussing adjustment) |
| **Winston (2004)** | 2.2, 3.2, 6.0–6.4, 7.3, 9.1 | 3.0 intro |
| **Holt, Modigliani & Simon (1955)** | 2.2 (historical only) | |
| **Leung, Wu & Lai (2006)** | 2.2, 3.2, 6.1, 6.4, 7.3, 9.1 | |
| **SSB (2024)** | 5.4, 6.4 | 5.5 |
| **NNN (2024–2026)** | 6.3, 6.6 | 5.4 |

---

## Implementation Notes

1. **Each claim now has a source:** Walk through sections 2, 3, 5, 6, and crosscheck against this map.
2. **Avoid orphan claims:** If you write something not in this map, either cite it here or remove it.
3. **Consistent voice:** Use "cites X show that..." or "Per X (author, year)..." for smooth flow.
4. **Footnotes optional:** Inline citations in (Author, Year, Section) format work well.
5. **Verify before submission:** Do a final read of each section to ensure every methodological claim is grounded in a source.

