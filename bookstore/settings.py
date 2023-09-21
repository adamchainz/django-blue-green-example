import os
from pathlib import Path

# 1. Django Core Settings

# Dangerous: disable host header validation
ALLOWED_HOSTS = ["*"]

BASE_DIR = Path(__file__).resolve().parent.parent

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": "db.sqlite3",
    },
}

DEBUG = os.environ.get("DEBUG", "") == "1"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

INSTALLED_APPS = [
    "bookstore",
]

ROOT_URLCONF = "bookstore.urls"

SECRET_KEY = "django-insecure-5(bqk13ad%!09ze8g5baw(=(32st^hrltp-4q)_zb*&(9kz3#%"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
    },
]

USE_TZ = True
