import os
import sys

path = '/home/dj/app'
if path not in sys.path:	
    sys.path.append(path)

path = '/home/dj'
if path not in sys.path:	
    sys.path.append(path)




os.environ['DJANGO_SETTINGS_MODULE'] = 'app.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()

