# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'zayrkja09!-(v(9o30ex0f)w5wojh@$f(say8j6r#zx@=*5tr+'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

SITE_ID = 1 
ANONYMOUS_USER_ID = -1

PROJECT_LINK = 'localhost'
# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
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
    # 'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'premierelevator.urls'

WSGI_APPLICATION = 'premierelevator.wsgi.application'


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
        'NAME': 'premier_test',                      # Or path to database file if using sqlite3.
        'USER': 'postgres',                      # Not used with sqlite3.
        'PASSWORD': 'qweqwe',                  # Not used with sqlite3.
        'HOST': 'localhost',                      # Set to empty string for localhost. Not used with sqlite3.
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


MEDIA_ROOT = '/home/mamun/django/premierelevator/media'

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
    'premierelevator.context_processors.site_name',
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
        'URL': 'http://127.0.0.1:9200/',
        'INDEX_NAME': 'contact',
        "INDEX": "not_analyzed",
        'EXCLUDED_INDEXES': ['inventory.search_indexes.ItemIndex', 
                            'schedule.search_indexes.JobIndex',
                            'purchase.search_indexes.PurchaseOrderIndex', 
                            'schedule.search_indexes.JobControlIndex',
                            'purchase.search_indexes.ShippingListIndex', 
                            'purchase.search_indexes.PackingListIndex',],
    },
    'inventory': {
        # 'ENGINE': 'haystack.backends.elasticsearch_backend.ElasticsearchSearchEngine',
        'ENGINE': 'premierelevator.search_backend.ConfigurableElasticSearchEngine',
        'URL': 'http://127.0.0.1:9200/',
        'INDEX_NAME': 'inventory',
        "INDEX": "not_analyzed",
        'EXCLUDED_INDEXES': ['contacts.search_indexes.ContactIndex', 
                            'schedule.search_indexes.JobIndex',
                            'purchase.search_indexes.PurchaseOrderIndex', 
                            'purchase.search_indexes.ShippingListIndex', 
                            'purchase.search_indexes.PackingListIndex', 
                            'schedule.search_indexes.JobControlIndex',],
    },
    'job': {
        # 'ENGINE': 'haystack.backends.elasticsearch_backend.ElasticsearchSearchEngine',
        'ENGINE': 'premierelevator.search_backend.ConfigurableElasticSearchEngine',
        'URL': 'http://127.0.0.1:9200/',
        'INDEX_NAME': 'job',
        'EXCLUDED_INDEXES': ['contacts.search_indexes.ContactIndex', 
                            'inventory.search_indexes.ItemIndex',
                            'purchase.search_indexes.PurchaseOrderIndex',
                            'purchase.search_indexes.ShippingListIndex', 
                            'purchase.search_indexes.PackingListIndex',
                            'schedule.search_indexes.JobControlIndex', ],
    },
    'jobcontrol': {
        # 'ENGINE': 'haystack.backends.elasticsearch_backend.ElasticsearchSearchEngine',
        'ENGINE': 'premierelevator.search_backend.ConfigurableElasticSearchEngine',
        'URL': 'http://127.0.0.1:9200/',
        'INDEX_NAME': 'jobcontrol',
        'EXCLUDED_INDEXES': ['contacts.search_indexes.ContactIndex', 
                            'inventory.search_indexes.ItemIndex',
                            'purchase.search_indexes.PurchaseOrderIndex',
                            'purchase.search_indexes.ShippingListIndex', 
                            'purchase.search_indexes.PackingListIndex', 
                            'schedule.search_indexes.JobIndex',],
    },
    'po': {
        # 'ENGINE': 'haystack.backends.elasticsearch_backend.ElasticsearchSearchEngine',
        'ENGINE': 'premierelevator.search_backend.ConfigurableElasticSearchEngine',
        'URL': 'http://127.0.0.1:9200/',
        'INDEX_NAME': 'po',
        'EXCLUDED_INDEXES': ['contacts.search_indexes.ContactIndex', 
                            'inventory.search_indexes.ItemIndex',
                            'schedule.search_indexes.JobIndex', 
                            'schedule.search_indexes.JobControlIndex',
                            'purchase.search_indexes.ShippingListIndex', 
                            'purchase.search_indexes.PackingListIndex',],
    },
    'pl': {
        # 'ENGINE': 'haystack.backends.elasticsearch_backend.ElasticsearchSearchEngine',
        'ENGINE': 'premierelevator.search_backend.ConfigurableElasticSearchEngine',
        'URL': 'http://127.0.0.1:9200/',
        'INDEX_NAME': 'po',
        'EXCLUDED_INDEXES': ['contacts.search_indexes.ContactIndex', 
                            'inventory.search_indexes.ItemIndex',
                            'schedule.search_indexes.JobIndex', 
                            'schedule.search_indexes.JobControlIndex',
                            'purchase.search_indexes.ShippingListIndex',
                            'purchase.search_indexes.PurchaseOrderIndex',],
    },
    'sl': {
        # 'ENGINE': 'haystack.backends.elasticsearch_backend.ElasticsearchSearchEngine',
        'ENGINE': 'premierelevator.search_backend.ConfigurableElasticSearchEngine',
        'URL': 'http://127.0.0.1:9200/',
        'INDEX_NAME': 'po',
        'EXCLUDED_INDEXES': ['contacts.search_indexes.ContactIndex', 
                            'inventory.search_indexes.ItemIndex',
                            'schedule.search_indexes.JobIndex', 
                            'schedule.search_indexes.JobControlIndex', 
                            'purchase.search_indexes.PackingListIndex',
                            'purchase.search_indexes.PurchaseOrderIndex',],
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

HAYSTACK_ROUTERS = ['inventory.routers.MasterRouter', 
                'schedule.routers.MasterRouter', 
                'purchase.routers.PORouter','purchase.routers.SLRouter','purchase.routers.PLRouter',
                'haystack.routers.DefaultRouter',]