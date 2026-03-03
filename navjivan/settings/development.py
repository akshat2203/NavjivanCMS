"""Local development settings."""

import os

from .base import *  # noqa: F403,F401

DEBUG = True
ALLOWED_HOSTS = ["*"]

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

# Local dev fallback: use sqlite when USE_SQLITE=True
if os.getenv("USE_SQLITE", "False") == "True":
    DATABASES = {  # noqa: F405
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",  # noqa: F405
        }
    }
