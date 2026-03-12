# Proposal LOG650

**Gruppemedlemmer:**
Davor Necemer (individuell oppgave)

**Område:**
Produksjonsplanlegging og styring, kombinert med etterspørselsprognoser. Prosjektet fokuserer på kvantitativ kapasitetsplanlegging i en konvergerende logistikkstruktur. Kunstig intelligens/maskinlæring benyttes som beslutningsstøtte til prognostisering og modellering.

**Bedrift (valgbart):**
Anonymisert norsk produksjons- og distribusjonsmiljø innen næringsmiddelindustri. Prosjektet baseres på aggregerte produksjons og volumdata tilgjengelig gjennom studentens yrkesrolle. Data behandles anonymisert og uten personopplysninger.

**Problemstilling:**
Bedriften har to parallelle varestrømmer (ferskvare og sekundær/handelsvare) som samles i et felles distribusjonsledd. Distribusjonsleddet har flere faste, daglige ferdigstillelsesfrister (sonevise cut-offs). Utfordringen er at det oppstår en sammensatt flaskehalsdynamikk som truer fristene, selv om den totale ukekapasiteten kan virke tilstrekkelig.

Målet med prosjektet er å beregne nøyaktig hvor mye ekstra kapasitet som må settes inn per uke i tre ulike prosessledd for å ferdigstille volumet. I topper kan kapasitetstiltak også innebære å planlegge tidligere oppstart av dagsproduksjonen for å rekke cut-off. Behovet for tidlig oppstart beregnes ut fra forventet volum, som predikeres ved hjelp av historiske data kombinert med informasjon om planlagte kampanjer. Modellen optimaliserer primært tiltak og tidlig oppstart for sekundær/handelsvare, mens ferskvare behandles som en operasjonell begrensning med kort tidsvindu.

**Data:**
Prosjektet vil bygge på følgende datagrunnlag:
- Historiske, ukentlige volumdata over minimum to år for de to varestrømmene. Volumet standardiseres til en felles måleenhet (FPK-ekvivalenter).
- Historisk kampanjekalender (indikatorvariabler for planlagte tilbud/kampanjer) for å fange opp eksterne etterspørselsdrivere.
- Aggregert, historisk informasjon om grunnkapasitet per uke i tre hovedledd: (1) primær pakkeprosess, (2) sekundær pakkeprosess og (3) distribusjonsklargjøring.
- Data på faste distribusjonsfrister (sonevise cut-offs) som styrer når varene senest må være ferdigstilt.

**Beslutningsvariabler:**
- Allokering av ekstra kapasitet (f.eks. overtid, ekstra skift eller midlertidig bemanning) per uke i de tre prosessleddene.
- Fremskynding av klargjøring (planlegging av tidligere oppstart av dagsproduksjon) for å imøtekomme spesifikke fristkrav.

**Målfunksjon:**
Målfunksjonen minimerer samlet bruk av ekstra kapasitet (ressursbruk) over planhorisonten, samtidig som det prognostiserte volumet ferdigstilles innen de sonevise fristene. For å håndtere ekstreme topper der frister ikke kan nås uansett tiltak, inkluderes en teoretisk straff (penalty) for fristbrudd (antall enheter som overstiger kapasiteten). Modellen finner den beste avveiningen mellom kapasitetstiltak, tidlig oppstart og leveranseevne ved å minimere summen av innsatt kapasitet og vektet straff for fristbrudd.

**Avgrensninger:**
- **Aggregeringsnivå:** Modellen bygger utelukkende på ukentlig nivå, ikke ned på dags- eller skiftnivå.
- **Fysisk omfang:** Modellen avgrenses til de tre nevnte hovedleddene og to parallelle varestrømmer.
- **Personvern:** Ingen persondata eller personopplysninger inngår i prosjektet.
- **Økonomi:** Kostnadsoptimalisering i form av faktiske kroner inngår ikke eksplisitt; forbedring måles via kapasitetsenheter/timer og omfang av fristbrudd.
- **Implementering:** Prosjektet er en teoretisk modellutvikling og skal ikke implementeres operativt i denne fasen.
- **Scenarioanalyse:** Usikkerhet i etterspørsel eller plutselig bortfall av kapasitet behandles gjennom sensitivitets- og scenarioanalyser i etterkant, og er ikke direkte beslutningsvariabler.
