# Proposal for integrert volumprognose og kapasitetsanalyse Revidert

**Gruppemedlemmer:**
Davor Necemer (individuell oppgave)

**Område:**
Produksjonsplanlegging og styring, kombinert med etterspørselsprognoser.
Prosjektet fokuserer på kvantitativ kapasitetsplanlegging i en konvergerende logistikkstruktur. Kunstig intelligens/maskinlæring benyttes som beslutningsstøtte til prognostisering og modellering.

**Bedrift (valgfritt):**
Anonymisert norsk produksjons- og distribusjonsmiljø innen næringsmiddelindustri.
Prosjektet baseres på aggregerte produksjons og volumdata tilgjengelig gjennom studentens yrkesrolle. Data behandles anonymisert og uten personopplysninger.

**Problemstilling:**
Bedriften har to parallelle varestrømmer (ferskvare og sekundær/handelsvare) som samles i et felles distribusjonsledd. Distribusjonsleddet har flere faste, daglige ferdigstillelsesfrister (sonevise cut-offs). Utfordringen er at det oppstår en sammensatt flaskehalsdynamikk som truer fristene, selv om den totale ukekapasiteten kan virke tilstrekkelig.

Målet med prosjektet er å beregne nøyaktig hvor mye ekstra kapasitet (for eksempel overtid, ekstra skift eller midlertidig bemanning) som må settes inn per uke i distribusjonsklargjøringen for å ferdigstille volumet innen cut-off. Kapasitetsmodellen avgrenses til to operative dispatcherledd: `P1 = PD / for-klargjøring` og `P2 = ED / endelig dispatch/ekspedering`. I topper kan kapasitetstiltak også innebære tidligere oppstart av for-klargjøring eller ekspedering for å rekke cut-off. Behovet for tidlig oppstart beregnes ut fra forventet volum, som predikeres ved hjelp av historiske data (f.eks. tilsvarende perioder året før) kombinert med informasjon om planlagte kampanjer. Modellen optimaliserer kapasitetstiltak i dispatcherleddet, mens varestrømmene ferskvare og sekundær/handelsvare behandles som voluminput til samme distribusjonsflaskehals.

Selv om modellen kjøres på ukesnivå, representeres de sonevise cut-offene ved at distribusjonsleddets kapasitet og fristkrav aggregeres til ukentlige krav/kapasitetsgrenser basert på sonestruktur. Først utarbeides en etterspørselsprognose per uke basert på historiske data (for å fange opp trend og sesong). Denne prognosen brukes deretter utelukkende som en forhåndsgitt input/parameter i kapasitetsmodellen. Selve beslutningen kapasitetsmodellen tar, er allokeringen av ekstra kapasitet og (der relevant) fremskynding av klargjøring i et begrenset tidsvindu før fristene.

**Data:**
Prosjektet vil bygge på følgende datagrunnlag:

Historiske, ukentlige volumdata over minimum to år for de to varestrømmene. Volumet standardiseres til en felles måleenhet (FPK-ekvivalenter) for å bygge prognosemodellen. I distribusjonsleddet tolkes FPK-ekvivalenten som en operasjonell håndteringsenhet: dersom en DPK, kurv eller tilsvarende salgsenhet plukkes og sorteres som én fysisk enhet, teller den som én enhet i modellen selv om den inneholder flere underliggende forbrukerenheter.

Historisk kampanjekalender (indikatorvariabler for planlagte tilbud/kampanjer) for å fange opp eksterne etterspørselsdrivere i prognosen.

Prognosen estimeres med etablerte tidsseriemetoder, og valg av modell begrunnes ved sammenligning av prognosefeil.

Aggregert, historisk informasjon om grunnkapasitet per uke i to hovedledd i distribusjonsklargjøringen: (1) `P1 = PD / for-klargjøring` og (2) `P2 = ED / endelig dispatch/ekspedering`. Eventuelle `DD`-handlinger behandles som en direkte eller særskilt dispatchflyt og vurderes i tidsgrunnlaget, men modelleres ikke som et eget hovedledd med mindre volumet viser seg å være vesentlig.

Denne prosessavgrensningen er viktig fordi de tilgjengelige tidsdataene kommer fra produksjonslister og dispatcher actions for lager 310. Datagrunnlaget måler dermed arbeid knyttet til klargjøring mot distribusjonsfrister, ikke primær eller sekundær produksjonspakking. Ved å la prosessdefinisjonene følge det observerbare tidsgrunnlaget reduseres risikoen for å estimere kapasitet for prosesser som ikke faktisk er målt i datasettet.

Data på faste distribusjonsfrister (sonevise cut-offs) som styrer når varene senest må være ferdigstilt.

**Målfunksjon:**
Målfunksjonen beskriver hvordan vi måler at systemet forbedres. I dette prosjektet er hovedmålet å minimere samlet bruk av ekstra kapasitet (og dermed indirekte ressursbruken) over planhorisonten. Samtidig må det prognostiserte volumet ferdigstilles innen de sonevise fristene. Siden det i ekstreme høysesonger kan være umulig å rekke alle frister uansett tiltak, inkluderes en teoretisk "straff" (penalty) i målfunksjonen for hvert fristbrudd. Et fristbrudd kvantifiseres her som antall enheter (FPK) som overstiger den aggregerte sonekapasiteten for den gitte uken. Modellen minimerer dermed summen av innsatt ekstra kapasitet og omfanget av fristbrudd. Penalty-vekten settes slik at fristbrudd normalt prioriteres høyere enn ekstra kapasitet, og testes gjennom scenarioanalyse. Slik finner modellen automatisk den beste avveiningen (trade-off) mellom kapasitetstiltak, tidlig oppstart og leveranseevne.

**Avgrensninger:**
Aggregeringsnivå: Modellen bygger utelukkende på ukentlig nivå, ikke ned på dags- eller skiftnivå.

Fysisk omfang: Modellen avgrenses til distribusjonsklargjøringen for lager 310, modellert som `P1 = PD / for-klargjøring` og `P2 = ED / endelig dispatch/ekspedering`, med to parallelle varestrømmer som voluminput.

Personvern: Ingen persondata/personopplysninger inngår.

Økonomi: Kostnadsoptimalisering i form av faktiske norske kroner inngår ikke eksplisitt; forbedring måles via kapasitetsenheter/timer og omfang av fristbrudd.

Implementering: Prosjektet er en teoretisk modellutvikling, og skal ikke implementeres operativt.

Scenarioanalyse: Variabler som usikkerhet i etterspørsel (f.eks. ±X % volumavvik) eller plutselig bortfall av kapasitet (sykdom/vedlikehold) er ikke beslutningsvariabler i modellen. Dette benyttes utelukkende i etterkant for å utføre sensitivitets- og scenarioanalyser for å teste hvor robust modellens løsning er.
