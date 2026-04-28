# Datakrav for prosjektet

## Formaal

Dette dokumentet definerer hvilket datagrunnlag som faktisk trengs for prosjektet
`Integrert volumprognose og kapasitetsanalyse`.

Maalet er aa hente inn minst mulig data, men nok til aa:
- estimere en ukentlig forecast per varestroem
- oversette forecast til faktisk arbeidsbelastning i prosessene
- beregne behov for ekstra kapasitet under aggregerte sonevise cut-offs

## Viktigste prinsipp

Det mest kritiske datakravet er ikke flere volumkolonner. Det viktigste er aa ha
en tydelig kobling mellom:
- volum i `FPK-ekvivalenter`
- arbeidsforbruk i `minutter` eller `timer`
- tilgjengelig kapasitet per prosess og uke

Uten denne koblingen blir LP-modellen ikke operativt gyldig.

### Operasjonell definisjon av FPK-ekvivalent

I denne modellen betyr `FPK-ekvivalent` en operasjonell haandteringsenhet i
distribusjonsleddet, ikke noedvendigvis antall underliggende forbrukerenheter.
Hvis en DPK, kurv eller tilsvarende salgsenhet tas ut, plukkes eller sorteres som
en fysisk enhet, teller den som `1` i `volume_fpk_eq`.

Eksempel:
- `1` DPK franske landbroed kan inneholde `4` broed, men hvis DPK-en haandteres
  som en kurv i distribusjonen, teller den som `1` haandteringsenhet i modellen.

Begrunnelsen er at kapasitetsbelastningen i distribusjonsklargjoering bestemmes
av antall fysiske haandteringer, ikke bare av antall produkter inne i hver DPK.

## Minimumssett du maa ha

Foelgende fem datablokker er minimum for aa kunne gjennomfoere prosjektet paa en
faglig troverdig maate.

### 1. Ukentlig volumhistorikk for forecast

Anbefalt fil: `weekly_volume.csv`

| Felt | Paa-krevd | Beskrivelse | Kommentar |
|---|---|---|---|
| `year_week` | Ja | Ukenummer paa format `YYYY-WW` | Maa vaere sammenhengende uten manglende uker |
| `week_start_date` | Ja | Startdato for uke | Brukes for sporbarhet og kalendereffekter |
| `stream_id` | Ja | `F` for ferskvare, `S` for sekundaervare | Minst disse to varestroemmene |
| `volume_fpk_eq` | Ja | Ukentlig volum i standardisert FPK-ekvivalent | Forecastens hovedvariabel |
| `campaign_flag` | Ja | `0/1` for kampanje i aktuell uke | Viktig eksogen variabel |
| `campaign_type` | Nei | Type kampanje | Nyttig hvis ulike kampanjer gir ulik effekt |
| `holiday_flag` | Anbefalt | `0/1` for paasken, jul, helligdager osv. | Viktig ved ukesdata |
| `anomaly_flag` | Anbefalt | `0/1` for avvikende uke | For eksempel streik, systemfeil eller spesialordre |
| `constrained_week_flag` | Anbefalt | `0/1` hvis volumet var begrenset av manglende kapasitet/lager | Viktig for aa skille faktisk etterspoersel fra avkortet leveranse |
| `notes` | Nei | Fritekst | Kun ved behov |

Minimum historikk:
- minimum `104` sammenhengende uker
- helst `156` uker hvis tilgjengelig

Kritisk merknad:
- Hvis `volume_fpk_eq` egentlig er utsendt volum og ikke faktisk etterspoersel, maa
  uker med stockout, produksjonsstopp eller kapasitetsbrudd merkes. Ellers vil
  forecasten kunne undervurdere reelle topper.
- Hvis datakilden teller underliggende forbrukerenheter i stedet for operative
  haandteringsenheter, maa volumet omregnes eller dokumenteres i `notes`.

### 2. Omregning fra volum til tidsforbruk

Anbefalt fil: `process_time_matrix.csv`

| Felt | Paa-krevd | Beskrivelse | Kommentar |
|---|---|---|---|
| `stream_id` | Ja | `F`, `S` eller `ALL` | Kobler varestroem til prosessbehov. Bruk `ALL` hvis samme dispatcher-standardtid gjelder begge stroemmer |
| `process_id` | Ja | `P1`, `P2` | `P1=PD/for-klargjoering`, `P2=ED/endelig dispatch/ekspedering` |
| `minutes_per_fpk` | Ja | Standard tidsbruk per FPK i aktuell prosess | Den viktigste parameteren i hele modellen |
| `source_basis` | Ja | Hvordan tallet er fastsatt | Tidsstudie, standardtid, erfaringsverdi, ERP-avledning |
| `valid_from` | Nei | Gyldig fra dato | Hvis standarden har endret seg over tid |
| `valid_to` | Nei | Gyldig til dato | Hvis standarden har endret seg over tid |
| `comment` | Nei | Fritekst | Forklarer antagelser eller forenklinger |

Denne tabellen er noekkelen til aa loese svakheten i dagens modell.
Prosessene avgrenses til distribusjonsklargjoering fordi tidsgrunnlaget kommer
fra produksjonslister og dispatcher actions, ikke fra primaer eller sekundaer
produksjonspakking. Her maa du kunne si noe slikt:
- `1 haandteringsenhet krever x minutter i P1/PD/for-klargjoering`
- `1 haandteringsenhet krever y minutter i P2/ED/endelig dispatch`

`DD` behandles foreloepig som direkte eller saerskilt dispatchflyt. Den kan
inngaa i tidsgrunnlaget hvis volumet er relevant, men modelleres ikke som et
eget hovedledd foer flere uker viser at den er operativt vesentlig.

Hvis prosessforbruket varierer mye mellom undergrupper, kan du dele videre paa
`product_family`. Hvis variasjonen er liten, behold dagens grovere inndeling.

### 3. Ukentlig tilgjengelig kapasitet per prosess

Anbefalt fil: `capacity_weekly.csv`

| Felt | Paa-krevd | Beskrivelse | Kommentar |
|---|---|---|---|
| `year_week` | Ja | Ukenummer | Maa kunne fange ferieuker og helligdager |
| `process_id` | Ja | `P1`, `P2` | Samme ID-er som i modellen |
| `base_hours` | Ja | Normal tilgjengelig kapasitet i timer | Grunnkapasitet i aktuell uke |
| `overtime_max_hours` | Ja | Maks mulig overtid i timer | Modellgrense |
| `extra_shift_max_hours` | Anbefalt | Maks ekstra skift/bemanning | Hvis dette er et faktisk tiltak |
| `early_start_max_hours` | Anbefalt | Maks timer som kan vinnes via tidlig oppstart | Sentralt hvis dette skal bli beslutningsvariabel |
| `capacity_reduction_flag` | Nei | `0/1` for kjent bortfall | For ferie, vedlikehold, stengt linje |
| `comment` | Nei | Fritekst | Forklarer spesialuker |

Hvis kapasiteten er nesten konstant, kan du starte med en enklere baseline-tabell.
Hvis kapasiteten varierer med kalender, maa du ha ukespesifikke verdier.

### 4. Aggregerte sone- og fristparametre

Anbefalt fil: `zone_cutoff_profile.csv`

| Felt | Paa-krevd | Beskrivelse | Kommentar |
|---|---|---|---|
| `stream_id` | Anbefalt | `F`, `S` eller `ALL` | Bruk `ALL` hvis samme profil gjelder begge stroemmer |
| `zone_bucket` | Ja | For eksempel `Z1`, `Z2`, `Z3` | Aggregerte fristboetter |
| `cutoff_label` | Ja | For eksempel `00:00`, `01:00`, `02:00` | Operativ frist |
| `share_of_weekly_volume` | Ja | Andel av ukens volum som maa vaere ferdig innen denne fristen | Maa summere til `1.0` per profil |
| `basis_period` | Ja | Hvordan andelen er beregnet | Historiske data, forretningsregel, gjennomsnitt av representative uker |
| `season_segment` | Nei | For eksempel `normal`, `high_season` | Brukes hvis sonemiksen endres i sesong |
| `comment` | Nei | Fritekst | Forklarer usikkerhet eller forenklinger |

Dette er dataene som skal underbygge `p1`, `p2`, `p3` i modellen.
Hvis disse andelene ikke finnes i historiske data, kan de fastsettes som en
driftsregel bekreftet av virksomheten, men det maa dokumenteres eksplisitt.

### 5. Tiltaks- og kostnadsparametre for ekstra kapasitet

Anbefalt fil: `action_parameters.csv`

| Felt | Paa-krevd | Beskrivelse | Kommentar |
|---|---|---|---|
| `process_id` | Ja | `P1`, `P2` | Hvor tiltaket kan brukes |
| `action_type` | Ja | `overtime`, `extra_shift`, `early_start` | Modellens beslutningsgrep |
| `max_hours_per_week` | Ja | Maks bruk per uke | Viktig constraint |
| `relative_cost_weight` | Ja | Relativ kost/vekt i maalfunksjonen | Kan brukes i stedet for NOK |
| `activation_rule` | Nei | Eventuell regel for tiltaket | F.eks. kun ved sekundaervare |
| `comment` | Nei | Fritekst | Dokumenterer logikken |

Hvis du ikke har faktiske kostnader i kroner:
- bruk relative vekter, for eksempel `1.0` for overtid, `1.3` for ekstra skift,
  `0.8` eller `1.1` for tidlig oppstart, avhengig av lokal vurdering

## Data som er sterkt anbefalt, men ikke absolutt noedvendig

Foelgende data vil styrke prosjektet betydelig:

### 6. Historikk for faktiske kapasitetsproblemer

Anbefalt fil: `operational_events_weekly.csv`

| Felt | Paa-krevd | Beskrivelse | Kommentar |
|---|---|---|---|
| `year_week` | Anbefalt | Uke | Kobles til forecast og kapasitet |
| `process_id` | Anbefalt | Prosess | Hvor problemet oppstod |
| `actual_overtime_hours` | Anbefalt | Faktisk overtid | Gir bedre kalibrering |
| `breach_flag` | Anbefalt | `0/1` for fristbrudd | Nyttig for validering |
| `breach_volume_fpk` | Nei | Omfang av brudd | Kan brukes til slack-penalty |
| `downtime_hours` | Nei | Bortfall i timer | Nyttig i scenarioanalyse |
| `note` | Nei | Fritekst | Forklarer spesialhendelser |

Denne tabellen er veldig nyttig hvis du vil vise at modellen faktisk fanger uker
der driften historisk ble presset.

## Data som kan droppes naa

Foelgende data er normalt ikke noedvendig i denne fasen:
- personnavn, skiftlister per ansatt og andre personopplysninger
- kunde-ID paa detaljnivaa
- ordrelinjer per kunde hvis ukentlig aggregering er tilstrekkelig
- full kostnadsbokfoering i NOK
- maskin-sensorlogger og sekunduploesning per linje
- geografiske koordinater og rutedata, med mindre de direkte paavirker cut-off-profilen

## Praktisk anbefalt datainnsamling

Hvis du vil hente inn data i riktig rekkefolge, bruk denne prioriteringen.

### Prioritet 1 - maa paa plass foerst

1. `weekly_volume.csv`
2. `process_time_matrix.csv`
3. `capacity_weekly.csv`

Uten disse tre kan vi ikke bygge en troverdig forecast-til-kapasitet-kobling.

### Prioritet 2 - maa paa plass for aa forsvare aggregeringen

4. `zone_cutoff_profile.csv`
5. `action_parameters.csv`

Disse trengs for aa vise hvordan ukemodellen faktisk representerer sonevise frister
og hvilke tiltak modellen faar lov til aa velge.

### Prioritet 3 - til validering og styrking

6. `operational_events_weekly.csv`

## Minste brukbare versjon

Hvis du maa starte veldig smalt, er dette den minste brukbare datapakken:

### Forecast
- `year_week`
- `stream_id`
- `volume_fpk_eq`
- `campaign_flag`

### Kapasitet
- `process_id`
- `year_week`
- `base_hours`
- `overtime_max_hours`

### Kobling mellom forecast og kapasitet
- `stream_id`
- `process_id`
- `minutes_per_fpk`

### Soneaggregering
- `zone_bucket`
- `cutoff_label`
- `share_of_weekly_volume`

## Kvalitetskrav foer data brukes

Foer datasettene brukes i modellen, boer disse kontrollene vaere oppfylt:
- ingen manglende uker i volumhistorikken
- samme definisjon av `FPK-ekvivalent` gjennom hele perioden
- samme definisjon av prosessene `P1` og `P2`
- kapasitet og volum er dokumentert i kompatible enheter
- kampanjer og spesialuker er merket konsekvent
- soneandelene summerer til `1.0`
- avvik og databrudd er dokumentert

## Neste naturlige modellkobling

Naar disse dataene er samlet inn, er neste steg aa bygge en eksplisitt
matematisk oversettelse:

`forecast volum -> workload i minutter -> kapasitet per prosess -> behov for tiltak`

Det er dette som vil gjoere modellen din faglig sterkere og mer operativt troverdig.
