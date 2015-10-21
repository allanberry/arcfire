from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = Path(PROJ_DIR, "_key.secret").read_file()

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
        'PASSWORD': Path(PROJ_DIR, "_db_pass.secret").read_file(),
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