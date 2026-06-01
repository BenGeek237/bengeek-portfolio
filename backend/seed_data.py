import os
import django

# Configuration de l'environnement Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio_backend.settings')
django.setup()

from django.contrib.auth.models import User
from projects.models import Project
from blog.models import Category, Post
from django.utils import timezone

def seed():
    print("Début du seeding de la base de données...")

    # 1. Récupération ou création d'un utilisateur auteur pour le blog
    author = User.objects.first()
    if not author:
        author = User.objects.create_superuser('admin', 'admin@example.com', 'adminpass')
        print(f"Superutilisateur créé : {author.username}")
    else:
        print(f"Utilisateur auteur trouvé : {author.username}")

    # 2. Création de la catégorie de blog
    blog_category, created = Category.objects.get_or_create(
        slug='architecture-backend',
        defaults={'name': 'Architecture & Backend'}
    )
    if created:
        print(f"Catégorie de blog '{blog_category.name}' créée.")
    else:
        print(f"Catégorie de blog '{blog_category.name}' déjà existante.")

    # 3. Création du projet "Gestion des Dettes"
    project_desc_fr = """### 🎯 À propos du projet
**Gestion des Dettes** est une application web d'entreprise moderne de type **Full-stack**, conçue pour relever les défis de la gestion financière client. Reposant sur Java 21 et Spring Boot 3, l'application implémente une architecture n-tiers hautement modulaire pour séparer rigoureusement les responsabilités et assurer une maintenance aisée.

### 🏛️ L'Architecture en Couches (MVC étendu)
L'application est découpée de manière très stricte en couches logicielles :
*   **`entity/` (Modèle de données)** : Classes Java annotées avec JPA représentant directement les tables relationnelles (`Client`, `Dette`, `Paiement`).
*   **`repository/` (Accès aux données)** : Interfaces Spring Data JPA qui s'occupent d'interagir avec la base de données. Hibernate traduit automatiquement les opérations en requêtes SQL.
*   **`service/` (Logique Métier)** : Le cerveau de l'application où sont validées les règles métiers strictes (ex: *"Un client ne peut pas être supprimé s'il possède encore des dettes actives"*).
*   **`controller/` (Contrôleur)** : Gère le routage des requêtes HTTP et redirige vers les vues Thymeleaf appropriées.
*   **`dto/` (Data Transfer Object)** : Objets d'échange de données utilisés pour sécuriser l'application en évitant d'exposer directement les entités de la base de données au client.
*   **`templates/` (Vues)** : Pages HTML dynamiques animées par le moteur de template **Thymeleaf**, stylisées avec **Bootstrap 5** pour être parfaitement responsives.

### 🛡️ Sécurité & Fonctionnalités clés
*   **Spring Security** : Authentification complète par e-mail/mot de passe, protection contre les failles courantes (comme CSRF), et restriction des routes selon les rôles (Admin vs Caissier).
*   **Tableau de Bord Analytique** : Une interface interactive avec graphiques (courbes, anneaux) générés via **Chart.js** pour offrir des statistiques en temps réel sur la santé financière générale (total des dettes contractées vs réglées).
*   **Double Source de Données (H2 / MySQL)** : Utilisation d'une base de données H2 en mémoire en environnement de développement pour des tests rapides sans configuration, et structure prête pour une migration transparente vers MySQL en production."""

    project, created = Project.objects.update_or_create(
        slug='gestion-dettes',
        defaults={
            'title': 'Gestion des Dettes - Application Web N-Tiers',
            'description': project_desc_fr,
            'short_description': 'Application web d\'entreprise Full-stack robuste pour la gestion et le suivi des dettes clients, développée avec Spring Boot 3 et une architecture n-tiers (MVC).',
            'category': 'web',
            'technologies': 'Java 21, Spring Boot 3, Spring Security, Spring Data JPA, Hibernate, Thymeleaf, Bootstrap 5, Chart.js, H2 Database, MySQL, Maven',
            'github_url': 'https://github.com/BenGeek237/gestion-dettes',
            'featured': True
        }
    )
    if created:
        print(f"Projet '{project.title}' créé avec succès.")
    else:
        print(f"Projet '{project.title}' mis à jour.")

    # 4. Création de l'article de blog technique sur l'architecture Spring Boot
    blog_content = """## Introduction : Pourquoi Spring Boot 3 et Java 21 ?

Dans le développement d'applications d'entreprise, la clarté de la structure et la robustesse de la logique métier sont indispensables. Lors de la conception de mon projet **"Gestion des Dettes"**, j'ai choisi de m'appuyer sur l'écosystème robuste de **Java 21** et **Spring Boot 3**. 

L'objectif était de construire une application web robuste capable de gérer simultanément une base de données relationnelle, d'assurer une sécurité infaillible au niveau des rôles utilisateurs, et de fournir une interface utilisateur moderne et réactive. Voici un retour d'expérience complet sur l'architecture et les technologies que nous avons mises en place.

---

## 1. L'Architecture en Couches (MVC étendu / N-Tiers)

Le cœur de la réussite de ce projet réside dans sa structure. Plutôt que de mélanger l'accès aux données, la logique métier et l'interface utilisateur, l'application respecte un modèle **N-Tiers** où chaque composant a une responsabilité unique :

```mermaid
graph TD
    A[Client Browser] -->|HTTP Request| B[Controller]
    B -->|Calls with DTO| C[Service Layer]
    C -->|Validates Business Rules| C
    C -->|Uses Repository| D[Repository Layer]
    D -->|Translates to SQL via Hibernate| E[(Database: H2 / MySQL)]
    D -->|Returns Entities| C
    C -->|Prepares Model| B
    B -->|Renders dynamic HTML| F[Thymeleaf Template]
    F -->|Sends complete Page| A
```

### 🏛️ Détail du découpage fonctionnel :

1.  **`entity/` (Le Modèle de données)** :
    Ce sont des classes Java pures (POJO) annotées avec `@Entity`. Elles correspondent exactement aux tables de notre base de données (`Client`, `Dette`, `Paiement`). L'utilisation des annotations JPA (comme `@OneToMany`, `@ManyToOne`, `@JoinColumn`) définit proprement les relations physiques et d'intégrité de notre base.
    
2.  **`repository/` (L'Accès aux données)** :
    Grâce à **Spring Data JPA**, les repositories sont de simples interfaces héritant de `JpaRepository<T, ID>`. Pas besoin d'écrire de requêtes SQL manuelles compliquées pour les opérations CRUD élémentaires ; Spring génère automatiquement les implémentations et traduit nos appels en requêtes SQL performantes.
    
3.  **`service/` (La Logique Métier - Le "Cerveau")** :
    C'est la couche la plus cruciale de l'application. Elle contient toutes les vérifications et règles d'affaires. Par exemple, la règle assurant qu'**"un client ne peut pas être supprimé s'il a encore des dettes"** ou la validation du montant maximal autorisé d'une dette y sont centralisées sous l'annotation `@Service`. Cela garantit que la base de données reste toujours cohérente, quelle que soit l'action de l'utilisateur.
    
4.  **`dto/` (Data Transfer Object)** :
    Pour éviter d'exposer directement nos entités de base de données à la couche d'affichage (ce qui peut poser de graves problèmes de sécurité ou de performances), nous utilisons des DTOs. Ce sont des objets légers qui transportent uniquement les données requises pour la vue, découplant ainsi le stockage physique de l'affichage.
    
5.  **`controller/` (Le Contrôleur)** :
    Annotés avec `@Controller`, ils interceptent les requêtes HTTP, appellent les services pour réaliser les opérations requises, ajoutent les résultats au `Model` de Spring, puis désignent le gabarit Thymeleaf à renvoyer à l'utilisateur.

---

## 2. Les Moteurs du Back-End

*   **Java 21 (LTS)** : Nous profitons des dernières innovations de Java, comme le *Pattern Matching* pour les instructions switch, les *Records* (très utiles pour les DTOs rapides) et les *Virtual Threads* pour des performances asynchrones accrues.
*   **Spring Security** : Un composant indispensable pour protéger notre application. Il gère l'authentification sécurisée des utilisateurs (e-mail et mot de passe chiffrés), protège contre les attaques de type CSRF (Cross-Site Request Forgery) grâce à l'intégration automatique de jetons dans nos formulaires Thymeleaf, et contrôle l'accès par rôles (seul un utilisateur avec le rôle `ADMIN` peut supprimer un enregistrement, tandis qu'un `CAISSIER` peut uniquement enregistrer des paiements).
*   **Gestion des environnements de données (H2 vs MySQL)** :
    En développement, nous utilisons la base de données en mémoire **H2**, ultra-rapide et ne nécessitant aucune installation matérielle locale. Les configurations Hibernate sont définies de sorte que le schéma soit mis à jour dynamiquement au démarrage. Pour la mise en production, il suffit de configurer le profil de connexion **MySQL** dans les propriétés Spring sans changer une seule ligne de code Java !

---

## 3. L'Expérience Visuelle (Le Front-End)

Pour une application robuste de gestion interne, nous avons opté pour une approche de rendu côté serveur (Server-Side Rendering) hautement interactive :

*   **Thymeleaf** : C'est notre moteur de gabarit de choix. Sa force est de permettre l'écriture de code HTML valide et standard, tout en y insérant des attributs dynamiques (comme `th:each` pour boucler sur la liste des dettes ou `th:if` pour afficher des alertes). L'affichage est fluide et parfaitement intégré avec la session utilisateur.
*   **Bootstrap 5** : Offre une interface professionnelle, responsive et épurée. Les tableaux, les grilles Bento de gestion, les formulaires de création et les modales de validation s'adaptent instantanément aux smartphones et tablettes des utilisateurs sur le terrain.
*   **Chart.js** : Pour donner de la hauteur aux données de l'application, nous avons intégré un tableau de bord analytique interactif. Grâce à Chart.js, les gérants d'ateliers peuvent visualiser en un clin d'œil le taux de recouvrement des dettes et les statistiques mensuelles sous forme de graphiques en courbes et en anneaux dynamiques.

---

## Conclusion & Prochaines Étapes

Ce projet m'a permis d'assimiler les meilleures pratiques du développement d'applications d'entreprise en Java. Le découpage strict en couches garantit que l'application reste évolutive. Si demain je souhaite passer à un frontend découplé en Single Page Application (comme Vue.js ou React), il me suffira de remplacer les contrôleurs de templates par des `@RestController` qui retournent du JSON, sans toucher à mes couches `Service` ni `Repository` !

**Et vous, quelle architecture privilégiez-vous pour vos applications Spring Boot ?** Parlons-en dans les commentaires !"""

    post, created = Post.objects.update_or_create(
        slug='architecture-ntiers-spring-boot',
        defaults={
            'title': "Conception d'une architecture n-tiers robuste avec Spring Boot 3",
            'author': author,
            'category': blog_category,
            'excerpt': "Comment concevoir une application d'entreprise moderne avec Spring Boot 3 ? Découvrez le découpage en couches (Entity, Repository, Service, Controller, DTO) à travers notre retour d'expérience.",
            'content': blog_content,
            'status': 'published',
            'published_date': timezone.now()
        }
    )
    if created:
        print(f"Article de blog '{post.title}' créé avec succès.")
    else:
        print(f"Article de blog '{post.title}' mis à jour.")

    print("Seeding terminé avec succès !")

if __name__ == '__main__':
    seed()
