from pathlib import Path
from dotenv import load_dotenv
from os import environ

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent


try:
    SECRET_KEY = environ["SECRET_KEY"]
    DEBUG = environ["DEBUG"] == "True"
    GEOPOSITION_GOOGLE_MAPS_API_KEY = GOOGLE_MAPS_API_KEY = environ["GOOGLE_MAPS"]
except KeyError as e:
    raise RuntimeError("Could not find a SECRET_KEY in environment") from e


ALLOWED_HOSTS = [".turjman.site"]
CSRF_TRUSTED_ORIGINS = ["https://turjman.site", "https://www.turjman.site"]

if DEBUG:
    ALLOWED_HOSTS.append("*")

INSTALLED_APPS = [
    "main",
    "user",
    "admin_interface",
    "django_google_maps",
    "colorfield",
    "django_summernote",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sites",
    "django.contrib.sitemaps",
    "django_unused_media",
    "api",
    "rest_framework",
    "rest_framework.authtoken",
]

SITE_ID = 1

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

SUMMERNOTE_CONFIG = {
    "summernote": {
        "lang": "ar-AR",
    },
    "toolbar": [
        ["style", ["style"]],
        ["font", ["bold", "underline", "clear"]],
        ["fontname", ["fontname"]],
        ["color", ["color"]],
        ["para", ["ul", "ol", "paragraph"]],
        ["table", ["table"]],
        ["insert", ["link", "picture", "video"]],
        ["insert", ["ltr", "rtl"]],
        ["view", ["fullscreen", "codeview", "help"]],
    ],
    "js": ("/static/assets/js/summernote-ext-rtl.js",),
}

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
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
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

REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
    )
}

X_FRAME_OPTIONS = "SAMEORIGIN"
SILENCED_SYSTEM_CHECKS = ["security.W019"]

LANGUAGE_CODE = "ar-EG"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

# * Static Files Management
STATICFILES_DIRS = [BASE_DIR / "static"]
STATIC_URL = "static/"
STATIC_ROOT = "/home/hushm/Turjman/www/static"

# * Media Files Management
MEDIA_URL = "media/"
MEDIA_ROOT = "/home/hushm/Turjman/www/media"
if DEBUG:
    MEDIA_ROOT = BASE_DIR / "media"

CRISPY_TEMPLATE_PACK = "bootstrap4"


DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

LOGIN_REDIRECT_URL = "dashboard"
LOGOUT_REDIRECT_URL = "home"

EMAIL_HOST = "localhost"
EMAIL_PORT = 1025
