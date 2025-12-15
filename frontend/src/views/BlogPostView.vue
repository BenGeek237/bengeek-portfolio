<!-- frontend/src/views/BlogPostView.vue -->
<template>
  <div class="min-h-screen pt-24 pb-16">
      <!-- Chargement -->
      <div v-if="loading" class="container mx-auto px-4 text-center py-12">
        <div class="inline-block animate-spin rounded-full h-12 w-12 border-t-2 border-b-2 border-primary-600"></div>
      </div>

      <!-- Article non trouvé -->
      <div v-else-if="!post" class="container mx-auto px-4 text-center py-12">
        <div class="text-5xl mb-4">❌</div>
        <h1 class="text-3xl font-bold text-gray-900 dark:text-white mb-4">
          Article non trouvé
        </h1>
        <router-link to="/blog" class="btn-primary">
          Retour au blog
        </router-link>
      </div>

      <!-- Article -->
      <article v-else class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8">
        <!-- En-tête -->
        <header class="mb-12">
          <!-- Catégorie -->
          <div class="flex items-center justify-between mb-6">
            <router-link
              :to="{ name: 'blog', query: { category: post.category?.slug } }"
              class="inline-flex items-center px-4 py-2 bg-primary-100 dark:bg-primary-900/30 text-primary-700 dark:text-primary-300 rounded-full text-sm font-medium hover:bg-primary-200 dark:hover:bg-primary-800/40 transition-colors"
            >
              <span>{{ post.category?.name || 'Général' }}</span>
            </router-link>
            <button
              @click="toggleBookmark"
              class="p-2 rounded-full bg-gray-100 dark:bg-gray-800 text-gray-700 dark:text-gray-300 hover:bg-gray-200 dark:hover:bg-gray-700 transition-colors"
              :aria-label="isBookmarked ? 'Retirer des favoris' : 'Ajouter aux favoris'"
            >
              <BookmarkIcon v-if="isBookmarked" class="w-5 h-5 text-primary-600" />
              <BookmarkIcon v-else class="w-5 h-5" />
            </button>
          </div>

          <!-- Titre -->
          <h1 class="text-4xl md:text-5xl font-bold text-gray-900 dark:text-white mb-6">
            {{ post.title }}
          </h1>

          <!-- Métadonnées -->
          <div class="flex flex-wrap items-center gap-4 text-gray-600 dark:text-gray-400 mb-8">
            <div class="flex items-center">
              <UserCircleIcon class="w-5 h-5 mr-2" />
              <span>{{ post.author?.username || 'Auteur' }}</span>
            </div>
            <div class="flex items-center">
              <CalendarDaysIcon class="w-5 h-5 mr-2" />
              <span>{{ formatDate(post.published_date) }}</span>
            </div>
            <div class="flex items-center">
              <ClockIcon class="w-5 h-5 mr-2" />
              <span>{{ readingTime }} min de lecture</span>
            </div>
            <div class="flex items-center">
              <EyeIcon class="w-5 h-5 mr-2" />
              <span>{{ post.views || 0 }} vues</span>
            </div>
          </div>

          <!-- Image de couverture -->
          <div v-if="post.image" class="rounded-2xl overflow-hidden mb-8">
            <img
              :src="post.image"
              :alt="post.title"
              class="w-full h-[400px] object-cover"
            />
          </div>
        </header>

        <!-- Contenu -->
        <div class="prose prose-lg dark:prose-invert max-w-none mb-12">
          <Markdown :source="post.content" />
        </div>

        <!-- Tags -->
        <div v-if="post.tags && post.tags.length" class="mb-12">
          <h3 class="text-lg font-semibold text-gray-900 dark:text-white mb-4">
            Tags
          </h3>
          <div class="flex flex-wrap gap-2">
            <span
              v-for="tag in post.tags"
              :key="tag"
              class="px-3 py-1 bg-gray-100 dark:bg-gray-800 text-gray-700 dark:text-gray-300 rounded-full text-sm"
            >
              {{ tag }}
            </span>
          </div>
        </div>

        <!-- Partage -->
        <div class="border-t border-b border-gray-200 dark:border-gray-800 py-6 mb-12">
          <h3 class="text-lg font-semibold text-gray-900 dark:text-white mb-4">
            Partager cet article
          </h3>
          <div class="flex space-x-4">
            <button
              v-for="platform in sharePlatforms"
              :key="platform.name"
              @click="shareArticle(platform)"
              class="flex items-center space-x-2 px-4 py-2 rounded-lg bg-gray-100 dark:bg-gray-800 text-gray-700 dark:text-gray-300 hover:bg-gray-200 dark:hover:bg-gray-700 transition-colors"
            >
              <span class="text-lg">{{ platform.icon }}</span>
              <span>{{ platform.name }}</span>
            </button>
          </div>
        </div>

        <!-- Navigation -->
        <div class="grid grid-cols-1 md:grid-cols-2 gap-8 mb-12">
          <button
            v-if="prevPost"
            @click="goToPost(prevPost)"
            class="group p-6 rounded-xl bg-gray-50 dark:bg-gray-800 hover:bg-gray-100 dark:hover:bg-gray-700 transition-colors text-left"
          >
            <div class="flex items-center text-primary-600 dark:text-primary-400 mb-2">
              <ArrowLeftIcon class="w-4 h-4 mr-2" />
              <span class="text-sm font-medium">Article précédent</span>
            </div>
            <h3 class="font-semibold text-gray-900 dark:text-white group-hover:text-primary-600 transition-colors">
              {{ prevPost.title }}
            </h3>
          </button>

          <button
            v-if="nextPost"
            @click="goToPost(nextPost)"
            class="group p-6 rounded-xl bg-gray-50 dark:bg-gray-800 hover:bg-gray-100 dark:hover:bg-gray-700 transition-colors text-left md:text-right"
          >
            <div class="flex items-center justify-end text-primary-600 dark:text-primary-400 mb-2">
              <span class="text-sm font-medium">Article suivant</span>
              <ArrowRightIcon class="w-4 h-4 ml-2" />
            </div>
            <h3 class="font-semibold text-gray-900 dark:text-white group-hover:text-primary-600 transition-colors">
              {{ nextPost.title }}
            </h3>
          </button>
        </div>

        <!-- Auteur -->
        <div class="card mb-12">
          <div class="flex items-center space-x-4 mb-4">
            <div class="w-16 h-16 rounded-full bg-gradient-to-br from-primary-400 to-purple-500 flex items-center justify-center">
              <span class="text-2xl text-white">👨‍💻</span>
            </div>
            <div>
              <h3 class="text-xl font-bold text-gray-900 dark:text-white">
                {{ post.author?.username || 'Auteur' }}
              </h3>
              <p class="text-gray-600 dark:text-gray-400">
                Développeur Full-Stack Passionné
              </p>
            </div>
          </div>
          <p class="text-gray-600 dark:text-gray-400">
            Passionné par le développement web et le partage de connaissances. 
            J'aime créer des applications modernes et documenter mes apprentissages.
          </p>
        </div>

        <!-- Commentaires (à implémenter) -->
        <div class="card">
          <h3 class="text-2xl font-bold text-gray-900 dark:text-white mb-6">
            Commentaires ({{ comments.length }})
          </h3>
          <div v-if="comments.length === 0" class="text-center py-8">
            <p class="text-gray-600 dark:text-gray-400 mb-4">
              Soyez le premier à commenter cet article !
            </p>
            <button @click="showCommentForm = true" class="btn-primary">
              Ajouter un commentaire
            </button>
          </div>
          <!-- Liste des commentaires ici -->
        </div>
    </article>
  </div>
</template>

<script setup>
import { ref, computed, onMounted, watch } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { blogService } from '@/services/api'
import Markdown from 'vue3-markdown-it'
import {
  UserCircleIcon,
  CalendarDaysIcon,
  ClockIcon,
  EyeIcon,
  BookmarkIcon,
  ArrowLeftIcon,
  ArrowRightIcon,
  ArrowUpTrayIcon
} from '@heroicons/vue/24/outline'

const route = useRoute()
const router = useRouter()

// États
const post = ref(null)
const loading = ref(true)
const isBookmarked = ref(false)
const showCommentForm = ref(false)
const comments = ref([])
const allPosts = ref([])

// Données de partage
const sharePlatforms = [
  { name: 'Twitter', icon: '🐦', color: 'text-blue-400' },
  { name: 'LinkedIn', icon: '💼', color: 'text-blue-600' },
  { name: 'Facebook', icon: '📘', color: 'text-blue-700' },
  { name: 'Copier le lien', icon: '🔗', color: 'text-gray-600' },
]

// Récupérer l'article
const fetchPost = async () => {
  try {
    loading.value = true
    // Réinitialiser l'état
    post.value = null
    isBookmarked.value = false
    
    const slug = route.params.slug
    const response = await blogService.getPostBySlug(slug)
    
    if (response && (Array.isArray(response) ? response[0] : response)) {
      post.value = Array.isArray(response) ? response[0] : response
      
      // Incrémenter les vues
      if (post.value.id) {
        await blogService.incrementViews(post.value.id)
        
        // Vérifier si l'article est dans les bookmarks
        const bookmarks = JSON.parse(localStorage.getItem('bookmarks') || '[]')
        if (bookmarks.includes(post.value.id)) {
          isBookmarked.value = true
        }
      }
    }
    
    // Récupérer tous les articles pour la navigation
    const allResponse = await blogService.getAllPosts()
    allPosts.value = Array.isArray(allResponse) ? allResponse : allResponse?.results || []
    
  } catch (error) {
    console.error('Erreur chargement article:', error)
    post.value = null
  } finally {
    loading.value = false
  }
}

// Navigation entre articles
const currentIndex = computed(() => {
  return allPosts.value.findIndex(p => p.slug === post.value?.slug)
})

const prevPost = computed(() => {
  if (currentIndex.value > 0) {
    return allPosts.value[currentIndex.value - 1]
  }
  return null
})

const nextPost = computed(() => {
  if (currentIndex.value < allPosts.value.length - 1) {
    return allPosts.value[currentIndex.value + 1]
  }
  return null
})

// Aller à un article
const goToPost = (post) => {
  router.push({ name: 'blog-post', params: { slug: post.slug } })
}

// Formater la date
const formatDate = (dateString) => {
  if (!dateString) return ''
  return new Date(dateString).toLocaleDateString('fr-FR', {
    day: 'numeric',
    month: 'long',
    year: 'numeric'
  })
}

// Temps de lecture
const readingTime = computed(() => {
  if (!post.value?.content) return 0
  const wordsPerMinute = 200
  const words = post.value.content.trim().split(/\s+/).length
  return Math.ceil(words / wordsPerMinute)
})

// Bookmark
const toggleBookmark = () => {
  isBookmarked.value = !isBookmarked.value
  // Sauvegarder dans localStorage
  if (!post.value) return
  
  const bookmarks = JSON.parse(localStorage.getItem('bookmarks') || '[]')
  if (isBookmarked.value) {
    if (!bookmarks.includes(post.value.id)) {
      bookmarks.push(post.value.id)
    }
  } else {
    const index = bookmarks.indexOf(post.value.id)
    if (index > -1) bookmarks.splice(index, 1)
  }
  localStorage.setItem('bookmarks', JSON.stringify(bookmarks))
}

// Partager
const shareArticle = (platform) => {
  const url = window.location.href
  const title = post.value?.title || ''
  
  switch (platform.name) {
    case 'Twitter':
      window.open(`https://twitter.com/intent/tweet?text=${encodeURIComponent(title)}&url=${encodeURIComponent(url)}`, '_blank')
      break
    case 'LinkedIn':
      window.open(`https://www.linkedin.com/sharing/share-offsite/?url=${encodeURIComponent(url)}`, '_blank')
      break
    case 'Facebook':
      window.open(`https://www.facebook.com/sharer/sharer.php?u=${encodeURIComponent(url)}`, '_blank')
      break
    case 'Copier le lien':
      navigator.clipboard.writeText(url)
      alert('Lien copié dans le presse-papier !')
      break
  }
}

// Initialisation
onMounted(() => {
  fetchPost()
})

// Observer les changements de route (pour la navigation entre articles)
watch(
  () => route.params.slug,
  (newSlug) => {
    if (newSlug) {
      fetchPost()
      window.scrollTo({ top: 0, behavior: 'smooth' })
    }
  }
)
</script>

<style>
/* Styles pour le contenu de l'article */
.prose {
  color: #374151;
}

.prose.dark\:prose-invert {
  color: #D1D5DB;
}

.prose img {
  border-radius: 0.5rem;
  margin: 1.5rem auto;
}

.prose h2 {
  font-size: 1.875rem;
  font-weight: 700;
  margin-top: 2rem;
  margin-bottom: 1rem;
}

.prose h3 {
  font-size: 1.5rem;
  font-weight: 600;
  margin-top: 1.5rem;
  margin-bottom: 0.75rem;
}

.prose code {
  background-color: #F3F4F6;
  padding: 0.25rem 0.5rem;
  border-radius: 0.25rem;
  font-family: 'Monaco', 'Menlo', 'Ubuntu Mono', monospace;
}

.dark .prose code {
  background-color: #374151;
}
</style>