# Round-2 review-integrasjon før peer-review-innlevering

**Dato:** 2026-04-30
**Trigger:** Eriks krav i økt 1+2 (29. april 2026): *"Bruk av review for kvalitetssikring — Uavhengig gjennomgang (f.eks. via egen agent) forbedrer kvaliteten. Iterasjon og kritiske spørsmål avdekker feil og uklarheter."*
**Reviewmetode:** Uavhengig sub-agent uten tidligere prosjektkontekst, kun med rapport, `model_run_summary.json`, og Eriks kvalitetskriterier som input. Scope: §1 Innledning til §9 Diskusjon + §11 Bibliografi (§10 Konklusjon ble strammet inn parallelt og var ikke inkludert i denne reviewen).

## Funn integrert i denne hovedutkast-versjonen

### Kritiske typo-er (problemstilling og introduksjon)
- §1.1 Problemstilling: "minimaliser resursforbuke" → "minimalisere ressursforbruk".
- §1 Innledning: "stramme restruksjoner" → "stramme restriksjoner"; "søne- og dagsvise" → "sone- og dagsvise".
- §1.3 Avgrensinger: "avgangtidspunkt" → "avgangstidspunkt".

### Internt konsistente referanser
- §2.1 og §3.1: "Hyndman & Athanasopoulos (2021, kapitlene 9 og 9.9)" → "kapittel 9, særlig avsnitt 9.9 om sesonglige ARIMA-modeller". Tidligere formulering var ikke en gyldig kapittelreferanse.

### Ukeantall (118 raw vs. 117 modell)
Sammendraget og §5.4 var uklare på distinksjonen mellom 118 raw uker (publiserbar fil) og 117 modelluker (etter eksklusjon av delvis uke 2026-14). Begge stedene presiserer nå:
- Sammendrag: "118 ukentlige observasjoner per varestrøm i den publiserbare indeks-fila; av disse brukes 117 som modelluker"
- §5.4 Datakvalitet: tilsvarende formulering med eksplisitt henvisning til eksklusjons-punktet.

### Rounding av soneprofil
Sammendraget oppga "Z1 = 0.325, Z2 = 0.335, Z3 = 0.339, sum 1.000". De avrundede verdiene summerer faktisk til 0.999. Korrigert til å vise eksakte andeler (0.325311, 0.335234, 0.339455 med eksakt sum 1.000000) og forklare avrundings-artefakten.

### Tabell-enheter (Eriks krav om "selvforklarende tabeller")
- §7.1: kolonneoverskrifter har nå "(indeks)" der det er relevant; fotnote forklarer indeks-skala og CV.
- §8.3: Bemanning-kolonnen merket som FTE med fotnote.

### LP-modell §6.5 var formelt ufullstendig
$X^{deadline}_{k,t}$ var definert i sonenivå-restriksjonen men aldri inkludert i målfunksjonen $Z$ i §6.3. Lagt til eksplisitt forklaring at sonenivå-leddene er en designskisse for operativ utvidelse og ikke inngår i den ukentlige hovedmodellen som ble kjørt i §8.4.

### LP smoke-test caveat (§8.4)
Lagt til konkret skala-forklaring: P2-basekapasitet = 8 640 minutter mot maksimal indeks-belastning ~3.83 indeks-minutter, så 0.00 ekstra-timer er en konsekvens av indeks-skalaen, ikke et bevis på kapasitetsmargin.

### §9.2 muddled wording
"104 treningsobservasjoner × 52-ukes sesong = akkurat minimum" var matematisk feil. Korrigert til "104 treningsobservasjoner / 52-ukes sesongperiode = 2 sesonger".

### Figur-captions (Eriks krav om selvforklarende figurer)
- Figur 1: "uke 12-14 (påske)" var generisk og matchet ikke alle 3 år; spesifisert til "2024-W13, 2025-W16, 2026-W14".
- Figur 2: "F-volumet ... innenfor et smalt bånd (~80–115)" understatet faktisk spread (min 29.31). Korrigert til "for det meste innenfor et bånd på ca. 70–125; enkeltobservasjoner (uke 2026-01) ligger lavere".

### Bibliografi (Eriks krav om reelle, etterprøvbare referanser)
- SSB (2024): lagt til inline-sitering i §5.1.2 ("(~6 % årlig; SSB, 2024)").
- NNN (2024–2026): bibliografi-entry oppdatert til ærlig å markere at NNN er bakgrunnsdokument, ikke direkte sitert (siden $c_j$ holdes som generiske relative vekter).
- KML Kompendium (2026): bibliografi-entry oppdatert til å markere det som metodisk bakgrunn, ikke direkte sitert (de spesifikke teoretiske påstandene støttes av primærkildene).

## Funn utsatt til endelig innlevering 29. mai

- Bokmål/engelsk-konsistens: "Mitigation", "smoke-test", "scope", "constraints", "limitation" — krever en glossar-pass eller systematisk oversetting (defer).
- AICc-verdier i §7.2 modellvalg-tabell: tilgjengelige i `sarimax_candidate_results.csv` og `model_run_summary.json` (F: 723.44, S: 1058.15) men ikke rapportert eksplisitt i tabellen. Defer.
- §8.5 og §9.4 har overlappende "gjenstår"-lister. Konsolidering kan skje i siste pass.
- Fildes, Ma & Kolassa: PDF i `003 references/` er 2018 working paper, mens publisert versjon er 2022 (samme DOI, samme innhold). Bibliografien siterer 2022 (publisert), som er korrekt — kun en notat for transparens.
- Winston (2004) bibliografi-entry: mangler forlagsby. Mindre.

## Verifisering etter integrasjon

- PDF regenerert via `005 report/scripts/build_report_pdf.py` — 2070 KB, alle figurer innebygget.
- Talltest mot `004 data/processed/model_run_summary.json` opprettholdt: F-RMSE 13.21, S-RMSE 6.67, P1 max 0.00660, P2 max 0.06384 — ingen drift fra rettingene.
- Internt konsistente ukeantall: sammendrag, §5.4, §7.1 og §10 viser nå alle 117 modelluker / 234 modellobservasjoner med eksplisitt referanse til 118 raw der relevant.

## Endringer gjort på fil

- `005 report/Sluttrapport_Volumprognose-Kapasitetsanalyse_DavorNecemer.md` — ~15 inline-rettinger
- `013 fase 3 - review/Sluttrapport_Volumprognose-Kapasitetsanalyse_DavorNecemer.pdf` — regenerert
- `013 fase 3 - review/REVIEW_INTEGRATION_2026-04-30.md` — denne fila
