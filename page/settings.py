import os

from django.conf import settings
import mimetypes

#global

root = os.path.realpath(os.path.dirname(__file__))

url = "localhost"
port = 8000

#main

SECRET_KEY = "0"
DEBUG = True

BASE_DIR = root

ALLOWED_HOSTS = ["*"]

INSTALLED_APPS = [
    "django.contrib.staticfiles",
]

#pages

ROOT_URLCONF = "page.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            os.path.join(
                root,
                "views/front"
            ),
        ],
        "APP_DIRS": False,
    }
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