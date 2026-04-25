# Second Review - 2026-04-25

## Scope

Ny review etter oppdateringer i repoet, uten gjennomgang av `000 templates/`.

Vurderte hovedkilder:
- `005 report/Sluttrapport_Volumprognose-Kapasitetsanalyse_DavorNecemer.md`
- `011 fase 1 - proposal/Proposal for integrert volumprognose og kapasitetsanalyse Revidert.md`
- `012 fase 2 - plan/project-plan.md`
- `012 fase 2 - plan/status.md`
- `012 fase 2 - plan/oppgave og status.md`
- `012 fase 2 - plan/LOG650_Prosjektstyringsplan_Davor_Necemer_1.2.md`
- referansenotater i `003 references/`

## Overall Assessment

Aggregeringsargumentet er betydelig forbedret. Proposal, prosjektplan og rapport er naa i hovedsak konsistente i valget om ukentlig modellnivaa med sonebasert aggregering. Det som gjenstaar er ikke primart en konflikt i omfang, men en svak operasjonalisering av modellen og en fortsatt uferdig sluttrapport.

## Findings

### 1. LP-modellen har en alvorlig enhetsfeil mellom volum og kapasitet

I kapasitetsrestriksjonen sammenlignes `V_eff,j,t` i FPK-ekvivalenter direkte med `CAP_base` og `OT` i mann-timer. Uten en eksplisitt konvertering mellom volum og tidsforbruk per prosess er modellen matematisk inkonsistent og kan ikke gi meningsfulle kapasitetsbeslutninger.

Referanser:
- `005 report/Sluttrapport_Volumprognose-Kapasitetsanalyse_DavorNecemer.md:355`
- `005 report/Sluttrapport_Volumprognose-Kapasitetsanalyse_DavorNecemer.md:388`
- `005 report/Sluttrapport_Volumprognose-Kapasitetsanalyse_DavorNecemer.md:392`

Konsekvens:
- optimaliseringen kan se korrekt ut paa papir, men representerer ikke faktisk produksjonskapasitet
- modellen mangler den kritiske koblingen mellom forecast og workload

### 2. Sonevise cut-offs er beskrevet, men ikke formelt modellert

Rapporten forklarer na at sonefrister aggregeres til ukentlige begrensninger, men i selve modellen blir dette ikke operasjonalisert fullt ut. Parametrene `p1`, `p2`, `p3` er ikke definert som data, og den forenklede restriksjonen kollapser tilbake til en samlet ukekapasitet med ett slack-ledd. Dermed er det fortsatt uklart hvordan soneprofilen faktisk paavirker loesningen.

Referanser:
- `005 report/Sluttrapport_Volumprognose-Kapasitetsanalyse_DavorNecemer.md:128`
- `005 report/Sluttrapport_Volumprognose-Kapasitetsanalyse_DavorNecemer.md:404`
- `005 report/Sluttrapport_Volumprognose-Kapasitetsanalyse_DavorNecemer.md:416`
- `011 fase 1 - proposal/Proposal for integrert volumprognose og kapasitetsanalyse Revidert.md:19`

Konsekvens:
- leseren forstaar prinsippet, men kan ikke etterprove hvordan sonestrukturen styrer kapasitetsbehovet
- modellens viktigste case-spesifikke bidrag blir forelopig for svakt dokumentert

### 3. Tidlig oppstart er lovet som beslutningsgrep, men er ikke en beslutningsvariabel i modellen

Problemstilling, proposal og metode sier at tidlig oppstart er ett av tiltakene modellen skal vurdere. I modellkapittelet er dette imidlertid redusert til en flagg-regel som utloeses hvis `OT_2,t` passerer en terskel. Det betyr at tidlig oppstart ikke optimaliseres i LP-en, men bare anbefales i etterkant.

Referanser:
- `005 report/Sluttrapport_Volumprognose-Kapasitetsanalyse_DavorNecemer.md:112`
- `005 report/Sluttrapport_Volumprognose-Kapasitetsanalyse_DavorNecemer.md:192`
- `005 report/Sluttrapport_Volumprognose-Kapasitetsanalyse_DavorNecemer.md:424`
- `011 fase 1 - proposal/Proposal for integrert volumprognose og kapasitetsanalyse Revidert.md:17`

Konsekvens:
- modellen leverer ikke fullt ut paa eget beslutningsmandat
- ett av de mest operative tiltakene i caset er fortsatt uten formell optimeringslogikk

### 4. Forecasting-delen er fortsatt for svak paa sesongspesifikasjon og modellsporbarhet

Rapporten argumenterer for sesongpregede ukesdata og viser til SARIMA/SARIMAX-lignende logikk, men den formelle modellspesifikasjonen i metodekapittelet viser kun en ikke-sesongmessig ARIMAX-form. For et ukentlig naeringsmiddelcase med hoysesonger boer sesongleddet enten modelleres eksplisitt eller utelates med en tydelig faglig begrunnelse.

Referanser:
- `005 report/Sluttrapport_Volumprognose-Kapasitetsanalyse_DavorNecemer.md:152`
- `005 report/Sluttrapport_Volumprognose-Kapasitetsanalyse_DavorNecemer.md:176`
- `005 report/Sluttrapport_Volumprognose-Kapasitetsanalyse_DavorNecemer.md:275`
- `005 report/Sluttrapport_Volumprognose-Kapasitetsanalyse_DavorNecemer.md:284`

Konsekvens:
- prognosedelen virker faglig plausibel, men ikke ferdig spesifisert nok til aa bli reproduserbar
- det blir vanskelig aa forsvare modellvalget dersom sesongmønster er en sentral del av caset

### 5. Sluttrapporten er fortsatt uferdig i sentrale kapitler

Data-, analyse-, resultat-, diskusjons- og konklusjonskapitlene inneholder fortsatt maltekst eller plassholdere. Dette er naa den stoerste leveranserisikoen i repoet.

Referanser:
- `005 report/Sluttrapport_Volumprognose-Kapasitetsanalyse_DavorNecemer.md:68`
- `005 report/Sluttrapport_Volumprognose-Kapasitetsanalyse_DavorNecemer.md:332`
- `005 report/Sluttrapport_Volumprognose-Kapasitetsanalyse_DavorNecemer.md:452`
- `005 report/Sluttrapport_Volumprognose-Kapasitetsanalyse_DavorNecemer.md:464`
- `005 report/Sluttrapport_Volumprognose-Kapasitetsanalyse_DavorNecemer.md:506`
- `005 report/Sluttrapport_Volumprognose-Kapasitetsanalyse_DavorNecemer.md:524`

Konsekvens:
- dokumentet er enda ikke naer innleveringsklar status
- gode forbedringer i metode og modell mister verdi hvis sluttkapitlene ikke fylles med faktisk analyse

### 6. Prosjektstatusdokumentene er ikke oppdatert og undergraver styringsbildet

Statusfilene beskriver fortsatt rapporten som ikke startet, referansemapper som tomme og prosjektet som mer blokkerte enn repoet faktisk viser. Som prosjektlederdokumentasjon er dette problematisk fordi styringsgrunnlaget blir misvisende.

Referanser:
- `012 fase 2 - plan/status.md:16`
- `012 fase 2 - plan/oppgave og status.md:78`
- `012 fase 2 - plan/oppgave og status.md:82`
- `012 fase 2 - plan/oppgave og status.md:83`

Konsekvens:
- fremdriftskommunikasjonen mister troverdighet
- det blir vanskeligere aa prioritere riktige neste steg og dokumentere faktisk progresjon

## Recommended Next Steps

1. Legg inn prosess-spesifikke konverteringsparametre fra FPK til tidsforbruk, for eksempel standard minutter per FPK per varestroem og prosess.
2. Formaliser soneaggregeringen som eksplisitte parametre og restriksjoner, ikke bare beskrivende tekst.
3. Avklar om tidlig oppstart skal vaere en ekte beslutningsvariabel eller et etterbehandlet anbefalingssignal.
4. Spiss forecasting-modellen: enten bruk en eksplisitt sesongmodell eller forklar hvorfor en enklere ARIMAX er tilstrekkelig.
5. Rydd ut all gjenværende maltekst i kapittel 5.2 og 7-12 saa snart metodisk retning er fast.
6. Oppdater `status.md` og `oppgave og status.md` slik at prosjektstyringen samsvarer med faktisk repo-innhold.

## Data Note

Data er bevisst ikke reviewet i detalj naa. Neste naturlige steg er derfor aa definere minimumssettet av data som kreves for aa kunne estimere forecast-modellen og binde den korrekt sammen med kapasitetsmodellen.

## Follow-up Note - Detailed Data Specification

Det er naa utarbeidet en konkret dataspesifikasjon for prosjektet i:
- `004 data/Datakrav_for_prosjektet.md`

Det viktigste avklaringspunktet fra denne spesifikasjonen er at modellen maa ha en eksplisitt kobling mellom:
- volum i `FPK-ekvivalenter`
- arbeidsforbruk i `minutter per FPK`
- tilgjengelig kapasitet i `timer per prosess per uke`

Foelgende datablokker er definert som prioritet 1:
- `weekly_volume.csv` for ukentlig volumhistorikk og kampanjeeffekt
- `process_time_matrix.csv` for omregning fra volum til arbeidsbelastning
- `capacity_weekly.csv` for grunnkapasitet og maksimal ekstra kapasitet

Foelgende datablokker er definert som prioritet 2:
- `zone_cutoff_profile.csv` for aa underbygge soneaggregeringen med faktiske andeler
- `action_parameters.csv` for tiltakslogikk og relative kostnadsvekter

Foelgende datablokk er anbefalt for validering:
- `operational_events_weekly.csv` for historisk overtid, brudd og driftsavvik

Det er ogsaa opprettet tomme CSV-maler i `004 data/` for alle disse datasettene, slik at videre datainnhenting kan gjores maalrettet og med minst mulig irrelevant informasjon.
