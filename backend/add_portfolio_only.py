"""
Script pour ajouter uniquement le projet Portfolio
"""

from projects.models import Project

# Supprimer tous les projets existants
print("Nettoyage des projets existants...")
Project.objects.all().delete()

# Créer uniquement le projet Portfolio
portfolio_data = {
    'title': 'Portfolio Moderne',
    'description': 'Portfolio personnel développé avec Vue.js 3 et Django REST Framework. Interface bilingue (Français/Anglais) avec système i18n complet. Features: animations avancées avec gradient animé, dark mode, design responsive, et architecture moderne.',
    'short_description': 'Portfolio interactif bilingue avec animations avancées',
    'category': 'web',
    'technologies': 'Vue.js, Django, Tailwind CSS, Vue I18n, PostgreSQL',
    'github_url': 'https://github.com/mohamedelbachir/portfolio-project',
    'live_url': 'http://localhost:5174',
    'featured': True,
}

project = Project.objects.create(**portfolio_data)
print(f"Projet cree: {project.title}")

print("\nTermine!")
