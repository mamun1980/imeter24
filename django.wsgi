import sys

sys.path.append('/usr/home/www/')
sys.path.append('/usr/home/www/www.imeter24.com/')

import os

os.environ['DJANGO_SETTINGS_MODULE'] = 'imeter24.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
