
from pathlib import Path
from dotenv import load_dotenv
from os import environ
load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent


try:
    SECRET_KEY = environ["SECRET_KEY"]
    DEBUG = environ["DEBUG"]
except KeyError as e:
    raise RuntimeError("Could not find a SECRET_KEY in environment") from e


ALLOWED_HOSTS = [".tarjuman.tech"]

if DEBUG : 
    ALLOWED_HOSTS.append('*')

INSTALLED_APPS = [
    "main",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
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

ROOT_URLCONF = "Tarjuman.urls"

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

WSGI_APPLICATION = "Tarjuman.wsgi.application"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": environ['DBNAME'],
        "USER": environ['DBUSER'],
        "PASSWORD": environ['DBPASS'],
        "HOST": environ['DBHOST'],
        "PORT": environ['DBPORT'],
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

#* Static Files Management 
STATICFILES_DIRS = [BASE_DIR / "static"]  
STATIC_URL = "static/"
STATIC_ROOT = '/var/www/tarjuman.tech/static'

#* Media Files Management 
MEDIA_URL = "media/"
if DEBUG : 
    MEDIA_ROOT = BASE_DIR / 'media'
MEDIA_ROOT = '/var/www/tarjuman.tech/media'


DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"