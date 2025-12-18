<template>
  <section id="projects" class="py-8 bg-gray-50 dark:bg-gray-900 relative overflow-hidden">
    <!-- Background decorative elements -->
    <div class="absolute inset-0 overflow-hidden pointer-events-none">
      <div class="absolute top-20 -right-20 w-96 h-96 bg-primary-500/5 dark:bg-primary-500/10 rounded-full blur-3xl"></div>
      <div class="absolute bottom-20 -left-20 w-96 h-96 bg-purple-500/5 dark:bg-purple-500/10 rounded-full blur-3xl"></div>
    </div>

    <div class="container mx-auto px-4 sm:px-6 lg:px-8 relative z-10">
      <div v-if="!limit" class="text-center mb-8" data-aos="fade-up">
        <div class="inline-block mb-4">
          <span class="px-4 py-1.5 bg-primary-100 dark:bg-primary-900/30 text-primary-700 dark:text-primary-300 text-sm font-bold rounded-full border border-primary-200 dark:border-primary-800 flex items-center gap-2">
            <BriefcaseIcon class="w-4 h-4" /> PORTFOLIO
          </span>
        </div>
        <h2 class="text-4xl md:text-5xl lg:text-6xl font-black text-gray-900 dark:text-white mb-4 tracking-tight">
          {{ locale === 'fr' ? 'Mes Projets' : 'My Projects' }} <span class="text-transparent bg-clip-text bg-gradient-to-r from-primary-600 to-purple-600">{{ locale === 'fr' ? 'Récents' : 'Recent' }}</span>
        </h2>
        <p class="text-lg md:text-xl text-gray-600 dark:text-gray-400 max-w-2xl mx-auto">
          {{ locale === 'fr' ? 'Découvrez mes réalisations en développement web full-stack' : 'Discover my full-stack web development achievements' }}
        </p>
      </div>
      <div v-else class="text-center mb-8" data-aos="fade-up">
        <h2 class="section-title">
          {{ locale === 'fr' ? 'Quelques' : 'Some' }} <span class="text-transparent bg-clip-text bg-gradient-to-r from-primary-600 to-purple-600">{{ locale === 'fr' ? 'Réalisations' : 'Achievements' }}</span>
        </h2>
        <p class="text-lg text-gray-600 dark:text-gray-400">
          {{ locale === 'fr' ? 'Un aperçu de mon travail' : 'A glimpse of my work' }}
        </p>
      </div>

      <!-- Chargement -->
      <div v-if="loading" class="text-center py-20">
        <div class="inline-block relative">
          <div class="animate-spin rounded-full h-16 w-16 border-4 border-gray-200 dark:border-gray-800 border-t-primary-600"></div>
          <div class="absolute inset-0 flex items-center justify-center">
            <div class="w-8 h-8 bg-primary-600 rounded-full animate-pulse"></div>
          </div>
        </div>
        <p class="mt-6 text-gray-600 dark:text-gray-400 font-mono text-sm">{{ locale === 'fr' ? 'Chargement des projets...' : 'Loading projects...' }}</p>
      </div>

      <!-- Erreur -->
      <div v-else-if="error" class="text-center py-20">
        <div class="inline-block p-4 bg-red-100 dark:bg-red-900/20 rounded-2xl mb-4">
          <svg class="w-12 h-12 text-red-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z"/>
          </svg>
        </div>
        <h3 class="text-xl font-bold text-gray-900 dark:text-white mb-2">{{ locale === 'fr' ? 'Erreur de chargement' : 'Loading Error' }}</h3>
        <p class="text-gray-600 dark:text-gray-400 mb-6">{{ error }}</p>
        <button @click="fetchProjects" class="btn-primary px-6 py-3 rounded-xl font-semibold hover:scale-105 transition-transform">
          🔄 {{ locale === 'fr' ? 'Réessayer' : 'Retry' }}
        </button>
      </div>

      <!-- Projets -->
      <div v-else>
        <!-- Filtres (Masqués si limit est défini) -->
        <div v-if="!limit" class="flex flex-wrap justify-center gap-3 mb-8" data-aos="fade-up">
          <button 
            @click="filter = 'all'"
            :class="[
              'px-5 py-2.5 text-sm font-bold rounded-xl transition-all duration-300 border-2',
              filter === 'all' 
                ? 'bg-primary-600 text-white border-primary-600 shadow-lg shadow-primary-500/30 scale-105' 
                : 'bg-white dark:bg-gray-800 text-gray-700 dark:text-gray-300 border-gray-200 dark:border-gray-700 hover:border-primary-500 hover:scale-105'
            ]"
          >
            <SparklesIcon class="w-4 h-4 inline mr-1" /> {{ locale === 'fr' ? 'Tous' : 'All' }}
          </button>
          <button 
            v-for="cat in categories"
            :key="cat"
            @click="filter = cat"
            :class="[
              'px-5 py-2.5 text-sm font-bold rounded-xl transition-all duration-300 border-2',
              filter === cat 
                ? 'bg-primary-600 text-white border-primary-600 shadow-lg shadow-primary-500/30 scale-105' 
                : 'bg-white dark:bg-gray-800 text-gray-700 dark:text-gray-300 border-gray-200 dark:border-gray-700 hover:border-primary-500 hover:scale-105'
            ]"
          >
            <component :is="getCategoryIcon(cat)" class="w-4 h-4 inline mr-2" /> {{ cat }}
          </button>
        </div>

        <!-- Grille Simple et Uniforme -->
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6" data-aos="fade-up">
          <div 
            v-for="(project, index) in filteredProjects" 
            :key="project.id"
            class="card hover:scale-[1.02] hover:-translate-y-2 transition-all duration-500 shadow-lg hover:shadow-2xl hover:shadow-primary-500/20 group cursor-pointer overflow-hidden border border-gray-100 dark:border-gray-800 bg-white/80 dark:bg-gray-800/80 backdrop-blur-sm hover:border-primary-500/50 hover:bg-white dark:hover:bg-gray-800 rounded-2xl"
            data-aos="fade-up"
            :data-aos-delay="index * 100"
          >
            <!-- Card Container -->
            <div class="relative h-full">
              
              <!-- Status Badge -->
              <div class="absolute top-3 left-3 z-20 flex gap-1.5">
                <span v-if="project.featured" class="px-2 py-0.5 bg-gradient-to-r from-yellow-400 to-orange-500 text-white text-[10px] font-black rounded-full shadow-lg flex items-center gap-1">
                  <StarIcon class="w-3 h-3 fill-current" /> FEATURED
                </span>
                <span v-if="project.live_url" class="px-2 py-0.5 bg-green-500 text-white text-[10px] font-black rounded-full shadow-lg flex items-center gap-1 animate-pulse">
                  <span class="w-1.5 h-1.5 bg-white rounded-full"></span>
                  LIVE
                </span>
              </div>

              <!-- Category Badge -->
              <div class="absolute top-3 right-3 z-20">
                <span class="px-2 py-1 bg-gray-900/80 dark:bg-white/90 backdrop-blur-sm text-white dark:text-gray-900 text-[10px] font-black rounded-full border border-white/20 shadow-lg">
                  {{ getCategoryLabel(project.category) }}
                </span>
              </div>

              <!-- Image Container -->
              <div class="h-32 overflow-hidden relative bg-gradient-to-br from-primary-100 via-purple-100 to-pink-100 dark:from-gray-900 dark:via-gray-800 dark:to-gray-900">
                <div v-if="project.image" class="w-full h-full">
                  <img 
                    :src="project.image" 
                    :alt="project.title"
                    class="w-full h-full object-cover transform group-hover:scale-110 transition-transform duration-700"
                  />
                </div>
                <div v-else class="w-full h-full bg-gradient-to-br from-gray-800 to-gray-900 flex items-center justify-center group-hover:scale-110 transition-transform duration-700">
                  <RocketLaunchIcon class="w-12 h-12 text-gray-500" />
                </div>
                
                <!-- Gradient Overlay -->
                <div class="absolute inset-0 bg-gradient-to-t from-black/80 via-black/20 to-transparent opacity-60 group-hover:opacity-80 transition-opacity duration-500"></div>
                
                <!-- Quick Actions Overlay -->
                <div class="absolute inset-0 flex items-center justify-center gap-3 opacity-0 group-hover:opacity-100 transition-all duration-300">
                  <a 
                    v-if="project.github_url"
                    :href="project.github_url"
                    target="_blank"
                    @click.stop
                    class="p-4 bg-white dark:bg-gray-900 rounded-2xl shadow-xl hover:scale-110 transition-transform duration-300 group/btn"
                  >
                    <svg class="w-6 h-6 text-gray-900 dark:text-white" fill="currentColor" viewBox="0 0 24 24">
                      <path fill-rule="evenodd" d="M12 2C6.477 2 2 6.484 2 12.017c0 4.425 2.865 8.18 6.839 9.504.5.092.682-.217.682-.483 0-.237-.008-.868-.013-1.703-2.782.605-3.369-1.343-3.369-1.343-.454-1.158-1.11-1.466-1.11-1.466-.908-.62.069-.608.069-.608 1.003.07 1.531 1.032 1.531 1.032.892 1.53 2.341 1.088 2.91.832.092-.647.35-1.088.636-1.338-2.22-.253-4.555-1.113-4.555-4.951 0-1.093.39-1.988 1.029-2.688-.103-.253-.446-1.272.098-2.65 0 0 .84-.27 2.75 1.026A9.564 9.564 0 0112 6.844c.85.004 1.705.115 2.504.337 1.909-1.296 2.747-1.027 2.747-1.027.546 1.379.202 2.398.1 2.651.64.7 1.028 1.595 1.028 2.688 0 3.848-2.339 4.695-4.566 4.943.359.309.678.92.678 1.855 0 1.338-.012 2.419-.012 2.747 0 .268.18.58.688.482A10.019 10.019 0 0022 12.017C22 6.484 17.522 2 12 2z" clip-rule="evenodd" />
                    </svg>
                  </a>
                  <a 
                    v-if="project.live_url"
                    :href="project.live_url"
                    target="_blank"
                    @click.stop
                    class="p-4 bg-primary-600 rounded-2xl shadow-xl hover:scale-110 transition-transform duration-300 group/btn"
                  >
                    <svg class="w-6 h-6 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14"/>
                    </svg>
                  </a>
                </div>
              </div>

              <!-- Content -->
              <div class="p-3">
                <h3 class="text-base md:text-lg font-black text-gray-900 dark:text-white mb-1.5 group-hover:text-primary-600 dark:group-hover:text-primary-400 transition-colors line-clamp-1">
                  {{ project.title }}
                </h3>
                
                <p class="text-gray-600 dark:text-gray-400 mb-2 line-clamp-1 text-[11px] leading-relaxed">
                  {{ project.short_description || project.description }}
                </p>

                <!-- Technologies -->
                <div class="flex flex-wrap gap-1.5 mb-3">
                  <span 
                    v-for="tech in (project.technologies_list || [project.technologies]).slice(0, 3)"
                    :key="tech"
                    class="px-2 py-0.5 bg-gray-100 dark:bg-gray-900 text-gray-700 dark:text-gray-300 text-[10px] font-bold rounded-md border border-gray-200 dark:border-gray-700 hover:border-primary-500 hover:text-primary-600 dark:hover:text-primary-400 transition-colors"
                  >
                    {{ tech.trim() }}
                  </span>
                </div>

                <!-- Stats (si disponibles) -->
                <div v-if="project.stats" class="grid grid-cols-3 gap-1.5 pt-2 border-t border-gray-200 dark:border-gray-700">
                  <div class="text-center">
                    <div class="text-xs font-black text-primary-600">{{ project.stats.stars || '0' }}</div>
                    <div class="text-[9px] text-gray-500">Stars</div>
                  </div>
                  <div class="text-center">
                    <div class="text-xs font-black text-purple-600">{{ project.stats.forks || '0' }}</div>
                    <div class="text-[9px] text-gray-500">Forks</div>
                  </div>
                  <div class="text-center">
                    <div class="text-xs font-black text-green-600">{{ project.stats.commits || '0' }}</div>
                    <div class="text-[9px] text-gray-500">Commits</div>
                  </div>
                </div>
              </div>

              <!-- Hover Effect Border -->
              <div class="absolute inset-0 rounded-3xl opacity-0 group-hover:opacity-100 transition-opacity duration-500 pointer-events-none">
                <div class="absolute inset-0 rounded-3xl bg-gradient-to-r from-primary-500 via-purple-500 to-pink-500 blur-xl opacity-30"></div>
              </div>
            </div>
          </div>
        </div>

        <!-- Bouton Voir Tout (si limit est actif) -->
        <div v-if="limit && projects.length > limit" class="text-center mt-10" data-aos="fade-up">
          <router-link to="/projects" class="inline-flex items-center gap-3 px-6 py-3.5 bg-gradient-to-r from-primary-600 to-purple-600 text-white font-black rounded-2xl shadow-xl shadow-primary-500/30 hover:shadow-2xl hover:shadow-primary-500/50 hover:scale-105 transition-all duration-300 group">
            <span>{{ locale === 'fr' ? 'Voir tous les projets' : 'View all projects' }}</span>
            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="3" stroke="currentColor" class="w-5 h-5 group-hover:translate-x-2 transition-transform">
              <path stroke-linecap="round" stroke-linejoin="round" d="M13.5 4.5L21 12m0 0l-7.5 7.5M21 12H3" />
            </svg>
          </router-link>
        </div>

        <!-- Message si aucun projet -->
        <div v-if="filteredProjects.length === 0" class="text-center py-20" data-aos="fade-up">
          <div class="inline-block p-8 bg-gray-100 dark:bg-gray-800 rounded-3xl mb-6">
            <InboxIcon class="w-16 h-16 text-gray-400" />
          </div>
          <h3 class="text-2xl font-black text-gray-900 dark:text-white mb-3">
            {{ locale === 'fr' ? 'Aucun projet trouvé' : 'No projects found' }}
          </h3>
          <p class="text-gray-600 dark:text-gray-400 text-lg">
            {{ filter === 'all' 
              ? (locale === 'fr' ? 'Ajoutez des projets dans l\'admin Django' : 'Add projects in Django admin')
              : (locale === 'fr' ? 'Aucun projet dans cette catégorie' : 'No projects in this category')
            }}
          </p>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { projectService } from '@/services/api'
import { useI18n } from 'vue-i18n'
import { 
  BriefcaseIcon, SparklesIcon, RocketLaunchIcon, InboxIcon, StarIcon,
  GlobeAltIcon, DevicePhoneMobileIcon, CpuChipIcon, PaintBrushIcon, BoltIcon, CubeIcon 
} from '@heroicons/vue/24/outline'

const { t, locale } = useI18n()

const props = defineProps({
  limit: {
    type: Number,
    default: 0 // 0 means no limit
  }
})

const projects = ref([])
const loading = ref(true)
const error = ref(null)
const filter = ref('all')

// Catégories disponibles
const categories = computed(() => {
  const cats = [...new Set(projects.value.map(p => p.category))]
  return cats.sort()
})

// Projets filtrés
const filteredProjects = computed(() => {
  let result = projects.value
  
  if (filter.value !== 'all') {
    result = result.filter(p => p.category === filter.value)
  }
  
  // Appliquer la limite si elle existe
  if (props.limit > 0) {
    return result.slice(0, props.limit)
  }
  
  return result
})

// Traduction des catégories
const getCategoryLabel = (category) => {
  const labels = {
    'web': 'Web',
    'mobile': 'Mobile',
    'ai': 'IA',
    'design': 'Design',
    'other': 'Autre'
  }
  return labels[category] || category
}

// Icônes des catégories
// Icônes des catégories
const getCategoryIcon = (category) => {
  const icons = {
    'web': GlobeAltIcon,
    'mobile': DevicePhoneMobileIcon,
    'ai': CpuChipIcon,
    'design': PaintBrushIcon,
    'other': BoltIcon
  }
  return icons[category] || CubeIcon
}

// BENTO GRID LOGIC
// Pattern de tailles : large, medium, small, medium, small, large, etc.
const bentoPattern = ['large', 'medium', 'small', 'medium', 'large', 'small', 'medium', 'small', 'large']

const getBentoClass = (index) => {
  const size = bentoPattern[index % bentoPattern.length]
  
  const baseClasses = 'relative transition-all duration-500'
  
  // Classes de grille selon la taille
  const sizeClasses = {
    'large': 'col-span-1 md:col-span-2 row-span-1 md:row-span-2',
    'medium': 'col-span-1 md:col-span-1 row-span-1',
    'small': 'col-span-1 md:col-span-1 row-span-1'
  }
  
  return `${baseClasses} ${sizeClasses[size]}`
}

// Hauteur des images selon la taille de la carte
const getBentoImageHeight = (index) => {
  const size = bentoPattern[index % bentoPattern.length]
  
  const heights = {
    'large': 'h-40 md:h-52',
    'medium': 'h-32 md:h-40',
    'small': 'h-28 md:h-32'
  }
  
  return heights[size]
}

// Effet de hover 3D
const cardTransforms = ref({})

const handleCardHover = (index, event) => {
  // Initialiser la transformation pour cette carte
  cardTransforms.value[index] = { rotateX: 0, rotateY: 0 }
}

const handleCardMove = (index, event) => {
  const card = event.currentTarget
  const rect = card.getBoundingClientRect()
  
  // Calculer la position de la souris relative à la carte
  const x = event.clientX - rect.left
  const y = event.clientY - rect.top
  
  // Calculer la rotation (max ±10 degrés)
  const rotateY = ((x / rect.width) - 0.5) * 20
  const rotateX = ((y / rect.height) - 0.5) * -20
  
  cardTransforms.value[index] = { rotateX, rotateY }
  
  // Appliquer la transformation
  const cardElement = card.querySelector('.relative.h-full')
  if (cardElement) {
    cardElement.style.transform = `perspective(1000px) rotateX(${rotateX}deg) rotateY(${rotateY}deg) scale3d(1.02, 1.02, 1.02)`
  }
}

const handleCardLeave = (index) => {
  cardTransforms.value[index] = { rotateX: 0, rotateY: 0 }
  
  // Réinitialiser la transformation
  const cards = document.querySelectorAll('.bento-item')
  if (cards[index]) {
    const cardElement = cards[index].querySelector('.relative.h-full')
    if (cardElement) {
      cardElement.style.transform = 'perspective(1000px) rotateX(0deg) rotateY(0deg) scale3d(1, 1, 1)'
    }
  }
}

// Récupérer les projets depuis l'API
const fetchProjects = async () => {
  try {
    loading.value = true
    error.value = null
    const response = await projectService.getAllProjects()
    
    // Vérifier la structure de la réponse
    if (Array.isArray(response)) {
      projects.value = response
    } else if (response && response.results) {
      projects.value = response.results
    } else {
      projects.value = []
    }
    
  } catch (err) {
    console.error('Erreur API:', err)
    error.value = 'Impossible de charger les projets. Vérifiez que le serveur Django est en marche sur http://127.0.0.1:8000'
    projects.value = []
  } finally {
    loading.value = false
  }
}

// Charger au montage
onMounted(() => {
  fetchProjects()
})
</script>

<style scoped>
/* BENTO GRID LAYOUT */
.bento-grid {
  display: grid;
  grid-template-columns: repeat(1, 1fr);
  gap: 1.5rem;
  width: 100%;
}

@media (min-width: 768px) {
  .bento-grid {
    grid-template-columns: repeat(2, 1fr);
    grid-auto-rows: minmax(200px, auto);
    gap: 1rem;
  }
}

@media (min-width: 1024px) {
  .bento-grid {
    grid-template-columns: repeat(3, 1fr);
    gap: 1rem;
  }
}

/* Bento Item Animations */
.bento-item {
  transform-style: preserve-3d;
  will-change: transform;
}

.bento-item .relative.h-full {
  transition: transform 0.3s ease-out;
}

/* Smooth hover transitions */
.bento-item:hover {
  z-index: 10;
}

/* Line clamp utilities */
.line-clamp-2 {
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
}

.line-clamp-3 {
  display: -webkit-box;
  -webkit-line-clamp: 3;
  -webkit-box-orient: vertical;
  overflow: hidden;
}

/* Animations personnalisées */
@keyframes float {
  0%, 100% {
    transform: translateY(0px);
  }
  50% {
    transform: translateY(-10px);
  }
}

.bento-item:nth-child(odd) {
  animation: float 6s ease-in-out infinite;
}

.bento-item:nth-child(even) {
  animation: float 8s ease-in-out infinite;
  animation-delay: 1s;
}

/* Désactiver l'animation sur mobile pour les performances */
@media (max-width: 768px) {
  .bento-item {
    animation: none !important;
  }
}
</style>