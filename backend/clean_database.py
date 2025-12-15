"""
Script pour nettoyer la base de données - Version corrigée
"""

from projects.models import Project
from blog.models import Post

# Supprimer tous les projets sauf le portfolio
print("Suppression des projets de demo...")
try:
    deleted_projects = Project.objects.exclude(title='Portfolio Moderne').delete()
    print(f"Projets supprimes: {deleted_projects[0]}")
except Exception as e:
    print(f"Erreur projets: {e}")

# Supprimer tous les articles de blog
print("\nSuppression des articles de blog...")
try:
    deleted_posts = Post.objects.all().delete()
    print(f"Articles supprimes: {deleted_posts[0]}")
except Exception as e:
    print(f"Erreur articles: {e}")

# Afficher les projets restants
try:
    remaining_projects = Project.objects.all()
    print(f"\nProjets restants: {remaining_projects.count()}")
    for project in remaining_projects:
        print(f"  - {project.title}")
except Exception as e:
    print(f"Erreur affichage: {e}")

print("\nNettoyage termine!")
