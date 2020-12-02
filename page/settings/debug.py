import os

import page.globall as globall

# >>>
# Debug Setting Overrides
# >>>

ALLOWED_HOSTS = [
    "*",
]

# >>>
# Database
# >>>

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "OPTIONS": {},

        "HOST": "",
        "PORT": "",
        "NAME": "./db/db.db",
        "USER": "UpGrade",
        "PASSWORD": "SQL",
    }
}