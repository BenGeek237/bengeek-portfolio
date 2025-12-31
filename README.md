# Portfolio  - Mamoudou Bia

[![Vue.js](https://img.shields.io/badge/Vue.js-3.x-4FC08D?logo=vue.js)](https://vuejs.org/)
[![Django](https://img.shields.io/badge/Django-4.x-092E20?logo=django)](https://www.djangoproject.com/)
[![Tailwind CSS](https://img.shields.io/badge/Tailwind-3.x-38B2AC?logo=tailwind-css)](https://tailwindcss.com/)
[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

> Portfolio personnel moderne avec Bento Grid, animations avancées, et design premium

![Portfolio Preview](https://via.placeholder.com/1200x600/10b981/ffffff?text=Portfolio+Preview)

## ✨ Fonctionnalités

### 🎨 Design Moderne
- **Bento Grid Layout** - Grille asymétrique unique
- **Loading Screen Terminal** - Première impression mémorable
- **Featured Project** - Section dédiée au projet phare
- **Dark/Light Mode** - Thème adaptatif avec animation
- **Responsive Design** - Parfait sur tous les appareils

### 🎬 Animations Avancées
- **Page Transitions** - 5 types de transitions fluides
- **Animated Counters** - Statistiques qui s'animent au scroll
- **3D Hover Effects** - Cartes avec rotation perspective
- **Micro-animations** - 15+ effets subtils
- **Smooth Scrolling** - Navigation fluide

### 🛠️ Technologies
- **Frontend**: Vue.js 3 (Composition API) + Vite
- **Backend**: Django 4 + Django REST Framework
- **CMS**: WordPress (sites performants et personnalisés)
- **Mobile**: Flutter (applications cross-platform)
- **Styling**: Tailwind CSS + Custom Animations
- **Database**: PostgreSQL (production) / SQLite (dev)
- **Deployment**: Vercel (frontend) + Railway (backend)

## 📸 Screenshots

### Hero Section
![Hero](https://via.placeholder.com/800x400/000000/10b981?text=Hero+Section)

### Bento Grid Projects
![Bento Grid](https://via.placeholder.com/800x400/1a1a1a/3b82f6?text=Bento+Grid)

### Featured Project
![Featured](https://via.placeholder.com/800x400/0a0a0a/8b5cf6?text=Featured+Project)

## 🚀 Installation

### Prérequis
- Node.js 18+ 
- Python 3.11+
- PostgreSQL (optionnel pour dev)

### Frontend Setup

```bash
# Cloner le repo
git clone https://github.com/BenGeek237/bengeek-portfolio.git
cd bengeek-portfolio/frontend

# Installer les dépendances
npm install

# Créer .env
cp .env.example .env

# Lancer le dev server
npm run dev
```

Le frontend sera accessible sur `http://localhost:5174`

### Backend Setup

```bash
# Aller dans le dossier backend
cd ../backend

# Créer un environnement virtuel
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Installer les dépendances
pip install -r requirements.txt

# Créer .env
cp .env.example .env

# Migrations
python manage.py migrate

# Créer un superuser
python manage.py createsuperuser

# Lancer le serveur
python manage.py runserver
```

Le backend sera accessible sur `http://localhost:8000`

## 📁 Structure du Projet

```
portfolio-project/
├── frontend/                 # Application Vue.js
│   ├── src/
│   │   ├── components/      # Composants Vue
│   │   │   ├── layout/     # Navbar, Footer
│   │   │   ├── sections/   # Hero, Projects, etc.
│   │   │   └── ui/         # LoadingScreen, Counter, etc.
│   │   ├── views/          # Pages/Routes
│   │   ├── router/         # Configuration routes
│   │   ├── stores/         # Pinia stores
│   │   ├── services/       # API calls
│   │   └── assets/         # CSS, images
│   ├── public/             # Fichiers statiques
│   └── package.json
│
├── backend/                 # API Django
│   ├── portfolio/          # App principale
│   │   ├── models.py      # Modèles de données
│   │   ├── views.py       # API endpoints
│   │   ├── serializers.py # DRF serializers
│   │   └── urls.py        # Routes API
│   ├── portfolio_backend/ # Configuration Django
│   ├── manage.py
│   └── requirements.txt
│
├── IMPROVEMENTS.md         # Détails des améliorations
├── VISUAL_GUIDE.md        # Guide de test
├── ROADMAP_PHASE2.md      # Prochaines étapes
├── DEPLOYMENT_GUIDE.md    # Guide de déploiement
├── FINAL_SUMMARY.md       # Résumé complet
└── README.md              # Ce fichier
```

## 🎯 Fonctionnalités Détaillées

### 1. Bento Grid Layout
Layout asymétrique moderne avec 3 tailles de cartes:
- **Large**: 2 colonnes × 2 lignes
- **Medium**: 1 colonne × 1 ligne  
- **Small**: 1 colonne × 1 ligne

Effets:
- Rotation 3D au hover
- Quick actions overlay
- Badges animés (FEATURED, LIVE)
- Filtres par catégorie

### 2. Loading Screen
Écran de chargement style terminal:
- 7 étapes d'initialisation
- Barre de progression avec shimmer
- Curseur clignotant
- Disparition automatique (2.8s)

### 3. Featured Project
Section dédiée au projet phare:
- Layout 2 colonnes (info + visual)
- Mockup navigateur interactif
- Statistiques avec gradients
- Stack technique avec hover effects
- CTA avec shimmer effect

### 4. Animated Counters
Compteurs animés avec:
- Intersection Observer
- Easing function (easeOutExpo)
- Animation fluide (2s)
- Support préfixes/suffixes

### 5. Page Transitions
5 types de transitions:
- **Fade**: Fondu simple
- **Slide Left**: Navigation avant
- **Slide Right**: Navigation arrière
- **Slide Up**: Pages détails
- **Scale**: Effet zoom

### 6. Micro-animations
15+ animations CSS:
- Hover lift
- Magnetic buttons
- Glow effects
- Bounce & shake
- Gradient text animé
- Reveal progressif
- Stagger children
- Et plus...

## 📊 Performance

### Lighthouse Scores
- Performance: 95+
- Accessibility: 100
- Best Practices: 100
- SEO: 100

### Optimisations
- ✅ Code splitting automatique
- ✅ Lazy loading des routes
- ✅ Images optimisées
- ✅ CSS minifié
- ✅ Gzip compression
- ✅ CDN global (Vercel)

## 🔧 Scripts Disponibles

### Frontend
```bash
npm run dev          # Dev server
npm run build        # Build production
npm run preview      # Preview build
npm run lint         # Linter
```

### Backend
```bash
python manage.py runserver        # Dev server
python manage.py migrate          # Migrations
python manage.py createsuperuser  # Admin user
python manage.py collectstatic    # Static files
```

## 🌐 Déploiement

Voir [DEPLOYMENT_GUIDE.md](DEPLOYMENT_GUIDE.md) pour les instructions détaillées.

### Quick Deploy

**Frontend (Vercel)**:
```bash
cd frontend
vercel --prod
```

**Backend (Railway)**:
```bash
cd backend
railway up
```

## 📝 Variables d'Environnement

### Frontend (.env)
```bash
VITE_API_URL=http://localhost:8000/api
```

### Backend (.env)
```bash
SECRET_KEY=your-secret-key
DEBUG=True
DATABASE_URL=postgresql://user:pass@localhost/dbname
ALLOWED_HOSTS=localhost,127.0.0.1
CORS_ALLOWED_ORIGINS=http://localhost:5174
```

## 🤝 Contribution

Les contributions sont les bienvenues ! 

1. Fork le projet
2. Créer une branche (`git checkout -b feature/AmazingFeature`)
3. Commit les changements (`git commit -m 'Add AmazingFeature'`)
4. Push vers la branche (`git push origin feature/AmazingFeature`)
5. Ouvrir une Pull Request

## 📄 License

Ce projet est sous licence MIT. Voir [LICENSE](LICENSE) pour plus de détails.

## 👤 Auteur

**Mamoudou Bia**

- 🌐 Portfolio: [https://mamoudou-bia.vercel.app](https://mamoudou-bia.vercel.app)
- 💼 LinkedIn: [bengeek237](https://linkedin.com/in/bengeek237)
- 🐙 GitHub: [@BenGeek237](https://github.com/BenGeek237)
- 📧 Email: mamoudoubiya3@gmail.com
- 📱 WhatsApp: [+237 698 340 664](https://wa.me/237698340664)

## 🙏 Remerciements

- [Vue.js](https://vuejs.org/) - Framework frontend
- [Django](https://www.djangoproject.com/) - Framework backend
- [Tailwind CSS](https://tailwindcss.com/) - Framework CSS
- [Vercel](https://vercel.com/) - Hébergement frontend
- [Railway](https://railway.app/) - Hébergement backend
- [Heroicons](https://heroicons.com/) - Icônes
- [Google Fonts](https://fonts.google.com/) - Typographie

## 📚 Documentation

- [IMPROVEMENTS.md](IMPROVEMENTS.md) - Détails techniques des améliorations
- [VISUAL_GUIDE.md](VISUAL_GUIDE.md) - Guide de test visuel
- [ROADMAP_PHASE2.md](ROADMAP_PHASE2.md) - Prochaines fonctionnalités
- [DEPLOYMENT_GUIDE.md](DEPLOYMENT_GUIDE.md) - Guide de déploiement
- [FINAL_SUMMARY.md](FINAL_SUMMARY.md) - Résumé complet du projet

## 🎉 Changelog

### Version 2.0.0 (13 Décembre 2025)
- ✨ Ajout Bento Grid Layout
- ✨ Loading Screen Terminal
- ✨ Featured Project Section
- ✨ Animated Counters
- ✨ Page Transitions
- ✨ 15+ Micro-animations
- 🎨 Design system complet
- 📱 Responsive amélioré
- ⚡ Performance optimisée

### Version 1.0.0
- 🎉 Version initiale
- ✅ Hero Section
- ✅ About Section
- ✅ Projects Grid
- ✅ Skills Section
- ✅ Blog Preview
- ✅ Contact Section
- ✅ Dark/Light Mode

---

<div align="center">

**Développé avec ❤️ par Mamoudou Bia**

⭐ Si ce projet vous plaît, n'hésitez pas à lui donner une étoile !

</div>
