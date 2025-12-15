# Système d'Internationalisation (i18n) - Portfolio

## ✅ Implémentation Complète

### 📦 Installation
- ✅ Vue I18n v9 installé
- ✅ Configuration i18n créée

### 🌍 Langues Supportées
- **Français (FR)** - Langue par défaut
- **Anglais (EN)**

### 📁 Structure des Fichiers

```
frontend/src/
├── i18n/
│   ├── index.js           # Configuration i18n
│   └── locales/
│       ├── fr.json        # Traductions françaises
│       └── en.json        # Traductions anglaises
├── stores/
│   └── language.js        # Store Pinia pour la gestion de la langue
└── components/
    ├── layout/
    │   └── Navbar.vue     # ✅ Traduit + bouton de langue
    └── sections/
        └── HeroSection.vue # ✅ Traduit
```

### 🎨 Fonctionnalités

#### 1. **Bouton de Changement de Langue**
- **Desktop** : Bouton avec drapeaux animés (🇫🇷 ↔️ 🇬🇧) dans la navbar
- **Mobile** : Bouton dans le menu hamburger
- **Animation** : Transition fluide avec rotation lors du changement

#### 2. **Persistance**
- La langue sélectionnée est sauvegardée dans `localStorage`
- Restauration automatique au rechargement de la page

#### 3. **Composants Traduits**
- ✅ **Navbar** : Navigation, boutons, menu mobile
- ✅ **HeroSection** : Titre, rôles, boutons, stats, scroll indicator

#### 4. **Animations Intelligentes**
- Les rôles rotatifs se réinitialisent automatiquement lors du changement de langue
- Transition fluide entre les langues

### 🔑 Clés de Traduction Disponibles

#### Navigation (`nav.*`)
- `home`, `about`, `skills`, `projects`, `blog`, `contact`

#### Hero Section (`hero.*`)
- `greeting` : "Salut, je suis" / "Hi, I'm"
- `roles.*` : 6 rôles professionnels traduits
- `exploreProjects`, `hireMe`
- `stats.*` : projects, linesOfCode, satisfaction, available
- `scrollDown`

#### Autres Sections (Prêtes pour traduction)
- `about.*` : À propos, formation, certifications
- `skills.*` : Compétences
- `projects.*` : Projets, filtres
- `blog.*` : Blog, articles
- `contact.*` : Formulaire de contact
- `footer.*` : Pied de page
- `common.*` : Textes communs (loading, error, etc.)

### 🚀 Utilisation dans les Composants

```vue
<script setup>
import { useI18n } from 'vue-i18n'

const { t, locale } = useI18n()
</script>

<template>
  <!-- Texte simple -->
  <h1>{{ t('hero.greeting') }}</h1>
  
  <!-- Computed avec traduction -->
  <div v-for="item in navItems" :key="item.id">
    {{ t(`nav.${item.id}`) }}
  </div>
</template>
```

### 📝 Prochaines Étapes

Pour traduire d'autres composants :
1. Ajouter les clés de traduction dans `fr.json` et `en.json`
2. Importer `useI18n` dans le composant
3. Remplacer les textes statiques par `{{ t('cle.de.traduction') }}`

### 🎯 Statut Actuel

- ✅ Système i18n configuré et fonctionnel
- ✅ Navbar entièrement traduite
- ✅ HeroSection entièrement traduit
- ⏳ Autres sections : traductions prêtes, à implémenter dans les composants
