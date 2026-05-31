# Fase 4 - handoff for morgenokt 2026-06-01

**Les denne + `Fase_4_kickoff.md` forst.** Denne fila erstatter eldre sluttvask-handoff.
Stol alltid pa `git log` og `git status`, ikke eldre hash-notater.

## Status akkurat na

- Dato/tid ved handoff: 2026-05-31 ca. 23:16.
- Frist: **mandag 2026-06-01 kl. 14:00** i WISEflow.
- Aktiv branch: `Fase_4_report`.
- Siste rapport-/PDF-endrende commit: `61e6142` - `fase4: juster sluttlesingsfunn`.
- Det kan ligge en senere ren status-/handoff-commit pa toppen av branch.
- `main` er **ikke** merget enna. Ikke merge til `main` for final-PDF er lest og godkjent.

For oppstart:

```powershell
git fetch origin --prune
git log --oneline -8
git status --short --branch
```

Forventet status etter fetch:

- `HEAD -> Fase_4_report, origin/Fase_4_report` pa siste pushede commit.
- Rapport-/PDF-baseline er fortsatt `61e6142` dersom det bare er status-/handoff-commit etter den.
- Kun lokale/uversjonerte ting utenfor commit: `.claude/settings.local.json`, `.codex/review/*` og `000 templates/*`.
- Disse skal ikke committes eller leveres.

## Final-PDF akkurat na

Final-PDF:

`014 fase 4 - report/Sluttrapport_Volumprognose-Kapasitetsanalyse_DavorNecemer_endelig.pdf`

Teknisk verifisert etter siste build:

- 36 sider.
- A4 pa alle sider (`595.28 x 841.89 pt`).
- Forsiden sier 36 sider.
- `Bruk av KI-verktøy` starter pa egen side etter obligatoriske erklaeringer og nevner Claude/Claude Code + Codex.
- `Datatilgjengelighet og reproduserbarhet` starter sammen med tilhorende tekst.
- Tabell 2 caption og tabell er samlet.
- Tabell 10 star samlet pa egen side.
- Vedlegg J starter pa neste side og kan splittes over siste side.

Bygg pa nytt ved endringer:

```powershell
python "005 report/scripts/build_report_pdf_latex.py"
```

Scriptet bygger na som default til fase 4-finalen og bruker A4.

## Siste endringer som er lukket

Review-fourth / sluttvask-punkter som na er lukket:

- **NSD/Sikt:** Teksten sier `Nei` etter avklaring med veileder. Rapporten presiserer at innlevert/publisert materiale er anonymisert/aggregerte data uten personopplysninger.
- **A4:** PDF er bygget i A4, ikke US Letter.
- **Sone/cut-off og SLACK:** Sprak dempet. `SLACK` omtales som udekket aggregert arbeidsbelastning/kapasitetsmangel, ikke dokumentert sonevist fristbrudd.
- **Prosess-tid-konfidensialitet:** Rapporten sier at aggregerte prosess-tidsrater inngar; reelle volum, kunde-/produktdetaljer og kostnader inngar ikke.
- **Teoretisk hull:** Dempet til case-spesifikt metodisk bidrag.
- **S-modellen:** RMSE-basert minimumskjoring, med SNaive som konservativ operativ fallback.
- **NNN/SSB:** NNN-navn/tittel rettet. SSB oppdatert til 2026/tabell 12439 og source note lagt i `003 references`.
- **Vedlegg F-I:** Forklart som lokale genererte kontrollfiler som ikke folger med dersom innleveringen bare er PDF.
- **Vedlegg/GitHub:** Rapporten sier at publiserbare kode-, rapport- og referanseartefakter ligger i GitHub, mens sensitive/lokale filer ikke deles.
- **Qlik:** Rettet til `Qlik Sense`.
- **KI:** Codex lagt til i KI-verktøy-seksjonen.

## Morgendagens anbefalte rekkefolge

1. **Kort ny review hvis ønsket.**
   - Bruk kun rapport/PDF/kode/referanser, ikke `000 templates/` med mindre bruker eksplisitt ber om det.
   - Prioriter bare reelle blokkerende funn. Ikke start store refaktorer.
2. **Menneskelig sluttlesing av PDF.**
   - Forside, obligatoriske erklaeringer, KI-seksjon, sammendrag/abstract.
   - Tabell 2, Figur 2, Tabell 10, Vedlegg J.
   - Sjekk at SLACK/sonefrist-sprak ikke overselger operativ fristmodell.
3. **Eventuelle siste mikrofiks pa `Fase_4_report`.**
   - Bygg PDF.
   - Verifiser A4, 36/evt. nytt sidetall, og sideflyt.
   - Commit og push bare relevante filer.
4. **Nar PDF er godkjent:**
   - Merge `Fase_4_report` til `main`.
   - Push `main`.
   - Lever kun final-PDF i WISEflow.
5. **GitHub-opprydding etter innlevering / etter godkjent final:**
   - Gjor repoet oversiktlig for veileder fordi GitHub kan bli last etter fristen.
   - Ikke slett eller flytt noe som kan endre den leverte rapportens sporbarhet rett for innlevering.
   - Ikke legg inn sensitive lokale data.

## GitHub-opprydding - forslag etter final

Dette bor vente til PDF er levert eller finalen er helt godkjent:

- Oppdater `README.md` hvis den er utdatert, med kort prosjektoversikt og peker til final-PDF.
- Sjekk at `003 references/` har ryddige README/LINKS/source notes.
- Sjekk at `004 data/` kun inneholder publiserbare filer som skal ligge i repo.
- La `000 templates/`, `.codex/review/` og `.claude/settings.local.json` forbli utenfor commit.
- Ikke rydd ved a slette historikk eller gjore destruktive git-kommandoer.

## Ikke gjor

- Ikke les/skann `000 templates/` rutinemessig.
- Ikke endre `013 fase 3 - review/`.
- Ikke commit `.claude/settings.local.json`, `.codex/review/` eller `000 templates/`.
- Ikke merge til `main` for bruker sier at PDF er endelig godkjent.
- Ikke lever eller zip hele workspace. WISEflow-leveranse er final-PDF.

## Muntlig forsvar - husk

Hvis sensor spør om LP/SLACK:

- Denne rapportversjonen viser en teknisk integrasjon SARIMAX -> LP pa publiserbar indeks-skala.
- `SLACK` i smoke-testen er udekket aggregert arbeidsbelastning, ikke dokumentert sonevist fristbrudd.
- Operativ fristmodell krever reell FPK-skala, dags-/soneniva og kalibrert `CAP_deadline`.

Hvis sensor spør om NSD/Sikt:

- Veileder har avklart at `NSD/Sikt = Nei` er korrekt for innlevert/publisert materiale.
- Rapporten publiserer bare anonymiserte og aggregerte data uten personopplysninger.
