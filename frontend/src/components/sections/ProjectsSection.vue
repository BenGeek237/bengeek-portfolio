<template>
  <section id="projects" class="section-light section-padded">
    <div class="projects-container">
      <!-- Header -->
      <div data-aos="fade-up">
        <h2 class="section-heading" style="text-transform: uppercase; font-size: clamp(2rem, 5vw, 3rem); letter-spacing: 0.05em;">
          PORTFOLIO
        </h2>
        <p class="projects-subtitle">
          {{ locale === 'fr' ? 'Présentation de mes dernières expériences.' : 'Presentation of my latest experiences.' }}
        </p>
        <div class="section-divider"></div>
      </div>

      <!-- Loading -->
      <div v-if="loading" class="loading-wrap">
        <div class="spinner"></div>
      </div>

      <!-- Error -->
      <div v-else-if="error" class="error-wrap">
        <p>{{ error }}</p>
        <button class="btn-accent" @click="fetchProjects">
          {{ locale === 'fr' ? 'Réessayer' : 'Retry' }}
        </button>
      </div>

      <!-- Empty -->
      <div v-else-if="displayedProjects.length === 0" class="empty-wrap">
        <p>{{ locale === 'fr' ? 'Aucun projet trouvé.' : 'No projects found.' }}</p>
      </div>

      <!-- Portfolio grid -->
      <div v-else class="portfolio-grid" data-aos="fade-up" data-aos-delay="100">
        <div
          v-for="(project, index) in displayedProjects"
          :key="project.id"
          class="portfolio-item"
          @click="openModal(project)"
          data-aos="fade-up"
          :data-aos-delay="index * 60"
        >
          <img
            v-if="project.image"
            :src="project.image"
            :alt="project.title"
            loading="lazy"
          />
          <div v-else class="portfolio-placeholder">
            <span>{{ project.title.charAt(0) }}</span>
          </div>

          <!-- Overlay orange au hover -->
          <div class="portfolio-overlay">
            <span class="portfolio-plus">+</span>
          </div>
        </div>
      </div>

      <!-- "Voir tout" link sur la home -->
      <div v-if="limit && projects.length > limit" class="see-all-wrap" data-aos="fade-up">
        <router-link to="/projects" class="btn-accent">
          {{ locale === 'fr' ? 'Voir tous les projets' : 'View all projects' }}
        </router-link>
      </div>
    </div>

    <!-- Modal projet -->
    <Teleport to="body">
      <Transition name="modal-fade">
        <div v-if="activeProject" class="project-modal-overlay" @click.self="closeModal">
          <div class="project-modal-box">
            <button class="project-modal-close" @click="closeModal" aria-label="Fermer">✕</button>

            <h3 class="modal-title">{{ activeProject.title }}</h3>
            <p class="modal-category">{{ getCategoryLabel(activeProject.category) }}</p>

            <img
              v-if="activeProject.image"
              :src="activeProject.image"
              :alt="activeProject.title"
              class="modal-image"
            />

            <p class="modal-desc">{{ activeProject.description || activeProject.short_description }}</p>

            <!-- Tech tags -->
            <div class="modal-tags" v-if="activeProject.technologies_list?.length">
              <span
                v-for="tech in activeProject.technologies_list.slice(0, 6)"
                :key="tech"
                class="modal-tag"
              >{{ tech.trim() }}</span>
            </div>

            <!-- Links -->
            <div class="modal-links">
              <a
                v-if="activeProject.github_url"
                :href="activeProject.github_url"
                target="_blank"
                class="btn-accent"
              >
                GitHub
              </a>
              <a
                v-if="activeProject.live_url"
                :href="activeProject.live_url"
                target="_blank"
                class="btn-light-pill"
                style="border: 2px solid #212529;"
              >
                {{ locale === 'fr' ? 'Voir le site' : 'View site' }}
              </a>
              <button class="btn-secondary" @click="closeModal">
                {{ locale === 'fr' ? 'Retour' : 'Back' }}
              </button>
            </div>
          </div>
        </div>
      </Transition>
    </Teleport>
  </section>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { projectService } from '@/services/api'
import { useI18n } from 'vue-i18n'

const { locale } = useI18n()

const props = defineProps({
  limit: { type: Number, default: 0 },
})

const projects = ref([])
const loading = ref(true)
const error = ref(null)
const activeProject = ref(null)

const displayedProjects = computed(() =>
  props.limit > 0 ? projects.value.slice(0, props.limit) : projects.value
)

const getCategoryLabel = (cat) => {
  const labels = { web: 'Web', mobile: 'Mobile', ai: 'IA', design: 'Design', other: 'Autre' }
  return labels[cat] || cat
}

const openModal = (project) => {
  activeProject.value = project
  document.body.style.overflow = 'hidden'
}

const closeModal = () => {
  activeProject.value = null
  document.body.style.overflow = ''
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

<style scoped>
.projects-container {
  max-width: 1140px;
  margin: 0 auto;
  padding: 0 1.5rem;
  text-align: center;
}

.projects-subtitle {
  font-family: 'Merriweather', serif;
  font-style: italic;
  font-size: 0.95rem;
  color: #6c757d;
  margin-bottom: 0.25rem;
}

/* Grid */
.portfolio-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 1rem;
  margin-top: 1rem;
}

@media (max-width: 900px) {
  .portfolio-grid { grid-template-columns: repeat(2, 1fr); }
}

@media (max-width: 560px) {
  .portfolio-grid { grid-template-columns: 1fr; }
}

/* Items */
.portfolio-item {
  position: relative;
  overflow: hidden;
  cursor: pointer;
  border-radius: 4px;
  background: #e9ecef;
}

.portfolio-item img {
  width: 100%;
  height: 220px;
  object-fit: cover;
  display: block;
  transition: transform 0.4s ease;
}

.portfolio-item:hover img {
  transform: scale(1.05);
}

.portfolio-placeholder {
  height: 220px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 3rem;
  font-weight: 800;
  color: #adb5bd;
  font-family: 'Open Sans', sans-serif;
}

/* Orange overlay */
.portfolio-overlay {
  position: absolute;
  inset: 0;
  background: rgba(240, 95, 64, 0.92);
  display: flex;
  align-items: center;
  justify-content: center;
  opacity: 0;
  transition: opacity 0.35s ease;
}

.portfolio-item:hover .portfolio-overlay {
  opacity: 1;
}

.portfolio-plus {
  font-size: 3.5rem;
  color: #ffffff;
  font-weight: 300;
  line-height: 1;
  font-family: 'Open Sans', sans-serif;
}

/* See all */
.see-all-wrap {
  margin-top: 2.5rem;
  display: flex;
  justify-content: center;
}

/* Loading / Error */
.loading-wrap, .empty-wrap, .error-wrap {
  padding: 4rem 0;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 1rem;
}

.spinner {
  width: 36px;
  height: 36px;
  border: 3px solid #dee2e6;
  border-top-color: #6366f1;
  border-radius: 50%;
  animation: spin 0.8s linear infinite;
}

@keyframes spin {
  to { transform: rotate(360deg); }
}

/* Modal */
.modal-title {
  font-family: 'Open Sans', sans-serif;
  font-weight: 800;
  font-size: 1.5rem;
  color: #212529;
  margin-bottom: 0.25rem;
}

.modal-category {
  font-family: 'Open Sans', sans-serif;
  font-size: 0.8rem;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.1em;
  color: #6366f1;
  margin-bottom: 1.25rem;
}

.modal-image {
  width: 100%;
  border-radius: 6px;
  margin-bottom: 1.25rem;
  max-height: 300px;
  object-fit: cover;
}

.modal-desc {
  font-family: 'Merriweather', serif;
  font-size: 0.9rem;
  color: #555;
  line-height: 1.75;
  margin-bottom: 1.25rem;
}

.modal-tags {
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem;
  margin-bottom: 1.5rem;
}

.modal-tag {
  padding: 0.3rem 0.85rem;
  background: #f8f9fa;
  border: 1px solid #dee2e6;
  border-radius: 300px;
  font-family: 'Open Sans', sans-serif;
  font-size: 0.75rem;
  font-weight: 600;
  color: #495057;
}

.modal-links {
  display: flex;
  gap: 0.75rem;
  flex-wrap: wrap;
}

/* Modal transitions */
.modal-fade-enter-active,
.modal-fade-leave-active {
  transition: opacity 0.25s ease;
}

.modal-fade-enter-from,
.modal-fade-leave-to {
  opacity: 0;
}
</style>