# 🚀 Guide de Déploiement - Portfolio BenGeek

**Date:** 2025-12-15  
**Version:** 2.0.0  
**Statut:** ✅ Prêt pour le déploiement

---

## 📋 Checklist Pré-Déploiement

### ✅ Vérifications Complétées

- [x] Toutes les informations personnelles mises à jour
- [x] Liens GitHub pointent vers `bengeek-portfolio`
- [x] WordPress et Flutter ajoutés aux compétences
- [x] SEO optimisé (meta tags, Open Graph, Twitter Card)
- [x] Fichiers `.env.example` présents
- [x] `.gitignore` configuré correctement
- [x] README.md à jour
- [x] Package.json avec informations du repository

### 🔒 Sécurité

- [x] Fichiers `.env` dans `.gitignore`
- [x] Base de données SQLite dans `.gitignore`
- [x] `node_modules/` et `venv/` ignorés
- [x] Secrets Django non exposés

---

## 🌐 Déploiement sur GitHub

### 1. Vérifier le statut Git

```bash
cd "c:\Users\BenGeek\Documents\MES PROJETS WEB\portfolio-project"
git status
```

### 2. Ajouter tous les fichiers modifiés

```bash
git add .
```

### 3. Créer un commit

```bash
git commit -m "feat: Portfolio v2.0 - WordPress & Flutter skills added"
```

### 4. Pousser vers GitHub

```bash
git push origin main
```

Si c'est la première fois :
```bash
git branch -M main
git remote add origin https://github.com/BenGeek237/bengeek-portfolio.git
git push -u origin main
```

---

## 🎯 Déploiement Frontend (Vercel)

### Option 1: Via GitHub (Recommandé)

1. **Aller sur [Vercel](https://vercel.com)**
2. **Connecter votre compte GitHub**
3. **Importer le repository** `bengeek-portfolio`
4. **Configuration du projet** :
   - Framework Preset: `Vite`
   - Root Directory: `frontend`
   - Build Command: `npm run build`
   - Output Directory: `dist`

5. **Variables d'environnement** :
   ```
   VITE_API_BASE_URL=https://votre-backend.railway.app/api
   VITE_EMAILJS_SERVICE_ID=votre_service_id
   VITE_EMAILJS_TEMPLATE_ID=votre_template_id
   VITE_EMAILJS_PUBLIC_KEY=votre_public_key
   ```

6. **Déployer** 🚀

### Option 2: Via CLI

```bash
cd frontend
npm install -g vercel
vercel login
vercel --prod
```

---

## 🐍 Déploiement Backend (Railway)

### Option 1: Via GitHub (Recommandé)

1. **Aller sur [Railway](https://railway.app)**
2. **Créer un nouveau projet**
3. **Déployer depuis GitHub** → Sélectionner `bengeek-portfolio`
4. **Configuration** :
   - Root Directory: `backend`
   - Start Command: `python manage.py migrate && python manage.py collectstatic --noinput && gunicorn portfolio_backend.wsgi`

5. **Variables d'environnement** :
   ```
   SECRET_KEY=votre-cle-secrete-super-longue-et-aleatoire
   DEBUG=False
   ALLOWED_HOSTS=votre-app.railway.app
   CORS_ALLOWED_ORIGINS=https://votre-frontend.vercel.app
   DATABASE_URL=postgresql://... (fourni par Railway)
   ```

6. **Ajouter PostgreSQL** :
   - Dans Railway, ajouter un service PostgreSQL
   - La variable `DATABASE_URL` sera automatiquement configurée

7. **Déployer** 🚀

### Option 2: Via CLI

```bash
cd backend
npm install -g @railway/cli
railway login
railway init
railway up
```

---

## 📦 Installation de Gunicorn (Production)

Ajouter dans `backend/requirements.txt` :
```
gunicorn==21.2.0
psycopg2-binary==2.9.9
```

Puis :
```bash
cd backend
pip install -r requirements.txt
pip freeze > requirements.txt
```

---

## 🔧 Configuration Production Django

### Mettre à jour `settings.py` pour la production :

```python
import dj_database_url

# Production settings
if not DEBUG:
    # Database
    DATABASES['default'] = dj_database_url.config(
        default=os.getenv('DATABASE_URL'),
        conn_max_age=600
    )
    
    # Security
    SECURE_SSL_REDIRECT = True
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    SECURE_BROWSER_XSS_FILTER = True
    SECURE_CONTENT_TYPE_NOSNIFF = True
    X_FRAME_OPTIONS = 'DENY'
```

---

## 🎨 Déploiement Alternatif

### Frontend - Netlify

1. Connecter GitHub sur [Netlify](https://netlify.com)
2. Build command: `npm run build`
3. Publish directory: `dist`
4. Base directory: `frontend`

### Backend - Render

1. Connecter GitHub sur [Render](https://render.com)
2. Type: Web Service
3. Build Command: `pip install -r requirements.txt`
4. Start Command: `gunicorn portfolio_backend.wsgi:application`
5. Root Directory: `backend`

---

## 📊 Post-Déploiement

### 1. Tester le Frontend
- [ ] Vérifier que le site charge correctement
- [ ] Tester la navigation entre les pages
- [ ] Vérifier le mode sombre/clair
- [ ] Tester le formulaire de contact
- [ ] Vérifier les animations

### 2. Tester le Backend
- [ ] Accéder à l'admin Django : `https://votre-backend.railway.app/admin/`
- [ ] Vérifier les API endpoints
- [ ] Tester la création de projets
- [ ] Tester la création d'articles de blog

### 3. Configuration Finale
- [ ] Configurer un nom de domaine personnalisé (optionnel)
- [ ] Activer HTTPS (automatique sur Vercel/Railway)
- [ ] Configurer Google Analytics (optionnel)
- [ ] Ajouter des projets via l'admin Django
- [ ] Publier des articles de blog

---

## 🐛 Dépannage

### Erreur CORS
Si vous avez des erreurs CORS :
```python
# backend/settings.py
CORS_ALLOWED_ORIGINS = [
    'https://votre-frontend.vercel.app',
    'http://localhost:5174',  # Pour le dev
]
```

### Erreur Static Files
```bash
python manage.py collectstatic --noinput
```

### Erreur Database
Vérifier que `DATABASE_URL` est bien configuré dans Railway.

---

## 📝 URLs du Projet

- **Repository GitHub** : https://github.com/BenGeek237/bengeek-portfolio
- **Frontend (Vercel)** : À configurer après déploiement
- **Backend (Railway)** : À configurer après déploiement
- **Admin Django** : `https://votre-backend.railway.app/admin/`

---

## 🎉 Félicitations !

Votre portfolio est maintenant déployé et accessible au monde entier ! 🚀

N'oubliez pas de :
- Ajouter vos projets via l'admin Django
- Publier des articles de blog
- Partager votre portfolio sur LinkedIn et GitHub
- Mettre à jour votre CV avec le lien du portfolio

---

**Créé par:** Antigravity AI  
**Pour:** Mamoudou Bia (BenGeek)  
**Version:** 2.0.0
