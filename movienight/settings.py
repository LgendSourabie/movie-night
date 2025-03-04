"""
Django settings for movienight project.

Generated by 'django-admin startproject' using Django 3.2.5.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""
from datetime import timedelta
from pathlib import Path
from configurations import Configuration, values
import os

class Dev(Configuration):
        # Build paths inside the project like this: BASE_DIR / 'subdir'.
        BASE_DIR = Path(__file__).resolve().parent.parent

        # Quick-start development settings - unsuitable for production
        # See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

        # SECURITY WARNING: keep the secret key used in production secret!
        SECRET_KEY = "django-insecure-p5+$5*@#^f3t#1274_h^ro0jnjtfpncj^(mikp#9&eh^u^v4lw"

        # SECURITY WARNING: don't run with debug turned on in production!
        DEBUG = True

        ALLOWED_HOSTS = ["localhost", "0.0.0.0"]

        # Application definition

        INSTALLED_APPS = [
            "movienight_auth",
            "django.contrib.admin",
            "django.contrib.auth",
            "django.contrib.contenttypes",
            "django.contrib.sessions",
            "django.contrib.messages",
            "django.contrib.staticfiles",
            "django_registration",
            "crispy_forms",
            "crispy_bootstrap5",
            "movies",
            "rest_framework",
            "rest_framework.authtoken",
            'django_celery_results',
            'django_celery_beat',
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

        ROOT_URLCONF = "movienight.urls"

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

        WSGI_APPLICATION = "movienight.wsgi.application"

        # Database
        # https://docs.djangoproject.com/en/3.2/ref/settings/#databases

        DATABASES = {
            "default": {
                "ENGINE": "django.db.backends.sqlite3",
                "NAME": BASE_DIR / "db.sqlite3",
            }
        }

        # Password validation
        # https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
        # https://docs.djangoproject.com/en/3.2/topics/i18n/

        LANGUAGE_CODE = "en-us"

        TIME_ZONE = "UTC"

        USE_I18N = True

        USE_L10N = True

        USE_TZ = True

        # Static files (CSS, JavaScript, Images)
        # https://docs.djangoproject.com/en/3.2/howto/static-files/

        STATIC_URL = "/static/"

        # Default primary key field type
        # https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

        DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

        AUTH_USER_MODEL = "movienight_auth.User"

        CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
        CRISPY_TEMPLATE_PACK = "bootstrap5"

        EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

        ACCOUNT_ACTIVATION_DAYS = 7

        BASE_URL = "https://indigoguru-torchlucas-8000.codio.io"

        OMDB_KEY = "1efbd3d9"

        CELERY_RESULT_BACKEND = 'django-db'

        CELERY_BROKER_URL = "redis://localhost:6379/0"

        SIMPLE_JWT = {
            "ACCESS_TOKEN_LIFETIME": timedelta(days=1),
            "REFRESH_TOKEN_LIFETIME": timedelta(days=7),
        }

        REST_FRAMEWORK = {
            "DEFAULT_PERMISSION_CLASSES":[
             'rest_framework.permissions.IsAuthenticated',
            ],
            "DEFAULT_AUTHENTICATION_CLASSES":[
                'rest_framework.authentication.BasicAuthentication',
                'rest_framework.authentication.SessionAuthentication',
                'rest_framework.authentication.TokenAuthentication',
                'rest_framework_simplejwt.authentication.JWTAuthentication',
            ],
            "DEFAULT_PAGINATION_CLASS": 'rest_framework.pagination.PageNumberPagination',
             'PAGE_SIZE': 100,
        }
            
        

        LOGGING = {
                "version": 1,
                "disable_existing_loggers": False,
                "filters": {
                        "require_debug_false": {
                        "()": "django.utils.log.RequireDebugFalse",
                        },
                    },
                "formatters": {
                        "verbose": {
                        "format": "{levelname} {asctime} {module}{process:d} {thread:d} {message}",
                        "style": "{",
                         },
                    },
                "handlers": {
                        "console": {
                            "class": "logging.StreamHandler",
                            "stream": "ext://sys.stdout",
                            "formatter": "verbose",
                        },
                        "mail_admins": {
                            "level": "ERROR",
                            "class": "django.utils.log.AdminEmailHandler",
                            "filters": ["require_debug_false"],
                        },
                    },
                "loggers": {
                        "django.request": {
                            "handlers": ["mail_admins"],
                            "level": "ERROR",
                            "propagate": True,
                        },
                    },
                "root": {
                            "handlers": ["console"],
                            "level": "DEBUG",
                    },
            }


