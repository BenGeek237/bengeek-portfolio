from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from blog.models import Category, Post
from django.utils.text import slugify
from datetime import datetime, timedelta


class Command(BaseCommand):
    help = 'Crée des articles de blog de démonstration'

    def handle(self, *args, **kwargs):
        # Créer ou récupérer un utilisateur
        user, created = User.objects.get_or_create(
            username='admin',
            defaults={
                'email': 'admin@example.com',
                'is_staff': True,
                'is_superuser': True
            }
        )
        if created:
            user.set_password('admin123')
            user.save()
            self.stdout.write(self.style.SUCCESS(f'Utilisateur créé: {user.username}'))
        else:
            self.stdout.write(self.style.WARNING(f'Utilisateur existant: {user.username}'))

        # Créer des catégories
        categories_data = [
            {'name': 'Développement Web', 'slug': 'developpement-web'},
            {'name': 'Python & Django', 'slug': 'python-django'},
            {'name': 'JavaScript & Vue.js', 'slug': 'javascript-vuejs'},
            {'name': 'DevOps & Cloud', 'slug': 'devops-cloud'},
            {'name': 'Cybersécurité', 'slug': 'cybersecurite'},
        ]

        categories = {}
        for cat_data in categories_data:
            category, created = Category.objects.get_or_create(
                slug=cat_data['slug'],
                defaults={'name': cat_data['name']}
            )
            categories[cat_data['slug']] = category
            status = 'créée' if created else 'existante'
            self.stdout.write(self.style.SUCCESS(f'Catégorie {status}: {category.name}'))

        # Créer des articles de blog
        posts_data = [
            {
                'title': 'Introduction à Vue.js 3 et la Composition API',
                'category': 'javascript-vuejs',
                'excerpt': 'Découvrez les nouveautés de Vue.js 3 et comment utiliser la Composition API pour créer des applications modernes et performantes.',
                'content': '''
# Introduction à Vue.js 3

Vue.js 3 apporte de nombreuses améliorations par rapport à la version 2. La Composition API est l'une des fonctionnalités les plus importantes.

## Qu'est-ce que la Composition API ?

La Composition API est une nouvelle façon d'organiser la logique des composants. Elle offre plus de flexibilité et une meilleure réutilisabilité du code.

### Exemple de base

```javascript
import { ref, computed } from 'vue'

export default {
  setup() {
    const count = ref(0)
    const doubleCount = computed(() => count.value * 2)
    
    function increment() {
      count.value++
    }
    
    return { count, doubleCount, increment }
  }
}
```

## Avantages

- Meilleure organisation du code
- Réutilisabilité accrue
- TypeScript natif
- Performance améliorée

La Composition API rend Vue.js encore plus puissant et flexible !
                ''',
                'days_ago': 2
            },
            {
                'title': 'Créer une API REST avec Django REST Framework',
                'category': 'python-django',
                'excerpt': 'Guide complet pour créer une API REST professionnelle avec Django REST Framework, incluant l\'authentification et les permissions.',
                'content': '''
# Django REST Framework : Guide Complet

Django REST Framework (DRF) est l'outil parfait pour créer des APIs REST avec Django.

## Installation

```bash
pip install djangorestframework
```

## Configuration de base

Ajoutez 'rest_framework' dans INSTALLED_APPS :

```python
INSTALLED_APPS = [
    ...
    'rest_framework',
]
```

## Créer un Serializer

```python
from rest_framework import serializers

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['id', 'title', 'content', 'created_at']
```

## Créer une ViewSet

```python
from rest_framework import viewsets

class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
```

## Conclusion

DRF simplifie grandement la création d'APIs REST avec Django. C'est un outil indispensable pour tout développeur Django !
                ''',
                'days_ago': 5
            },
            {
                'title': 'Les bases de la cybersécurité pour développeurs',
                'category': 'cybersecurite',
                'excerpt': 'Apprenez les principes fondamentaux de la cybersécurité et comment protéger vos applications web contre les attaques courantes.',
                'content': '''
# Cybersécurité pour Développeurs

La sécurité doit être une priorité dès le début du développement.

## Les 10 risques OWASP

1. **Injection SQL** - Toujours utiliser des requêtes paramétrées
2. **Authentification cassée** - Implémenter une authentification robuste
3. **Exposition de données sensibles** - Chiffrer les données sensibles
4. **XXE** - Désactiver les entités externes XML
5. **Contrôle d'accès défaillant** - Vérifier les permissions

## Bonnes pratiques

### Validation des entrées

```python
from django.core.validators import validate_email

def validate_user_input(email):
    try:
        validate_email(email)
        return True
    except ValidationError:
        return False
```

### Utiliser HTTPS

Toujours utiliser HTTPS en production pour chiffrer les communications.

### Mise à jour régulière

Gardez vos dépendances à jour pour corriger les vulnérabilités connues.

## Conclusion

La sécurité est un processus continu. Restez informé des dernières menaces et bonnes pratiques !
                ''',
                'days_ago': 7
            },
            {
                'title': 'Docker et Docker Compose pour les débutants',
                'category': 'devops-cloud',
                'excerpt': 'Maîtrisez Docker et Docker Compose pour containeriser vos applications et simplifier votre workflow de développement.',
                'content': '''
# Docker : Le Guide du Débutant

Docker révolutionne la façon dont nous déployons nos applications.

## Qu'est-ce que Docker ?

Docker permet de packager une application avec toutes ses dépendances dans un conteneur isolé.

## Installation

Téléchargez Docker Desktop depuis le site officiel.

## Premier Dockerfile

```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
```

## Docker Compose

```yaml
version: '3.8'

services:
  web:
    build: .
    ports:
      - "8000:8000"
    volumes:
      - .:/app
    depends_on:
      - db
  
  db:
    image: postgres:15
    environment:
      POSTGRES_DB: mydb
      POSTGRES_PASSWORD: secret
```

## Commandes essentielles

```bash
docker build -t myapp .
docker run -p 8000:8000 myapp
docker-compose up
```

Docker simplifie le déploiement et garantit que votre application fonctionne partout de la même manière !
                ''',
                'days_ago': 10
            },
            {
                'title': 'Optimisation des performances web',
                'category': 'developpement-web',
                'excerpt': 'Techniques et astuces pour améliorer les performances de vos applications web et offrir une meilleure expérience utilisateur.',
                'content': '''
# Optimisation des Performances Web

La performance est cruciale pour l'expérience utilisateur et le SEO.

## Métriques importantes

- **FCP** (First Contentful Paint)
- **LCP** (Largest Contentful Paint)
- **TTI** (Time to Interactive)
- **CLS** (Cumulative Layout Shift)

## Techniques d'optimisation

### 1. Lazy Loading

```javascript
<img src="image.jpg" loading="lazy" alt="Description">
```

### 2. Code Splitting

```javascript
const Component = () => import('./Component.vue')
```

### 3. Compression

Activez la compression gzip/brotli sur votre serveur.

### 4. CDN

Utilisez un CDN pour servir vos assets statiques.

### 5. Caching

```javascript
// Service Worker pour le cache
self.addEventListener('fetch', (event) => {
  event.respondWith(
    caches.match(event.request)
      .then(response => response || fetch(event.request))
  )
})
```

## Outils de mesure

- Google Lighthouse
- WebPageTest
- Chrome DevTools

## Conclusion

L'optimisation des performances est un processus continu. Mesurez, optimisez, et mesurez à nouveau !
                ''',
                'days_ago': 14
            }
        ]

        for post_data in posts_data:
            published_date = datetime.now() - timedelta(days=post_data['days_ago'])
            
            post, created = Post.objects.get_or_create(
                slug=slugify(post_data['title']),
                defaults={
                    'title': post_data['title'],
                    'author': user,
                    'category': categories[post_data['category']],
                    'excerpt': post_data['excerpt'],
                    'content': post_data['content'],
                    'status': 'published',
                    'published_date': published_date,
                    'views': 0
                }
            )
            
            status = 'créé' if created else 'existant'
            self.stdout.write(self.style.SUCCESS(f'Article {status}: {post.title}'))

        self.stdout.write(self.style.SUCCESS('\n✅ Données de démonstration créées avec succès !'))
        self.stdout.write(self.style.WARNING('\n📝 Vous pouvez maintenant accéder aux articles sur votre site.'))
