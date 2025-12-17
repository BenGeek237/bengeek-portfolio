import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView,
      meta: {
        title: 'Accueil',
        transition: 'fade',
        index: 0
      }
    },
    {
      path: '/blog',
      name: 'blog',
      component: () => import('../views/BlogView.vue'),
      meta: {
        title: 'Blog',
        transition: 'slide-left',
        index: 1
      }
    },
    {
      path: '/projects',
      name: 'projects',
      component: () => import('../views/ProjectsView.vue'),
      meta: {
        title: 'Projets',
        transition: 'slide-left',
        index: 2
      }
    },
    {
      path: '/blog/:slug',
      name: 'blog-post',
      component: () => import('../views/BlogPostView.vue'),
      props: true,
      meta: {
        title: 'Article',
        transition: 'slide-up',
        index: 3
      }
    },
    {
      path: '/:pathMatch(.*)*',
      name: 'not-found',
      component: () => import('../views/NotFoundView.vue'),
      meta: {
        title: 'Page non trouvée',
        transition: 'fade',
        index: 4
      }
    },
  ],
  scrollBehavior(to, from, savedPosition) {
    if (to.hash) {
      return {
        el: to.hash,
        behavior: 'smooth',
      }
    }
    return { top: 0, behavior: 'smooth' }
  },
})

// Mise à jour automatique du titre de la page
router.beforeEach((to, from, next) => {
  // Utiliser le titre de la route ou un titre par défaut
  const defaultTitle = 'Mamoudou Bia - Développeur Full-Stack | Portfolio'
  document.title = to.meta.title || defaultTitle
  next()
})

export default router