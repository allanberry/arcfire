from .base import *
import json

# Get config credentials from external source,
# outside of Git root for security.
secret = json.loads(Path(PROJ_DIR.parent, "arcfire_config.json").read_file())

SECRET_KEY = secret['SECRET_KEY']

ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1',
    '0.0.0.0'
]

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'arcfire',
        'USER': 'aljabear',
        'PASSWORD': secret['DATABASE_PASSWORD'],
        'HOST': '127.0.0.1',
        # 'PORT': '5432', #(using default)
        # 'TEST': {
        #     'NAME': 'arcfire_test'
        # }
    }
}

STATIC_URL = '/static/'
STATIC_ROOT =  PROJ_DIR.child('static')

MEDIA_URL  = '/media/'
MEDIA_ROOT =  '/Users/aljabear/Projects/arcfire_proj/media'

MEDIA_URL  = 'http://localhost:1917/media/'
UPLOAD_ROOT = MEDIA_ROOT + 'uploads/'

#email
EMAIL_HOST          = 'localhost'
EMAIL_PORT          = 1025
#EMAIL_HOST_USER     = '<mailbox>'
#EMAIL_HOST_PASSWORD = '<password>'
#DEFAULT_FROM_EMAIL  = '<address>'
#SERVER_EMAIL        = '<address>'