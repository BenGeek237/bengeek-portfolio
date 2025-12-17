#!/usr/bin/env python
"""
Script pour créer un superuser automatiquement
Usage: python create_superuser.py
"""
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio_backend.settings')
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()

# Configurer vos identifiants depuis les variables d'environnement
username = os.getenv('DJANGO_SUPERUSER_USERNAME', 'admin')
email = os.getenv('DJANGO_SUPERUSER_EMAIL', 'admin@example.com')
password = os.getenv('DJANGO_SUPERUSER_PASSWORD', 'changeme123')

# Supprimer l'ancien superuser s'il existe
if User.objects.filter(username=username).exists():
    User.objects.filter(username=username).delete()
    print(f'🗑️ Ancien superuser "{username}" supprimé.')

# Créer le nouveau superuser
User.objects.create_superuser(username=username, email=email, password=password)
print(f'✅ Superuser "{username}" créé avec succès!')
print(f'   Username: {username}')
print(f'   Email: {email}')
print(f'   Password: {password}')
