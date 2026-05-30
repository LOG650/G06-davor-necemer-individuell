# Fase 4 — handoff for neste chat (BØR-gruppe 2)

**Du leser dette + `Fase_4_kickoff.md` først.** Frisk kontekst for å spare tokens.
Forrige økt brukte mye kontekst; derfor byttes det chat her ved en ren commit-grense.

## Status akkurat nå (committet, pushet)

Aktiv branch: `Fase_4_report`. Siste commit: **`fdf0a6f`** (= origin).

**Ferdig fra BØR-lista (verifisert mot faktisk fil + `model_run_summary.json`):**
- #5 Innledning — faglig bidrag løftet til §1.0; smoke-test-ramme i §1.1. (commit `c417590`)
- #6 Modellvalg S — RMSE-begrunnelse i §7.2 (konveks kostnadsstruktur; S vinner kun
  på RMSE 6.67<7.53, taper MAE 5.15<6.17 og MAPE 60.2%<76.0%). (`c417590`)
- #9 (delvis) — §1.4 Antagelse 3 justert som biprodukt av #11. **Selve §1.3-funnet
  gjenstår** (se under).
- #10 LP smoke-test-framing — §8.4 overskrift + lead. (`fdf0a6f`)
- #11 Sensitivitet-metode — §5.1.2 skiller ramme vs. faktisk kjørt. (`fdf0a6f`)

## Gjenstår på BØR — DENNE GRUPPENS JOBB

Rekkefølge anbefalt (resultatdelen er nå ærlig/konsistent, så syntese kan skrives trygt):

1. **#8 Konklusjon (§10)** — restrukturer i tre eksplisitte bolker:
   "Utviklet og testet teknisk" / "Dokumentert med data" / "Gjenstår før operativ bruk".
   Stoffet finnes allerede spredt i §10 (Hovedfunn + Begrensninger + Gjenstående arbeid);
   dette er hovedsakelig omstrukturering, ikke nyskriving. ~20 min.
2. **#7 Diskusjon (§9.2/§9.4 + §9.3)** — to funn:
   (a) eksplisitt gap-avsnitt: ukentlig modell vs. dagsvise/sonevise frister, foreslå
       videreutvikling med dag/sone-data. Naturlig i §9.4 (eller slutten av §9.2).
   (b) utvid §9.3 "Modellens tiltenkte verdi"-listen til et fullt avsnitt om
       proaktiv-vs-reaktiv-skiftet (ukesplanlegging). ~40 min.
3. **#9 Metode §1.3 (Aggregeringsnivå)** — reformuler avgrensningen til
   "praktisk forenkling med kjent kostnad — dagsvis modellering ligger utenfor scope
   men er kritisk for operativ bruk". NB: §1.3-overskriften i fila heter "1.3 Avgrensinger"
   (linje ~155), og første kulepunkt er "**Aggregeringsnivå – fra dag/sone til uke:**"
   (linje ~157). Det finnes IKKE noen dobbel overskrift (det var en hallusinasjon i en
   tidligere økt — ignorer slike spor). ~15 min.

**KAN om tid (karakter-relevant tross "KAN"):**
- #13 — flytt/kopier teoretisk-hull-poenget fra §9.4 opp til §2.3 (slutten), fordi
  vurderingskriteriene eksplisitt etterspør diskusjon av teoretiske hull. ~15 min.

## Ekte tall (fasit = `004 data/processed/model_run_summary.json`)

| Strøm | SNaive MAE/RMSE/MAPE | SARIMAX MAE/RMSE/MAPE | Beslutning |
|---|---|---|---|
| F | 12.88 / 18.96 / 24.4% | 8.18 / 13.21 / 16.3% | SARIMAX slår på alle tre |
| S | 5.15 / 7.53 / 60.2% | 6.17 / 6.67 / 76.0% | SARIMAX kun på RMSE → tolkes varsomt |

LP indeks-smoke-test: 0.00 ekstra indeks-timer, 0.00 slack (skala-artefakt, ikke
kapasitetsmargin — se §8.4 brødtekst). Soneandeler Z1=0.325, Z2=0.335, Z3=0.339.
Basekapasitet P1=24 t/uke, P2=144 t/uke. Prosess-tid P1=0.003885, P2=0.037555 min/FPK.

## VIKTIG arbeidsdisiplin (lærdom fra forrige økt)

- **Les den FAKTISKE fila før hver Edit.** En tidligere økt jobbet mot hallusinert
  innhold (placeholder-kommentarer, dobbel "## Avgrensninger", RMSE-tall 9.36/9.95 —
  ALT FALSKT). Alle de redigeringene feilet. Ikke stol på gjenkalt/oppsummert tekst —
  åpne fila.
- **Eksakt-streng Edit** på unik, nettopp-lest tekst.
- **Commit via fil**, ikke PowerShell here-string: skriv melding til `COMMIT_MSG_tmp.txt`,
  `git commit -F COMMIT_MSG_tmp.txt`, slett fila etterpå. (Here-strings med linjer som
  starter med `#` ble tolket som pathspecs av PowerShell 5.1 og feilet to ganger.)
- **Verifiser med adversarisk workflow** etter redigering: 3 linser (tall / metode↔
  resultat-konsistens / nye-selvmotsigelser) som leser faktisk fil + JSON-fasit.
  Bruk `agentType: 'Explore'`. Dette fanget feilmodusen sist.

## Bygg PDF + commit

```
python "005 report/scripts/build_report_pdf_latex.py" --output "014 fase 4 - report/Sluttrapport_Volumprognose-Kapasitetsanalyse_DavorNecemer_endelig.pdf"
```
Verifiser exit 0 og "Wrote PDF". Oppdater status i `012 fase 2 - plan/status.md` OG
`014 fase 4 - report/G05_INTEGRATION_PLAN.md` som del av commiten (ikke før).

## Ikke gjør

- Ikke skann `000 templates/`. Ikke endre `013 fase 3 - review/` (frosset).
- Ikke prøv G05s top-3 (reell-skala LP, fristkapasitet-kalibrering, full
  sensitivitetsanalyse) — de er bevisst dokumentert som "gjenstår" i §8.5/§9.4/§10.
- Ikke merge til main før hele fase 4 er ferdig.

## Frist

Innlevering 31.05.2026. Muntlig presentasjon 05.06.2026.
