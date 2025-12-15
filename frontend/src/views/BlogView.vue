<template>
  <div class="min-h-screen">
    <div class="pt-24 pb-16">
      <div class="container mx-auto px-4 sm:px-6 lg:px-8">
        <!-- En-tête avec recherche -->
        <div class="text-center mb-12">
          <h1 class="text-4xl md:text-5xl font-bold text-gray-900 dark:text-white mb-4">
            Blog Technique
          </h1>
          <p class="text-xl text-gray-600 dark:text-gray-400 max-w-2xl mx-auto mb-8">
            Tutoriels, bonnes pratiques et retours d'expérience
          </p>
          
          <!-- Barre de recherche -->
          <div class="max-w-xl mx-auto">
            <div class="relative">
              <input
                v-model="searchQuery"
                @input="searchPosts"
                type="text"
                placeholder="Rechercher un article..."
                class="w-full px-6 py-3 rounded-xl bg-white dark:bg-gray-800 border border-gray-300 dark:border-gray-700 focus:ring-2 focus:ring-primary-500 focus:border-transparent pl-12"
              />
              <MagnifyingGlassIcon class="absolute left-4 top-3.5 w-5 h-5 text-gray-400" />
            </div>
          </div>
        </div>

        <!-- Contenu principal -->
        <div class="grid grid-cols-1 lg:grid-cols-4 gap-8">
          <!-- Articles -->
          <div class="lg:col-span-3">
            <!-- Filtres -->
            <div class="flex flex-wrap gap-2 mb-8">
              <button
                @click="filterByCategory('all')"
                :class="[
                  'px-4 py-2 rounded-full font-medium transition-all',
                  activeCategory === 'all'
                    ? 'bg-primary-600 text-white'
                    : 'bg-gray-200 dark:bg-gray-800 text-gray-700 dark:text-gray-300 hover:bg-gray-300 dark:hover:bg-gray-700'
                ]"
              >
                Tous
              </button>
              <button
                v-for="category in categories"
                :key="category.id"
                @click="filterByCategory(category.slug)"
                :class="[
                  'px-4 py-2 rounded-full font-medium transition-all',
                  activeCategory === category.slug
                    ? 'bg-primary-600 text-white'
                    : 'bg-gray-200 dark:bg-gray-800 text-gray-700 dark:text-gray-300 hover:bg-gray-300 dark:hover:bg-gray-700'
                ]"
              >
                {{ category.name }}
              </button>
            </div>

            <!-- Articles list -->
            <div v-if="loading" class="text-center py-12">
              <div class="inline-block animate-spin rounded-full h-12 w-12 border-t-2 border-b-2 border-primary-600"></div>
            </div>

            <div v-else-if="filteredPosts.length === 0" class="text-center py-12">
              <div class="text-5xl mb-4">📭</div>
              <h3 class="text-xl font-semibold text-gray-900 dark:text-white mb-2">
                Aucun article trouvé
              </h3>
              <p class="text-gray-600 dark:text-gray-400">
                {{ searchQuery ? 'Aucun résultat pour votre recherche' : 'Aucun article publié pour le moment' }}
              </p>
            </div>

            <div v-else class="space-y-8">
              <article
                v-for="post in filteredPosts"
                :key="post.id"
                class="card hover:shadow-2xl hover:-translate-y-1 transition-all duration-500 group cursor-pointer"
              >
                <div class="flex flex-col md:flex-row gap-6">
                  <!-- Image -->
                  <div class="md:w-1/3">
                    <div class="aspect-video rounded-lg overflow-hidden bg-gradient-to-br from-primary-100 to-purple-100 dark:from-gray-800 dark:to-gray-900 relative">
                      <img
                        v-if="post.image"
                        :src="post.image"
                        :alt="post.title"
                        class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-700"
                      />
                      <div v-else class="w-full h-full flex items-center justify-center">
                        <span class="text-4xl group-hover:scale-125 transition-transform duration-300">📝</span>
                      </div>
                      <!-- Overlay au survol -->
                      <div class="absolute inset-0 bg-gradient-to-t from-primary-600/20 to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-500"></div>
                    </div>
                  </div>

                  <!-- Contenu -->
                  <div class="md:w-2/3">
                    <div class="flex items-center justify-between mb-3">
                      <span class="px-3 py-1 bg-primary-100 dark:bg-primary-900/30 text-primary-700 dark:text-primary-300 text-sm rounded-full">
                        {{ post.category?.name || 'Général' }}
                      </span>
                      <span class="text-sm text-gray-500">
                        {{ formatDate(post.published_date) }}
                      </span>
                    </div>

                    <h2 class="text-2xl font-bold text-gray-900 dark:text-white mb-3 group-hover:text-primary-600 transition-colors">
                      {{ post.title }}
                    </h2>

                    <p class="text-gray-600 dark:text-gray-400 mb-4 line-clamp-2">
                      {{ post.excerpt || post.content.substring(0, 200) + '...' }}
                    </p>

                    <div class="flex items-center justify-between">
                      <div class="flex items-center text-sm text-gray-500">
                        <span class="mr-4">👁️ {{ post.views || 0 }} vues</span>
                        <span>⏱️ {{ readingTime(post.content) }} min</span>
                      </div>
                      <router-link
                        :to="{ name: 'blog-post', params: { slug: post.slug } }"
                        class="inline-flex items-center text-primary-600 hover:text-primary-700 font-medium"
                      >
                        Lire l'article
                        <ArrowRightIcon class="w-4 h-4 ml-2 group-hover:translate-x-1 transition-transform" />
                      </router-link>
                    </div>
                  </div>
                </div>
              </article>
            </div>

            <!-- Pagination -->
            <div v-if="totalPages > 1" class="flex justify-center items-center space-x-2 mt-12">
              <button
                @click="prevPage"
                :disabled="currentPage === 1"
                class="px-4 py-2 rounded-lg bg-gray-200 dark:bg-gray-800 text-gray-700 dark:text-gray-300 disabled:opacity-50 disabled:cursor-not-allowed"
              >
                Précédent
              </button>
              <span class="px-4 py-2">
                Page {{ currentPage }} sur {{ totalPages }}
              </span>
              <button
                @click="nextPage"
                :disabled="currentPage === totalPages"
                class="px-4 py-2 rounded-lg bg-gray-200 dark:bg-gray-800 text-gray-700 dark:text-gray-300 disabled:opacity-50 disabled:cursor-not-allowed"
              >
                Suivant
              </button>
            </div>
          </div>

          <!-- Sidebar -->
          <div class="lg:col-span-1">
            <div class="sticky top-24 space-y-6">
              <!-- À propos -->
              <div class="card">
                <h3 class="text-lg font-bold text-gray-900 dark:text-white mb-3">
                  À propos du blog
                </h3>
                <p class="text-gray-600 dark:text-gray-400 text-sm">
                  Je partage ici mes découvertes, solutions techniques et bonnes pratiques en développement web. 
                  Chaque article est basé sur des expériences réelles.
                </p>
              </div>

              <!-- Catégories -->
              <div class="card">
                <h3 class="text-lg font-bold text-gray-900 dark:text-white mb-3">
                  Catégories
                </h3>
                <div class="space-y-2">
                  <button
                    v-for="category in categories"
                    :key="category.id"
                    @click="filterByCategory(category.slug)"
                    class="flex items-center justify-between w-full text-left text-gray-600 dark:text-gray-400 hover:text-primary-600 dark:hover:text-primary-400 transition-colors"
                  >
                    <span>{{ category.name }}</span>
                    <span class="text-sm bg-gray-100 dark:bg-gray-800 px-2 py-1 rounded">
                      {{ getCategoryCount(category.slug) }}
                    </span>
                  </button>
                </div>
              </div>

              <!-- Articles populaires -->
              <div class="card">
                <h3 class="text-lg font-bold text-gray-900 dark:text-white mb-3">
                  Articles populaires
                </h3>
                <div class="space-y-4">
                  <div
                    v-for="post in popularPosts"
                    :key="post.id"
                    class="flex items-center space-x-3 group cursor-pointer"
                    @click="$router.push({ name: 'blog-post', params: { slug: post.slug } })"
                  >
                    <div class="flex-shrink-0 w-12 h-12 rounded-lg bg-gradient-to-br from-primary-100 to-purple-100 dark:from-gray-800 dark:to-gray-900 flex items-center justify-center">
                      <span class="text-lg">🔥</span>
                    </div>
                    <div>
                      <h4 class="font-medium text-gray-900 dark:text-white group-hover:text-primary-600 transition-colors text-sm line-clamp-2">
                        {{ post.title }}
                      </h4>
                      <p class="text-xs text-gray-500">{{ post.views }} vues</p>
                    </div>
                  </div>
                </div>
              </div>

            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted, watch } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { blogService } from '@/services/api'
import { MagnifyingGlassIcon, ArrowRightIcon } from '@heroicons/vue/24/outline'


const route = useRoute()
const router = useRouter()

// États
const posts = ref([])
const categories = ref([])
const popularPosts = ref([])
const loading = ref(true)
const searchQuery = ref('')
const activeCategory = ref('all')
const currentPage = ref(1)
const postsPerPage = 6

// Récupérer les données
const fetchData = async () => {
  try {
    loading.value = true
    
    // Articles
    const postsResponse = await blogService.getAllPosts()
    posts.value = Array.isArray(postsResponse) ? postsResponse : postsResponse?.results || []
    
    // Catégories
    const categoriesResponse = await blogService.getCategories()
    categories.value = Array.isArray(categoriesResponse) ? categoriesResponse : categoriesResponse?.results || []
    
    // Articles populaires (triés par vues)
    popularPosts.value = [...posts.value]
      .sort((a, b) => (b.views || 0) - (a.views || 0))
      .slice(0, 3)
      
  } catch (error) {
    console.error('Erreur chargement blog:', error)
  } finally {
    loading.value = false
  }
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

// Temps de lecture estimé
const readingTime = (content) => {
  if (!content) return 0
  const wordsPerMinute = 200
  const words = content.trim().split(/\s+/).length
  return Math.ceil(words / wordsPerMinute)
}

// Filtrer les articles
const filteredPosts = computed(() => {
  let filtered = [...posts.value]
  
  // Filtre par catégorie
  if (activeCategory.value !== 'all') {
    filtered = filtered.filter(post => post.category?.slug === activeCategory.value)
  }
  
  // Filtre par recherche
  if (searchQuery.value) {
    const query = searchQuery.value.toLowerCase()
    filtered = filtered.filter(post => 
      post.title?.toLowerCase().includes(query) ||
      post.excerpt?.toLowerCase().includes(query) ||
      post.content?.toLowerCase().includes(query)
    )
  }
  
  // Pagination
  const start = (currentPage.value - 1) * postsPerPage
  const end = start + postsPerPage
  return filtered.slice(start, end)
})

// Pagination
const totalFilteredPosts = computed(() => {
  let filtered = [...posts.value]
  
  if (activeCategory.value !== 'all') {
    filtered = filtered.filter(post => post.category?.slug === activeCategory.value)
  }
  
  if (searchQuery.value) {
    const query = searchQuery.value.toLowerCase()
    filtered = filtered.filter(post => 
      post.title?.toLowerCase().includes(query) ||
      post.excerpt?.toLowerCase().includes(query) ||
      post.content?.toLowerCase().includes(query)
    )
  }
  
  return filtered
})

const totalPages = computed(() => {
  return Math.ceil(totalFilteredPosts.value.length / postsPerPage)
})

// Compter les articles par catégorie
const getCategoryCount = (categorySlug) => {
  return posts.value.filter(post => post.category?.slug === categorySlug).length
}


const nextPage = () => {
  if (currentPage.value < totalPages.value) {
    currentPage.value++
    window.scrollTo({ top: 0, behavior: 'smooth' })
  }
}

const prevPage = () => {
  if (currentPage.value > 1) {
    currentPage.value--
    window.scrollTo({ top: 0, behavior: 'smooth' })
  }
}

// Filtre par catégorie
const filterByCategory = (categorySlug) => {
  activeCategory.value = categorySlug
  currentPage.value = 1
}

// Recherche
const searchPosts = () => {
  currentPage.value = 1
}

// Initialisation
onMounted(() => {
  fetchData()
  
  // Vérifier si une catégorie est spécifiée dans l'URL
  if (route.query.category) {
    activeCategory.value = route.query.category
  }
})

// Watch pour mettre à jour l'URL
watch(activeCategory, (newCategory) => {
  router.push({ 
    query: { 
      ...route.query, 
      category: newCategory !== 'all' ? newCategory : undefined 
    }
  })
})
</script>

<style>
.line-clamp-2 {
  display: -webkit-box;
  -webkit-line-clamp: 2;
  line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
}
</style>