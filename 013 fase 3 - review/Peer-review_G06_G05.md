# Peer-review-rapport — LOG650 (Våren 2026)

## 1. Forsideopplysninger

| | |
|---|---|
| **Vurderende gruppe** | G06 — Davor Necemer (individuell) |
| **Vurdert gruppe** | G05 |
| **Tittel på vurdert rapport** | Prosjektoppgave LOG650 — AI-basert klassifiseringsmodell for kanalisering av brukte mobilenheter (Modino AS) |
| **Dato** | 08.05.2026 |
| **Status på vurdert rapport** | ~80 %-utkast (endelig versjon innleveres 31.05.2026) |
| **Emnekode** | LOG650 — Forskningsprosjekt: Logistikk og kunstig intelligens |

> **Merknad om arbeidsform.** Tilbakemeldingen er utarbeidet med AI som støtte i lese- og skrivefasen, jf. veiledningen for peer-review LOG650 (Våren 2026, pkt. 1). G06 står faglig ansvarlig for innholdet og prioriteringene. Vurderingen er framoverrettet: substansielle metode- og analysepunkter er løftet fram fordi de krever reelt arbeid før 31.05.2026, mens formelle ferdigstillelsespunkter er listet som forventet sluttføring uten dypere kritikk.

---

## 2. Helhetsinntrykk

Rapporten behandler et reelt og næringslivsrelevant beslutningsproblem hos Modino AS og posisjonerer det godt i sirkulærøkonomi-, reverse-logistics- og maskinlæringslitteraturen. Forskningsspørsmålet er klart formulert og operasjonalisert i to konkrete delproblemer, og den valgte metoden (Random Forest med stratifisert 80/20-splitt og 5-fold kryssvalidert hyperparametertuning) er faglig forsvarlig. For et 80 %-utkast er teori, metodebeskrivelse, modellkjøring og resultatpresentasjon kommet langt. Hovedutfordringene er knyttet til *realismen* i evalueringen: modellen bruker variabler som ikke er kjent ved beslutningstidspunktet (post-decision target leakage), target encoding er sannsynligvis ikke pipeline-trygg, klasse B og C har nær identiske marginer, og målvariabelen er avledet fra eksisterende inspeksjonsgrad. Dette gjør at rapporterte 92,4 % accuracy og ~390 000 NOK/år er øvre estimater. Punktene er løsbare innen tidsfristen og vil løfte rapporten betydelig.

---

## 3. Områdevis vurdering

### 3.1 Innledning

**Styrker.** Bakgrunn, kontekst og motivasjon (kap. 1) er stringent forankret i etablert litteratur (Stahel, 2016; Ferguson et al., 2009; Guide & Van Wassenhove, 2009; Ibrahim & Abdul-Kader, 2025). Forskningsspørsmål og delproblemer er presist formulert, og utvidelsen fra Norge til fem nordiske/baltiske land (kap. 1.2) er begrunnet eksplisitt med datavolum.

**Forbedringspunkter.**
- *Lineær 1 %/uke-påstand.* Setningen om at «10 ukers forsinkelse … kan tilsvare et verditap på 10 %» (gjentatt i kap. 8.3) impliserer lineær degradering. Verifiser at Guide & Van Wassenhove (2009) faktisk angir lineær rate, ellers reformuler («omtrent 10 % på 10 uker»).
- *Vitenskapelig bidrag.* Modino-betydningen er konkret, men *bidraget til litteraturen* (utover å løse Modinos problem) kunne formuleres tydeligere. Govindan et al. (2015) er nevnt som anerkjent forskningshull — men er over 10 år gammel. Kombiner gjerne med en nyere referanse (Ibrahim & Abdul-Kader, 2025) og presiser hva som *fortsatt* er underbelyst.

**Konkret forslag.** Legg inn én avsluttende setning i kap. 1 som plasserer studiens bidrag: f.eks. *«Studien demonstrerer at trebaserte ML-metoder kan operasjonaliseres på industrielle SAP-data for kanaliseringsbeslutninger i recommerce, et område Govindan et al. (2015) har pekt på som empirisk underdekket.»*

### 3.2 Litteraturgjennomgang og teoretisk forankring

**Styrker.** Teorikapittelet (kap. 2) er strukturert ryddig rundt tre faglige pilarer. Bruken av 9R-rammeverket (Potting et al., 2017) som kobling mellom sirkulærøkonomi og lønnsomhetsklasser (Figur 2.1) er en god konseptuell løsning. Identifikasjonen av Govindan et al. (2015) som hullsreferanse er treffende.

**Forbedringspunkter.**
- *Ferguson et al. (2009) – feil baseline.* Ferguson rapporterer 11 % kostnadsreduksjon ved å innføre *gradering der ingen fantes* (Pitney Bowes, printer-tilbehør). Modino *har allerede* manuell gradering. Den korrekte sammenligningen for prosjektet er *manuell gradering vs. ML-gradering*, ikke *gradering vs. ingen gradering*. 11 %-tallet bør refereres med dette forbeholdet (kap. 2.2.1, gjentatt i kap. 1 og 8.2).
- *Overførbarhet.* Flere sentrale kilder (Geyer et al., 2007; Hübner et al., 2020; Turkolmez et al., 2024) er på andre produktkategorier. Forbeholdet er nevnt løpende, men kunne samles i én setning i kap. 2.4.
- *Uverifiserte kilder.* Markører som «[Verifiser tilgang via Oria]» (Turkolmez 2024, Ibrahim & Abdul-Kader 2025, Turban 2011, Géron 2022, Zheng & Casari 2018, Rogers & Tibben-Lembke 1999) må avklares før innlevering.

**Konkret forslag.** I kap. 2.2.1, etter «reduserer totalkostnadene med omtrent 11 %», legg til: *«Tallet gjelder gevinsten av å innføre gradering der ingen finnes; for prosjektets ML-mot-manuell-sammenligning er dette en øvre referanse, ikke et direkte sammenlignbart resultat.»*

### 3.3 Metode

**Styrker.** Metodekapittelet (kap. 4) er grundig: forskningsdesignet er forankret i Rekdal & Pettersen (2025), datakilden er tydelig spesifisert, og analyseopplegget (Figur 4.2) er sporbart. Stratifisert splitting, 5-fold CV og GridSearchCV med definert hyperparametersøkerom er metodisk solid. Begrunnelsen for Random Forest framfor Gradient Boosting er eksplisitt.

**Forbedringspunkter.**
- *Feature-tilgjengelighet på beslutningstidspunkt (kritisk).* Variablene `revenue`, `margin` og `revenue_cost_ratio` er først kjent etter salg, og `dager_inspeksjon_til_faktura` først etter fakturering. Disse er klassiske post-decision-variabler og må fjernes fra produksjonsmodellen. `cost`-feltet er **uklart**: hvis det er innkjøpskost kjent ved mottak, er det legitim input; hvis det er total kost etter behandling, er det leakage. G05 må definere hva feltet faktisk inneholder (kap. 4.2.2 / 4.3.2).
- *Target encoding kan i seg selv lekke (kritisk).* `Transaction Type_enc`, `brand_enc` og `Inspection Color_enc` er konstruert ved hjelp av målvariabelen. Dersom encodingen er fit-et på hele datasettet før train/test-splitt, eller utenfor en pipeline i CV, har testsettet indirekte lekket inn i trening. Dette kan alene gi kunstig høy accuracy *selv etter* at åpenbare post-decision-variabler er fjernet. Encoding må legges i en `sklearn`-pipeline som fit-es per CV-fold; rapporter også en kontrollkjøring med enklere one-hot- eller frekvenskoding.
- *Tidsbasert validering mangler.* Recommerce-data er tidsavhengige (markedspriser, produktgenerasjoner, kampanjer endrer seg). Random 80/20-splitt skjuler temporal degradering. Suppler med en train-2024 / test-2025-kjøring (eller tilsvarende periodesplitt) som realisme-test.
- *Land/marked som feature mangler.* Datasettet er utvidet til Estland, Finland, Sverige og Romania for volumets skyld, men `country` er ikke med som forklaringsvariabel. Markedene har ulike prisnivåer, kanalstrukturer og produktmiks. Inkluder land som feature, eller rapporter accuracy per marked, eller begrunn eksplisitt hvorfor markedseffekter er irrelevante.
- *Etiske hensyn / personvern.* Kap. 4 mangler eksplisitt drøfting av personvern og datasikkerhet. SAP-data inneholder ikke direkte personopplysninger, men leverandør-, butikk- og inspeksjons-ID kan være indirekte identifikatorer. NSD-vurdering nevnes på forsiden men er tom. Et avsnitt på 5–10 linjer er nødvendig for å oppfylle rubrikkriteriet «Validitet, reliabilitet og etiske hensyn er forklart».
- *Plansetning i ferdig tekst.* Avsnittet i kap. 4.2.2 om at «Tabellen er foreløpig og oppdateres etter gjennomgang av Modinos SAP-uttrekk» hører ikke hjemme i en ferdig versjon. Erstatt med endelig variabeltabell (Tabell 6.2) eller en henvisning til den.
- *Definisjon av målvariabel.* Kap. 4.2.2 definerer klasse A som «enhet reparert og solgt i nettbutikk med positivt dekningsbidrag», mens kap. 6.1 mapper klassene direkte fra inspeksjonsgrad (A,B → A; C → B; D,E,F → C). Disse to definisjonene er ikke ekvivalente — se også 3.4 nedenfor.

**Konkret forslag.** Legg inn en *feature availability table* i kap. 4.3 eller 6.1 som klassifiserer hver feature som «kjent ved inspeksjon / under prosess / etter prosess». Eksempel:

| Feature | Tilgjengelig ved inspeksjon? | Kommentar |
|---|---|---|
| `Inspected Device Value` | Ja (forutsatt satt før kanalvalg) | Bekreft mot Modino |
| `Device Category`, `brand_enc`, `Inspection Color_enc` | Ja, ved korrekt encoding-pipeline | Risikoen ligger i encoding-prosedyren, ikke rå variabel |
| `Transaction Type_enc` | Uklart / trolig nei | Kan være kanal-/salgskode → direkte lekkasje |
| `cost`, `kostnadsforhold` | Uklart | Avhenger av kost-definisjon |
| `revenue`, `margin`, `revenue_cost_ratio` | Nei | Først kjent etter salg |
| `dager_inspeksjon_til_faktura` | Nei | Først kjent etter fakturering |

### 3.4 Analyse og resultater

**Styrker.** Resultatkapittelet (kap. 7) er kvantitativt fyldig og leservennlig. Confusion matrix er korrekt rapportert (8 186 + 7 855 + 2 779 = 18 820 = 20 % av 94 096). Modellsammenligningen i Tabell 7.1 viser et tydelig hierarki, og rapporteringen av per-klasse precision/recall er metodisk korrekt. Tabell 7.6 (margindifferanse per klassifiseringsutfall) er en transparent måte å presentere lønnsomhetsestimatet på. Det er positivt at kap. 7.7.1 selv kommenterer at klasse B og C har nær identiske marginer.

**Forbedringspunkter — dette er rapportens største svakhet og fortjener mest oppmerksomhet.**

- *Sirkulær målvariabel (kritisk).* Klassene A/B/C er definert som en mapping av inspeksjonsgrad (kap. 6.1). Inspeksjonsgrad er Modinos *eksisterende* klassifisering. Modellen lærer derfor i praksis å gjenskape inspeksjonsgraden, ikke å predikere lønnsomhet. Dette er nevnt i kap. 8.4, men bør flagges allerede i kap. 6.1, og helst valideres ved en parallellmodell trent mot *faktisk realisert dekningsbidrag* som målvariabel.
- *Post-decision target leakage (kritisk).* `revenue` (0,098), `cost` (0,104), `margin` (0,071) og `revenue_cost_ratio` (0,074) står sammen for ~34,7 % av modellens prediktive kraft (Tabell 7.3). Target leakage-risikoen nevnes i kap. 8.4, men presenteres ikke kontrollert. **Uten en kontrafaktisk modellkjøring uten leakage-features kan reell modellnytte ikke kvantifiseres.** Kjør samme pipeline med kun pre-decision-variabler (med korrekt target encoding, jf. 3.3) og rapporter accuracy + per-klasse-metrikker som Tabell 7.7. Dette er det enkeltforbedringspunktet som vil løfte rapporten mest.
- *Lønnsomhetsestimatet er optimistisk øvre grense (kritisk).* +156 072 NOK på testsettet og ~390 000 NOK/år forutsetter at (i) modellens avvikende prediksjoner er korrekte, (ii) en historisk klasse B-enhet faktisk *kan* repareres til klasse A-margin, (iii) marginene 484/197/195 NOK fra Tabell 7.4 gjelder også de avvikende enhetene, og (iv) klasse B og C er meningsfullt forskjellige. Antakelse (iv) motbevises av tallene selv (197 vs. 195 NOK). Beregn et nedre estimat (f.eks. der avvikende prediksjoner antas 50/50 korrekte) og presenter resultatet som et intervall.
- *Asymmetriske feilkostnader.* Accuracy er ikke optimal styringsmetrikk når en A→C-feil er økonomisk dyrere enn en B→C-feil. Lag en kostnadsmatrise basert på Tabell 7.6, og rapporter forventet økonomisk verdi som hovedmetrikk i tillegg til accuracy.
- *B = C i marginer — implikasjon ikke trukket.* Rapporten nevner forskjellen i kap. 7.7.1, men bærer ikke implikasjonen videre til diskusjon, konklusjon eller modelloppsett. Vurder eksplisitt om det reelle beslutningsproblemet er binært (A vs. ikke-A), og om B/C-skillet primært er operasjonelt heller enn økonomisk.
- *Talluinkonsistens i datasettstørrelse.* Kap. 6.1 og 6.3 oppgir n = 94 096 (træning + test = 75 276 + 18 820); kap. 7.7.1 (Tabell 7.4) oppgir n = 92 119; kap. 1.2 oppgir 92 119 transaksjoner for de fem inkluderte landene. Differansen på 1 977 observasjoner må forklares. En kort *datavandring* (rader inn → ut for hvert filter-, koblings- og rensesteg) i kap. 6.1 vil løse flere uklarheter samtidig.
- *Inkonsistens i graderingssystem.* Kap. 3.2 sier «Modino bruker en gradering fra A til C ved mottak»; kap. 6.1 mapper fra 6 grader (A–F) til 3 lønnsomhetsklasser. Avklar hvilket av disse som er korrekt — det påvirker forståelsen av hvilken inspeksjonsinformasjon som er tilgjengelig på beslutningstidspunktet.
- *Feature importance bør tolkes forsiktig.* Impurity-basert feature importance favoriserer kontinuerlige og høyt kardinale variabler, og target-enkodede variabler kan få kunstig forklaringskraft. Validér med permutation importance eller SHAP, eller marker eksplisitt at importance leses *indikativt, ikke kausalt*.

### 3.5 Diskusjon

**Styrker.** Kap. 8 kobler hovedfunnene tilbake til problemstillingen og litteraturen, og kap. 8.4 viser metodisk modenhet ved at fire reelle svakheter erkjennes. Drøftingen av brand-effekten (lavt importance-tall, forklart med at økonomiske variabler indirekte fanger opp merkeeffekt) er innsiktsfull.

**Forbedringspunkter.**
- *Asymmetri funn vs. forbehold.* Kap. 8.1 og 8.3 rapporterer 92,4 % accuracy som suksesskriterium, mens kap. 8.4 leser dette som påvirket av leakage og sirkulær mapping. Refaktorer slik at forbeholdene formuleres allerede i 8.1 og 8.3: f.eks. *«92,4 % er det optimistiske taket gitt nåværende dataoppsett. Sensitivitetsanalysen uten post-decision-variabler (Tabell 7.7) viser at reell ytelse forventes lavere.»*
- *Implementerbarhet i Modino.* Diskusjonen mangler et avsnitt om hva modellen *faktisk* kan brukes til ved inspeksjon, gitt at sentrale features ikke er tilgjengelige. Dette må sies eksplisitt i kap. 8.3.
- *Sammenligning med Ibrahim & Abdul-Kader (2025).* Kap. 8.2 sier resultatene er «konsistente med» studien, men oppgir ikke deres rapporterte accuracy til sammenligning. Hvis tallene er svært ulike, blir påstanden misvisende.
- *Land/marked som feilkilde.* Diskuter eksplisitt om modellen lærer et samlet nordisk/baltisk mønster eller om den faktisk er gyldig for Modinos norske virksomhet (jf. 3.3).

### 3.6 Konklusjon

**Styrker.** Konklusjonen (kap. 9) er konsis, besvarer begge delproblemer eksplisitt, og listen over videre forskning korresponderer godt med rapportens egne metodiske svakheter — en ærlig og handlingsrettet liste.

**Forbedringspunkter.**
- *Bekreftelsesbias.* Setningen «Samlet svarer prosjektet bekreftende på forskningsspørsmålet» (linje 1021) er sterkere enn evidensen tillater når 8.4 tas inn over seg. Forslag til reformulering: *«Resultatene indikerer at en AI-basert klassifiseringsmodell potensielt kan forbedre Modinos kanaliseringsbeslutninger, men robustheten er betinget av at modellen valideres uten target leakage og at klassemappingen testes mot faktiske kanalvalg.»*
- *Bidrag til teori.* Konklusjonen sier mye om praksis og lite om teoretisk bidrag. Legg til 2–3 setninger om f.eks. metodisk demonstrasjon av at SAP-data alene kan brukes til klassifisering i recommerce, eller bekreftelse av at trebaserte metoder fungerer på mobiltelefon-domenet (utover Ibrahim & Abdul-Kader, 2025).
- *Skrivefeil.* «svarer … bekreften på» (linje 1021) skal være «bekreftende på».

### 3.7 Skriveflyt, formelle aspekter og helhetsvurdering

**Styrker.** Språket er gjennomgående klart og fagligpresist. Kapitlene har tydelig progresjon, figurnummerering med «Egenprodusert»-merking er forbilledlig, og APA 7-formatet er i hovedsak korrekt med DOI-lenker.

**Reelle forbedringspunkter.**
- *TOC vs. tekst.* Innholdsfortegnelsen og kapittelnummereringen i kap. 1 må samkjøres (kontroller at 1.2/1.3 stemmer i begge).
- *APA 7-finpuss.* Volumnummer skal være i kursiv; en gjennomgang før innlevering vil fange opp tilsvarende detaljer.
- *Forkortelser.* Innfør en kort forkortelsesliste (BER, DSS, SMOTE, CV, GridSearchCV, K-fold) foran kap. 1 for å hjelpe rask lesing.
- *Konsolidering av referanser.* Kap. 4 har en lokal referanseliste (s. ~662–694) i tillegg til hovedbibliografien. APA 7 bruker normalt én samlet liste til slutt — flytt og fjern dubletter.

**Forventet ferdigstillelsesarbeid (uten dypere kritikk).** Forsidemal, sammendrag (~200 ord, norsk), abstract (~200 ord, engelsk), vedlegg (kap. 12), erstatning av ASCII-figurer med PNG/SVG (`confusion_matrix_final.png` og `feature_importance.png` finnes allerede som filer), verifisering/fjerning av «[Verifiser tilgang via Oria]»-markører, og korrekturlesing.

---

## 4. Prioritert tiltaksplan (08.05 – 31.05.2026)

### Kategori A — Substansielt (høyest verdi, gjør først)

| # | Tiltak | Hvor | Estimert tid |
|---|---|---|---|
| A1 | Lag *feature availability table* (3.3); definér eksplisitt hva `cost` inneholder; fjern bekreftede post-decision-variabler (`revenue`, `margin`, `revenue_cost_ratio`, `dager_inspeksjon_til_faktura`). | Kap. 4.3 / 6.1 | 0,5 dag |
| A2 | Legg target encoding inn i `sklearn`-pipeline som fit-es per CV-fold; rapporter kontrollkjøring med enklere encoding. | Kap. 4.3.2 / 6.3 | 1 dag |
| A3 | Kjør Random Forest med kun pre-decision-features og korrekt encoding. Rapporter som Tabell 7.7 (reell modellytelse). | Kap. 7 + 8.1 / 9 | 1 dag |
| A4 | Tidsbasert robustness-test: train 2024 / test 2025 (eller tilsvarende). | Kap. 7 | 0,5–1 dag |
| A5 | Inkluder `country` som feature *eller* rapporter accuracy per marked *eller* begrunn fravær eksplisitt. | Kap. 4.3 / 7 / 8 | 0,5 dag |
| A6 | Beregn nedre lønnsomhetsestimat (intervall i stedet for punktestimat); kommenter B/C-margin-konsekvensen for valg av 2- vs. 3-klasse-modell. | Kap. 7.7 / 8 | 0,5 dag |
| A7 | Lag kostnadsmatrise for asymmetriske feilkostnader; rapporter forventet økonomisk verdi som hovedmetrikk. | Kap. 7.7 / 8.3 | 0,5 dag |
| A8 | Drøft sirkulær målvariabel eksplisitt (kap. 6.1 + utvid 8.4); helst valider mot faktisk realisert dekningsbidrag. | Kap. 6.1 / 8.4 | 1 dag (uten revalidering) / 3–4 dager (med) |

### Kategori B+C — Strukturelt og sluttføring

| # | Tiltak | Hvor |
|---|---|---|
| B1 | *Datavandring*-tabell som forklarer 94 096 vs. 92 119 obs. og alle filtre-/rensetrinn. | Kap. 6.1 |
| B2 | Avklar A–C vs. A–F-gradering. | Kap. 3.2 + 6.1 |
| B3 | Erstatt plansetning «Tabellen er foreløpig …» med endelig variabeltabell. | Kap. 4.2.2 |
| B4 | Nytt delkapittel «Etiske og forskningsetiske hensyn» (5–10 linjer; SAP-data, indirekte identifikatorer, NSD-status). | Kap. 4 |
| B5 | Reformuler Ferguson (2009) sin 11 %-påstand som «gradering vs. ingen gradering». | Kap. 1, 2.2.1, 8.2 |
| B6 | Balanser konklusjonen — mindre kategorisk formulering. | Kap. 9 |
| B7 | Samkjør TOC og kapittelnummerering (1.2/1.3). | TOC |
| C1 | Forsidemal, sammendrag (~200 ord), abstract (~200 ord). | Forside / forord |
| C2 | Konsolider referanser til én samlet bibliografi (fjern lokal liste i kap. 4). | Kap. 11 |
| C3 | Verifiser/fjern «[Verifiser tilgang via Oria]»-markører. | Bibliografi |
| C4 | Erstatt ASCII-figurer med PNG/SVG. | Kap. 2, 4, 7 |
| C5 | Forkortelsesliste (BER, DSS, SMOTE, CV, GridSearchCV) foran kap. 1. | Forord |
| C6 | APA 7-finpuss og korrekturlesing. | Hele dokumentet |

**Anbefalt rekkefølge:** A1 → A2 → A3 (A4–A7 kan kjøres parallelt) → A8 → B1–B7 → C1–C6. Kategori A er det som flytter rapporten faglig; B er rydding; C er pakking til innlevering.

---

*Tilbakemeldingen er ment som konstruktiv input til G05 i forbindelse med ferdigstillelse innen 31.05.2026, og er ikke grunnlag for karaktersetting. Vurderingen er basert på Avdeling for logistikks kriterier slik de er gjengitt i veiledningen for peer-review LOG650 (Våren 2026).*
