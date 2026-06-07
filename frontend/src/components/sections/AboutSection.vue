<template>
  <section id="about" class="section-orange section-padded">
    <!-- Particles en overlay très léger -->
    <ParticlesBg color="#c7d2fe" :particle-count="55" :opacity="0.2" />

    <div class="container" style="position: relative; z-index: 1;">
      <div data-aos="fade-up">
        <h2 class="section-heading" style="color: #fff;">
          {{ locale === 'fr' ? 'Faisons connaissance :)' : 'Let\'s get acquainted :)' }}
        </h2>
        <div class="section-divider-white"></div>

        <div class="about-text">
          <p>
            {{ locale === 'fr'
              ? "Avant toute chose, je me présente. Je suis Mamoudou Bia, développeur Fullstack passionné basé à Ngaoundéré, au Cameroun. Je conçois des applications web et mobiles avec Vue.js, Django, Flutter, et j'interviens également en infographie et en gestion de Systèmes d'Information complexes."
              : "First of all, let me introduce myself. I'm Mamoudou Bia, a passionate Fullstack developer based in Ngaoundéré, Cameroon. I build web and mobile applications with Vue.js, Django, Flutter, and I also work in graphic design and complex Information Systems management." }}
          </p>
          <p>
            {{ locale === 'fr'
              ? "Au fil de mes formations et de mes expériences, je me suis spécialisé dans le développement Fullstack tout en restant polyvalent : design, cybersécurité, support IT, développement de jeux vidéo. Je vous invite à consulter le panel de mes compétences et projets ci-dessous."
              : "Through my training and experiences, I have specialized in Fullstack development while remaining versatile: design, cybersecurity, IT support, game development. I invite you to explore my skills and projects below." }}
          </p>
        </div>

        <div class="about-cta" data-aos="fade-up" data-aos-delay="200">
          <button class="btn-light-pill" @click="scrollToServices">
            CONTINUER
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" d="M19 9l-7 7-7-7"/>
            </svg>
          </button>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
import { useI18n } from 'vue-i18n'
import ParticlesBg from '@/components/ui/ParticlesBg.vue'

const { locale } = useI18n()

const scrollToServices = () => {
  const el = document.getElementById('services')
  if (el) {
    const top = el.getBoundingClientRect().top + window.pageYOffset - 70
    window.scrollTo({ top, behavior: 'smooth' })
  }
}
</script>

<style scoped>
.container {
  max-width: 860px;
  margin: 0 auto;
  padding: 0 1.5rem;
  text-align: center;
}

.about-text {
  max-width: 760px;
  margin: 0 auto 2.5rem;
}

.about-text p {
  font-family: 'Merriweather', serif;
  font-size: 1rem;
  color: rgba(255,255,255,0.92);
  line-height: 1.85;
  margin-bottom: 1.25rem;
}

.about-cta {
  display: flex;
  justify-content: center;
}
</style>