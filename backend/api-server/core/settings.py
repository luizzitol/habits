from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Default to production environment
# Add DEPLOYMENT_ENVIRONMENT=dev to run in development mode
DEPLOYMENT_ENVIRONMENT = os.environ.get("DEPLOYMENT_ENVIRONMENT", "dev")

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "dummy-secret-key"
AUTH_USER_MODEL = "accounts.User"

# Application definition
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    "allauth.headless",
    "allauth.usersessions",
    "allauth.socialaccount.providers.dummy",
    "accounts",
    "ninja_demo",
    "projects",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "allauth.account.middleware.AccountMiddleware",
]

ROOT_URLCONF = "core.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "static")],
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

WSGI_APPLICATION = "core.wsgi.application"

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = "static/"

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

AUTHENTICATION_BACKENDS = ("allauth.account.auth_backends.AuthenticationBackend",)

ACCOUNT_USER_MODEL_USERNAME_FIELD = None
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = "mandatory"
ACCOUNT_LOGIN_METHODS = {"email"}
ACCOUNT_LOGOUT_ON_PASSWORD_CHANGE = False
ACCOUNT_LOGIN_BY_CODE_ENABLED = True
ACCOUNT_EMAIL_VERIFICATION_BY_CODE_ENABLED = True
ACCOUNT_SIGNUP_FIELDS = ["email*", "password1*", "password2*"]

HEADLESS_ONLY = True
HEADLESS_FRONTEND_URLS = {
    "account_confirm_email": "/account/verify-email/{key}",
    "account_reset_password": "/account/password/reset",
    "account_reset_password_from_key": "/account/password/reset/key/{key}",
    "account_signup": "/account/signup",
    "socialaccount_login_error": "/account/provider/callback",
}
HEADLESS_SERVE_SPECIFICATION = True

DEBUG = True
ALLOWED_HOSTS = ["*"]

if DEPLOYMENT_ENVIRONMENT == "prod":
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
else:
    EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
    EMAIL_HOST = "mail"
    EMAIL_PORT = 1025
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
        }
    }
    #crfs trusted origins
    CSRF_TRUSTED_ORIGINS = ["http://localhost:3000", "http://localhost:10000"]
