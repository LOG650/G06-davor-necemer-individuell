"""
Genererer strukturerte prosjektstyringsfiler for LOG650-prosjektet:
  core.json, requirements.json, risk.json, schedule.json, wbs.json, project-plan.md, status.md
"""

import json
import os
from datetime import date

OUTPUT_DIR = os.path.dirname(os.path.abspath(__file__))
TODAY = "2026-04-26"


# ─────────────────────────────────────────────
# DATA
# ─────────────────────────────────────────────

CORE = {
    "project_id": "LOG650-G06-IND",
    "name": "Integrert volumprognose og kapasitetsanalyse",
    "course": "LOG650",
    "institution": "Høgskolen i Molde",
    "owner": "Davor Necemer",
    "status": "delayed",
    "start_date": "2026-01-12",
    "deadline_report": "2026-05-29",
    "deadline_presentation": "2026-06-05",
    "description": (
        "Datadrevet kapasitetsmodell for et anonymisert norsk næringsmiddelmiljø. "
        "To parallelle varestrømmer (ferskvare og sekundær/handelsvare) samles i et "
        "felles distribusjonsledd med faste daglige cut-off-frister. "
        "Målet er å minimere ekstra kapasitetsbruk og unngå fristbrudd ved hjelp av "
        "volumpronoser og en kapasitetsoptimeringsmodell."
    ),
    "approach": "Kvantitativ, casebasert studieoppgave",
    "tools": ["Python", "Microsoft Project", "Word/Markdown", "GitHub", "VS Code"],
}


REQUIREMENTS = [
    {
        "id": "R01",
        "category": "data",
        "description": "Bygge på relevante historiske virksomhetsdata (min. 2 år, ukentlig volum)",
        "priority": "must",
        "status": "open",
    },
    {
        "id": "R02",
        "category": "forecasting",
        "description": "Bruke volumprognoser som input til kapasitetsanalysen",
        "priority": "must",
        "status": "open",
    },
    {
        "id": "R03",
        "category": "capacity",
        "description": "Analysere behov for ekstra kapasitet i tre produksjonsledd",
        "priority": "must",
        "status": "open",
    },
    {
        "id": "R04",
        "category": "capacity",
        "description": "Inkludere faste distribusjonsfrister (sonevise cut-offs) som rammebetingelser",
        "priority": "must",
        "status": "open",
    },
    {
        "id": "R05",
        "category": "documentation",
        "description": "Dokumentere analysen slik at fremgangsmåte og vurderinger er etterprøvbare",
        "priority": "must",
        "status": "open",
    },
    {
        "id": "R06",
        "category": "reporting",
        "description": "Levere sluttrapport og kildekode som grunnlag for muntlig presentasjon",
        "priority": "must",
        "status": "open",
    },
    {
        "id": "R07",
        "category": "data",
        "description": "Anonymisere og transformere bedriftsdata – ingen personopplysninger",
        "priority": "must",
        "status": "open",
    },
    {
        "id": "R08",
        "category": "model",
        "description": "Gjennomføre scenarioanalyse for sensitivitetstesting av modellens robusthet",
        "priority": "should",
        "status": "open",
    },
]


RISKS = [
    {
        "id": "RK01",
        "title": "Kompleks datainnsamling og datavask",
        "description": (
            "Data må hentes fra flere systemer og i ulike formater, "
            "noe som kan gjøre sammenstilling og rensing tidkrevende."
        ),
        "probability": "high",
        "impact": "high",
        "status": "active",
        "mitigation": "Starte datavask tidlig og bruke skript/verktøy for å effektivisere arbeidet.",
    },
    {
        "id": "RK02",
        "title": "Utfordringer med modellvalg og modellutvikling",
        "description": (
            "Det kan ta tid å finne og utvikle en hensiktsmessig "
            "prognose- og kapasitetsmodell."
        ),
        "probability": "medium",
        "impact": "high",
        "status": "active",
        "mitigation": "Starte med en enkel baseline-løsning og utvikle modellen trinnvis.",
    },
    {
        "id": "RK03",
        "title": "Konfidensialitet og sensitive bedriftsdata",
        "description": (
            "Prosjektet bygger på data fra en næringsmiddelbedrift – "
            "feil håndtering kan føre til personvern- eller forretningsproblemer."
        ),
        "probability": "low",
        "impact": "high",
        "status": "mitigated",
        "mitigation": "Anonymisere og transformere datagrunnlaget før analyse og rapportering.",
    },
    {
        "id": "RK04",
        "title": "Ustrukturert litteratur- og referansehåndtering",
        "description": (
            "Svak oversikt over kilder kan føre til feil i referanseliste og teorigrunnlag."
        ),
        "probability": "medium",
        "impact": "medium",
        "status": "active",
        "mitigation": (
            "Lagre relevante kilder systematisk i «003 references» "
            "og oppdatere bibliografien fortløpende."
        ),
    },
    {
        "id": "RK05",
        "title": "For høy modellkompleksitet i forhold til tid",
        "description": (
            "Ambisjonsnivået i modelleringen kan bli for høyt "
            "i forhold til prosjektets rammer og frister."
        ),
        "probability": "high",
        "impact": "high",
        "status": "active",
        "mitigation": (
            "Prioritere en gjennomførbar minimumsløsning først "
            "og utvide bare dersom tidsplanen tillater det."
        ),
    },
]


SCHEDULE = {
    "project": "Integrert volumprognose og kapasitetsanalyse",
    "baseline_date": "2026-03-16",
    "status_date": TODAY,
    "phases": [
        {
            "id": "F1",
            "name": "Fase 1: Initiering",
            "start": "2026-01-12",
            "end": "2026-02-24",
            "status": "completed",
            "tasks": [
                {"id": "1.1", "name": "Utvikle første utkast", "duration_days": 29,
                 "start": "2026-01-12", "end": "2026-02-19", "status": "completed"},
                {"id": "1.2", "name": "Levere første utkast", "duration_days": 0,
                 "start": "2026-02-19", "end": "2026-02-19", "milestone": True, "status": "completed"},
                {"id": "1.3", "name": "Vente på tilbakemelding fra veileder", "duration_days": 1,
                 "start": "2026-02-20", "end": "2026-02-20", "status": "completed"},
                {"id": "1.4", "name": "Revidere proposal", "duration_days": 1,
                 "start": "2026-02-23", "end": "2026-02-23", "status": "completed"},
                {"id": "1.5", "name": "Levere revidert versjon", "duration_days": 1,
                 "start": "2026-02-24", "end": "2026-02-24", "status": "completed"},
                {"id": "1.6", "name": "Milepæl: Godkjent prosjektbeskrivelse", "duration_days": 0,
                 "start": "2026-02-24", "end": "2026-02-24", "milestone": True, "status": "completed"},
            ],
        },
        {
            "id": "F2",
            "name": "Fase 2: Prosjektplan",
            "start": "2026-02-24",
            "end": "2026-03-16",
            "status": "completed",
            "tasks": [
                {"id": "2.1", "name": "Utvikle styringsplan og risikoanalyse", "duration_days": 9,
                 "start": "2026-02-25", "end": "2026-03-09", "status": "completed"},
                {"id": "2.2", "name": "Bygge WBS og Gantt i MS Project", "duration_days": 5,
                 "start": "2026-03-10", "end": "2026-03-16", "status": "completed"},
                {"id": "2.3", "name": "Starte formelt litteratursøk", "duration_days": 10,
                 "start": "2026-02-25", "end": "2026-03-10", "status": "partial",
                 "note": "Kun 1 referanse funnet i repo"},
                {"id": "2.4", "name": "Milepæl: Godkjent prosjektplan", "duration_days": 0,
                 "start": "2026-03-16", "end": "2026-03-16", "milestone": True, "status": "completed"},
            ],
        },
        {
            "id": "F3",
            "name": "Fase 3: Gjennomføring & Review",
            "start": "2026-03-16",
            "end": "2026-05-08",
            "status": "delayed",
            "tasks": [
                {"id": "3.1", "name": "Utarbeide teoretisk rammeverk", "duration_days": 8,
                 "start": "2026-03-17", "end": "2026-03-26", "status": "delayed",
                 "days_late": 31, "note": "Kun 1 metodologi-ref. Mangler forecasting & capacity refs."},
                {"id": "3.2", "name": "Datainnsamling og vask av bedriftsdata", "duration_days": 8,
                 "start": "2026-03-17", "end": "2026-03-26", "status": "not_started",
                 "days_late": 31, "note": "KRITISK: 004 data/ mappen er tom"},
                {"id": "3.3", "name": "Utvikling og trening av KI-prognosemodell", "duration_days": 10,
                 "start": "2026-03-27", "end": "2026-04-09", "status": "not_started",
                 "days_late": 17, "note": "Avhenger av 3.2"},
                {"id": "3.4", "name": "Utvikling av kapasitetsoptimeringsmodell", "duration_days": 11,
                 "start": "2026-04-10", "end": "2026-04-24", "status": "not_started",
                 "days_late": 2, "note": "Avhenger av 3.2 og 3.3"},
                {"id": "3.5", "name": "Analyse av resultater", "duration_days": 5,
                 "start": "2026-04-27", "end": "2026-05-01", "status": "not_started",
                 "note": "Avhenger av 3.3 og 3.4"},
                {"id": "3.6", "name": "Gjennomføre peer-to-peer review", "duration_days": 5,
                 "start": "2026-05-04", "end": "2026-05-08", "status": "not_started"},
                {"id": "3.7", "name": "Milepæl: Godkjent hovedutkast", "duration_days": 0,
                 "start": "2026-05-08", "end": "2026-05-08", "milestone": True, "status": "not_started"},
            ],
        },
        {
            "id": "F4",
            "name": "Fase 4: Sluttrapport",
            "start": "2026-05-08",
            "end": "2026-06-05",
            "status": "not_started",
            "tasks": [
                {"id": "4.1", "name": "Ferdigstille introduksjon", "duration_days": 4,
                 "start": "2026-05-11", "end": "2026-05-14", "status": "not_started"},
                {"id": "4.2", "name": "Skrive diskusjon og konklusjon", "duration_days": 6,
                 "start": "2026-05-15", "end": "2026-05-22", "status": "not_started"},
                {"id": "4.3", "name": "Finpuss, kvalitetssikring og APA 7th", "duration_days": 5,
                 "start": "2026-05-25", "end": "2026-05-29", "status": "not_started"},
                {"id": "4.4", "name": "Milepæl: Innlevering av rapport og kode", "duration_days": 0,
                 "start": "2026-05-29", "end": "2026-05-29", "milestone": True, "status": "not_started"},
                {"id": "4.5", "name": "Forberede og gjennomføre muntlig presentasjon",
                 "duration_days": 5, "start": "2026-06-01", "end": "2026-06-05", "status": "not_started"},
            ],
        },
    ],
}


WBS = {
    "project": "Integrert volumprognose og kapasitetsanalyse",
    "deliverables": [
        {
            "id": "WBS-1",
            "name": "Initiering og proposal",
            "description": "Første utkast og revidert proposal levert og godkjent",
            "work_packages": [
                {"id": "WBS-1.1", "name": "Utarbeide problemstilling og scope"},
                {"id": "WBS-1.2", "name": "Definere målfunksjon og avgrensninger"},
                {"id": "WBS-1.3", "name": "Revidere etter tilbakemelding"},
            ],
        },
        {
            "id": "WBS-2",
            "name": "Prosjektplanlegging og risikoanalyse",
            "description": "Prosjektstyringsplan, Gantt og risikoregister",
            "work_packages": [
                {"id": "WBS-2.1", "name": "Prosjektstyringsplan (scope, mål, budsjett, interessenter)"},
                {"id": "WBS-2.2", "name": "WBS og Gantt-plan i MS Project"},
                {"id": "WBS-2.3", "name": "Risikoregister med tiltak"},
            ],
        },
        {
            "id": "WBS-3",
            "name": "Litteratursøk og teoretisk rammeverk",
            "description": "Relevant litteratur om prognoser, kapasitetsplanlegging og optimering",
            "work_packages": [
                {"id": "WBS-3.1", "name": "Søk etter litteratur om etterspørselsprognoser"},
                {"id": "WBS-3.2", "name": "Søk etter litteratur om kapasitetsplanlegging"},
                {"id": "WBS-3.3", "name": "Skriv teoretisk rammeverk"},
            ],
        },
        {
            "id": "WBS-4",
            "name": "Datainnsamling og datavask",
            "description": "Historiske volumdata og kampanjekalender klargjort for analyse",
            "work_packages": [
                {"id": "WBS-4.1", "name": "Hente historiske volumdata (min. 2 år)"},
                {"id": "WBS-4.2", "name": "Hente kampanjekalender"},
                {"id": "WBS-4.3", "name": "Standardisere til FPK-ekvivalenter"},
                {"id": "WBS-4.4", "name": "Datavask og anonymisering"},
            ],
        },
        {
            "id": "WBS-5",
            "name": "Prognosemodellering",
            "description": "Tidsserie- eller ML-modell for ukentlig volumprognose",
            "work_packages": [
                {"id": "WBS-5.1", "name": "Velge og begrunne prognosemodell (ARIMA, ETS, ML)"},
                {"id": "WBS-5.2", "name": "Trene og validere modell"},
                {"id": "WBS-5.3", "name": "Dokumentere prognosefeil og modellvalg"},
            ],
        },
        {
            "id": "WBS-6",
            "name": "Kapasitetsmodell og analyse",
            "description": "Optimeringsmodell for ekstra kapasitet og produksjonsstart",
            "work_packages": [
                {"id": "WBS-6.1", "name": "Definere optimeringsmål og beslutningsvariabler"},
                {"id": "WBS-6.2", "name": "Implementere kapasitetsoptimeringsmodell"},
                {"id": "WBS-6.3", "name": "Kjøre analyse og tolke resultater"},
                {"id": "WBS-6.4", "name": "Scenarioanalyse og sensitivitetstesting"},
            ],
        },
        {
            "id": "WBS-7",
            "name": "Review, kvalitetssikring og sluttrapport",
            "description": "Peer-review, finpuss og ferdigstilt rapport",
            "work_packages": [
                {"id": "WBS-7.1", "name": "Peer-to-peer review av hovedutkast"},
                {"id": "WBS-7.2", "name": "Skrive introduksjon, diskusjon og konklusjon"},
                {"id": "WBS-7.3", "name": "Finpuss, APA 7th og sluttkontroll"},
            ],
        },
        {
            "id": "WBS-8",
            "name": "Innlevering og muntlig presentasjon",
            "description": "Rapport og kode levert, presentasjon gjennomført",
            "work_packages": [
                {"id": "WBS-8.1", "name": "Innlevering av rapport og kode (29.05.26)"},
                {"id": "WBS-8.2", "name": "Forberede presentasjon"},
                {"id": "WBS-8.3", "name": "Gjennomføre muntlig presentasjon (01–05.06.26)"},
            ],
        },
    ],
}


# ─────────────────────────────────────────────
# STATUS.MD
# ─────────────────────────────────────────────

def build_status_md():
    lines = [
        "# Prosjektstatus – Integrert volumprognose og kapasitetsanalyse",
        "",
        f"**Dato:** {TODAY}  ",
        "**Prosjektleder:** Davor Necemer  ",
        "**Dager til innlevering:** 33 (29.05.2026)",
        "",
        "---",
        "",
        "## Sammendrag",
        "",
        "| Fase | Status |",
        "|------|--------|",
        "| Fase 1: Initiering | ✅ Fullført |",
        "| Fase 2: Prosjektplan | ✅ Fullført |",
        "| Fase 3: Gjennomføring | 🔴 Forsinket |",
        "| Fase 4: Sluttrapport | 🔴 Ikke startet |",
        "",
        "---",
        "",
        "## Aktivitetsoversikt",
        "",
    ]

    STATUS_ICON = {
        "completed": "✅",
        "partial": "⚠️",
        "delayed": "⚠️",
        "not_started": "🔴",
        "in_progress": "🔵",
    }

    for phase in SCHEDULE["phases"]:
        lines.append(f"### {phase['name']}")
        lines.append("")
        lines.append("| ID | Aktivitet | Planlagt slutt | Status | Merknad |")
        lines.append("|----|-----------|----------------|--------|---------|")
        for t in phase["tasks"]:
            icon = STATUS_ICON.get(t["status"], "❓")
            label = t["status"].replace("_", " ").capitalize()
            days_late = f" ({t['days_late']} d forsinket)" if "days_late" in t else ""
            note = t.get("note", "")
            lines.append(
                f"| {t['id']} | {t['name']} | {t['end']} "
                f"| {icon} {label}{days_late} | {note} |"
            )
        lines.append("")

    lines += [
        "---",
        "",
        "## Kritiske risikoer akkurat nå",
        "",
        "1. **RK01 – Datainnsamling:** `004 data/` er tom. Blokkerer 3.3, 3.4, 3.5.",
        "2. **RK05 – Modellkompleksitet:** 33 dager igjen – prioriter minimumsløsning.",
        "3. **RK02 – Modellvalg:** Velg enkel baseline-modell raskt.",
        "",
        "## Prioriterte tiltak",
        "",
        "| Prioritet | Tiltak |",
        "|-----------|--------|",
        "| 🚨 Kritisk | Start datainnsamling (3.2) UMIDDELBART |",
        "| ⚠️ Høy | Ferdigstill litteratursøk og rammeverk (3.1) |",
        "| ⚠️ Høy | Start prognosemodell parallelt med datavask (3.3) |",
        "| Medium | Kapasitetsmodell når data er klart (3.4) |",
        "",
    ]
    return "\n".join(lines)


# ─────────────────────────────────────────────
# PROJECT-PLAN.MD
# ─────────────────────────────────────────────

def build_project_plan_md():
    return f"""# Prosjektplan – {CORE['name']}

**Emne:** {CORE['course']} – {CORE['institution']}
**Student:** {CORE['owner']}
**Start:** {CORE['start_date']} | **Innlevering:** {CORE['deadline_report']} | **Presentasjon:** {CORE['deadline_presentation']}

---

## Problemstilling

{CORE['description']}

---

## Mål

Utvikle en datadrevet modell som minimerer samlet bruk av ekstra kapasitet og reduserer
risikoen for fristbrudd i et næringsmiddeldistribusjonsmiljø med faste daglige cut-off-frister.

---

## WBS – Arbeidsnedbrytningsstruktur

| ID | Leveranse |
|----|-----------|
""" + "\n".join(
        f"| {d['id']} | {d['name']} |"
        for d in WBS["deliverables"]
    ) + """

---

## Milepæler

| Dato | Milepæl |
|------|---------|
| 24.02.2026 | ✅ Godkjent prosjektbeskrivelse |
| 16.03.2026 | ✅ Godkjent prosjektplan |
| 08.05.2026 | 🔴 Godkjent hovedutkast |
| 29.05.2026 | 🔴 Innlevering av rapport og kode |
| 01–05.06.2026 | 🔴 Muntlig presentasjon |

---

## Kritisk linje

Datainnsamling (3.2) → Prognosemodell (3.3) → Kapasitetsmodell (3.4) → Analyse (3.5) → Rapport (Fase 4)

---

## Risikoer (topp 3)

| ID | Risiko | Sannsynlighet | Konsekvens |
|----|--------|--------------|------------|
| RK01 | Datainnsamling og datavask | Høy | Høy |
| RK02 | Modellvalg og utvikling | Medium | Høy |
| RK05 | Modellkompleksitet vs. tid | Høy | Høy |
"""


# ─────────────────────────────────────────────
# WRITE FILES
# ─────────────────────────────────────────────

def write_json(filename, data):
    path = os.path.join(OUTPUT_DIR, filename)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"  Skrevet: {filename}")


def write_md(filename, content):
    path = os.path.join(OUTPUT_DIR, filename)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"  Skrevet: {filename}")


def main():
    print(f"Genererer prosjektstyringsfiler i: {OUTPUT_DIR}\n")

    write_json("core.json", CORE)
    write_json("requirements.json", {"requirements": REQUIREMENTS})
    write_json("risk.json", {"risks": RISKS})
    write_json("schedule.json", SCHEDULE)
    write_json("wbs.json", WBS)
    write_md("status.md", build_status_md())
    write_md("project-plan.md", build_project_plan_md())

    print("\nFullfort. Genererte filer:")
    for f in ["core.json", "requirements.json", "risk.json",
              "schedule.json", "wbs.json", "status.md", "project-plan.md"]:
        print(f"  012 fase 2 - plan/{f}")


if __name__ == "__main__":
    main()
