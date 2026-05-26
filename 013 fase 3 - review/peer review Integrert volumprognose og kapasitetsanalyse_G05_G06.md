# Peer review-rapport – LOG650

| | |
|---|---|
| **Gruppe som vurderer:** | G05 – BirgitteVera |
| **Gruppe som blir vurdert:** | G06 |
| **Rapport som vurderes:** | Integrert volumprognose og kapasitetsanalyse |
| **Dato:** | 07.05.2026 |

---

## 1. Helhetsinntrykk

Rapporten er ambisiøs, relevant og godt strukturert. Den tar for seg en praktisk logistikkutfordring i næringsmiddelbransjen der to varestrømmer møtes i et felles distribusjonsledd og kan skape kapasitetsproblemer selv om ukekapasiteten totalt sett virker tilstrekkelig. Det er positivt at rapporten kobler etterspørselsprognoser og kapasitetsoptimering i ett samlet rammeverk, og at den har en tydelig rød tråd fra problemstilling til metode, modellering og diskusjon.

Rapporten er foremost sterkest som modellrammeverk. LP-modellen er kjørt på indekserte og anonymiserte data, noe som betyr at resultatene viser at systemet fungerer teknisk, men ikke fullt ut hva det faktiske kapasitetsbehovet vil være i praksis. Dette gjør at flere av de sentrale spørsmålene i problemstillingen foreslås løst metodisk, men ikke er besvart med faktiske tall. Potensialet i rammeverket er likevel tydelig, og med reelle FPK-volumer på plass vil rapporten stå vesentlig sterkere.

---

## 2. Områdevis vurdering

### 2.1 Innledning

Innledningen fungerer godt. Bakgrunn og kontekst er tydelig forklart, og det kommer klart frem at utfordringen ikke bare handler om samlet ukekapasitet, men om hvordan volumtopper og sonevise cut-off-frister kan skape flaskehalser. Problemstillingen er tydelig formulert, og delproblemene skiller ryddig mellom prognosedelen og kapasitetsdelen.

To forbedringspunkter: (1) Avsnitt 1.1 bør tydeliggjøre at rapporten leverer et teknisk rammeverk og en smoke-test, ikke en ferdig operativ analyse. Dette vil sette forventningene riktig fra starten og unngå at leseren tolker resultatene for sterkt. (2) Rapporten påpeker i avsnitt 9.4 at kombinasjonen av SARIMAX og LP i ett distribusjonsrammeverk sjelden behandles samlet i litteraturen — dette er et genuint faglig bidrag som fortjener å fremheves allerede i innledningen.

### 2.2 Litteraturgjennomgang og teoretisk forankring

Litteraturgjennomgangen dekker relevante temaer og begrunner godt valget av både prognosemodell og optimeringsmodell. Det er positivt at rapporten bruker Seasonal Naive som sammenligningsgrunnlag — det viser god metodisk forståelse, fordi en mer avansert modell ikke automatisk gir bedre resultater.

To forbedringspunkter: (1) Teorien bør knyttes tydeligere til caset. Litteraturdelen forklarer metodene, men kobler dem sjelden konkret til de spesifikke valgene som gjøres i denne modellen. Det ville gjort overgangen fra teori til metode sterkere. (2) Rapporten mangler en eksplisitt diskusjon av teoretiske hull, noe vurderingskriteriene etterspør. Poenget fra avsnitt 9.4 — at integrert prognose-optimering sjelden behandles samlet — burde kommet frem allerede i kapittel 2 som faglig grunngivelse for hele studien.

### 2.3 Metode

Metodekapitlet er grundig og viser tydelig sammenheng mellom problemstilling, datagrunnlag og modellvalg. Det er positivt at rapporten er åpen om begrensningene i datagrunnlaget, særlig at publiserbare data er indeksert og at LP-kjøringen derfor ikke kan tolkes som et operativt estimat på reelle mann-timer.

Tre forbedringspunkter: (1) Avsnitt 1.3 har en intern spenning: rapporten begrunner aggregeringen til ukentlig nivå med at sonevise frister kan modelleres som ukentlige andeler — men selve problemstillingen er at ukesaggregater skjuler de kritiske dagsvise belastningstoppene. Forfatteren bør være eksplisitt på at dette er en praktisk forenkling med en kjent kostnad, ikke fremstille det som metodisk uproblematisk. (2) Prosess-tidsmatrisen (avsnitt 8.2) bygger på 8 observasjoner og tar ikke høyde for at håndteringstid per enhet trolig varierer med sesong. I næringsmiddellogistikk er det rimelig å anta at arbeidstempo er annerledes i juleuker enn i normale uker — nettopp når kapasitetsmodellen er mest kritisk. Dette bør diskuteres som begrensning og ideelt inngå i sensitivitetsanalysen. (3) Validitet og reliabilitet bør forklares tydeligere, og tekniske detaljer som skriptbaner og filnavn bør flyttes til vedlegg slik at hovedteksten får bedre flyt.

### 2.4 Analyse og resultater

Det er en styrke at SARIMAX sammenlignes kritisk med Seasonal Naive, og at resultatene vurderes separat per varestrøm. Tre forbedringspunkter: (1) Modellvalget for S er ikke tilstrekkelig begrunnet. I avsnitt 7.2 og 8.4 velges SARIMAX(0,1,0) på RMSE alene, men modellen gir dårligere MAE og MAPE enn den enkle SNaive-baselines. For kapasitetsplanlegging kan det argumenteres begge veier — vi etterlyser en eksplisitt begrunnelse for hvorfor RMSE prioriteres fremfor MAE og MAPE i denne sammenhengen. (2) LP-resultatet på indeksskala bør forklares tydeligere som en teknisk smoke-test, ikke som et mål på faktisk kapasitetsbehov i drift. (3) Den lovede sensitivitetsanalysen fra avsnitt 1.4 og 5.1.2 — som beskriver pluss/minus 10 % volum, kapasitetsbortfall og ekstreme høysesonger — er i praksis redusert til en indeks-kjøring der alle scenarier gir 0,00 ekstra timer. Forfatteren bør enten justere metodebeskrivelsen til å matche det som faktisk er gjort, eller tydeliggjøre at full sensitivitetsanalyse gjenstår.

### 2.5 Diskusjon

Diskusjonen er en av de sterkere delene av rapporten og viser god bevissthet om egne begrensninger. Det er positivt at det skilles mellom teknisk modellkjøring og operativ bruk. To forbedringspunkter: (1) Funnene bør knyttes tydeligere tilbake til problemstillingen. Rapporten beskriver at kapasitetsproblemene oppstår gjennom sonevise cut-off-frister, mens modellen opererer på ukentlig nivå. Forfatteren bør enten forklare dette gapet eksplisitt, eller vise hvordan modellen kan videreutvikles med mer granulære data på dag- og sone-nivå. (2) Diskusjonen berører implikasjonene for knapt. For praksis er den viktigste implikasjonen at modellen kan flytte planleggingen fra reaktiv ekstrahjelp til proaktiv ukesplanlegging — dette nevnes kort i avsnitt 9.3, men fortjener et eget avsnitt. For teori viser rammeverket en overførbar måte å integrere SARIMAX og LP på i distribusjonskontekster med sonevise frister, noe som kan ha verdi for liknende operasjoner i næringsmiddel- og dagligvarebransjen.

### 2.6 Konklusjon

Konklusjonen oppsummerer rapportens hovedbidrag, men bør skille klarere mellom hva som er utviklet og testet teknisk, hva som er dokumentert med data, og hva som gjenstår før modellen kan brukes som beslutningsstøtte i drift. Vi anbefaler at forfatteren særlig prioriterer tre ting før endelig innlevering: (1) kjør LP-modellen på reelle FPK-volumer lokalt og rapporter resultater i anonymisert eller relativ form, (2) kalibrer sonevise fristkapasiteter mot faktisk bemanning og tidsvinduer, og (3) gjennomfør en reell sensitivitetsanalyse med pluss/minus 10–20 % endring i volum, prosess-tid og kapasitet.

### 2.7 Skriveflyt, formelle aspekter og helhetsvurdering

Rapporten er generelt ryddig skrevet og godt organisert, og strukturen gjør det lett å følge hovedideen fra problemstilling til resultater. Vi vil likevel påpeke flere forbedringspunkter knyttet til form og lesbarhet.

**Språk og pedagogikk:** Rapporten er skrevet dokumenterende heller enn pedagogisk, og forutsetter at leseren kjenner både SARIMAX-modellering og lineær programmering. Begreper som «parsimonisk», «eksogen variabel» og «out-of-sample validering» er oversatt direkte fra engelsk på en måte som ikke alltid fungerer naturlig på norsk, og forklares ikke når de introduseres. Vi anbefaler at forfatteren går gjennom de tekniske avsnittene med spørsmålet: «Vil en logistikkleder uten programmeringsbakgrunn forstå hva dette betyr?» — og legger til korte forklaringer der svaret er nei. Matematiske formler og tekniske implementasjonsdetaljer i kapittel 5 og 6 bør flyttes til vedlegg slik at hovedteksten kan fokusere på valg, begrunnelser og resultater.

**Figurtekster:** Den detaljerte figurforklaringen er satt som uthevet brødtekst like etter figurene (f.eks. Figur 1 på s. 21, Figur 3 og 4 på s. 23–24) i stedet for som kort figurtekst. Standard akademisk praksis er at figurteksten er kort og beskrivende, mens tolkningen hører til i brødteksten med eksplisitt kryssreferanse. Vi anbefaler at forfatteren skiller disse to elementene tydelig i alle figurer.

**Layoutfeil:** Rapporten har visuelle feil på side 19, 23, 29 og 30 der lange modellnavn og filnavn i tabellceller overlapper nabotekst og gjør innholdet uleselig. På side 19 og 23 er modellbetegnelsene SARIMAX(1,1,1)(0,0,0)[52] og ARIMA/SARIMAX(0,1,0)(0,0,0)[52] ikke lesbare i kolonnen «Valgt modell». På side 29–30 er vedleggsoversikten (vedlegg A, E, F, G, H og I) uleselig fordi filnavnene presser inn over kolonnen til høyre. Løsning: aktiver automatisk tekstbryting og juster kolonnebreddene i alle tabeller.

**Forkortelser og APA 7:** Forkortelsene FPK, P1, P2, DD, ED, PD og LP introduseres uten forklaring første gang de brukes i teksten. Bibliografien inneholder «Bruk»-kommentarer for flere kilder som ikke hører hjemme i en APA 7-referanseliste og bør fjernes.

Vår samlede vurdering er at rapporten er et sterkt og lovende arbeid som viser god forståelse for prognoser, kapasitetsplanlegging, datakvalitet og anonymisering. Rammeverket er solid, og de metodiske valgene er gjennomtenkte. For å gjøre rapporten operativt nyttig gjenstår LP-kjøring på reelle FPK-volumer, kalibrering av sonevise fristkapasiteter og en reell sensitivitetsanalyse. Med disse stegene på plass vil rapporten stå vesentlig sterkere som beslutningsstøtte i kapasitetsplanleggingen.
