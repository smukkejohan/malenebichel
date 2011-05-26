import os
import sys
import site

site.addsitedir('/home/malene/.virtualenvs/wetart/lib/python2.6/site-packages')

sys.path.append('/home/malene/srv/')
sys.path.append('/home/malene/srv/malene')

os.environ['DJANGO_SETTINGS_MODULE'] = 'p4w.settings'

import django.core.handlers.wsgi

application = django.core.handlers.wsgi.WSGIHandler()