# G05 peer-review — integrasjonsplan for sluttrapport

**Kilde:** [`013 fase 3 - review/peer review Integrert volumprognose og kapasitetsanalyse_G05_G06.md`](../013%20fase%203%20-%20review/peer%20review%20Integrert%20volumprognose%20og%20kapasitetsanalyse_G05_G06.md)
**Reviewer:** G05 – Birgitte Bellsund og Vera
**Dato review:** 2026-05-07 (dokument internt datert), mottatt 2026-05-08 13:01
**Frist sluttrapport:** 2026-05-31 (1 dag fra plan-dato 2026-05-30)
**Mål-fil:** [`005 report/Sluttrapport_Volumprognose-Kapasitetsanalyse_DavorNecemer.md`](../005%20report/Sluttrapport_Volumprognose-Kapasitetsanalyse_DavorNecemer.md)

## Realisme om scope (kritisk å lese først)

G05s top-3-prioriteringer er: (1) LP på reelle FPK-volum, (2) kalibrer sonevise fristkapasiteter, (3) reell sensitivitetsanalyse ±10–20 %. **Disse er ikke realistiske som fullskala arbeid med 1 dag igjen.** I stedet:

- **Må gjøre (≈2 t totalt):** APA, forkortelser, layout-fix, figurtekst-skille
- **Bør gjøre (≈2.5 t totalt):** Ramme-presisering (1.1, 7.2, 8.4, 9.x), modellvalg-S-begrunnelse, konklusjons-skille
- **Kan gjøre om tid:** Reell sensitivitetsanalyse på indeks-skala (varier parametre i en parametrisk kjøring)

For G05s top-3 er den ærlige posisjonen: erkjenn eksplisitt at de gjenstår, og styrk "Gjenstår før operativ bruk"-seksjonen i §10 med konkrete neste-steg fremfor å forsøke en halvgjort kjøring.

---

## 19 funn fra G05

Status-kolonne: `Pending` (ikke startet), `In progress`, `Done`, `Deferred` (utsatt med begrunnelse).

### Innledning (G05 §2.1) — 2 funn

| Funn (G05) | Lokasjon | Tiltak | Estimat | Status |
|---|---|---|---|---|
| Tydeliggjør at rapporten leverer teknisk rammeverk + smoke-test, ikke ferdig operativ analyse | Sluttrapport §1.1 (problemstilling) | Legg til 1–2 setninger som eksplisitt skiller rammeverk fra operativt resultat | 15 min | Done (eget avsnitt i §1.1 etter den todelte problemstillingen: "teknisk rammeverk + smoke-test, ikke ferdig operativ analyse", operativt grunnlag → §9.4/§10) |
| Faglig bidrag fra §9.4 (integrert SARIMAX+LP sjelden samlet i litteratur) bør fremheves allerede i innledningen | Sluttrapport §1.0 (innledning) | Legg til 1 avsnitt med faglig bidrag før §1.1 | 15 min | Done (faglig-bidrag-avsnitt løftet opp i innledningen, krysshenviser §9.4) |

### Litteratur (G05 §2.2) — 2 funn

| Funn (G05) | Lokasjon | Tiltak | Estimat | Status |
|---|---|---|---|---|
| Teori bør knyttes tydeligere til caset (kobler metoder, men ikke konkrete modellvalg) | Sluttrapport §2.1, §2.2 | Legg til 1 setning per kilde som forklarer hvordan den begrunner et spesifikt valg i denne rapporten | 20 min | Pending |
| Mangler eksplisitt diskusjon av teoretiske hull (vurderingskriteriene etterspør dette) | Sluttrapport §2.3 (slutt) | Flytt opp avsnittet fra §9.4 om integrert prognose-optimering som teoretisk hull | 15 min | Done (#13 — nytt **Teoretisk hull**-avsnitt i §2.3 m/ kilder for begge sider + callback fra §9.4; §9.4-heading utvidet til "Bidrag, kritikk og videre forskning") |

### Metode (G05 §2.3) — 3 funn

| Funn (G05) | Lokasjon | Tiltak | Estimat | Status |
|---|---|---|---|---|
| Intern spenning i §1.3: uke-aggregering forsvares uten å erkjenne at det skjuler dagsvise topper | Sluttrapport §1.3 (Aggregeringsnivå) | Reformuler avgrensning: "praktisk forenkling med kjent kostnad — dagsvis modellering ligger utenfor scope men er kritisk for operativ bruk" | 15 min | Done (a1a726d — §1.3 omformulert m/ *Kjent kostnad*-setning, kryssref §9.4) |
| Prosess-tidsmatrise (n=8) ignorerer sesongvariasjon i håndteringstid | Sluttrapport §5.4 + §8.2 | Legg inn 1 avsnitt om sesongvariasjons-risiko som begrensning | 20 min | Pending |
| Validitet/reliabilitet bør forklares tydeligere; tekniske detaljer (skriptbaner, filnavn) til vedlegg | Sluttrapport §5.4 + §5.5 | Add validitet/reliabilitet-avsnitt; flytt §5.3-paths til Vedlegg | 30 min | Deferred (tidskrevende, lavest ROI) |

### Analyse og resultater (G05 §2.4) — 3 funn

| Funn (G05) | Lokasjon | Tiltak | Estimat | Status |
|---|---|---|---|---|
| Modellvalg for S ikke tilstrekkelig begrunnet (RMSE prioriteres over MAE/MAPE) | Sluttrapport §7.2 + §8.4 | Legg inn 1 avsnitt som begrunner RMSE-prioritet for kapasitetsplanlegging (store feil = store kapasitetsavvik = dyrere). Erkjenn at MAE/MAPE indikerer S-modellen bør tolkes varsomt | 20 min | Done (§7.2: RMSE-begrunnelse via konveks kostnadsstruktur — store avvik = dyre kapasitetsavvik; eksplisitt at S kun vinner på RMSE 6.67<7.53, SNaive bedre på MAE 5.15<6.17 og MAPE 60.2%<76.0%, S tolkes varsomt; F robust på alle tre) |
| LP-resultat på indeksskala må forklares tydeligere som smoke-test (ikke faktisk behov) | Sluttrapport §8.4 | Allerede delvis gjort i tidligere round-2-review; styrk overskrift og første setning | 10 min | Done (overskrift → "Prognosevalidering og LP smoke-test" + i innholdsfortegnelse; LP-del åpner med fet smoke-test-ramme) |
| Lovet sensitivitetsanalyse fra §1.4 og §5.1.2 er i praksis bare indeks-kjøring med 0.00 utfall — metode og resultat matcher ikke | Sluttrapport §5.1.2 + §8.4 | Reformuler metodebeskrivelsen til å matche faktisk gjennomført arbeid; flytt full sensitivitetsanalyse til "Gjenstår" | 25 min | Done (§5.1.2 skiller nå metodisk ramme vs. faktisk kjørt; full sensitivitet/skyggepris rutet til §8.5/§9.4/§10; §1.4 Antagelse 3 også justert) |

### Diskusjon (G05 §2.5) — 2 funn

| Funn (G05) | Lokasjon | Tiltak | Estimat | Status |
|---|---|---|---|---|
| Funn bør knyttes tydeligere til problemstilling — gap mellom ukentlig modell og dagsvise frister | Sluttrapport §9.2 eller §9.4 | Legg til avsnitt som eksplisitt erkjenner gap-et og foreslår videreutvikling med dag/sone-data | 20 min | Done (a1a726d — nytt "Tidsoppløsning"-gap-avsnitt i §9.4, foreslår dag/sone-disaggregering fra dispatcher-data) |
| Implikasjoner berøres kort — proaktiv ukesplanlegging fortjener eget avsnitt | Sluttrapport §9.3 | Utvid "Modellens tiltenkte verdi"-listen til et fullt avsnitt om proaktiv-vs-reaktiv-skiftet | 20 min | Done (a1a726d — nytt proaktiv-vs-reaktiv-avsnitt i §9.3) |

### Konklusjon (G05 §2.6) — 1 funn

| Funn (G05) | Lokasjon | Tiltak | Estimat | Status |
|---|---|---|---|---|
| Skille klarere mellom utviklet+testet, dokumentert, og gjenstår | Sluttrapport §10 | Restrukturer §10 i tre eksplisitte bolker: "Utviklet og testet teknisk" / "Dokumentert med data" / "Gjenstår før operativ bruk" | 20 min | Done (a1a726d — §10 tre-bolk + Praktisk implikasjon/Begrensninger; prosess-tid rettet til eksakt 0.003885/0.037555) |

### Skriveflyt og formelle aspekter (G05 §2.7) — 6 funn

| Funn (G05) | Lokasjon | Tiltak | Estimat | Status |
|---|---|---|---|---|
| Språk for ikke-tekniske lesere; "parsimonisk", "eksogen", "out-of-sample" mangler kort forklaring | Sluttrapport §5.1.1 + §7.2 | Legg til 1 setning forklaring ved første forekomst | 30 min | Pending |
| Matematiske formler og tekniske implementasjonsdetaljer i §5 og §6 bør flyttes til vedlegg | Sluttrapport §5, §6 → §12 | Stor endring; vurder delvis: behold formler men flytt skript-detaljer | 45 min | Deferred (struktur-endring) |
| Figurtekster: kort caption + tolkning til brødtekst med kryssreferanse | Sluttrapport §8 (alle Figur N-tekster) | Splitt eksisterende lange captions: behold faktisk beskrivelse i caption, flytt tolkning til brødtekst | 45 min | Done (Figur 1–6: caption = kort faktabeskrivelse, tolkning flyttet til eget brødtekst-avsnitt som starter "Figur N viser at …") |
| Layout-feil på side 19, 23, 29, 30: lange modellnavn/filnavn overlapper nabotekst | Sluttrapport §7.2-tabell, §8.4-tabell, §12-vedleggsoversikt | Pandoc + xelatex: bruk `\small` på de problematiske tabellene, eller del lange filnavn med `\allowbreak` | 30 min | Done — kombinasjon: (a) eksplisitt kolonnebredde via bindestrek-andeler i separatorlinjen for §7.2/§8.4/§8.3, (b) `\allowbreak` i modellnavn, (c) `\footnotesize` på §7.1/§8.3/§12, (d) preamble `hyphenat[htt]`+`\sloppy`+`emergencystretch` for filstier/URL. **Verifisert objektivt: 0 Overfull \hbox i xelatex-loggen** (mot 9+ før). Fant også §7.1 og §8.4 hadde samme feil utover G05s liste. |
| Forkortelser FPK, P1, P2, DD, ED, PD, LP introduseres uten forklaring første gang | Sluttrapport §4.1 (første ED-forekomst), §1.0 (LP) | Legg til forkortelses-liste etter §1.0, ELLER forklar inline ved første forekomst | 20 min | Done (samlet "Forkortelser og symboler"-tabell lagt inn etter Innhold + oppført i Innhold) |
| Bibliografi inneholder "Bruk:"-kommentarer som ikke hører hjemme i APA 7 | Sluttrapport §11 | Fjern alle "Bruk:"-bullets fra bibliografi; vurder eget vedlegg "Anvendelse av kilder" hvis ønskelig | 15 min | Done (ren APA 7-liste, alfabetisert; "Bruk:"/"Merk:" flyttet til nytt Vedlegg J) |

---

## Oppsummering — prioritert tiltaksliste

### MÅ gjøre (≈2 t)

1. Bibliografi APA: fjern "Bruk:"-kommentarer (15 min)
2. Forkortelser introduseres ved første forekomst (20 min)
3. Layout-fix av brutte tabeller s.19/23/29/30 (30 min)
4. Figurtekst-skille (45 min)

### BØR gjøre (≈2.5 t)

5. Innledning: ramme-presisering + faglig bidrag opp (30 min)
6. Modellvalg S: begrunn RMSE-prioritet (20 min)
7. Diskusjon: gap-erkjennelse + implikasjoner-avsnitt (40 min)
8. Konklusjon: tre-bolks-restrukturering (20 min)
9. Metode: praktisk-forenkling-formulering i §1.3 (15 min)
10. LP smoke-test framing (10 min)
11. Sensitivitetsanalyse-metode justert mot faktisk arbeid (25 min)

### KAN gjøre om tid

12. Teori knyttet tydeligere til case (20 min)
13. Teoretisk hull fra §9.4 til §2 (15 min)
14. Sesongvariasjon prosess-tid som begrensning (20 min)
15. Språk-glossar for tekniske begreper (30 min)

### Utsatt (Deferred)

16. Validitet/reliabilitet + flytt skriptpaths til vedlegg (30 min — tidskrevende, lav ROI)
17. Flytt formler fra §5-§6 til vedlegg (45 min — struktur-endring, risiko)

### Ikke realistisk innen frist (top-3 fra G05)

18. **Reell-skala LP på lokal weekly_volume.csv** — krever gjennomarbeidet pipeline med ikke-publiserbart resultat. Tiltak: erkjenn eksplisitt at dette gjenstår og hvilke steg som mangler.
19. **Kalibrer sonevise fristkapasiteter** — krever daglig nattprofil-data som ikke er etablert. Tiltak: dokumenter hva som trengs i §6.5 og §10 "Gjenstår".

20. **Full sensitivitetsanalyse ±10-20 %** — krever parametrisk LP-grid. Tiltak: utfør minimal versjon (kjør 5 scenarier ved indeks-skala med varierte volum-baner) om tid, ellers presenter som gjenstående.

---

## Workflow per tiltak

1. Les §X i hovedrapporten
2. Implementer endring per "Tiltak"-kolonnen
3. Oppdater status til `Done` i tabellen over
4. Etter hver "MÅ"-gruppe: kjør `python "005 report/scripts/build_report_pdf_latex.py"` for å verifisere at PDF-en fortsatt bygger
5. Etter alle "MÅ"+"BØR": full PDF-rebuild og les gjennom hele PDF-en manuelt
6. Commit etter logiske grupper (ikke per enkelt-tiltak) for ryddig historikk
