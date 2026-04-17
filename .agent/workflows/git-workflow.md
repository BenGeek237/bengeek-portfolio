---
description: Workflow Git pour éviter les redéploiements inutiles
---

# 🔄 Workflow Git Optimisé

## 📌 Principe
- **Branche `main`** : Code de production (déclenche auto-deploy sur Railway)
- **Branche `develop`** : Développement et modifications mineures
- **Commits directs sur `main`** : Uniquement pour docs/commentaires

---

## 🎯 Scénarios d'utilisation

### 1️⃣ **Modifications de documentation/commentaires UNIQUEMENT**

```bash
# Vous êtes sur main
git add .
git commit -m "docs: mise à jour des commentaires"
git push origin main
```

**Résultat** : Push sur GitHub ✅ | Railway redéploie ⚠️ (mais aucun impact)

---

### 2️⃣ **Modifications de code fonctionnel**

```bash
# Créer/basculer sur la branche develop
git checkout -b develop  # ou: git checkout develop

# Faire vos modifications, puis :
git add .
git commit -m "feat: nouvelle fonctionnalité"
git push origin develop

# Tester localement si nécessaire

# Quand prêt à déployer :
git checkout main
git merge develop
git push origin main
```

**Résultat** : Contrôle total sur quand déployer ✅

---

### 3️⃣ **Plusieurs petites modifications avant déploiement**

```bash
# Sur develop
git add .
git commit -m "fix: correction bug 1"
git push origin develop

# Continuer à travailler...
git add .
git commit -m "fix: correction bug 2"
git push origin develop

# Quand tout est prêt :
git checkout main
git merge develop
git push origin main  # ← Déploiement unique
```

---

## 🚀 Configuration initiale

### Créer la branche develop
```bash
git checkout -b develop
git push -u origin develop
git checkout main
```

### Configurer Railway (optionnel)
Dans Railway Dashboard :
- Settings → Deploys → Branch : `main`
- Cela garantit que seuls les push sur `main` déclenchent un déploiement

---

## 💡 Conventions de commit

Utilisez des préfixes clairs :

| Préfixe | Usage | Exemple |
|---------|-------|---------|
| `feat:` | Nouvelle fonctionnalité | `feat: ajout système de blog` |
| `fix:` | Correction de bug | `fix: résolution erreur 404` |
| `docs:` | Documentation/commentaires | `docs: ajout commentaires views.py` |
| `style:` | CSS/UI uniquement | `style: amélioration navbar` |
| `refactor:` | Refactoring code | `refactor: optimisation queries` |
| `chore:` | Maintenance | `chore: mise à jour dépendances` |

---

## 🎓 Résumé rapide

**Règle d'or** :
- 📝 Docs/commentaires → Push direct sur `main` (pas grave si redéploie)
- 💻 Code fonctionnel → Travailler sur `develop`, merger dans `main` quand prêt

**Avantage** : Vous contrôlez exactement quand Railway redéploie ! 🎯
