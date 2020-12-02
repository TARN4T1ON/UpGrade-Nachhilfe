import page.globall as globall

# >>>
# Production Setting Overrides
# >>>

ALLOWED_HOSTS = [
    globall.url,
    "upgrade.cringe.one",
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