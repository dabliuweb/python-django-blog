import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'your_project.settings')
django.setup()

from django.contrib.auth.models import User

# Create superuser if it does not exist
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', '', 'admin')