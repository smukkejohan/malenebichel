import os
import sys
import site

site.addsitedir('/home/malene/.virtualenvs/malenebichel/lib/python2.7/site-packages')

sys.path.append('/home/malene/srv/')
sys.path.append('/home/malene/srv/malene/')

os.environ['DJANGO_SETTINGS_MODULE'] = 'malenebichel.settings'

import django.core.handlers.wsgi

application = django.core.handlers.wsgi.WSGIHandler()