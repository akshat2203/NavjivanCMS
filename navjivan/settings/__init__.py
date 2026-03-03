"""Environment-aware Django settings loader."""

import os

DJANGO_ENV = os.getenv("DJANGO_ENV", "development").lower()

if DJANGO_ENV == "production":
    from .production import *  # noqa: F403,F401
else:
    from .development import *  # noqa: F403,F401
