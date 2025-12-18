<template>
  <section id="blog-preview" class="py-8 bg-gray-50 dark:bg-gray-900">
    <div class="container mx-auto px-4 sm:px-6 lg:px-8">
      <div class="text-center mb-6" data-aos="fade-up">
        <h2 class="section-title">{{ locale === 'fr' ? 'Mon Blog Technique' : 'My Technical Blog' }}</h2>
        <p class="section-subtitle text-lg">
          {{ locale === 'fr' ? 'Partages d\'expériences, tutoriels et bonnes pratiques' : 'Experience sharing, tutorials and best practices' }}
        </p>
      </div>

      <!-- Chargement -->
      <div v-if="loading" class="text-center py-10">
        <div class="inline-block animate-spin rounded-full h-10 w-10 border-t-2 border-b-2 border-primary-600"></div>
      </div>

      <!-- Articles -->
      <div v-else class="grid grid-cols-1 md:grid-cols-3 gap-6">
        <div 
          v-for="(post, index) in latestPosts"
          :key="post.id"
          class="card hover:scale-[1.02] hover:-translate-y-2 transition-all duration-500 shadow-lg hover:shadow-2xl hover:shadow-primary-500/20 group cursor-pointer overflow-hidden border border-gray-100 dark:border-gray-800 bg-white/80 dark:bg-gray-800/80 backdrop-blur-sm hover:border-primary-500/50 hover:bg-white dark:hover:bg-gray-800 rounded-2xl"
          data-aos="fade-up"
          :data-aos-delay="index * 100"
        >
          <!-- Image (si disponible) -->
          <div class="h-32 overflow-hidden relative">
            <div class="absolute inset-0 bg-gradient-to-t from-gray-900/80 to-transparent z-10 opacity-60 group-hover:opacity-40 transition-opacity duration-500"></div>
            <img 
              v-if="post.image" 
              :src="post.image" 
              :alt="post.title"
              class="w-full h-full object-cover transform group-hover:scale-110 transition-transform duration-700"
            />
            <div v-else class="w-full h-full bg-gradient-to-br from-gray-800 to-gray-900 flex items-center justify-center group-hover:scale-110 transition-transform duration-700">
              <PencilSquareIcon class="w-12 h-12 text-gray-500" />
            </div>
            
            <!-- Date et Catégorie sur l'image -->
            <div class="absolute top-3 right-3 z-20">
              <span class="px-2.5 py-1 bg-primary-600/90 text-white text-[10px] uppercase font-bold tracking-wide rounded-full backdrop-blur-sm shadow-lg">
                {{ post.category?.name || (locale === 'fr' ? 'Général' : 'General') }}
              </span>
            </div>
            
            <div class="absolute bottom-3 left-3 z-20">
              <span class="text-[10px] text-gray-200 font-mono bg-black/50 px-2 py-0.5 rounded backdrop-blur-sm">
                {{ formatDate(post.published_date) }}
              </span>
            </div>
          </div>

          <div class="p-3">
            <!-- Titre -->
            <h3 class="text-base font-bold text-gray-900 dark:text-white mb-1.5 group-hover:text-primary-600 transition-colors line-clamp-1">
              {{ post.title }}
            </h3>

            <!-- Extrait -->
            <p class="text-gray-600 dark:text-gray-400 mb-3 line-clamp-2 text-[11px] leading-relaxed">
              {{ post.excerpt || post.content.substring(0, 150) + '...' }}
            </p>

            <!-- Stats et Bouton -->
            <div class="flex items-center justify-between mt-auto">
              <div class="flex items-center text-[9px] text-gray-500 font-mono">
                <span class="mr-3 flex items-center"><EyeIcon class="w-3 h-3 mr-1" /> {{ post.views || 0 }}</span>
                <span class="flex items-center"><ClockIcon class="w-3 h-3 mr-1" /> {{ timeAgo(post.published_date) }}</span>
              </div>

              <router-link 
                :to="{ name: 'blog-post', params: { slug: post.slug } }"
                class="inline-flex items-center text-primary-600 hover:text-primary-700 font-medium text-xs group/btn"
              >
                {{ locale === 'fr' ? 'Lire' : 'Read' }}
                <ArrowRightIcon class="w-3.5 h-3.5 ml-1 transform group-hover/btn:translate-x-1 transition-transform" />
              </router-link>
            </div>
          </div>
        </div>

        <!-- CTA si pas d'articles -->
        <div 
          v-if="latestPosts.length === 0"
          class="md:col-span-3 card text-center py-8"
        >
          <div class="mb-3 flex justify-center">
            <PencilSquareIcon class="w-16 h-16 text-gray-300 dark:text-gray-600" />
          </div>
          <h3 class="text-lg font-bold text-gray-900 dark:text-white mb-2">
            {{ locale === 'fr' ? 'Aucun article pour le moment' : 'No articles yet' }}
          </h3>
          <p class="text-gray-600 dark:text-gray-400 mb-4 text-sm">
            {{ locale === 'fr' ? 'Les articles du blog seront bientôt disponibles !' : 'Blog articles coming soon!' }}
          </p>
          <router-link to="/blog" class="btn-primary text-sm px-4 py-2">
            {{ locale === 'fr' ? 'Voir le blog' : 'View blog' }}
          </router-link>
        </div>
      </div>

      <!-- Bouton vers blog complet -->
      <div class="text-center mt-10" data-aos="fade-up">
        <router-link to="/blog" class="inline-flex items-center gap-3 px-6 py-3.5 bg-gradient-to-r from-primary-600 to-purple-600 text-white font-black rounded-2xl shadow-xl shadow-primary-500/30 hover:shadow-2xl hover:shadow-primary-500/50 hover:scale-105 transition-all duration-300 group">
          <span>{{ locale === 'fr' ? 'Voir tous les articles' : 'View all articles' }}</span>
          <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="3" stroke="currentColor" class="w-5 h-5 group-hover:translate-x-2 transition-transform">
            <path stroke-linecap="round" stroke-linejoin="round" d="M13.5 4.5L21 12m0 0l-7.5 7.5M21 12H3" />
          </svg>
        </router-link>
      </div>
    </div>
  </section>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { blogService } from '@/services/api'
import { ArrowRightIcon, PencilSquareIcon, EyeIcon, ClockIcon } from '@heroicons/vue/24/outline'
import { useI18n } from 'vue-i18n'

const { t, locale } = useI18n()

const latestPosts = ref([])
const loading = ref(true)

// Formater la date
const formatDate = (dateString) => {
  if (!dateString) return ''
  const date = new Date(dateString)
  return date.toLocaleDateString('fr-FR', {
    day: 'numeric',
    month: 'long',
    year: 'numeric'
  })
}

// Temps écoulé
const timeAgo = (dateString) => {
  if (!dateString) return ''
  const date = new Date(dateString)
  const now = new Date()
  const diffMs = now - date
  const diffDays = Math.floor(diffMs / (1000 * 60 * 60 * 24))
  
  if (locale.value === 'fr') {
    if (diffDays === 0) return "Aujourd'hui"
    if (diffDays === 1) return 'Hier'
    if (diffDays < 7) return `Il y a ${diffDays} jours`
    if (diffDays < 30) return `Il y a ${Math.floor(diffDays / 7)} semaines`
    if (diffDays < 365) return `Il y a ${Math.floor(diffDays / 30)} mois`
    return `Il y a ${Math.floor(diffDays / 365)} ans`
  } else {
    if (diffDays === 0) return "Today"
    if (diffDays === 1) return 'Yesterday'
    if (diffDays < 7) return `${diffDays} days ago`
    if (diffDays < 30) return `${Math.floor(diffDays / 7)} weeks ago`
    if (diffDays < 365) return `${Math.floor(diffDays / 30)} months ago`
    return `${Math.floor(diffDays / 365)} years ago`
  }
}

// Récupérer les articles
const fetchLatestPosts = async () => {
  try {
    loading.value = true
    const response = await blogService.getLatestPosts(3)
    
    if (Array.isArray(response)) {
      latestPosts.value = response
    } else if (response && response.results) {
      latestPosts.value = response.results
    } else {
      latestPosts.value = []
    }
  } catch (err) {
    console.error('Erreur chargement articles:', err)
    latestPosts.value = []
  } finally {
    loading.value = false
  }
}

onMounted(() => {
  fetchLatestPosts()
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

.line-clamp-3 {
  display: -webkit-box;
  -webkit-line-clamp: 3;
  line-clamp: 3;
  -webkit-box-orient: vertical;
  overflow: hidden;
}
</style>