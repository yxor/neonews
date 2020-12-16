import os

from django.core.wsgi import get_wsgi_application


DEBUG = os.environ.get('debug')

SETTINGS_PATH = 'neonews.settings.dev' if bool(DEBUG) else 'neonews.settings.prod'

os.environ.setdefault('DJANGO_SETTINGS_MODULE', SETTINGS_PATH)

application = get_wsgi_application()
