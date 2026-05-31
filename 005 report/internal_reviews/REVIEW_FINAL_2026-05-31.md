# Uavhengig sluttreview — LOG650-prosjektet (Davor Necemer)

**Dato:** 2026-05-31 · **Metode:** 6 parallelle, adversariske reviewer-agenter (friske kontekster), én per dimensjon (tall · struktur · metode · kilder · språk/forsvar · scope-ærlighet). Hver agent verifiserte mot kanonisk rapport, fasit-JSON, modellkode, proposal, G05-review og kildestatus.

## Helhetsvurdering

Prosjektet er **innleverings-nært og solid**. Ingen dimensjon fikk «vesentlige-mangler». Tall-korrektheten er **plettfri** (se under). De øvrige fem dimensjonene er «mindre-mangler»: ekte, men fiksbare presisjons-/konsistens-punkter. To funn er **MÅ** (begge i §5.1.1: metodebeskrivelse stemmer ikke med koden, og en intern selvmotsigelse om modellvalgskriterium). Den mest sårbare flaten ved **muntlig forsvar** er bidragsverdien («hva har 0.00-resultatet egentlig vist?») og «teoretisk hull»-påstanden.

**Tall-fasit-sjekk: Er det noen tall som IKKE stemmer? → NEI.** Alle baseline-/SARIMAX-metrikker, Ljung-Box, prosess-tider, soneandeler, basekapasitet, ukestall/observasjoner, LP-resultater og deskriptiv statistikk matcher `model_run_summary.json` og underliggende CSV-er eksakt, med korrekte avrundinger (agenten reberegnet selvstendig fra CSV).

---

## MÅ — rett før innlevering

| # | Hvor | Funn | Tiltak |
|---|---|---|---|
| M1 | §5.1.1 pkt 2 vs `run_forecast_capacity_models.py` | Beskriver KPSS-test (d), Canova-Hansen (D) og ACF/PACF for ordensvalg — men koden gjør **ingen** av disse; den kjører en fast, uttømmende kandidat-grid. (grep: 0 treff på kpss/canova/auto_arima/pmdarima/adfuller). | Omformuler §5.1.1 til å beskrive det som faktisk gjøres: parsimonisk grid over lave (p,d,q)×(P,D,Q), d/D **enumereres** (ikke test-velges), rangert på out-of-sample RMSE. |
| M2 | §5.1.1 pkt 3 vs §7.2 + kode (l.248) | Selvmotsigelse: §5.1.1 sier valg «primært på **AICc**», men §7.2/Tabell 3/8 og koden (`sort_values(['rmse','aicc','n_params'])`) velger primært på **RMSE**. | Rett §5.1.1 til «primært out-of-sample validerings-RMSE (jf. §7.2), med AICc og parsimoni som sekundære, samt Ljung-Box residualdiagnostikk». |

## BØR — styrker forsvarbarheten merkbart

| # | Hvor | Funn | Tiltak |
|---|---|---|---|
| B1 | §5.1.1 (re-estimering) | Sier endelig modell «re-estimeres på hele datasettet før LP-input» — skjer ikke; LP mates med valideringsprognosen. | Presiser at smoke-testen mater valideringsprognosen; re-fit+forward-forecast hører til reell-skala (§9.4). |
| B2 | §7.2 | Begge valgte modeller har sesongorden **(0,0,0)** mens hele SARIMAX-motivasjonen er sterk årssesong — uforklart. (Sesongmodeller ble faktisk testet og tapte på RMSE.) | Én setning: sesongledd ble inkludert i griden, men ga ikke lavere RMSE (kun 2 treningssesonger); valgte modeller er effektivt ikke-sesonglige. |
| B3 | §7.2 / §8.4 (S-modell) | S-«SARIMAX» (0,1,0) gir én flat konstant **15.68** for alle 13 uker, som ligger over nesten hele faktiske S-spennet (5.4–19.15). RMSE-seieren (6.67 vs 7.53) skyldes SNaive sine enkeltbom, ikke prediktiv skill. | Skjerp: S er en drift-fri random walk uten reell prediktiv verdi; RMSE-fordelen er skjør. Vurder SNaive som operativ S-prognose. |
| B4 | §11 Bibliografi (SSB) | Tittel feil/oppdiktet: «Sykefraværet i industri og andre næringer». Faktisk SSB-tittel er **«Sykefravær»**. Kilde + ~6 %-tall er reelle. URL er generisk hjemmeside. | Endre tittel til «Sykefravær»; bytt URL til stabil statistikk-lenke (i `003 references/.../LINKS.txt`). |
| B5 | Vedlegg J (SSB-rad) | Krysseref-feil: hevder SSB brukt i «§5.4 og §6.3», men eneste inline-sitering er i **§5.1.2**. | Rett til §5.1.2. |
| B6 | §9.1 (l.1012) | Usitert kvantitativ regel («3–4 sesonger for stabil sesongestimering»). | Legg til kilde (Hyndman & Athanasopoulos 2021) **eller** omformuler til egen eksplisitt vurdering. |
| B7 | §1.1 + sammendrag/abstract vs §6.5 | Problemstilling/sammendrag fremhever «sonevise cut-offs», men den løste LP-en aggregerer dem bort (sone-constraints utenfor målfunksjonen). | Presiser i §1.1 (+ én setning i sammendrag/abstract) at sonefristene er aggregert til kumulative ukeandeler og ikke løses som egne constraints i denne versjonen. |
| B8 | Proposal vs §6.2/§6.3 | Fristbrudd-enhet endret fra **FPK** (proposal) til **minutter** (rapport, SLACK) uten forklaring. | Én setning: fristbrudd måles i arbeidsminutter for enhetskonsistens — bevisst raffinering av proposalens FPK-formulering. |
| B9 | Innhold (TOC) vs §5.0 | TOC oppgir «5.1 Metode», men brødteksten hopper rett til 5.1.1/5.1.2 — ingen `### 5.1`-overskrift. | Legg inn `### 5.1 Metode` (1–2 innledende setninger) før 5.1.1. |
| B10 | §9.1 (l.1014, 1022) | Engelske etiketter i norsk tekst: «**Mitigation:**», «**Limitation:**» (AI-oversettelsesrest). | Bytt til «Tiltak/avbøtning:» og «Begrensning:». Sjekk hele §9. |
| B11 | Gjennomgående | Uoversatte engelske faguttrykk der norsk term finnes («demand forecasting», «constraints», «Standard Working Hours», «raw dispatcher actions», «shipping dates», «trade-offs»). | Innfør norsk term ved første bruk (engelsk i parentes), bruk norsk konsekvent. |
| B12 | §3.2 (l.328), §3.3 (l.337), §5.3 (l.571) | **Residualt overclaim:** disse sier (present-tense) at usikkerheten «håndteres gjennom scenarioanalyse» / «±10 % → ±Y % overtid» — mens §8.4 sier 0.00 i alle baner. Nøyaktig det G05-funn #11 ba om å fjerne; fixen ble bare påført §1.4/§5.1.2/§8.4, ikke §3/§5.3. | Legg smoke-test-forbehold i alle tre: «tenkt håndtert … i denne versjonen kun trivial indeks-smoke-test (§8.4), full sensitivitet gjenstår». |
| B13 | `G05_INTEGRATION_PLAN.md` #11 | Status «Done» er **overrapportert** — funnet er kun delvis lukket (§3/§5.3 gjenstår, jf. B12). | Lukk B12, oppdater så status til reelt «Done» (eller «Done (delvis)» midlertidig). |
| B14 | Sammendrag (l.97) | S-forbeholdet kan gjøres enda tydeligere i samme setning som «forbedring». | «… 6.67 for S — men kun på RMSE; S taper på både MAE og MAPE og kan ikke regnes som reell forbedring over SNaive.» |

## KAN — finpuss

- **Bokmål/anglisismer:** `dyrbar`→kostbar (l.197), `ugentlig`→ukentlig (l.1050), `defensibelt`→forsvarbart (l.1014); sjekk også `peaker`, `granulare`, `transferabilitet`.
- **Tall-presentasjon (ikke feil):** Figur 4 oppgir +10 %-utnyttelse (0.030/0.049 %) — presiser at det er +10 %-tall; «forbedrer RMSE **fra 18.96** til 13.21» fjerner feillesning; harmoniser «118 totale / 117 modelluker» likt i norsk + engelsk sammendrag.
- **APA:** «et al.» fra første inline-sitering (streng APA 7); tematisk-delt bibliografi vs. én alfabetisk liste (forsvarlig som-er).
- **Scope:** sesongvariasjon i prosess-tid (n=8 dekker ikke juleuker) — 1–2 setninger i §5.4 som åpen begrensning (G05-funn fortsatt «Pending»).
- **Stil:** førsteperson «vi»/«Hvordan kan vi …» i problemstilling — vurder upersonlig passiv hvis veileder foretrekker.

## Falsk alarm (ikke et reelt funn)

Struktur-agenten flagget at «36 sider» ikke kan verifiseres «fordi ingen PDF finnes i repoet». **Dette stemmer ikke** — `014 fase 4 - report/Sluttrapport_…_endelig.pdf` finnes og er bekreftet 36 sider (agenten globbet kun `005 report/`). Sidetallet er korrekt.

---

## Muntlig forsvar — de mest sannsynlige kritiske spørsmålene (rangert etter risiko)

1. **«0.00 ekstra timer — hva har dere egentlig vist utover at koden kjører?»** Robust på ærlighet (rapporten sier selv det er en smoke-test, §8.4 l.975), men **svak på verdi**. Forbered et offensivt svar: hva smoke-testen *eliminerer* (enhetsfeil, datastrøm SARIMAX→LP, løserkonvergens) + det *integrerte* metodiske bidraget.
2. **«Det 'teoretiske hullet' (§2.3) — integrert prognose+optimering er jo APP fra 1955 (Holt et al.). Har dere bare ikke funnet litteraturen?»** **Svakest faglig punkt.** Nedjuster muntlig til at bidraget er det **konkrete oppsettet** (to-strøms terminaldrift under sonevise nattfrister), ikke et generelt teoretisk hull. Vær forberedt på spørsmål om litteraturdekning (kun 4 prognose-/LP-primærkilder).
3. **«S-modellen taper på MAE og MAPE — hvorfor velge den?»** Robust (RMSE/konveks-kostnad-argument, §7.2 l.847), men innrøm at S i praksis er for volatil for tilgjengelig historikk (B3).
4. **«§3 sier usikkerheten håndteres — gjør den det?»** Svak slik det står (selvmotsigelse §3 vs §8). **Lukk B12 før forsvar.**
5. **«§5.1.1 beskriver KPSS/AICc — men koden gjør grid/RMSE?»** Svak til M1/M2 er rettet; lett å forsvare etter retting.
6. **«Sone-mapping (Street→cut-off) — hvordan vet dere den stemmer?»** Middels; ærlig antakelse, men sensitivitet ikke kjørt. Bruk at andelene uansett er nær jevne (32.5/33.5/33.9 %).
7. **«Prosess-tid n=8 — varierer ikke tempo med sesong?»** Middels; erkjent som utvalg, men sesongvariasjon ikke diskutert (KAN-funn).

**Sterke flater (godt forberedt i teksten):** 0.00 = skala-artefakt (verifisert aritmetikk 8 640 min vs ~3.83 indeks-min), «gjenstår»-lista (§8.5/§10), datakrav-ærlighet (104 obs/2 sesonger), kildenes realitet (DOWNLOAD_STATUS).

---

## Supplement: kryssjekk mot Codex «Review-third» (annen modell)

Begge reviewene konkluderer: nær innleveringsklart, men ikke helt uten siste rettinger. Tallene stemmer; hovedrisikoen er metode-/scope-presisjon + personvern-erklæringen.

### Begge enige (høy tillit — rett definitivt)
M1+M2 (§5.1.1 metode↔kode + AICc-vs-RMSE), B1 (re-estimering), B2 (sesong (0,0,0)), B9 (TOC §5.1), B13 (G05-closure overrapportert), n=8-sesongvariasjon.

### NYE funn fra Codex (mine agenter overså)
| Alvor | Hvor | Funn | Tiltak |
|---|---|---|---|
| **MÅ** | §5.5/erklæring + REVIEW_FINDINGS_2026-04-29 §6 | **Personvern/NSD ikke forsonet.** Fase-3-review OG Codex: dispatcherdata hadde personnavn LOKALT før anonymisering — «behandling av personopplysninger (selv lokalt) skal formelt meldes». Erklæringen «ikke omfattes» dekker kun publisert data. Aldri lukket. | Avklar med veileder/NSD-koordinator FØR innlevering, ELLER demp erklæringen til å skille publisert (anonymisert) fra lokal rådatabehandling. Signert juridisk erklæring — høyest prioritet. |
| **MÅ** | Sammendrag/abstract/konklusjon | **Kampanjekalender-overclaim.** Sier SARIMAX bruker «kampanjekalender som eksogen variabel», men valgt F bruker `holiday_flag`, valgt S ingen. | Presiser: kandidatrammen tester kampanje/helligdag; valgt F = `holiday_flag`, valgt S = ingen. |
| **MÅ** | Figur 1 (l.896) | **Feil sluttuke:** caption «2024-W01 til 2026-W19», men modellgrunnlag slutter 2026-14. | Rett caption (og regenerer figur hvis den faktisk plotter til W19). |
| **MÅ** | Abstract/teori/konklusjon vs §6.5 | **LP sonefrister overselges** (løfter B7 til MÅ): antyder LP håndhever sonefrister som constraints; faktisk kun aggregert P1/P2, sonelast er output. | Skriv at soneandeler er beregnet/rapportert, ikke operasjonalisert som bindende fristconstraints i smoke-testen. |
| **MÅ** | Proposal vs §1.1/§10 | **Scope-reduksjon ikke eksplisitt:** proposal lover «nøyaktig ekstra kapasitet per uke»; rapport leverer indeks-smoke-test. | Én setning: avviker fra proposal, operativ reell-skala kapasitet avgrenset til videre arbeid. |
| BØR | Abstract + konklusjon (l.1095) | **Soneandeler «sum 1.000» feil** — avrundede 0.325+0.335+0.339 = 0.999 (norsk sammendrag korrekt). | Rett til 0.999 eller bruk eksakte andeler ved «sum 1.000000». |
| BØR | §11 (l.1149) | **«Notat til framtidig arbeid»** ligger i bibliografikapitlet; ikke bibliografisk. | Flytt til §9.4/§10. |
| BØR | Innhold (TOC) | **TOC uten sidetall** (manuell punktliste); malen har sidetallsbasert innhold. | Vurder auto-TOC (`--toc`) i bygget. |
| KAN | kjørekommando | Avhengigheter ikke pinnet (JSON logger pandas 3.0.2 / scipy 1.17.1 / statsmodels 0.14.6). | Legg ved requirements / skriv versjoner. |

### NYE funn fra min review (Codex overså)
B4 (SSB-tittel oppdiktet → «Sykefravær» + URL), B5 (Vedlegg J SSB-kryssref §5.1.2), B6 (usitert «3–4 sesonger»), B3 (S-modell flat konstant 15.68 — mer spesifikt), B12 (§3.2/§3.3/§5.3 spesifikke overclaim-lokasjoner).

**Netto:** Codex styrker særlig overclaim-/faktafronten (kampanje, sonefrister, Figur 1, sum 1.000) og fanget personvern-hullet. Min styrker kilde-/metodepresisjon (SSB, 3–4 sesonger, S-modell). Sammen gir de en komplett rettingsliste.
