"""Base Django settings shared by all environments."""

from datetime import timedelta
import os
from pathlib import Path
import warnings

from dotenv import find_dotenv, load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent.parent

env_path = find_dotenv(filename=".env")
if env_path:
    load_dotenv(env_path)

SECRET_KEY = os.getenv("SECRET_KEY", "django-insecure-change-me")
DEBUG = os.getenv("DEBUG", "False") == "True"

ALLOWED_HOSTS = [
    host.strip()
    for host in os.getenv("DJANGO_ALLOWED_HOSTS", "127.0.0.1,localhost").split(",")
    if host.strip()
]

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "clients",
    "rest_framework",
    "rest_framework_simplejwt",
    "drf_spectacular",
    "accounts",
    "profiles",
    "education",
    "government_ids",
    "documents",
    "audit_logs",
    "core",
    "storages",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "navjivan.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "navjivan.wsgi.application"
ASGI_APPLICATION = "navjivan.asgi.application"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.getenv("POSTGRES_DB", "navjivan"),
        "USER": os.getenv("POSTGRES_USER", "postgres"),
        "PASSWORD": os.getenv("POSTGRES_PASSWORD", "postgres"),
        "HOST": os.getenv("DB_HOST", "localhost"),
        "PORT": os.getenv("DB_PORT", "5432"),
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

STATIC_URL = "static/"
STATIC_ROOT = BASE_DIR / "staticfiles"
STATICFILES_DIRS = [BASE_DIR / "static"]

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
AUTH_USER_MODEL = "accounts.User"

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ),
    "DEFAULT_PERMISSION_CLASSES": (
        "rest_framework.permissions.IsAuthenticated",
    ),
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
    "DEFAULT_THROTTLE_CLASSES": [
        "rest_framework.throttling.UserRateThrottle",
        "rest_framework.throttling.AnonRateThrottle",
    ],
    "DEFAULT_THROTTLE_RATES": {
        "user": os.getenv("DRF_THROTTLE_USER", "200/min"),
        "anon": os.getenv("DRF_THROTTLE_ANON", "20/min"),
    },
    "EXCEPTION_HANDLER": "core.exceptions.custom_exception_handler",
}

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=int(os.getenv("JWT_ACCESS_MINUTES", "15"))),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=int(os.getenv("JWT_REFRESH_DAYS", "7"))),
    "ALGORITHM": "HS256",
}

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": os.getenv("REDIS_URL", "redis://127.0.0.1:6379/1"),
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        },
    }
}

DEFAULT_FILE_STORAGE = os.getenv(
    "DEFAULT_FILE_STORAGE",
    "django.core.files.storage.FileSystemStorage",
)
AWS_S3_BUCKET_NAME = os.getenv("AWS_S3_BUCKET_NAME", "")
AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID", "")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY", "")
AWS_REGION = os.getenv("AWS_REGION", "us-east-1")

FIELD_ENCRYPTION_KEY = os.getenv(
    "FIELD_ENCRYPTION_KEY",
    "MDEyMzQ1Njc4OWFiY2RlZjAxMjM0NTY3ODlhYmNkZWY=",
)
if os.getenv("FIELD_ENCRYPTION_KEY") is None:
    warnings.warn(
        "FIELD_ENCRYPTION_KEY is not set. Using development fallback key; set a strong key in production."
    )

SPECTACULAR_SETTINGS = {
    "TITLE": "NavjivanCMS API",
    "DESCRIPTION": "Secure Digital Profile Vault",
    "VERSION": "1.0.0",
    "SERVE_INCLUDE_SCHEMA": False,
}

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "{levelname} {asctime} {module} {process:d} {thread:d} {message}",
            "style": "{",
        },
        "simple": {
            "format": "{levelname} {message}",
            "style": "{",
        },
    },
    "handlers": {
        "console": {
            "level": os.getenv("LOG_LEVEL", "INFO"),
            "class": "logging.StreamHandler",
            "formatter": "verbose",
        },
    },
    "root": {
        "handlers": ["console"],
        "level": os.getenv("LOG_LEVEL", "INFO"),
    },
    "loggers": {
        "django": {
            "handlers": ["console"],
            "level": os.getenv("DJANGO_LOG_LEVEL", "INFO"),
            "propagate": False,
        },
    },
}
