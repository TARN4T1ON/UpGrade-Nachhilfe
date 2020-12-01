import os

import page.globall as globall

# >>>
# Debug Setting Overrides
# >>>

ALLOWED_HOSTS = [
    "*",
]

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "file": {
            "level": "DEBUG",
            "class": "logging.FileHandler",
            "filename": os.path.join(
                globall.root,
                "log",
                "debug.log"
            )
        }
    },
    "loggers": {
        "django": {
            "handlers": [
                "file"
            ],
            "level": "DEBUG",
            "propagate": True
        }
    },
}

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