from os import getenv
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = getenv("SECRET_KEY")

ALLOWED_HOSTS = ["localhost"]

BASE_DIR = Path(__file__).resolve().parent.parent

DEBUG = True

DEVELOPED_APPS = ["users"]

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest_framework",
    "drf_spectacular",
    *DEVELOPED_APPS,
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

ROOT_URLCONF = "teams.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
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

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": getenv("DATABASE_NAME"),
        "USER": getenv("DATABASE_USER"),
        "PASSWORD": getenv("DATABASE_PASSWORD"),
        "HOST": "localhost",
        "PORT": 5432,
    }
}

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

STATIC_URL = "static/"

STATIC_ROOT = "static/"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

REST_FRAMEWORK = {
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
}

WSGI_APPLICATION = "teams.wsgi.application"

USE_TZ = True

SPECTACULAR_SETTINGS = {
    "TITLE": "Teams manager",
    "DESCRIPTION": "A project which goal is to help organize one's teams.",
    "VERSION": "0.1.0",
    "SERVE_INCLUDE_SCHEMA": False,
}

AUTH_USER_MODEL = "users.User"
