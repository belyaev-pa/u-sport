import os, sys, site
PROJECT_DIR = ''
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "u-sport.settings")
sys.path.insert(0, PROJECT_DIR)
sys.path.insert(1, os.path.dirname(__file__))
#sys.path.insert(2, 'C:/python2.7/lib/site-packages')
from django.core.handlers.wsgi import WSGIHandler
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
