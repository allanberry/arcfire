from .base import *


ALLOWED_HOSTS = [
    '127.0.0.1',
]

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
STATIC_ROOT =  PROJ_DIR.child('static') # TODO

MEDIA_URL  = '/media/'
MEDIA_ROOT  =  PROJ_DIR.child('media') # TODO

MEDIA_URL  = 'http://localhost:8001/media/' # TODO
UPLOAD_ROOT = MEDIA_ROOT + 'uploads/'

#email
# EMAIL_HOST          = 'localhost'
# EMAIL_PORT          = 1025
#EMAIL_HOST_USER     = '<mailbox>'
#EMAIL_HOST_PASSWORD = '<password>'
#DEFAULT_FROM_EMAIL  = '<address>'
#SERVER_EMAIL        = '<address>'