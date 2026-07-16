#!/usr/bin/env python3
"""
audit.py — check EVERY trial in one pass:
  (1) does the stored primary DOI/PMID look correct?  and
  (2) which follow-up / subanalysis papers is it MISSING?

Ground truth is PubMed's registry link: `NCT<number>[si]` returns exactly the papers
whose authors declared that trial registration. For each trial we compare that set to
what you already have (its primary PMID + everything in `key_papers`) and report:

  primary_status:
    OK          - stored PMID is among the trial's registered papers
    OK?         - has a PMID but no NCT to cross-check against
    CHECK       - stored PMID is NOT among the registered papers (verify it!)
    NO_PRIMARY  - no DOI/PMID stored at all
  missing[]     - registered papers not yet stored (each scored HIGH/MED/LOW + kind)

Report only; never edits data. Live fetch needs internet (CI/local). Logic is
unit-tested offline with a fake client (`--selftest`).
"""
from __future__ import annotations

import json
import os
import sys

from pubmed_linker import Trial, PubMedClient, score_candidate
from proposer import _load_all


def _trial_from_row(row: dict) -> Trial:
    return Trial(acronym=row.get("acronym", ""), nct=row.get("nct", ""),
                 authors=row.get("authors", ""), journal=row.get("journal", ""),
                 year=row.get("year", ""), device=row.get("device", ""),
                 valve=row.get("valve", ""), disease=row.get("disease", ""),
                 procedure=row.get("procedure", ""), sample_size=row.get("sample_size", ""))


def audit_row(row: dict, client) -> dict:
    nct = row.get("nct", "")
    stored_pmid = row.get("pmid", "")
    stored_doi = row.get("doi", "")
    existing = {stored_pmid} | {p.get("pmid", "") for p in row.get("key_papers", [])}
    existing.discard("")

    registered = []
    if nct:
        ids = client.esearch(f"{nct}[si]", retmax=40)
        registered = client.efetch(ids) if ids else []

    if not stored_pmid and not stored_doi:
        primary, note = "NO_PRIMARY", "no DOI/PMID stored"
    elif registered:
        reg = {c.pmid for c in registered if c.pmid}
        if stored_pmid and stored_pmid not in reg:
            primary = "CHECK"
            note = f"stored PMID {stored_pmid} not among NCT-registered ({', '.join(sorted(reg)) or 'none'})"
        else:
            primary, note = "OK", ""
    else:
        primary = "OK?" if stored_pmid else "NO_PRIMARY"
        note = "" if nct else "no NCT to cross-check against"

    trial = _trial_from_row(row)
    missing = []
    for c in registered:
        if not c.pmid or c.pmid in existing:
            continue
        sc = score_candidate(trial, c)
        missing.append({"pmid": c.pmid, "doi": c.doi, "confidence": sc["confidence"],
                        "kind": sc["kind"], "title": c.title})
    return {"acronym": row.get("acronym", ""), "nct": nct,
            "primary_status": primary, "primary_note": note, "missing": missing}


def audit_store(store: dict, client, only_issues=True) -> list:
    out = []
    for _f, rows in store.items():
        for row in rows:
            if row.get("status") != "published":
                continue
            r = audit_row(row, client)
            if only_issues and r["primary_status"] in ("OK", "OK?") and not r["missing"]:
                continue
            out.append(r)
    return out


def print_report(reports: list, checked: int) -> None:
    n_check = sum(1 for r in reports if r["primary_status"] == "CHECK")
    n_noprim = sum(1 for r in reports if r["primary_status"] == "NO_PRIMARY")
    n_missing = sum(len(r["missing"]) for r in reports)
    print(f"# Trial audit — {checked} published trials checked")
    print(f"Flagged: {len(reports)} | primary needs CHECK: {n_check} | "
          f"missing a primary: {n_noprim} | missing follow-up papers: {n_missing}\n")
    for r in reports:
        head = f"## {r['acronym']}  (NCT {r['nct'] or '-'})  — primary: {r['primary_status']}"
        print(head)
        if r["primary_note"]:
            print(f"   ! {r['primary_note']}")
        for m in r["missing"]:
            print(f"   + MISSING [{m['confidence']:6s} {m['kind']:11s}] PMID {m['pmid']}"
                  f"  doi:{m['doi'] or '-'}\n       {m['title'][:80]}")
        print()


def _cli():
    import argparse
    ap = argparse.ArgumentParser(description="Audit every trial's primary link and follow-ups.")
    ap.add_argument("--selftest", action="store_true")
    ap.add_argument("--files", nargs="*", default=["trials.json", "trials_tricuspid.json"])
    ap.add_argument("--all", action="store_true", help="show every trial, not just flagged ones")
    args = ap.parse_args()
    if args.selftest:
        return _selftest()
    store = _load_all(args.files)
    checked = sum(1 for rows in store.values() for r in rows if r.get("status") == "published")
    client = PubMedClient(api_key=os.environ.get("NCBI_API_KEY"))
    reports = audit_store(store, client, only_issues=not args.all)
    print_report(reports, checked)
    return 0


def _selftest() -> int:
    from pubmed_linker import Candidate

    class FakeClient:
        """Pretends NCT03904147 has 3 registered papers; others have none."""
        REG = {
            "NCT03904147": [
                Candidate(pmid="36876753", title="Transcatheter Repair for Tricuspid Regurgitation",
                          authors=["Sorajja P"], journal="N Engl J Med", year="2023",
                          pubtypes=["randomized controlled trial"], nct_accessions=["NCT03904147"]),
                Candidate(pmid="40159089", title="Two-Year Outcomes: TRILUMINATE Pivotal",
                          authors=["Kar S"], journal="Circulation", year="2025",
                          pubtypes=["multicenter study"], nct_accessions=["NCT03904147"]),
                Candidate(pmid="99999999", title="Imaging Substudy of the TRILUMINATE Pivotal Trial",
                          authors=["Cavalcante J"], journal="JACC", year="2025",
                          pubtypes=["multicenter study"], nct_accessions=["NCT03904147"]),
            ],
        }

        def esearch(self, term, retmax=40):
            nct = term.split("[")[0]
            return [c.pmid for c in self.REG.get(nct, [])]

        def efetch(self, ids):
            flat = [c for lst in self.REG.values() for c in lst]
            return [c for c in flat if c.pmid in ids]

    store = {"trials_tricuspid.json": [
        # correct primary, but MISSING the imaging substudy (99999999)
        {"acronym": "TRILUMINATE Pivotal", "status": "published", "nct": "NCT03904147",
         "doi": "10.1056/NEJMoa2300525", "pmid": "36876753",
         "key_papers": [{"pmid": "40159089"}]},
        # WRONG primary PMID for this NCT -> should be flagged CHECK
        {"acronym": "Bad Primary", "status": "published", "nct": "NCT03904147",
         "doi": "", "pmid": "11111111", "key_papers": []},
        # fully correct + nothing missing -> should NOT be flagged
        {"acronym": "Clean", "status": "published", "nct": "NCT00000000",
         "doi": "10.1/clean", "pmid": "22222222", "key_papers": []},
    ]}
    reports = audit_store(store, FakeClient(), only_issues=True)
    by = {r["acronym"]: r for r in reports}

    ok = True
    # TRILUMINATE flagged with the missing imaging substudy
    t = by.get("TRILUMINATE Pivotal")
    cond1 = t and any(m["pmid"] == "99999999" for m in t["missing"]) and t["primary_status"] == "OK"
    # Bad Primary flagged CHECK
    cond2 = by.get("Bad Primary", {}).get("primary_status") == "CHECK"
    # Clean not flagged at all
    cond3 = "Clean" not in by
    for name, c in [("missing follow-up detected", cond1),
                    ("wrong primary flagged CHECK", cond2),
                    ("clean trial not flagged", cond3)]:
        print(f"[{'PASS' if c else 'FAIL'}] {name}")
        ok = ok and c
    print_report(reports, checked=3)
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(_cli())
