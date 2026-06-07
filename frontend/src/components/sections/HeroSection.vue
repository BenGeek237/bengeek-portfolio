<template>
  <section
    id="hero"
    class="section-dark"
    style="min-height: 100vh; display: flex; align-items: center; justify-content: center;"
  >
    <!-- Particles background -->
    <ParticlesBg color="#c7d2fe" :particle-count="90" :opacity="0.7" />

    <!-- Content -->
    <div class="hero-content" data-aos="fade-up">
      <h1 class="hero-title">
        {{ locale === 'fr'
          ? 'VOUS RECHERCHEZ UN DÉVELOPPEUR FULLSTACK ?'
          : 'LOOKING FOR A FULLSTACK DEVELOPER?' }}
      </h1>

      <div class="section-divider" style="background: linear-gradient(90deg, #6366f1, #818cf8); margin: 1rem auto 1.75rem;"></div>

      <p class="hero-subtitle">
        {{ locale === 'fr'
          ? "Ça tombe bien ! Je suis passionné par le développement web et j'ai acquis de solides compétences en Fullstack, Mobile, Design et Systèmes d'Information."
          : "Great news! I'm passionate about web development and have built strong skills in Fullstack, Mobile, Design, and Information Systems." }}
        <br>
        {{ locale === 'fr'
          ? 'La suite, c\'est à vous de la découvrir !'
          : "The rest is yours to discover!" }}
      </p>

      <div class="hero-cta" data-aos="fade-up" data-aos-delay="200">
        <button class="btn-light-pill" @click="scrollToNext">
          CONTINUER
          <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" d="M19 9l-7 7-7-7"/>
          </svg>
        </button>
      </div>
    </div>
  </section>
</template>

<script setup>
import { useI18n } from 'vue-i18n'
import ParticlesBg from '@/components/ui/ParticlesBg.vue'

const { locale } = useI18n()

const scrollToNext = () => {
  const el = document.getElementById('about')
  if (el) {
    const offset = 70
    const top = el.getBoundingClientRect().top + window.pageYOffset - offset
    window.scrollTo({ top, behavior: 'smooth' })
  }
}
</script>

<style scoped>
.hero-content {
  position: relative;
  z-index: 1;
  text-align: center;
  max-width: 860px;
  margin: 0 auto;
  padding: 8rem 1.5rem;
}

.hero-title {
  font-family: 'Open Sans', sans-serif;
  font-weight: 800;
  font-size: clamp(2rem, 5.5vw, 4rem);
  color: #ffffff;
  text-transform: uppercase;
  letter-spacing: -0.01em;
  line-height: 1.15;
  margin-bottom: 0;
}

.hero-subtitle {
  font-family: 'Merriweather', serif;
  font-size: clamp(0.9rem, 1.8vw, 1.05rem);
  color: rgba(255, 255, 255, 0.78);
  line-height: 1.8;
  max-width: 680px;
  margin: 0 auto 2.5rem;
}

.hero-cta {
  display: flex;
  justify-content: center;
}
</style>
