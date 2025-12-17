from django.db import migrations
from django.contrib.auth import get_user_model
import os


def create_superuser(apps, schema_editor):
    User = get_user_model()
    
    username = os.getenv('DJANGO_SUPERUSER_USERNAME', 'bengeek')
    email = os.getenv('DJANGO_SUPERUSER_EMAIL', 'mamoudou@example.com')
    password = os.getenv('DJANGO_SUPERUSER_PASSWORD', 'BenGeek2025!')
    
    # Supprimer l'ancien superuser s'il existe
    if User.objects.filter(username=username).exists():
        User.objects.filter(username=username).delete()
        print(f'🗑️ Ancien superuser "{username}" supprimé.')
    
    # Créer le nouveau superuser
    User.objects.create_superuser(username=username, email=email, password=password)
    print(f'✅ Superuser "{username}" créé avec succès!')
    print(f'   Username: {username}')
    print(f'   Email: {email}')


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_superuser),
    ]
