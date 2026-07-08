"""
data.py — Single source of truth loader.

Trials live in trials.json (edit that file, or use the Editor page).
This module loads them into Trial objects for the generator.
"""
from __future__ import annotations
import json
import os
from model import Trial

HERE = os.path.dirname(os.path.abspath(__file__))
JSON_PATH = os.path.join(HERE, "trials.json")


def load_trials():
    with open(JSON_PATH, encoding="utf-8") as f:
        raw = json.load(f)
    return [Trial.from_dict(d) for d in raw]


TRIALS = load_trials()
