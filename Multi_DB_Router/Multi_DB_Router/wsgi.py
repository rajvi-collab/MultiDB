"""
WSGI config for Multi_DB_Router project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/
"""

import os
from dotenv import load_dotenv

from django.core.wsgi import get_wsgi_application

load_dotenv(dotenv_path=os.path.join(os.path.dirname(os.path.dirname(__file__)), '.env'))

# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Multi_DB_Router.settings")
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Multi_DB_Router.settings.{}'.format(
    os.getenv('APP_ENV', 'production')))

application = get_wsgi_application()
