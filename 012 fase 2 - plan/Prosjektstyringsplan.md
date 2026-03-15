# Prosjektstyringsplan

## 1. Sammendrag
**Bakgrunn:** Prosjektet tar utgangspunkt i et norsk produksjons- og distribusjonsmiljø innen næringsmiddelindustrien. Bedriften håndterer parallelle varestrømmer som samles i et felles distribusjonsledd med faste daglige ferdigstillelsesfrister (cut-offs). Utfordringen i dag er at det oppstår flaskehalser som truer disse fristene, selv om den totale ukekapasiteten egentlig er tilstrekkelig.

**Problemstilling:** Hvordan kan vi optimalisere allokeringen av ekstra kapasitet og tidspunkt for produksjonsstart for å overholde faste distribusjonsfrister i et konvergerende logistikknettverk?

**Mål:** Hovedmålet er å utvikle en kapasitetsmodell som minimerer samlet bruk av ekstra kapasitet (som overtid og ekstra skift) og unngår fristbrudd. Modellen vil bruke KI og historiske data for å lage presise etterspørselsprognoser, som deretter fungerer som input for å planlegge kapasitetsbehovet.

**Prosjektrammer:** Dette dokumentet utgjør prosjektstyringsplanen for prosjektet. Det etablerer prosjektets rammer (baseline) for omfang, fremdrift og risiko. Arbeidet planlegges ferdigstilt innen utgangen av mai 2026, og løsningen støtter bedriftens strategiske mål om økt leveringspresisjon og mer kostnadseffektiv ressursutnyttelse.

## 2. Omfang (Scope)
**Krav:**
*   **Funksjonelle krav:** 
    *   Løsningen må kunne importere og prosessere historiske data for salg, produksjon og kampanjer.
    *   KI-modellen må kunne generere presise etterspørselsprognoser på ukentlig/daglig basis.
    *   Kapasitetsmodellen må kunne foreslå optimal allokering av overtid og ekstra skift for å unngå brudd på faste distribusjonsfrister (cut-offs).
*   **Ikke-funksjonelle krav:** 
    *   Modellen skal være utviklet i Python og dokumentert slik at den er reproduserbar for bedriften.
    *   Analysen og resultatene skal dokumenteres i en akademisk prosjektrapport i henhold til retningslinjene for LOG650.

**Løsning:**
*   Sluttproduktet er todelt: 
    1. En datadrevet, programmert kapasitets- og prognosemodell (skript/kode).
    2. En fullstendig prosjektrapport som redegjør for metodikk, analyse av flaskehalser, resultater fra modellen, samt en diskusjon og konklusjon.

**Arbeidsnedbrytningsstruktur (WBS):**
Prosjektet er strukturert i fire hovedfaser som reflekterer felles milepæler for faget:
1.  **Fase 1: Proposal (Fullført)**
    *   Definere problemstilling, mål og foreløpig litteratursøk.
2.  **Fase 2: Prosjektplan (Pågår)**
    *   Utvikle styringsplan for omfang, fremdrift og ressurser.
    *   Starte formelt litteratursøk og teoribygging.
3.  **Fase 3: Gjennomføring & Review**
    *   3.1 Utarbeide teoretisk rammeverk og litteraturstudie.
    *   3.2 Datainnsamling og vask av bedriftsdata.
    *   3.3 Utvikling og trening av KI-prognosemodell.
    *   3.4 Utvikling av kapasitetsoptimeringsmodell.
    *   3.5 Analyse av resultater.
    *   3.6 Gjennomføre peer-to-peer review av en annen gruppes utkast.
4.  **Fase 4: Sluttrapport**
    *   4.1 Ferdigstille introduksjon.
    *   4.2 Skrive diskusjon og konklusjon.
    *   4.3 Finpuss av teori- og metodedel.
    *   4.4 Korrekturlesing og formatering (APA 7th).
    *   4.5 Innlevering.

## 3. Fremdrift
Detaljert tidsplan, arbeidsrekkefølge og kritisk sti er modellert og vedlagt i et eget MS Project Gantt-diagram. Prosjektet styres etter de fire obligatoriske fasene i LOG650, med følgende hovedmilepæler:

*   **Milepæl 1 (Fullført):** Godkjent prosjektbeskrivelse (Proposal).
*   **Milepæl 2 (16. mars):** Godkjent prosjektplan og etablert Referanseplan (Baseline) i MS Project.
*   **Milepæl 3 (27. april):** Godkjent hovedutkast til forskningsrapport og gjennomført peer-to-peer review.
*   **Milepæl 4 (31. mai):** Innlevering av endelig forskningsrapport.
*   **Milepæl 5 (Starten av juni):** Muntlig presentasjon av prosjektet.

**Kritisk sti:** Prosjektets kritiske sti går primært gjennom uthenting/vask av data og treningen av KI-modellen. Forsinkelser i disse oppgavene vil direkte forskyve arbeidet med resultatanalyse og ferdigstilling av rapporten.

## 4. Risiko og tiltak
*   **Risiko 1: Kompleks datainnsamling og datavask.**
    *   *Beskrivelse:* Data må hentes fra flere systemer (ERP M3, Qlik Sense) og i ulike formater (PDF, Excel). Å sammenstille og rense dette kan bli svært tidkrevende.
    *   *Tiltak:* Starte datavasken umiddelbart i fase 3. Bruke KI (Claude) aktivt for å skrive Python-skript (Pandas) som automatiserer formatering og sammenslåing av dataene.
*   **Risiko 2: Utfordringer med KI-koding og modellvalg.**
    *   *Beskrivelse:* Det kan ta lang tid å finne og programmere riktig kapasitets- og prognosemodell (f.eks. SARIMA).
    *   *Tiltak:* Starte med en enkel standardmodell (baseline) for å sjekke at dataflyten fungerer. Bruke Claude Code systematisk som sparringspartner for koding og feilsøking.
*   **Risiko 3: Konfidensialitet og sensitive data.**
    *   *Beskrivelse:* Modellen tar utgangspunkt i data fra en næringsmiddelbedrift.
    *   *Tiltak:* Anonymisere og transformere dataene fullstendig før bruk i prosjektet. Konkrete produktnavn maskeres, og volumer skaleres/transformeres slik at reelle bedriftshemmeligheter ikke avsløres og dataene ikke lenger kan knyttes til bedriften.

*   **Risiko 4: Ustrukturert litteratur- og referansehåndtering.**
    *   *Beskrivelse:* Tidkrevende å holde oversikt over kilder, noe som kan føre til feil i referanselisten (APA 7th).
    *   *Tiltak:* Etablere en fast rutine hvor alle leste artikler lagres som PDF i en egen mappe (003 references). KI brukes til å lage korte oppsummeringer av artiklene for å spare tid.

*   **Risiko 5: For høy modellkompleksitet i forhold til tid.**
    *   *Beskrivelse:* Ambisjonsnivået for kapasitets- og prognosemodellen overgår den tilgjengelige tiden i Fase 3, noe som kan forsinke den kritiske stien.
    *   *Tiltak:* Innføre streng tidsstyring ("timeboxing") på modelleringen. Sikre at en enkel minimumsløsning (baseline) bygges først for å garantere at prosessen fra data til resultat fungerer. Ytterligere kompleksitet legges kun til dersom tidsplanen tillater det.

## 5. Ressurser
*   **Prosjektteam og roller:** Davor Necemer gjennomfører prosjektet individuelt og innehar alle roller, inkludert prosjektleder, dataanalytiker og KI-utvikler.
*   **Sponsor:** Høgskolen i Molde v/faglærerne. De fungerer som prosjektets godkjenningsinstans for de fire fasene og setter endelig vurdering (Godkjent/Ikke godkjent).
*   **Kunde:** Prosjektet eies i praksis av studenten selv. Det tas utgangspunkt i et reelt, men fullstendig anonymisert og transformert datagrunnlag fra en næringsmiddelbedrift. Det er ingen formell bedriftstilknytning, og dermed ikke behov for taushetserklæring.
*   **Tekniske verktøy:** MS Project for fremdriftsstyring (Gantt og referanseplan), GitHub for versjonskontroll, VS Code med Python for datamodellering, og Claude Code som KI-assistent for programmering og rapportstøtte.

## 6. Kommunikasjon
*   **Plattformer:** Løpende dialog med faglærere/veiledere skjer via en egen tildelt gruppe-kanal på MS Teams. GitHub brukes for deling og versjonskontroll av kode og rapport.
*   **Veiledermøter:** Som prosjektleder tar du initiativ til veiledningsmøter ved behov. For å sikre effektivitet sendes en konkret agenda til veileder senest 24 timer i forkant, etterfulgt av en kort skriftlig oppsummering.
*   **Bedriftskontakt:** Det er ingen formell bedriftstilknytning, så det er ikke behov for eksterne statusmøter.

## 7. Kvalitet og Endringshåndtering
*   **Faglig kvalitetssikring:** Arbeidet vil kvalitetssikres løpende ved bruk av de offisielle sjekklistene i LOG650-kompendiet (for problemstilling, teori/metode og figurer/tabeller) for å sikre at C-kravet for fasene og B-kravet for sluttproduktet nås.
*   **Peer-to-peer review:** I slutten av fase 3 leveres et hovedutkast som skal vurderes av en medstudent. Tilbakemeldingene herfra brukes for å forbedre rapporten i avslutningsfasen.
*   **Teknisk validering:** All KI-generert kode gjennomgås kritisk. Modellen og resultatene skal valideres for å sikre at løsningen er robust og gir mening på det anonymiserte datagrunnlaget.
*   **Endringshåndtering:** Opprinnelig tidsplan lagres som en Referanseplan (Baseline) i MS Project. Avvik mellom faktisk fremdrift og referanseplanen vil bli sporet og dokumentert, og større endringer i scope tas opp med veileder.

