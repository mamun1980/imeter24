import sys

sys.path.append('/usr/home/www/')
sys.path.append('/usr/home/www/test.premierelevator.com/')

import os

os.environ['DJANGO_SETTINGS_MODULE'] = 'premierelevator.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
