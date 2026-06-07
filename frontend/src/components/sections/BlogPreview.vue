<template>
  <section id="blog-preview" class="section-dark section-padded">
    <div class="container" style="max-width: 1140px; margin: 0 auto; padding: 0 1.5rem;">
      <div class="text-center" data-aos="fade-up" style="margin-bottom: 3rem;">
        <h2 class="section-heading" style="color: #ffffff;">
          {{ locale === 'fr' ? 'Mon Blog Technique' : 'My Technical Blog' }}
        </h2>
        <div class="section-divider-white"></div>
        <p style="font-family: 'Merriweather', serif; font-style: italic; color: #a1a1aa; font-size: 0.95rem;">
          {{ locale === 'fr' ? 'Partages d\'expériences, tutoriels et bonnes pratiques' : 'Experience sharing, tutorials and best practices' }}
        </p>
      </div>

      <!-- Chargement -->
      <div v-if="loading" class="text-center py-10">
        <div class="spinner"></div>
      </div>

      <!-- Articles -->
      <div v-else class="services-grid" style="grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));">
        <div 
          v-for="(post, index) in latestPosts"
          :key="post.id"
          class="blog-card"
          data-aos="fade-up"
          :data-aos-delay="index * 100"
        >
          <!-- Image (si disponible) -->
          <div style="height: 180px; overflow: hidden; position: relative;">
            <div style="position: absolute; inset: 0; background: linear-gradient(to top, #18181b 0%, transparent 100%); z-index: 10; opacity: 0.8;"></div>
            <img 
              v-if="post.image" 
              :src="post.image" 
              :alt="post.title"
              style="width: 100%; height: 100%; object-fit: cover; transition: transform 0.5s ease;"
              class="blog-img"
            />
            <div v-else style="width: 100%; height: 100%; background: #312e81; display: flex; align-items: center; justify-content: center; transition: transform 0.5s ease;" class="blog-img">
              <PencilSquareIcon style="width: 3rem; height: 3rem; color: #a1a1aa;" />
            </div>
            
            <!-- Date et Catégorie sur l'image -->
            <div style="position: absolute; top: 1rem; right: 1rem; z-index: 20;">
              <span class="blog-tag">
                {{ post.category?.name || (locale === 'fr' ? 'Général' : 'General') }}
              </span>
            </div>
            
            <div style="position: absolute; bottom: 1rem; left: 1rem; z-index: 20;">
              <span style="font-size: 0.75rem; color: #e4e4e7; font-family: 'Open Sans', sans-serif; background: rgba(0,0,0,0.5); padding: 0.2rem 0.5rem; border-radius: 4px;">
                {{ formatDate(post.published_date) }}
              </span>
            </div>
          </div>

          <div style="padding: 1.5rem; text-align: left; display: flex; flex-direction: column; flex-grow: 1;">
            <!-- Titre -->
            <h3 class="blog-title">
              {{ post.title }}
            </h3>

            <!-- Extrait -->
            <p class="blog-desc">
              {{ post.excerpt || post.content.substring(0, 150) + '...' }}
            </p>

            <!-- Stats et Bouton -->
            <div style="display: flex; align-items: center; justify-content: space-between; margin-top: auto; padding-top: 1rem; border-top: 1px solid #3f3f46;">
              <div style="display: flex; align-items: center; font-size: 0.75rem; color: #a1a1aa; font-family: 'Open Sans', sans-serif;">
                <span style="display: flex; align-items: center; margin-right: 1rem;"><EyeIcon style="width: 1rem; height: 1rem; margin-right: 0.25rem;" /> {{ post.views || 0 }}</span>
                <span style="display: flex; align-items: center;"><ClockIcon style="width: 1rem; height: 1rem; margin-right: 0.25rem;" /> {{ timeAgo(post.published_date) }}</span>
              </div>

              <router-link 
                :to="{ name: 'blog-post', params: { slug: post.slug } }"
                class="blog-link"
              >
                {{ locale === 'fr' ? 'Lire' : 'Read' }}
                <ArrowRightIcon style="width: 1rem; height: 1rem; margin-left: 0.25rem;" />
              </router-link>
            </div>
          </div>
        </div>

        <!-- CTA si pas d'articles -->
        <div 
          v-if="latestPosts.length === 0"
          style="grid-column: 1 / -1; text-align: center; padding: 4rem 2rem; background: #27272a; border-radius: 12px; border: 1px solid #3f3f46;"
        >
          <div style="display: flex; justify-content: center; margin-bottom: 1rem;">
            <PencilSquareIcon style="width: 4rem; height: 4rem; color: #52525b;" />
          </div>
          <h3 style="font-family: 'Open Sans', sans-serif; font-weight: 700; font-size: 1.25rem; color: #ffffff; margin-bottom: 0.5rem;">
            {{ locale === 'fr' ? 'Aucun article pour le moment' : 'No articles yet' }}
          </h3>
          <p style="font-family: 'Merriweather', serif; color: #a1a1aa; font-size: 0.9rem; margin-bottom: 1.5rem;">
            {{ locale === 'fr' ? 'Les articles du blog seront bientôt disponibles !' : 'Blog articles coming soon!' }}
          </p>
          <router-link to="/blog" class="btn-accent" style="padding: 0.75rem 1.5rem; font-size: 0.8rem;">
            {{ locale === 'fr' ? 'Voir le blog' : 'View blog' }}
          </router-link>
        </div>
      </div>

      <!-- Bouton vers blog complet -->
      <div style="text-align: center; margin-top: 3rem;" data-aos="fade-up">
        <router-link to="/blog" class="btn-accent">
          <span>{{ locale === 'fr' ? 'Voir tous les articles' : 'View all articles' }}</span>
          <ArrowRightIcon style="width: 1.25rem; height: 1.25rem; margin-left: 0.5rem;" />
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

<style scoped>
.spinner {
  width: 36px;
  height: 36px;
  border: 3px solid #3f3f46;
  border-top-color: var(--accent);
  border-radius: 50%;
  animation: spin 0.8s linear infinite;
  margin: 0 auto;
}

@keyframes spin {
  to { transform: rotate(360deg); }
}

.blog-card {
  background: #27272a;
  border: 1px solid #3f3f46;
  border-radius: 12px;
  overflow: hidden;
  transition: all 0.3s ease;
  display: flex;
  flex-direction: column;
}

.blog-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5);
  border-color: var(--accent);
}

.blog-card:hover .blog-img {
  transform: scale(1.05);
}

.blog-tag {
  background: var(--accent);
  color: #ffffff;
  padding: 0.25rem 0.75rem;
  border-radius: 20px;
  font-size: 0.7rem;
  font-weight: 700;
  font-family: 'Open Sans', sans-serif;
  text-transform: uppercase;
}

.blog-title {
  font-family: 'Open Sans', sans-serif;
  font-weight: 700;
  font-size: 1.1rem;
  color: #ffffff;
  margin-bottom: 0.5rem;
  line-height: 1.4;
  display: -webkit-box;
  -webkit-line-clamp: 2;
  line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
}

.blog-card:hover .blog-title {
  color: var(--accent-light);
}

.blog-desc {
  font-family: 'Merriweather', serif;
  font-size: 0.85rem;
  color: #a1a1aa;
  line-height: 1.6;
  margin-bottom: 1rem;
  display: -webkit-box;
  -webkit-line-clamp: 3;
  line-clamp: 3;
  -webkit-box-orient: vertical;
  overflow: hidden;
}

.blog-link {
  display: inline-flex;
  align-items: center;
  font-family: 'Open Sans', sans-serif;
  font-size: 0.8rem;
  font-weight: 700;
  color: var(--accent);
  text-decoration: none;
  text-transform: uppercase;
  transition: color 0.2s ease;
}

.blog-link:hover {
  color: var(--accent-hover);
}
</style>