"""
WSGI config for social_media_api project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os
import sys

path = "C:Users/Kang'eri/alx/backend/Alx_DjangoLearnLab/social_media_api"

if path not in sys.path:
    sys.path.append(path)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'social_media_api.settings')

from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()
