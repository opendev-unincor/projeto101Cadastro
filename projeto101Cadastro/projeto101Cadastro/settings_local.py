from .settings import *

DEBUG = True
ALLOWED_HOSTS = ['*']
INTERNAL_IPS = ('127.0.0.1', 'localhost',)

INSTALLED_APPS += [     'debug_toolbar',
]

MIDDLEWARE = [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
] + MIDDLEWARE

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


AUTH_PASSWORD_VALIDATORS = []


EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

