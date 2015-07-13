# pylint: disable=wildcard-import,unused-wildcard-import

from voting.settings.base import *  # noqa

DEBUG = False

ALLOWED_HOSTS = ['localhost']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'pylab',
        'USER': 'pylab',
    }
}

LOGGING['root'] = {
    'level': 'WARNING',
    'handlers': ['stdout'],
}
