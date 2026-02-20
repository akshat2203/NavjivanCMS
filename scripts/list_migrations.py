#!/usr/bin/env python3
"""
List Django migration files per app (except __init__.py). Useful to inspect which apps have migrations before cleanup.
Run from repo root: python3 scripts/list_migrations.py
"""
import os
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

print(f"Scanning migrations under: {ROOT}\n")

apps_with_migrations = []
for dirpath, dirnames, filenames in os.walk(ROOT):
    if os.path.basename(dirpath) == 'migrations':
        rel_app = Path(dirpath).relative_to(ROOT).parent
        migs = [f for f in filenames if f.endswith('.py') and f != '__init__.py']
        if migs:
            apps_with_migrations.append((str(rel_app), migs))

if not apps_with_migrations:
    print("No migration files found (except __init__.py)")
else:
    for app, migs in sorted(apps_with_migrations):
        print(f"App: {app}")
        for m in sorted(migs):
            print(f"  - {m}")
        print()

print("Done.")

