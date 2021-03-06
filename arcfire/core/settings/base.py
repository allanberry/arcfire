import os
import json
from unipath import Path
from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS as TCP
import datetime

# arcfire_proj/arcfire/
BASE_DIR =  Path(__file__).ancestor(3)
# arcfire_proj
PROJ_DIR = BASE_DIR.parent


# Get config credentials from external source,
# outside of Git root for security.
secret = json.loads(Path(PROJ_DIR.parent, "arcfire_config.json").read_file())

SECRET_KEY = secret['SECRET_KEY']

DEBUG = False

STATICFILES_DIRS = (BASE_DIR.child('arcfire').child('static'),)


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.humanize',
    'django.contrib.messages',
    'django.contrib.sessions',
    'django.contrib.staticfiles',
    #'compressor',
    'django_extensions',
    'gunicorn',
    'rest_framework',
    'coverage',
    # 'floppyforms',
    # 'haystack',
    'arcfire',
]

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    # 'compressor.finders.CompressorFinder',
)

# COMPRESS_PRECOMPILERS = (
#     ('text/scss', 'sass --scss {infile} {outfile}'),
# )

# COMPRESS_JS_FILTERS = [
#     'compressor.filters.template.TemplateFilter',
#     'compressor.filters.jsmin.JSMinFilter',
# ]

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'arcfire.context_processors.arcfire_global_context',
            ],
        },
    },
]

WSGI_APPLICATION = 'core.wsgi.application'



# Password validation
# https://docs.djangoproject.com/en/dev/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/dev/topics/i18n/

LANGUAGE_CODE = 'en-us'

USE_I18N = True
USE_L10N = True

# Time zone support for these stories would just add unnecessary complexity.
# TIME_ZONE = 'UTC'
# USE_TZ = False


REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ]
}

DEFAULT_TIME = datetime.datetime.now()
