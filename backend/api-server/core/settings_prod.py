import os

DEBUG = True

ALLOWED_HOSTS = ["*"]

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = os.environ.get("EMAIL_HOST")
EMAIL_PORT = os.environ.get("EMAIL_PORT", 465)
EMAIL_USE_TLS = False
EMAIL_USE_SSL = True
EMAIL_HOST_USER = os.environ.get("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = os.environ.get("EMAIL_HOST_PASSWORD")
DEFAULT_FROM_EMAIL = os.environ.get("DEFAULT_FROM_EMAIL")

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "habits",
        "USER": os.environ.get("RDS_USERNAME"),
        "PASSWORD": os.environ.get("RDS_PASSWORD"),
        "HOST": os.environ.get("RDS_HOSTNAME"),
        "PORT": os.environ.get("RDS_PORT", "5432"),
    }
}
