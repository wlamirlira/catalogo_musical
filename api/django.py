# api/django.py
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "catalogo.settings")

from django.core.asgi import get_asgi_application
app = get_asgi_application()
