"""Command line for CypherBench.

    python -m cypherbench list
    python -m cypherbench score SUBMISSION.json [--confirmed ID[,ID...]] [--json]
"""
from __future__ import annotations

import argparse
import json
import os
import sys

from . import checks


def cmd_list(_args) -> int:
    for cid in checks.ORDER:
        ch = checks.load_challenge(cid)
        print(f"{ch['order']}. {ch['title']}  [{cid}]")
        print(f"   {ch['size']}; {ch['status']} as of {ch['status_checked']}; check: {ch['verification']['type']}")
    return 0


def cmd_score(args) -> int:
    with open(args.submission, encoding="utf-8") as f:
        submission = json.load(f)
    confirmed = frozenset(x.strip() for x in (args.confirmed or "").split(",") if x.strip())
    unknown = confirmed - set(checks.ORDER)
    if unknown:
        sys.exit(f"unknown challenge id in --confirmed: {', '.join(sorted(unknown))}")
    base_dir = os.path.dirname(os.path.abspath(args.submission))
    results = checks.check_all(submission, base_dir, confirmed)
    solved, percent = checks.score(results)
    if args.json:
        print(json.dumps({"solver": submission.get("solver"), "solved": solved, "of": len(results), "score_percent": percent,
                          "challenges": [vars(r) for r in results]}, indent=2, ensure_ascii=False))
        return 0
    print(f"Solver: {submission.get('solver', 'unnamed')}\n")
    for r in results:
        title = checks.load_challenge(r.challenge)["title"]
        print(f"[{r.status.upper():^21}] {title}\n{'':24}{r.detail}")
        for name, text in r.parts.items():
            print(f"{'':24}{name}: {text}")
    print(f"\nScore: {solved} of {len(results)} solved = {percent}%")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(prog="python -m cypherbench", description="Check answers to the five CypherBench challenges.")
    sub = ap.add_subparsers(dest="command", required=True)
    sub.add_parser("list", help="show the five challenges").set_defaults(func=cmd_list)
    sc = sub.add_parser("score", help="check a submission and print its score")
    sc.add_argument("submission", help="path to a submission JSON file")
    sc.add_argument("--confirmed", help="comma-separated ids of challenges whose answer holder has confirmed the answer")
    sc.add_argument("--json", action="store_true", help="print the result as JSON")
    sc.set_defaults(func=cmd_score)
    args = ap.parse_args()
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
