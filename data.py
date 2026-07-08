"""
data.py — Single source of truth loader.

Loads trials.json PLUS any companion files named trials_*.json in this folder
(e.g. trials_tricuspid.json). This lets you keep a valve's trials in their own
file without touching the others. Add a new trials_<name>.json and it's picked
up automatically — no code changes needed.
"""
from __future__ import annotations
import glob
import json
import os
from model import Trial

HERE = os.path.dirname(os.path.abspath(__file__))


def _read(path):
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def load_trials():
    raw = []
    main = os.path.join(HERE, "trials.json")
    if os.path.exists(main):
        raw += _read(main)
    for path in sorted(glob.glob(os.path.join(HERE, "trials_*.json"))):
        raw += _read(path)          # e.g. trials_tricuspid.json
    return [Trial.from_dict(d) for d in raw]


TRIALS = load_trials()
