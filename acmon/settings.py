"""
Django settings for ACMon project.

For more information on this file, see
https://docs.djangoproject.com/

"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get("DEBUG") == 'TRUE'

SITE_URL = os.environ.get("SITE_URL")
FRONT_SITE_URL = os.environ.get("FRONT_SITE_URL")

ALLOWED_HOSTS = [os.environ.get("ALLOWED_HOSTS")]

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework.authtoken',
    'social_django',  # python social auth
    'colorfield',
    'corsheaders',
    'apps.accounts',
    'apps.tracking',
    'apps.car',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'acmon.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'acmon.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ.get("DB_NAME"),
        'USER': os.environ.get("DB_USER"),
        'PASSWORD': os.environ.get("DB_PASSWORD"),
        'HOST': os.environ.get("DB_HOST"),
        'PORT': os.environ.get("DB_PORT"),
    }
}

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = 'accounts.User'
LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/'


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'

# CORS settings
CORS_ORIGIN_ALLOW_ALL = os.environ.get("CORS_ORIGIN_ALLOW_ALL") == 'TRUE'
CORS_ORIGIN_WHITELIST = os.environ.get("CORS_ORIGIN_WHITELIST").split(" ")
CORS_ALLOW_HEADERS = os.environ.get("CORS_ALLOW_HEADERS").split(" ")
CORS_ALLOW_CREDENTIALS = False

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),

    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
    ),
}

# Authentication backends
# https://docs.djangoproject.com/en/1.10/ref/settings/#authentication-backends
# Here, we add two social authentication methods _above_ the default ModelBackend.
AUTHENTICATION_BACKENDS = (
    'social_core.backends.google.GoogleOAuth2',
    'social_core.backends.facebook.FacebookOAuth2',
    'django.contrib.auth.backends.ModelBackend',
)

# Set up social auth keys from the environment
# Why does this application need them, if the frontend is handling the entire
# OAuth2 process and we're just grabbing data from the social APIs using the
# access tokens? They're necessary for Python Social Auth to work properly,
# even if the application doesn't participate in the OAuth2 process.
for key in ['GOOGLE_OAUTH2_KEY',
            'GOOGLE_OAUTH2_SECRET',
            'FACEBOOK_KEY',
            'FACEBOOK_SECRET']:
    exec("SOCIAL_AUTH_{key} = os.environ.get('{key}', '')".format(key=key))

# We need to set at least the following scopes, to ensure that we can read
# basic profile details and email addresses.
# NB: These scopes are never actually used on the backend; things will work
# just fine if you omit these settings from the backend. However, the
# _frontend_ needs to be sure to send at least these scopes in order for the
# tokens to have enough permissions to get the user model updates / matching
# working properly.
SOCIAL_AUTH_FACEBOOK_SCOPE = os.environ.get("SOCIAL_AUTH_FACEBOOK_SCOPE").split(" ")
SOCIAL_AUTH_GOOGLE_OAUTH2_SCOPE = os.environ.get("SOCIAL_AUTH_GOOGLE_OAUTH2_SCOPE").split(" ")

# config per http://psa.matiasaguirre.net/docs/configuration/django.html#django-admin
SOCIAL_AUTH_ADMIN_USER_SEARCH_FIELDS = ['last_name', 'first_name', 'email']

# If this is not set, PSA constructs a plausible username from the first portion of the
# user email, plus some random disambiguation characters if necessary.
SOCIAL_AUTH_USERNAME_IS_FULL_EMAIL = os.environ.get("SOCIAL_AUTH_USERNAME_IS_FULL_EMAIL") == 'TRUE'

# define a custom social auth pipeline.
# The key thing here is to include email association. Both FB and Google
# only return validated user emails, so email validation is safe.
#
# Don't do this if you wish to use an OAuth2 provider which doesn't
# validate email addresses, as that opens up an attack vector.
# An attacker targeting one of your users might create an account with
# the OAuth2 provider, falsely claiming your user's email address as
# their own. Without validation, that provider can't know otherwise.
# They can then gain access to your user's account by logging in via
# that OAuth2 provider.
#
# See here for more details:
# http://psa.matiasaguirre.net/docs/use_cases.html#associate-users-by-email
SOCIAL_AUTH_PIPELINE = (
    'social_core.pipeline.social_auth.social_details',
    'social_core.pipeline.social_auth.social_uid',
    'social_core.pipeline.social_auth.auth_allowed',
    'social_core.pipeline.social_auth.social_user',
    'social_core.pipeline.user.get_username',
    'social_core.pipeline.social_auth.associate_by_email',  # <- this line not included by default
    'social_core.pipeline.user.create_user',
    'social_core.pipeline.social_auth.associate_user',
    'social_core.pipeline.social_auth.load_extra_data',
    'social_core.pipeline.user.user_details',
)
