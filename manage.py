import os
import sys

DEBUG = True

SETTINGS_PATH = 'neonews.settings.dev' if DEBUG else 'neonews.settings.prod'
os.environ.setdefault('debug', str(DEBUG))

if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', SETTINGS_PATH)
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)
