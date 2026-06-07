<template>
  <section id="banner-cv" class="section-dark" style="padding: 6rem 0; position: relative; overflow: hidden;">
    <!-- Particles -->
    <ParticlesBg color="#ffffff" :particle-count="60" :opacity="0.5" />

    <div class="banner-content" data-aos="fade-up">
      <h2 class="banner-title">
        {{ locale === 'fr' ? 'Consultez mon Curriculum Vitae en ligne' : 'View my Curriculum Vitae online' }}
      </h2>
      <a
        href="/cv/Mamoudou_Bia_CV.pdf"
        download="Mamoudou_Bia_CV.pdf"
        class="btn-light-pill"
      >
        CLIQUEZ ICI
      </a>
    </div>
  </section>
</template>

<script setup>
import ParticlesBg from '@/components/ui/ParticlesBg.vue'
import { useI18n } from 'vue-i18n'
const { locale } = useI18n()
</script>

<style scoped>
.banner-content {
  position: relative;
  z-index: 1;
  text-align: center;
  padding: 0 1.5rem;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 2rem;
}

.banner-title {
  font-family: 'Open Sans', sans-serif;
  font-weight: 700;
  font-size: clamp(1.2rem, 3vw, 1.8rem);
  color: #ffffff;
  max-width: 600px;
  line-height: 1.4;
}
</style>
