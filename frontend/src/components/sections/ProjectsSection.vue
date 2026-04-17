<template>
  <section id="projects" class="py-24 bg-gray-50 dark:bg-gray-900 section-diagonal-top">
    <div class="container mx-auto px-6 sm:px-8">

      <!-- Titre stylisé + lien voir tout -->
      <div class="flex flex-wrap items-end justify-between gap-4 mb-12" data-aos="fade-up">
        <h2 class="section-styled-title">
          -{{ locale === 'fr' ? 'Portfolio' : 'Portfolio' }}-
        </h2>
        <router-link v-if="limit" to="/projects"
          class="text-sm text-gray-500 dark:text-gray-400 hover:text-gray-900 dark:hover:text-white transition-colors underline-animated font-medium">
          {{ locale === 'fr' ? 'Voir tout →' : 'View all →' }}
        </router-link>
      </div>

      <!-- Filtres (page complète seulement) -->
      <div v-if="!limit" class="flex flex-wrap gap-2 mb-10" data-aos="fade-up">
        <button
          @click="filter = 'all'"
          class="px-4 py-1.5 text-sm rounded-full border font-medium transition-all duration-200"
          :class="filter === 'all'
            ? 'bg-gray-900 dark:bg-white text-white dark:text-gray-900 border-gray-900 dark:border-white'
            : 'border-gray-300 dark:border-gray-700 text-gray-500 dark:text-gray-400 hover:border-gray-500'"
        >{{ locale === 'fr' ? 'Tout' : 'All' }}</button>
        <button
          v-for="cat in categories" :key="cat"
          @click="filter = cat"
          class="px-4 py-1.5 text-sm rounded-full border font-medium capitalize transition-all duration-200"
          :class="filter === cat
            ? 'bg-gray-900 dark:bg-white text-white dark:text-gray-900 border-gray-900 dark:border-white'
            : 'border-gray-300 dark:border-gray-700 text-gray-500 dark:text-gray-400 hover:border-gray-500'"
        >{{ getCategoryLabel(cat) }}</button>
      </div>

      <!-- Loading -->
      <div v-if="loading" class="flex items-center justify-center py-24">
        <div class="animate-spin w-6 h-6 border-2 border-gray-900 dark:border-white border-t-transparent rounded-full"></div>
      </div>

      <!-- Error -->
      <div v-else-if="error" class="py-16 text-center">
        <p class="text-gray-500 dark:text-gray-400 mb-4">{{ error }}</p>
        <button @click="fetchProjects" class="btn-secondary">
          {{ locale === 'fr' ? 'Réessayer' : 'Retry' }}
        </button>
      </div>

      <!-- Empty -->
      <div v-else-if="filteredProjects.length === 0" class="py-16 text-center">
        <p class="text-gray-400 text-sm">{{ locale === 'fr' ? 'Aucun projet trouvé.' : 'No projects found.' }}</p>
      </div>

      <!-- Grille de projets -->
      <div v-else class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        <div
          v-for="(project, index) in filteredProjects"
          :key="project.id"
          class="project-card group relative rounded-2xl overflow-hidden bg-white dark:bg-gray-950 border border-gray-200 dark:border-gray-800 shadow-sm hover:shadow-xl transition-all duration-300 hover:-translate-y-1"
          data-aos="fade-up"
          :data-aos-delay="index * 60"
        >
          <!-- Image -->
          <div class="relative h-48 overflow-hidden bg-gray-100 dark:bg-gray-800">
            <img
              v-if="project.image"
              :src="project.image"
              :alt="project.title"
              loading="lazy"
              class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500"
            />
            <div v-else class="w-full h-full flex items-center justify-center">
              <span class="text-4xl text-gray-300 dark:text-gray-700 font-mono">{ }</span>
            </div>

            <!-- Overlay au hover avec liens -->
            <div class="absolute inset-0 bg-black/70 opacity-0 group-hover:opacity-100 transition-opacity duration-300 flex items-center justify-center gap-4">
              <a v-if="project.github_url" :href="project.github_url" target="_blank"
                 class="flex items-center gap-2 px-4 py-2 bg-white text-gray-900 text-xs font-semibold rounded-full hover:bg-gray-100 transition-colors"
                 @click.stop>
                <svg class="w-3.5 h-3.5" fill="currentColor" viewBox="0 0 24 24">
                  <path fill-rule="evenodd" d="M12 2C6.477 2 2 6.484 2 12.017c0 4.425 2.865 8.18 6.839 9.504.5.092.682-.217.682-.483 0-.237-.008-.868-.013-1.703-2.782.605-3.369-1.343-3.369-1.343-.454-1.158-1.11-1.466-1.11-1.466-.908-.62.069-.608.069-.608 1.003.07 1.531 1.032 1.531 1.032.892 1.53 2.341 1.088 2.91.832.092-.647.35-1.088.636-1.338-2.22-.253-4.555-1.113-4.555-4.951 0-1.093.39-1.988 1.029-2.688-.103-.253-.446-1.272.098-2.65 0 0 .84-.27 2.75 1.026A9.564 9.564 0 0112 6.844c.85.004 1.705.115 2.504.337 1.909-1.296 2.747-1.027 2.747-1.027.546 1.379.202 2.398.1 2.651.64.7 1.028 1.595 1.028 2.688 0 3.848-2.339 4.695-4.566 4.943.359.309.678.92.678 1.855 0 1.338-.012 2.419-.012 2.747 0 .268.18.58.688.482A10.019 10.019 0 0022 12.017C22 6.484 17.522 2 12 2z" clip-rule="evenodd"/>
                </svg>
                Code
              </a>
              <a v-if="project.live_url" :href="project.live_url" target="_blank"
                 class="flex items-center gap-2 px-4 py-2 bg-accent-600 text-white text-xs font-semibold rounded-full hover:bg-accent-700 transition-colors"
                 @click.stop>
                <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14"/>
                </svg>
                Demo
              </a>
            </div>

            <!-- Badges statut -->
            <div class="absolute top-3 left-3 flex gap-1.5">
              <span v-if="project.featured"
                class="px-2.5 py-0.5 bg-white/90 text-gray-800 text-[10px] font-bold rounded-full backdrop-blur-sm">
                ⭐ Featured
              </span>
              <span v-if="project.live_url"
                class="px-2.5 py-0.5 bg-emerald-500/90 text-white text-[10px] font-bold rounded-full backdrop-blur-sm">
                ● Live
              </span>
            </div>
          </div>

          <!-- Contenu carte -->
          <div class="p-5">
            <div class="flex items-start justify-between gap-2 mb-2">
              <h3 class="text-sm font-bold text-gray-900 dark:text-white leading-snug line-clamp-1">
                {{ project.title }}
              </h3>
              <span class="text-[10px] font-semibold text-accent-600 dark:text-accent-400 uppercase tracking-wide flex-shrink-0">
                {{ getCategoryLabel(project.category) }}
              </span>
            </div>

            <p class="text-xs text-gray-500 dark:text-gray-400 leading-relaxed mb-4 line-clamp-2">
              {{ project.short_description || project.description }}
            </p>

            <!-- Badges tech arrondis style Nicolas Wadoux -->
            <div class="flex flex-wrap gap-1.5">
              <span
                v-for="tech in (project.technologies_list || []).slice(0, 4)"
                :key="tech"
                class="px-2.5 py-0.5 text-[10px] font-medium rounded-full border border-gray-300 dark:border-gray-700 text-gray-600 dark:text-gray-400 bg-transparent"
              >{{ tech.trim() }}</span>
            </div>
          </div>
        </div>
      </div>

    </div>
  </section>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { projectService } from '@/services/api'
import { useI18n } from 'vue-i18n'

const { locale } = useI18n()

const props = defineProps({
  limit: { type: Number, default: 0 }
})

const projects = ref([])
const loading = ref(true)
const error = ref(null)
const filter = ref('all')

const categories = computed(() => [...new Set(projects.value.map(p => p.category))].sort())

const filteredProjects = computed(() => {
  let result = filter.value === 'all' ? projects.value : projects.value.filter(p => p.category === filter.value)
  return props.limit > 0 ? result.slice(0, props.limit) : result
})

const getCategoryLabel = (category) => {
  const labels = { web: 'Web', mobile: 'Mobile', ai: 'IA', design: 'Design', other: 'Autre' }
  return labels[category] || category
}

const fetchProjects = async () => {
  try {
    loading.value = true
    error.value = null
    const response = await projectService.getAllProjects()
    projects.value = Array.isArray(response) ? response : (response?.results ?? [])
  } catch (err) {
    error.value = locale.value === 'fr'
      ? 'Impossible de charger les projets. Vérifiez que le serveur est actif.'
      : 'Unable to load projects. Make sure the server is running.'
    projects.value = []
  } finally {
    loading.value = false
  }
}

onMounted(fetchProjects)
</script>