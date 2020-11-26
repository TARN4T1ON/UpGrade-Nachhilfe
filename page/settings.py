import os

import json
import mimetypes

from django.conf import settings

# @TODO: comment

#global

proot = os.path.realpath(
    os.path.dirname(
        os.path.dirname(__file__)
    )
)
root = os.path.realpath(
    os.path.dirname(__file__)
)

url = "localhost"
port = 8000

separator = " :: "

#main

SECRET_KEY = "01234567890987654321"
DEBUG = False

BASE_DIR = root

ALLOWED_HOSTS = ["*"]

INSTALLED_APPS = [
    "page.apps.pageConfig",

    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
]

#pages

ROOT_URLCONF = "page.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            os.path.join(
                root,
                "views"
            ),
            os.path.join(
                root,
                "views/user"
            ),
        ],
        "APP_DIRS": False,
    }
]

#sessions

SESSION_COOKIE_NAME = "session"

#database

#@TODO: dev sqlite db

DATABASE_CONFIG = open(
    os.path.join(
        proot,
        "db",
        "connection.json"
    )
)
DATABASE_CONN = json.load(DATABASE_CONFIG)
DATABASE_CONFIG.close()

DATABASE = {}
if DEBUG:
    for key in DATABASE_CONN["DEVELOPMENT"]:
        value = DATABASE_CONN["DEVELOPMENT"][key]

        if value == None:
            try:
                value = DATABASE_CONN["DEFAULT"][key]
            except:
                continue

            if value == None:
                continue

        DATABASE[key] = value
else:
    pass

DATABASES = {
    "default": DATABASE
}

#user

PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
    'django.contrib.auth.hashers.Argon2PasswordHasher',
    'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
]

#static files

STATIC_URL = "/static/"

STATIC_ROOT = os.path.join(
    root, 
    "_static"
)

STATICFILES_DIRS = [
    os.path.join(
        root,
        "static"
    ),
]

#mimetypes

mimetypes.add_type(
    "text/html", 
    ".html", 
    True
)
mimetypes.add_type(
    "text/css", 
    ".css", 
    True
)
mimetypes.add_type(
    "x-icon", 
    ".ico", 
    True
)
mimetypes.add_type(
    "image/png", 
    ".png", 
    True
)
mimetypes.add_type(
    "text/javascript", 
    ".js", 
    True
)
mimetypes.add_type(
    "text/json", 
    ".json", 
    True
)

#media files

MEDIA_URL = "/media/"