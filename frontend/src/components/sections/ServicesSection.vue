<template>
  <section id="services" class="section-light section-padded">
    <div class="services-container">
      <div data-aos="fade-up">
        <h2 class="section-heading">
          {{ locale === 'fr' ? 'À votre service !' : 'At your service!' }}
        </h2>
        <div class="section-divider"></div>
      </div>

      <div class="services-grid" data-aos="fade-up" data-aos-delay="100">
        <div
          v-for="(service, i) in services"
          :key="service.id"
          class="service-card"
          data-aos="fade-up"
          :data-aos-delay="i * 80"
        >
          <!-- Icône SVG inline -->
          <span class="service-icon" v-html="service.icon"></span>
          <h3 class="service-title">{{ service.title }}</h3>
          <p class="service-desc">{{ service.desc }}</p>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
import { computed } from 'vue'
import { useI18n } from 'vue-i18n'

const { locale } = useI18n()

const services = computed(() => [
  {
    id: 'fullstack',
    icon: `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" style="width:3.5rem;height:3.5rem;color:#6366f1">
      <path d="M12 2L2 7l10 5 10-5-10-5zM2 17l10 5 10-5M2 12l10 5 10-5"/>
    </svg>`,
    title: locale.value === 'fr' ? 'Développement Fullstack' : 'Fullstack Development',
    desc: locale.value === 'fr'
      ? 'Applications web complètes avec Vue.js, React côté front et Django, Spring Boot côté back. APIs REST robustes et bases de données optimisées.'
      : 'Full web applications with Vue.js, React on the front end and Django, Spring Boot on the back end. Robust REST APIs and optimized databases.',
  },
  {
    id: 'mobile',
    icon: `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" style="width:3.5rem;height:3.5rem;color:#6366f1">
      <path d="M17 2H7a2 2 0 00-2 2v16a2 2 0 002 2h10a2 2 0 002-2V4a2 2 0 00-2-2zm-5 18a1 1 0 110-2 1 1 0 010 2z"/>
    </svg>`,
    title: locale.value === 'fr' ? 'Développement Mobile' : 'Mobile Development',
    desc: locale.value === 'fr'
      ? 'Applications mobiles cross-platform avec Flutter & Dart. Développement de jeux avec Godot Engine et Pygame pour des expériences interactives.'
      : 'Cross-platform mobile applications with Flutter & Dart. Game development with Godot Engine and Pygame for interactive experiences.',
  },
  {
    id: 'design',
    icon: `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" style="width:3.5rem;height:3.5rem;color:#6366f1">
      <path d="M12 20h9M16.5 3.5a2.121 2.121 0 013 3L7 19l-4 1 1-4 12.5-12.5z"/>
    </svg>`,
    title: locale.value === 'fr' ? 'Design & Infographie' : 'Design & Infography',
    desc: locale.value === 'fr'
      ? 'Création d\'identités visuelles, maquettes UI/UX avec Figma, Photoshop et Illustrator. Design centré utilisateur pour des interfaces percutantes.'
      : 'Visual identity creation, UI/UX mockups with Figma, Photoshop and Illustrator. User-centered design for impactful interfaces.',
  },
  {
    id: 'systems',
    icon: `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" style="width:3.5rem;height:3.5rem;color:#6366f1">
      <path d="M9 3H5a2 2 0 00-2 2v4m6-6h10a2 2 0 012 2v4M9 3v18m0 0h10a2 2 0 002-2V9M9 21H5a2 2 0 01-2-2V9m0 0h18"/>
    </svg>`,
    title: locale.value === 'fr' ? 'Systèmes d\'Information' : 'Information Systems',
    desc: locale.value === 'fr'
      ? 'Conception et gestion de Systèmes d\'Information complexes (SI). Support IT, cybersécurité, administration réseaux et infrastructure Linux/Docker.'
      : 'Design and management of complex Information Systems. IT support, cybersecurity, network administration and Linux/Docker infrastructure.',
  },
])
</script>

<style scoped>
.services-container {
  max-width: 1140px;
  margin: 0 auto;
  padding: 0 1.5rem;
  text-align: center;
}

.services-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 1.5rem;
  margin-top: 1rem;
}

@media (max-width: 900px) {
  .services-grid {
    grid-template-columns: repeat(2, 1fr);
  }
}

@media (max-width: 500px) {
  .services-grid {
    grid-template-columns: 1fr;
  }
}

.service-card {
  text-align: center;
  padding: 2rem 1.25rem;
  transition: transform 0.25s ease;
}

.service-card:hover {
  transform: translateY(-6px);
}

.service-icon {
  display: flex;
  justify-content: center;
  margin-bottom: 1.25rem;
}

.service-title {
  font-family: 'Open Sans', sans-serif;
  font-weight: 700;
  font-size: 1.05rem;
  color: #212529;
  margin-bottom: 0.75rem;
}

.service-desc {
  font-family: 'Merriweather', serif;
  font-size: 0.82rem;
  color: #555;
  line-height: 1.75;
}
</style>
