#!/usr/bin/env bash
# Recreate migrations for all apps and apply them safely.
# Usage: from repo root run: bash scripts/recreate_migrations.sh
set -euo pipefail

echo "Making new migrations for all apps..."
python manage.py makemigrations --noinput

echo "Applying migrations..."
# If you're starting from existing DB with tables, you may want to run with --fake-initial
python manage.py migrate --noinput

echo "Migrations recreated and applied."

