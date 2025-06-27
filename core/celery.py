import os
from celery import Celery

# Default Django settings
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings.base")

app = Celery("core")

# Celery configni settingsdan oladi
app.config_from_object("django.conf:settings", namespace="CELERY")

# Barcha app lardan tasks.py fayllarni avtomatik topadi
app.autodiscover_tasks()
