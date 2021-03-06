import exportrecipe
import pathlib

PROJECT_DIR = pathlib.Path(__file__).parents[2]

config = exportrecipe.load(str(PROJECT_DIR / 'settings.json'))


# Django base settings
# https://docs.djangoproject.com/en/stable/ref/settings/

DEBUG = False
ROOT_URLCONF = 'voting.website.urls'
SECRET_KEY = config.secret_key
MEDIA_URL = '/media/'
MEDIA_ROOT = str(PROJECT_DIR / 'var/www/media')
STATIC_URL = '/static/'
STATIC_ROOT = str(PROJECT_DIR / 'var/www/static')
LANGUAGE_CODE = 'en'

INSTALLED_APPS = (
    'django.contrib.staticfiles',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.auth',
    'django.contrib.messages',
    'django.contrib.admin',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

TEMPLATE_CONTEXT_PROCESSORS = [
    'django.contrib.auth.context_processors.auth',
]
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': TEMPLATE_CONTEXT_PROCESSORS,
        }
    },
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'voting',
    }
}

MIGRATION_MODULES = {
    'account': 'voting.website.migrations.account',
    'website': 'voting.website.migrations.website',
    'openid': 'voting.website.migrations.openid',
    'socialaccount': 'voting.website.migrations.socialaccount',
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'stdout': {
            'format': (
                '%(levelname)s %(asctime)s %(module)s '
                '%(process)d %(thread)d %(message)s'
            ),
        },
        'console': {
            'format': '%(levelname)s %(module)s %(message)s',
        },
    },
    'handlers': {
        'stdout': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'stdout',
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'console',
        },
    },
    'loggers': {
        'django': {
            'propagate': True,
        },
    },
    'root': {
        'level': 'INFO',
        'handlers': ['console'],
    }
}


# Static assets, see config/assets.cfg
# https://pypi.python.org/pypi/hexagonit.recipe.download

STATICFILES_DIRS = (
    str(PROJECT_DIR / 'parts/jquery'),
    str(PROJECT_DIR / 'parts/bootstrap'),
    str(PROJECT_DIR / 'parts/requirejs'),
)


# django-ompressor settings
# https://pypi.python.org/pypi/django_compressor

INSTALLED_APPS += ('compressor',)
STATICFILES_FINDERS += ('compressor.finders.CompressorFinder',)

COMPRESS_PRECOMPILERS = (
    ('text/x-scss', 'django_libsass.SassCompiler'),
)


# django-debug-toolbar settings
# https://django-debug-toolbar.readthedocs.org/

INSTALLED_APPS += (
    'debug_toolbar',
)


# django-extensions
# http://django-extensions.readthedocs.org/

INSTALLED_APPS += (
    'django_extensions',
)


# django-nose
# https://pypi.python.org/pypi/django-nose

TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'

INSTALLED_APPS += (
    'django_nose',
)


# App settings

SERVER_PROTOCOL = 'http://'
SERVER_NAME = 'voting.pylab.lt'

SERVER_ALIASES = (
    'voting.pylab.lt',
    'www.voting.pylab.lt',
    'localhost',
    '127.0.0.1',
)

INSTALLED_APPS += (
    'voting.website',
    'voting.accounts',
)


# django-allauth
# http://django-allauth.readthedocs.org/

SITE_ID = 1
LOGIN_REDIRECT_URL = '/'
ACCOUNT_EMAIL_VERIFICATION = 'none'

SOCIALACCOUNT_AUTO_SIGNUP = False

ACCOUNT_SIGNUP_FORM_CLASS = 'voting.accounts.forms.SignupForm'

AUTHENTICATION_BACKENDS = (
    'allauth.account.auth_backends.AuthenticationBackend',
)

TEMPLATE_CONTEXT_PROCESSORS += [
    'django.template.context_processors.request',
    'allauth.socialaccount.context_processors.socialaccount',
]

INSTALLED_APPS += (
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.openid',
    'allauth.socialaccount.providers.persona',
    'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.facebook',
    'allauth.socialaccount.providers.linkedin',
    'allauth.socialaccount.providers.twitter',
    'allauth.socialaccount.providers.github',
)

SORTED_AUTH_PROVIDERS = (
    ('persona', STATIC_URL + 'auth/persona.png'),
    ('google', STATIC_URL + 'auth/google.png'),
    ('openid.yahoo', STATIC_URL + 'auth/yahoo.png'),
    ('facebook', STATIC_URL + 'auth/facebook.png'),
    ('linkedin', STATIC_URL + 'auth/linkedin.png'),
    ('twitter', STATIC_URL + 'auth/twitter.png'),
    ('github', STATIC_URL + 'auth/github.png'),
)

SORTED_OPENID_PROVIDERS = (
    dict(name='openid', url='', pattern=''),
    dict(name='lp', url='https://launchpad.net/~', pattern='https://launchpad.net/~%s'),
)

SOCIALACCOUNT_PROVIDERS = {
    'openid': {
        'SERVERS': [
            dict(id='google', name='Google', openid_url='https://www.google.com/accounts/o8/id'),
            dict(id='yahoo', name='Yahoo', openid_url='http://me.yahoo.com'),
        ],
    },
    'persona': {
        'AUDIENCE': '127.0.0.1',
    },
    'google': {
        'SCOPE': ['profile', 'email'],
        'AUTH_PARAMS': {
            'access_type': 'online',
        }
    },
    'facebook': {
        'SCOPE': ['email', 'public_profile'],
        'METHOD': 'oauth2',
        'VERIFIED_EMAIL': True,
        'VERSION': 'v2.3',
    },
    'linkedin': {
        'SCOPE': ['r_emailaddress'],
        'PROFILE_FIELDS': [
            'id',
            'first-name',
            'last-name',
            'email-address',
        ],
    },
}
