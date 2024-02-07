import os

from dotenv import load_dotenv

from .base import *

load_dotenv()


DEBUG = True

ALLOWED_HOSTS = ["*"]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "HOST": os.environ.get("DB_HOST"),
        "NAME": os.environ.get("DB_NAME"),
        "USER": os.environ.get("DB_USER"),
        "PASSWORD": os.environ.get("DB_PASS"),
        "PORT": 5432,
    }
}

DEVELOPMENT_APPS = ["drf_spectacular"]

REST_FRAMEWORK["DEFAULT_SCHEMA_CLASS"] = "drf_spectacular.openapi.AutoSchema"

INSTALLED_APPS += DEVELOPMENT_APPS
