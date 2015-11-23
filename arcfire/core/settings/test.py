from .base import *


ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1',
    '0.0.0.0'
]

DEBUG = True

# If debug is enabled, Compressor is turned off; # this will manually activate
# it.  This is important to provide Django tags (like 'static') to JS files
# COMPRESS_ENABLED = False

# However, in development, we had better override the JSMinFilter
COMPRESS_JS_FILTERS = [
    'compressor.filters.template.TemplateFilter',
    # 'compressor.filters.jsmin.JSMinFilter',
]


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'arcfire_test',
        'USER': 'aljabear',
        'PASSWORD': secret['DATABASE_PASSWORD'],
        'HOST': '127.0.0.1',

        # 'PORT': '5432', #(using default)
        # 'TEST': {
        #     'NAME': 'arcfire_test'
        # }
    }
}

STATIC_URL  = '/static/'
STATIC_ROOT =  PROJ_DIR.child('static')

MEDIA_URL   = '/media/'
MEDIA_ROOT  =  PROJ_DIR.child('media').child('test')

MEDIA_URL   = 'http://localhost:1917/media/'
UPLOAD_ROOT = MEDIA_ROOT + 'uploads/'

#email
EMAIL_HOST          = 'localhost'
EMAIL_PORT          = 1025
#EMAIL_HOST_USER     = '<mailbox>'
#EMAIL_HOST_PASSWORD = '<password>'
#DEFAULT_FROM_EMAIL  = '<address>'
#SERVER_EMAIL        = '<address>'
