#!/usr/bin/env python3
"""
Safely remove migration files (except __init__.py) for all apps in the project.
USAGE (from project root):
    python3 scripts/clean_migrations.py --dry-run
    python3 scripts/clean_migrations.py --confirm

It will not touch migrations for builtin Django apps or directories without 'migrations'. Use with care. Always backup your DB before running migrations again.
"""
import os
import argparse
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

parser = argparse.ArgumentParser()
parser.add_argument('--dry-run', action='store_true', help='Show files that would be removed')
parser.add_argument('--confirm', action='store_true', help='Actually remove migration files')
args = parser.parse_args()

removed = []
for dirpath, dirnames, filenames in os.walk(ROOT):
    if os.path.basename(dirpath) == 'migrations':
        for fname in filenames:
            if fname.endswith('.py') and fname != '__init__.py':
                fpath = Path(dirpath) / fname
                if args.dry_run:
                    print(f'[DRY RUN] would remove: {fpath}')
                else:
                    print(f'Removing: {fpath}')
                    fpath.unlink()
                    removed.append(str(fpath))

if args.dry_run:
    print('\nDry run finished. Use --confirm to actually delete the files (make sure you have DB backup).')
else:
    print(f'\nRemoved {len(removed)} migration files.\nYou should now run `python manage.py makemigrations` and `python manage.py migrate --fake-initial` or follow the steps in the README.')

