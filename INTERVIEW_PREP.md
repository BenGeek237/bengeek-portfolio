# 🎯 Préparation Entretien : Portfolio Vue 3 + Django

Ce document contient une simulation de questions/réponses d'entretien basée sur l'architecture et le code de votre portfolio (Version 2.0). L'objectif est de démontrer non seulement ce que vous avez fait, mais **pourquoi** vous l'avez fait.

---

## 🏛️ Catégorie 1 : Architecture et Choix Techniques

### Q1 : Pourquoi une architecture découplée (Vue.js + Django) plutôt qu'un framework full-stack ou les templates natifs de Django ?

**Réponse :**
> "J'ai choisi une architecture découplée (Headless) pour deux raisons principales. 
> 
> **1. Séparation des préoccupations et Scalabilité :** Cela me permet d'avoir une API Backend (Django DRF) robuste, centralisée et réutilisable. Si demain je souhaite développer une application mobile Flutter pour ce même projet, l'API est déjà prête à être consommée sans aucune modification.
> 
> **2. Expérience Utilisateur (UX) :** Les templates Django classiques nécessitent des rechargements complets de la page, ce qui casse l'immersion de l'utilisateur. Avec Vue 3, je crée une véritable SPA (Single Page Application). Cela me permet d'avoir des transitions fluides entre les vues, de garder l'état du lecteur audio ou du thème global intact pendant la navigation, et d'offrir des micro-animations complexes (comme mon Loading Screen style terminal). Le rendu global fait beaucoup plus "Application Native Premium" qu'un site web classique."

### Q2 : Comment gérez-vous la différence de base de données entre le développement et la production (SQLite vs PostgreSQL) ?

**Réponse :**
> "J'utilise SQLite en local pour sa simplicité : il n'y a pas de serveur de base de données à configurer, c'est immédiat pour commencer à développer. 
> 
> Cependant, pour la production sur PythonAnywhere, SQLite n'est pas adapté car il bloque facilement lors d'accès concurrents (écritures simultanées). J'ai donc opté pour PostgreSQL, qui est la norme de l'industrie pour sa robustesse. 
> 
> La transition est gérée de manière transparente grâce à la librairie `dj-database-url` et aux variables d'environnement (`.env`). Dans mon `settings.py`, Django regarde si une variable `DATABASE_URL` existe (ce qui est le cas sur mon serveur PythonAnywhere) et s'y connecte. Si elle est absente (comme en local par défaut), il fait un 'fallback' automatique sur la base SQLite locale."

---

## 💻 Catégorie 2 : Frontend (Vue 3, Pinia & UI/UX)

### Q3 : Vous utilisez la Composition API avec Vue 3. Quels avantages y trouvez-vous par rapport à l'Options API (Vue 2) ?

**Réponse :**
> "La Composition API (et spécifiquement le tag `<script setup>`) a été un vrai déclic d'organisation pour moi. 
> 
> Dans l'Options API, la logique d'une seule fonctionnalité complexe finit par être fragmentée entre les blocs `data`, `methods`, `computed`, et `watch`. C'est très difficile à lire quand le composant grossit.
> 
> Avec la Composition API, je peux regrouper le code par logique fonctionnelle. Par exemple, toute la logique qui gère le thème Dark/Light est regroupée au même endroit dans mon fichier. Surtout, cela me permet de créer des **Composables** (des fonctions réutilisables) que je peux injecter n'importe où dans l'application sans dupliquer de code."

### Q4 : Votre portfolio intègre un "Bento Grid", des compteurs animés et des effets 3D. Avez-vous utilisé de grosses librairies UI (Bootstrap, Vuetify) ? Comment gardez-vous l'application performante ?

**Réponse :**
> "J'ai délibérément évité les librairies UI lourdes pour garder le contrôle absolu sur le design et minimiser le poids du bundle JavaScript final. J'ai tout construit sur mesure en utilisant **Tailwind CSS**.
> 
> Pour maintenir les performances excellentes (scores Lighthouse à 95+), j'ai appliqué plusieurs stratégies :
> - **Intersection Observer natif :** Les animations (comme les compteurs) ne se déclenchent que lorsque l'élément entre visiblement dans l'écran, ce qui économise des ressources.
> - **Accélération matérielle :** J'utilise les classes utilitaires de Tailwind combinées aux propriétés CSS `transform` et `opacity`. Ces propriétés sont calculées par le GPU (carte graphique) du navigateur et non par le CPU, ce qui garantit les 60 FPS (images par seconde) sans saccades, même sur mobile.
> - **Lazy Loading :** Les composants ou les routes qui ne sont pas immédiatement nécessaires au premier chargement sont chargés de manière asynchrone."

### Q5 : Pourquoi avoir choisi Pinia plutôt que Vuex pour la gestion d'état ?

**Réponse :**
> "Pinia est devenu le standard recommandé par l'équipe Vue.js, et pour cause : 
> - Il est beaucoup plus léger que Vuex.
> - L'architecture est plus simple (finies les `mutations` redondantes de Vuex, on modifie le state directement depuis les `actions`).
> - Il offre une structure modulaire par défaut très propre et un excellent support TypeScript si je décide de typer mon code plus tard."

---

## ⚙️ Catégorie 3 : Backend (Django & DRF)

### Q6 : Quel est le rôle des "Serializers" (DRF) dans votre API ?

**Réponse :**
> "Mon frontend Vue.js et mon backend Django ne parlent pas la même langue : Vue utilise le format standardisé JSON, tandis que Django manipule des objets Python complexes générés par son ORM (QuerySets).
> 
> Les Serializers agissent comme des traducteurs.
> - Dans un sens (lecture) : ils prennent une instance de modèle Django (ex: le Projet Portfolio avec son image et son titre) et la convertissent en objet JSON renvoyé à l'API.
> - Dans l'autre sens (écriture) : si je soumets un formulaire depuis Vue, le Serializer prend les données JSON entrantes, les valide (vérifie que les types sont bons, que les champs requis sont là), et les désérialise en données sécurisées prêtes à être sauvegardées en base de données via l'ORM."

---

## 🚀 Catégorie 4 : DevOps, Déploiement et Sécurité

### Q7 : Vous hébergez le Frontend sur Vercel et le Backend sur PythonAnywhere. Avez-vous rencontré des problèmes de CORS ? Comment l'avez-vous résolu ?

**Réponse :**
> "Oui, c'est inévitable avec une architecture découplée. Le Frontend est sur un domaine (ex: `vercel.app`) et le Backend sur un autre (`pythonanywhere.com`). Par défaut, la politique de sécurité des navigateurs (Same-Origin Policy) bloque ces requêtes.
> 
> Pour résoudre cela de manière sécurisée :
> 1. J'ai installé le package `django-cors-headers` sur le backend.
> 2. Au lieu de configurer `CORS_ORIGIN_ALLOW_ALL = True` (ce qui est une très mauvaise pratique de sécurité), j'ai configuré `CORS_ALLOWED_ORIGINS` dans mon `settings.py`.
> 3. J'utilise les variables d'environnement pour y injecter explicitement l'URL exacte de mon frontend Vercel. Ainsi, mon API n'accepte les requêtes provenant **que** de mon application autorisée."

---

## 🧠 Catégorie 5 : Bilan et Soft Skills

### Q8 : Quel a été le plus grand défi technique rencontré lors de cette refonte (V2.0) et comment l'avez-vous surmonté ?

**Réponse :**
> "Le plus gros challenge a été de faire cohabiter des animations de survol 3D complexes (Bento Grid) avec le système de transitions fluides entre les pages de Vue Router.
> 
> Au départ, lors du changement de page, certaines animations "fantômes" continuaient de s'exécuter ou l'état 3D restait bloqué, causant des glitches visuels. J'ai dû plonger en profondeur dans le cycle de vie des composants Vue (`onMounted`, `onUnmounted`) pour m'assurer que les écouteurs d'événements (Event Listeners) et les instances d'Intersection Observer étaient correctement détruits (nettoyés) lors de la destruction des composants pour éviter les fuites de mémoire (memory leaks)."

### Q9 : Si vous aviez 1 mois de plus sur ce projet, quelle fonctionnalité prioriseriez-vous ?

**Réponse :**
> "Le projet couvre déjà très bien la Roadmap Phase 1. Pour aller plus loin (Phase 2), voici mes priorités :
> 
> 1. **Internationalisation (i18n) :** Le module `vue-i18n` est déjà dans le package.json. L'implémenter permettrait de s'ouvrir facilement à un marché anglophone.
> 2. **Système de Blog Markdown :** Ajouter une section technique gérée depuis l'admin Django, dont le contenu markdown serait rendu dynamiquement côté Vue avec `vue3-markdown-it`.
> 3. **Optimisation API :** Ajouter une couche de cache (comme Redis) sur Django REST Framework pour servir les données statiques du portfolio encore plus rapidement."
