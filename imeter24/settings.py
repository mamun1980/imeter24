# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'zayrkja09!-(v(9o30ex0f)w5wojh@$f(say8j6r#zx@=*5tr+'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ADMINS = (
    # ('Your Name', 'your_email@domain.com'),
    ('paul', 'paul@scom.ca'),
    ('mamun1980', 'mamun1980@scom.ca'),
)

MANAGERS = ADMINS

DEFAULT_FROM_EMAIL = 'support@imeter24.com'


TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ['*']

SITE_ID = 1 
SITE_NAME = 'IMETER24'

ANONYMOUS_USER_ID = -1

#Project settings base dir (where settings.py is)
PROJECT_PREFIX = 'imeter24'

#Project name base (for cache etc must be unique to the server)
PROJECT_NAME = 'imeter24'

#Project base home directory to server (ie /usr/home/www/(project start)/ ) - Needs the trailing slash
PROJECT_BASE_DIR = '/usr/home/www/www.imeter24.com/'

#Project HTTP (WWW Link include the '/')
PROJECT_HTTP = 'http://www.imeter24.com/'

#Project Link (without http) - Used for cache setup etc
PROJECT_LINK = 'www.imeter24.com'



# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # 'imeter24',
    'contacts',
    'controllers',
    # 'scomuser',
    # 'report',
    # 'schedule',
    # 'inventory',
    # 'events',
    # 'purchase',

    # 3rd party app ========
    'south',
    'guardian',
    'haystack',

)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    # 'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'imeter24.urls'

#WSGI_APPLICATION = 'imeter24.wsgi.application'
WSGI_APPLICATION = '%sdjango.wsgi' %PROJECT_BASE_DIR


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'imeter24',                      # Or path to database file if using sqlite3.
        'USER': 'scom_test',                      # Not used with sqlite3.
        'PASSWORD': 'Testxxyy',                  # Not used with sqlite3.
        'HOST': '10.220.0.41',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '5432',                      # Set to empty string for default. Not used with sqlite3.
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


MEDIA_ROOT = PROJECT_BASE_DIR+ '/media/'

MEDIA_URL = ''

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/
# STATIC_ROOT = BASE_DIR + '/statics/' 
STATIC_URL = '/statics/'

STATICFILES_DIRS = ( BASE_DIR + '/statics/' , )

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.request',
    'imeter24.context_processors.site_name',
)
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)
TEMPLATE_DIRS = ( BASE_DIR+'/templates/', )

AUTHENTICATION_BACKENDS = (
    # an email logon backend
    'django.contrib.auth.backends.ModelBackend',
    'guardian.backends.ObjectPermissionBackend',
)


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        },
    'console':{
            'level': 'INFO',
            'class': 'logging.StreamHandler'
        },
    'null':{
            'level': 'INFO',
            'class': 'logging.NullHandler'
        }


    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
        'elasticsearch': {
            'handlers': ['null'],
            'level': 'INFO',
            'propagate': True,
        },
        'elasticsearch.trace': {
            'handlers': ['null'],
            'level': 'INFO',
            'propagate': True,
        },
    }
}


HAYSTACK_CONNECTIONS = {
    'default': {
        # 'ENGINE': 'haystack.backends.elasticsearch_backend.ElasticsearchSearchEngine',
        'ENGINE': 'imeter24.search_backend.ConfigurableElasticSearchEngine',
        # 'ENGINE': 'elasticstack.backends.ConfigurableElasticSearchEngine',
        'URL': 'http://10.221.0.42:9202/',
        'INDEX_NAME': 'contact',
        "INDEX": "not_analyzed",
    },
    
}

HAYSTACK_DEFAULT_OPERATOR = 'AND'
# ELASTICSEARCH_INDEX_SETTINGS = {
#     # index settings
# }

# HAYSTACK_SIGNAL_PROCESSOR = 'haystack.signals.RealtimeSignalProcessor'
HAYSTACK_SIGNAL_PROCESSOR = 'haystack.signals.RealtimeSignalProcessor'
# HAYSTACK_SIGNAL_PROCESSOR = 'contacts.signals.RelatedRealtimeSignalProcessor'


# CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'

# HAYSTACK_ROUTERS = ['inventory.routers.MasterRouter', 'schedule.routers.MasterRouter', 
#                     'purchase.routers.SLRouter', 'purchase.routers.PLRouter',
#                     'haystack.routers.DefaultRouter']

HAYSTACK_ROUTERS = [
                'contacts.routers.ContactRouter',
                'haystack.routers.DefaultRouter',]
