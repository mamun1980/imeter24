# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))



#URL Base Setting
URL_PREFIX = "" 

#Project settings base dir (where settings.py is)
PROJECT_PREFIX = 'premierelevator' 

#Project name base (for cache etc must be unique to the server)
PROJECT_NAME = 'scomtest'

#Project base home directory to server (ie /usr/home/www/(project start)/ ) - Needs the trailing slash
PROJECT_BASE_DIR = '/usr/home/www/test.premierelevator.com/'

#Project HTTP (WWW Link include the '/')
PROJECT_HTTP = 'http://test.premierelevator.com/'

#Project Link (without http) - Used for cache setup etc
PROJECT_LINK = 'test.premierelevator.com'



# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '=p-w(0yxl$rm&kkoumfyuh)$hj#2su=nkkl+xe$f6e1ibr9lev'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True 
TEMPLATE_DEBUG = DEBUG 

ADMINS = (
    # ('Your Name', 'your_email@domain.com'),
    ('paul', 'paul@scom.ca'),
    ('mamun1980', 'mamun1980@scom.ca'),
)

MANAGERS = ADMINS

ALLOWED_HOSTS = ['*']

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
        'KEY_PREFIX': '%s.cache' %PROJECT_NAME
    }
}

CACHE_MIDDLEWARE_SECONDS = 300
SESSION_ENGINE = "django.contrib.sessions.backends.cached_db"
SESSION_SAVE_EVERY_REQUEST = True
CACHE_MIDDLEWARE_KEY_PREFIX = 'SCOMTEST'

SESSION_COOKIE_AGE = 60 * 60
SESSION_COOKIE_DOMAIN = '%s' %PROJECT_LINK
SESSION_EXPIRE_AT_BROWSER_CLOSE = True

SITE_ID = 1 
SITE_NAME = 'SCOMTEST'

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.sites',
    'django.contrib.staticfiles',
    'premierelevator',
    'contacts',
    'scomuser',
    'report',
    'schedule',
    'inventory',
    'events',
    'purchase',

    # 3rd party app ========
    'south',
    'selectable',
    'guardian',
    'haystack',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = '%s.urls' %PROJECT_PREFIX

WSGI_APPLICATION = '%sdjango.wsgi' %PROJECT_BASE_DIR


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'premier',                      # Or path to database file if using sqlite3.
        'USER': 'scom_test',                      # Not used with sqlite3.
        'PASSWORD': 'Testxxyy',                  # Not used with sqlite3.
        'HOST': '10.221.0.41',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '5432',                      # Set to empty string for default. Not used with sqlite3.
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

#TIME_ZONE = 'UTC'
TIME_ZONE = 'America/New_York'

USE_I18N = True

USE_L10N = True

USE_TZ = True

LOGIN_URL = "/contacts/login/"
LOGOUT_URL = "/contacts/logout/"

#Media Files
MEDIA_ROOT = "/usr/home/www/test.premierelevator.com/media/"
MEDIA_URL = "/media/"

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/
STATIC_ROOT = BASE_DIR + '/statics/' 
STATIC_URL = '/statics/'

#STATICFILES_DIRS = ( '%sstatics/' %PROJECT_BASE_DIR , )

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
    'premierelevator.context_processors.site_name',
)
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

#TEMPLATE_DIRS = ( '%stemplates/' %PROJECT_BASE_DIR )

TEMPLATE_DIRS = ( PROJECT_BASE_DIR+'templates/', )

AUTHENTICATION_BACKENDS = (
    # an email logon backend
    '%s.scom_auth.EmailAuthenticationBackend' %PROJECT_PREFIX,
    'django.contrib.auth.backends.ModelBackend',
    'guardian.backends.ObjectPermissionBackend',
)


ANONYMOUS_USER_ID = -1

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
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
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
        'elasticsearch': {
            'handlers': ['mail_admins'],
            'level': 'DEBUG',
            'propagate': True,
        },
    }
}
HAYSTACK_CONNECTIONS = {
    'default': {
        # 'ENGINE': 'haystack.backends.elasticsearch_backend.ElasticsearchSearchEngine',
        'ENGINE': 'premierelevator.search_backend.ConfigurableElasticSearchEngine',
        # 'ENGINE': 'elasticstack.backends.ConfigurableElasticSearchEngine',
        'URL': 'http://10.221.0.42:9200/',
        'INDEX_NAME': 'contact',
        "INDEX": "not_analyzed",
        'EXCLUDED_INDEXES': ['inventory.search_indexes.ItemIndex', 
                            'schedule.search_indexes.JobIndex',
                            'purchase.search_indexes.PurchaseOrderIndex', 
                            'schedule.search_indexes.JobControlIndex',
                            'purchase.search_indexes.ShippingListIndex', 
                            'purchase.search_indexes.PackingListIndex',
                            'scomuser.search_indexes.UserIndex',
                            'events.search_indexes.EventsIndex',],
    },
    'inventory': {
        # 'ENGINE': 'haystack.backends.elasticsearch_backend.ElasticsearchSearchEngine',
        'ENGINE': 'premierelevator.search_backend.ConfigurableElasticSearchEngine',
        'URL': 'http://10.221.0.42:9200/',
        'INDEX_NAME': 'inventory',
        "INDEX": "not_analyzed",
        'EXCLUDED_INDEXES': ['contacts.search_indexes.ContactIndex', 
                            'schedule.search_indexes.JobIndex',
                            'purchase.search_indexes.PurchaseOrderIndex', 
                            'purchase.search_indexes.ShippingListIndex', 
                            'purchase.search_indexes.PackingListIndex', 
                            'schedule.search_indexes.JobControlIndex',
                            'scomuser.search_indexes.UserIndex',
                            'events.search_indexes.EventsIndex',],
    },
    'job': {
        # 'ENGINE': 'haystack.backends.elasticsearch_backend.ElasticsearchSearchEngine',
        'ENGINE': 'premierelevator.search_backend.ConfigurableElasticSearchEngine',
        'URL': 'http://10.221.0.42:9200/',
        'INDEX_NAME': 'job',
        'EXCLUDED_INDEXES': ['contacts.search_indexes.ContactIndex', 
                            'inventory.search_indexes.ItemIndex',
                            'purchase.search_indexes.PurchaseOrderIndex',
                            'purchase.search_indexes.ShippingListIndex', 
                            'purchase.search_indexes.PackingListIndex',
                            'schedule.search_indexes.JobControlIndex',
                            'scomuser.search_indexes.UserIndex',
                            'events.search_indexes.EventsIndex',],
    },
    'jobcontrol': {
        # 'ENGINE': 'haystack.backends.elasticsearch_backend.ElasticsearchSearchEngine',
        'ENGINE': 'premierelevator.search_backend.ConfigurableElasticSearchEngine',
        'URL': 'http://10.221.0.42:9200/',
        'INDEX_NAME': 'jobcontrol',
        'EXCLUDED_INDEXES': ['contacts.search_indexes.ContactIndex', 
                            'inventory.search_indexes.ItemIndex',
                            'purchase.search_indexes.PurchaseOrderIndex',
                            'purchase.search_indexes.ShippingListIndex', 
                            'purchase.search_indexes.PackingListIndex', 
                            'schedule.search_indexes.JobIndex',
                            'scomuser.search_indexes.UserIndex',
                            'events.search_indexes.EventsIndex',],
    },
    'po': {
        # 'ENGINE': 'haystack.backends.elasticsearch_backend.ElasticsearchSearchEngine',
        'ENGINE': 'premierelevator.search_backend.ConfigurableElasticSearchEngine',
        'URL': 'http://10.221.0.42:9200/',
        'INDEX_NAME': 'po',
        'EXCLUDED_INDEXES': ['contacts.search_indexes.ContactIndex', 
                            'inventory.search_indexes.ItemIndex',
                            'schedule.search_indexes.JobIndex', 
                            'schedule.search_indexes.JobControlIndex',
                            'purchase.search_indexes.ShippingListIndex', 
                            'purchase.search_indexes.PackingListIndex',
                            'scomuser.search_indexes.UserIndex',
                            'events.search_indexes.EventsIndex',],
    },
    'pl': {
        # 'ENGINE': 'haystack.backends.elasticsearch_backend.ElasticsearchSearchEngine',
        'ENGINE': 'premierelevator.search_backend.ConfigurableElasticSearchEngine',
        'URL': 'http://10.221.0.42:9200/',
        'INDEX_NAME': 'pl',
        'EXCLUDED_INDEXES': ['contacts.search_indexes.ContactIndex', 
                            'inventory.search_indexes.ItemIndex',
                            'schedule.search_indexes.JobIndex', 
                            'schedule.search_indexes.JobControlIndex',
                            'purchase.search_indexes.ShippingListIndex',
                            'purchase.search_indexes.PurchaseOrderIndex',
                            'scomuser.search_indexes.UserIndex',
                            'events.search_indexes.EventsIndex',],
    },
    'sl': {
        # 'ENGINE': 'haystack.backends.elasticsearch_backend.ElasticsearchSearchEngine',
        'ENGINE': 'premierelevator.search_backend.ConfigurableElasticSearchEngine',
        'URL': 'http://10.221.0.42:9200/',
        'INDEX_NAME': 'sl',
        'EXCLUDED_INDEXES': ['contacts.search_indexes.ContactIndex', 
                            'inventory.search_indexes.ItemIndex',
                            'schedule.search_indexes.JobIndex', 
                            'schedule.search_indexes.JobControlIndex', 
                            'purchase.search_indexes.PackingListIndex',
                            'purchase.search_indexes.PurchaseOrderIndex',
                            'scomuser.search_indexes.UserIndex',
                            'events.search_indexes.EventsIndex',],
    },
    'user': {
        # 'ENGINE': 'haystack.backends.elasticsearch_backend.ElasticsearchSearchEngine',
        'ENGINE': 'premierelevator.search_backend.ConfigurableElasticSearchEngine',
        'URL': 'http://10.221.0.42:9200/',
        'INDEX_NAME': 'user',
        'EXCLUDED_INDEXES': ['contacts.search_indexes.ContactIndex', 
                            'inventory.search_indexes.ItemIndex',
                            'schedule.search_indexes.JobIndex', 
                            'schedule.search_indexes.JobControlIndex',
                            'purchase.search_indexes.ShippingListIndex', 
                            'purchase.search_indexes.PackingListIndex',
                            'purchase.search_indexes.PurchaseOrderIndex',
                            'events.search_indexes.EventsIndex',],
    },
    'events': {
        # 'ENGINE': 'haystack.backends.elasticsearch_backend.ElasticsearchSearchEngine',
        'ENGINE': 'premierelevator.search_backend.ConfigurableElasticSearchEngine',
        'URL': 'http://10.221.0.42:9200/',
        'INDEX_NAME': 'events',
        'EXCLUDED_INDEXES': ['contacts.search_indexes.ContactIndex', 
                            'inventory.search_indexes.ItemIndex',
                            'schedule.search_indexes.JobIndex', 
                            'schedule.search_indexes.JobControlIndex',
                            'purchase.search_indexes.ShippingListIndex', 
                            'purchase.search_indexes.PackingListIndex',
                            'purchase.search_indexes.PurchaseOrderIndex',
                            'scomuser.search_indexes.UserIndex',],
    },
}



HAYSTACK_DEFAULT_OPERATOR = 'AND'
ELASTICSEARCH_DEFAULT_ANALYZER = "whitespace"
HAYSTACK_SIGNAL_PROCESSOR = 'haystack.signals.RealtimeSignalProcessor'

HAYSTACK_ROUTERS = ['inventory.routers.MasterRouter', 
                'schedule.routers.MasterRouter', 
                'purchase.routers.PORouter','purchase.routers.SLRouter','purchase.routers.PLRouter',
                'scomuser.routers.UserRouter','events.routers.EventsRouter','haystack.routers.DefaultRouter',]