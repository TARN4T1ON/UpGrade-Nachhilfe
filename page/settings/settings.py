import os

import secrets

import mimetypes

from django.conf import settings

import page.globall as globall

# >>>
# Main
# >>>

# generate secret key during runtime
SECRET_KEY = secrets.token_hex(64)
DEBUG = True

if DEBUG:
    from page.settings.debug import *
else:
    from page.settings.production import *

BASE_DIR = globall.page

INSTALLED_APPS = [
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

MIDDLEWARE = [
    "django.middleware.common.CommonMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
]

# >>>
# Pages
# >>>

ROOT_URLCONF = "page.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            os.path.join(
                globall.page,
                "views/templates"
            ),
        ],
        "APP_DIRS": False,
    }
]

APPEND_SLASH = True

# >>>
# Sessions
# >>>

SESSION_COOKIE_NAME = "session"

# >>>
# Database
# >>>

# DATABASE_CONFIG = open(
#     os.path.join(
#         root,
#         "db",
#         "connection.json"
#     )
# )
# DATABASE_CONN = json.load(DATABASE_CONFIG)
# DATABASE_CONFIG.close()

# DATABASE = {}
# DATABASE_KEY: str
# if DEBUG:
#     DATABASE_KEY = "DEVELOPMENT"
# else:
#     DATABASE_KEY = "PRODUCTION"

# for key in DATABASE_CONN["DEVELOPMENT"]:
#     value = DATABASE_CONN["DEVELOPMENT"][key]

#     if value == None:
#         try:
#             value = DATABASE_CONN["DEFAULT"][key]
#         except:
#             continue

#         if value == None:
#             continue

#     DATABASE[key] = value

# >>>
# User
# >>>

AUTHENTICATION_BACKENDS = [
    "page.model.auth.email"
]

PASSWORD_HASHERS = [
    "django.contrib.auth.hashers.PBKDF2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher",
    "django.contrib.auth.hashers.Argon2PasswordHasher",
    "django.contrib.auth.hashers.BCryptSHA256PasswordHasher",
]

# >>>
# Static files
# >>>

STATIC_URL = "/static/"

STATIC_ROOT = os.path.join(
    globall.page, 
    "_static"
)

STATICFILES_DIRS = [
    os.path.join(
        globall.page,
        "static"
    ),
]

# >>>
# MIME types
# >>>

# used for debug server static file serving

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