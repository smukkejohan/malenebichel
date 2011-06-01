# coding=utf-8
import os.path
import sys
import platform

BASE_PATH = os.path.dirname(os.path.abspath(__file__))
ROOT_URLCONF = 'urls'

sys.path.append(BASE_PATH + '/apps')

PRODUCTION_HOSTNAME = "tango"

ADMINS = (
    ('Johan Bichel Lindegaard', 'sysadmin@tango.johan.cc'),
)
MANAGERS = ADMINS

DEVELOPMENT_MODE = (platform.node() != PRODUCTION_HOSTNAME)
if DEVELOPMENT_MODE:
    DEBUG = True
    MEDIA_URL = '/media/'
    STATIC_URL = '/static/'
else:
    DEBUG = False
    MEDIA_URL = 'http://static.malenebichel.dk/uploads/'
    STATIC_URL = 'http://static.malenebichel.dk/'
    ADMIN_MEDIA_PREFIX = STATIC_URL + 'admin/'

TEMPLATE_DEBUG = DEBUG

# Static files
MEDIA_ROOT = BASE_PATH + '/static/uploads'
STATICFILES_DIRS = (
    BASE_PATH + '/static',
)

TIME_ZONE = 'Europe/Copenhagen'
LANGUAGE_CODE = 'da_DK'
SITE_ID = 1
USE_I18N = True
USE_L10N = True

LOCALE_PATHS = (
    BASE_PATH + '/locale',
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.contrib.messages.context_processors.messages",
    "django.core.context_processors.request",
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

TEMPLATE_DIRS = (
    BASE_PATH + '/templates/'
)

INSTALLED_APPS = (

    'pages',
    'courses',
    'praise',

    'south',
    'treebeard',
    'sorl.thumbnail',

    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.markup',
)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}


TWITTER_USER = "malenebichel"
TWITTER_TIMEOUT = 3600


try:
    execfile(BASE_PATH + '/settings_local.py')
except IOError:
    sys.stderr.write("\nYou need to copy settings_local.example to settings_local.py and customize it.\n")
    sys.exit(1)