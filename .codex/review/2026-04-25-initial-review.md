# Initial Review - 2026-04-25

## Scope

Review av dagens endringer i:
- `005 report/Sluttrapport_Volumprognose-Kapasitetsanalyse_DavorNecemer.md`
- `003 references/01 forecasting/KML_Kompendium_Demand_Forecasting.md`
- `003 references/02 capacity_planning/KML_Kompendium_Production_Planning.md`

## Findings

### 1. Kritisk metodisk konflikt mellom problem og modellnivå

Rapporten beskriver problemet som daglige og sonevise cut-off-brudd, men avgrenser samtidig modellen til rent ukentlig aggregert nivaa. Det betyr at modellen slik den er beskrevet ikke kan dokumentere at daglige cut-offs faktisk overholdes, som er selve kjernen i caset.

Referanser:
- `005 report/Sluttrapport_Volumprognose-Kapasitetsanalyse_DavorNecemer.md:97`
- `005 report/Sluttrapport_Volumprognose-Kapasitetsanalyse_DavorNecemer.md:107`
- `005 report/Sluttrapport_Volumprognose-Kapasitetsanalyse_DavorNecemer.md:128`
- `005 report/Sluttrapport_Volumprognose-Kapasitetsanalyse_DavorNecemer.md:237`
- `005 report/Sluttrapport_Volumprognose-Kapasitetsanalyse_DavorNecemer.md:254`

Konsekvens:
- svak intern validitet
- risiko for at anbefalt kapasitetsplan ser optimal ut paa uke, men feiler operativt per dag eller sone

### 2. Kjerneseksjoner i oppgaven er fortsatt maltekst og ikke faglig innhold

Metode, data, modellering, analyse, resultat, diskusjon og konklusjon inneholder fortsatt instruksjoner fra malen og plassholdertekst. Rapporten framstaar derfor som vesentlig uferdig selv om tittel, problem og case er delvis skrevet.

Referanser:
- `005 report/Sluttrapport_Volumprognose-Kapasitetsanalyse_DavorNecemer.md:68`
- `005 report/Sluttrapport_Volumprognose-Kapasitetsanalyse_DavorNecemer.md:72`
- `005 report/Sluttrapport_Volumprognose-Kapasitetsanalyse_DavorNecemer.md:267`
- `005 report/Sluttrapport_Volumprognose-Kapasitetsanalyse_DavorNecemer.md:306`
- `005 report/Sluttrapport_Volumprognose-Kapasitetsanalyse_DavorNecemer.md:310`
- `005 report/Sluttrapport_Volumprognose-Kapasitetsanalyse_DavorNecemer.md:322`
- `005 report/Sluttrapport_Volumprognose-Kapasitetsanalyse_DavorNecemer.md:364`
- `005 report/Sluttrapport_Volumprognose-Kapasitetsanalyse_DavorNecemer.md:382`

Konsekvens:
- oppgaven kan ikke vurderes som ferdig faglig leveranse
- det finnes ingen dokumentert metodekjede fra data til prognose til kapasitetsbeslutning

### 3. Integrasjonen mellom forecast og LP er paastatt, men ikke operasjonalisert

Teksten sier at prognosefeil handteres i LP-modellen og at modellen minimerer ressursbruk under fristkrav, men det finnes ingen case-spesifikk maalfunksjon, ingen beslutningsvariabler, ingen constraints og ingen beskrivelse av hvordan forecast-usikkerhet faktisk oversettes til planparametere eller sikkerhetsmarginer.

Referanser:
- `005 report/Sluttrapport_Volumprognose-Kapasitetsanalyse_DavorNecemer.md:144`
- `005 report/Sluttrapport_Volumprognose-Kapasitetsanalyse_DavorNecemer.md:192`
- `005 report/Sluttrapport_Volumprognose-Kapasitetsanalyse_DavorNecemer.md:206`
- `005 report/Sluttrapport_Volumprognose-Kapasitetsanalyse_DavorNecemer.md:209`
- `005 report/Sluttrapport_Volumprognose-Kapasitetsanalyse_DavorNecemer.md:306`

Konsekvens:
- modellbidraget er forelopig konseptuelt, ikke etterprovbart
- det er umulig aa vurdere om LP-loesningen faktisk representerer produksjonsrealitetene

### 4. Kildegrunnlaget er for tynt og for lite sporbart til aa bære argumentasjonen

Bibliografien inneholder bare ett generelt kompendium og en eksplisitt plassholder om at flere referanser skal legges til. De to referansefilene under `003 references` oppsummerer bare samme kilde og tilfører ingen bredde i teori eller metodegrunnlag.

Referanser:
- `005 report/Sluttrapport_Volumprognose-Kapasitetsanalyse_DavorNecemer.md:378`
- `005 report/Sluttrapport_Volumprognose-Kapasitetsanalyse_DavorNecemer.md:382`
- `003 references/01 forecasting/KML_Kompendium_Demand_Forecasting.md:15`
- `003 references/01 forecasting/KML_Kompendium_Demand_Forecasting.md:19`
- `003 references/02 capacity_planning/KML_Kompendium_Production_Planning.md:15`
- `003 references/02 capacity_planning/KML_Kompendium_Production_Planning.md:19`

Konsekvens:
- svakt akademisk fundament
- hoy risiko for at sentrale paastander om forecasting og kapasitetsplanlegging ikke er godt nok underbygget

## Recommended Next Steps

1. Bestem riktig beslutningsnivaa: enten modellere dag/sone eksplisitt, eller skrive om problemstillingen slik at den faktisk gjelder ukentlig aggregate planning.
2. Erstatt all gjenværende maltekst i kapittel 5-10 med faktisk metode, modell, analyse, resultat og konklusjon.
3. Formaliser modellen med variabler, maalfunksjon, sentrale constraints, inputdata og antatt prognosehorisont.
4. Utvid litteraturgrunnlaget med fagkilder om tidsserieprognoser, forecast accuracy, aggregate production planning, kapasitetsbegrensninger og usikkerhet.
5. Rydd front matter før innleveringsmodus: sammendrag, abstract, veileder, studiepoeng, datoer og formelle avkryssinger.
