"""
Script pour ajouter rapidement des projets de démo
Usage: python manage.py shell < add_projects.py
"""

from portfolio.models import Project

# Supprimer les anciens projets de démo (optionnel)
# Project.objects.all().delete()

# Projets à ajouter
projects_data = [
    {
        'title': 'Portfolio Moderne',
        'description': 'Portfolio personnel développé avec Vue.js 3 et Django REST Framework. Features: Bento Grid layout, animations 3D, dark mode, loading screen terminal, et bien plus.',
        'short_description': 'Portfolio interactif avec Bento Grid et animations avancées',
        'category': 'web',
        'technologies': 'Vue.js, Django, Tailwind CSS, PostgreSQL',
        'github_url': 'https://github.com/mohamedelbachir/portfolio-project',
        'live_url': 'http://localhost:5174',
        'featured': True,
    },
    {
        'title': 'E-Commerce Platform',
        'description': 'Plateforme e-commerce complète avec panier, paiement Stripe, gestion des stocks, et dashboard admin.',
        'short_description': 'Plateforme e-commerce avec paiement intégré',
        'category': 'web',
        'technologies': 'React, Node.js, MongoDB, Stripe',
        'github_url': 'https://github.com/mohamedelbachir',
        'live_url': '',
    },
    {
        'title': 'Task Manager App',
        'description': 'Application de gestion de tâches avec drag & drop, notifications, et synchronisation temps réel.',
        'short_description': 'Gestionnaire de tâches avec temps réel',
        'category': 'web',
        'technologies': 'Vue.js, Firebase, Vuex, Tailwind CSS',
        'github_url': 'https://github.com/mohamedelbachir',
        'live_url': '',
    },
    {
        'title': 'Weather Dashboard',
        'description': 'Dashboard météo avec prévisions 7 jours, cartes interactives, et alertes personnalisées.',
        'short_description': 'Dashboard météo avec API OpenWeather',
        'category': 'web',
        'technologies': 'JavaScript, OpenWeather API, Chart.js',
        'github_url': 'https://github.com/mohamedelbachir',
        'live_url': '',
    },
    {
        'title': 'Chat Application',
        'description': 'Application de chat en temps réel avec rooms, emojis, et partage de fichiers.',
        'short_description': 'Chat temps réel avec WebSocket',
        'category': 'web',
        'technologies': 'Socket.io, Express, React, MongoDB',
        'github_url': 'https://github.com/mohamedelbachir',
        'live_url': '',
    },
]

# Créer les projets
created_count = 0
for project_data in projects_data:
    project, created = Project.objects.get_or_create(
        title=project_data['title'],
        defaults=project_data
    )
    if created:
        created_count += 1
        print(f"✅ Créé: {project.title}")
    else:
        print(f"⏭️  Existe déjà: {project.title}")

print(f"\n🎉 {created_count} projets créés sur {len(projects_data)}")
print("🚀 Rafraîchissez votre portfolio pour voir les changements!")
