from .base import *


ALLOWED_HOSTS = [
    'arcfire.allanberry.com',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'arcfire',
        'USER': 'admin_pg',
        'PASSWORD': secret['DATABASE_PASSWORD'],
        'HOST': '127.0.0.1',

        # 'PORT': '5432', #(using default)
        'TEST': {
            'NAME': 'arcfire_test'
        }
    }
}

STATIC_URL  = 'http://static.arcfire.allanberry.com/'
STATIC_ROOT =  PROJ_DIR.parent.parent.child('arcfire_static')

MEDIA_URL   = 'http://static.arcfire.allanberry.com/media/'
MEDIA_ROOT  = STATIC_ROOT.child('media')
UPLOAD_ROOT = MEDIA_ROOT.child('uploads')

#email
# EMAIL_HOST          = 'localhost'
# EMAIL_PORT          = 1025
#EMAIL_HOST_USER     = '<mailbox>'
#EMAIL_HOST_PASSWORD = '<password>'
#DEFAULT_FROM_EMAIL  = '<address>'
#SERVER_EMAIL        = '<address>'
