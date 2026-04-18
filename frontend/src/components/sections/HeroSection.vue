<template>
  <section
    id="hero"
    class="relative flex flex-col items-center justify-center overflow-hidden"
    style="height: 100vh;"
  >
    <!-- Fond dégradé sombre -->
    <div class="absolute inset-0 z-0 bg-gradient-to-br from-gray-950 via-gray-900 to-gray-800 dark:from-black dark:via-gray-950 dark:to-gray-900"></div>

    <!-- Contenu centré -->
    <div class="relative z-10 flex flex-col items-center text-center px-6" data-aos="fade-up">

      <!-- Nom stylisé avec tirets -->
      <h1 class="hero-name text-5xl sm:text-6xl md:text-7xl lg:text-8xl text-white mb-6 select-none">
        <span class="block text-2xl sm:text-3xl md:text-4xl font-light tracking-widest text-white/70 mb-2">
          {{ locale === 'fr' ? 'Salut, je suis' : "Hi, I'm" }}
        </span>
        -Mamoudou Bia-
      </h1>

      <!-- Badge glassmorphism - titre -->
      <div class="glass-badge mb-10">
        <Transition name="role" mode="out-in">
          <span :key="currentRole" class="text-base md:text-lg text-white/90 font-light tracking-wide">
            {{ currentRole }}
          </span>
        </Transition>
      </div>

      <!-- Points verts de disponibilité -->
      <div class="flex items-center gap-2 mb-10">
        <span class="relative flex h-2.5 w-2.5">
          <span class="animate-ping absolute inline-flex h-full w-full rounded-full bg-emerald-400 opacity-75"></span>
          <span class="relative inline-flex rounded-full h-2.5 w-2.5 bg-emerald-500"></span>
        </span>
        <span class="text-sm text-white/70 font-light">
          {{ locale === 'fr' ? 'Disponible pour de nouveaux projets' : 'Available for new projects' }}
        </span>
      </div>

      <!-- CTAs -->
      <div class="flex flex-wrap gap-4 justify-center" data-aos="fade-up" data-aos-delay="200">
        <button
          @click="scrollTo('projects')"
          class="px-7 py-3 bg-white text-gray-900 text-sm font-semibold rounded-full hover:bg-gray-100 transition-all duration-300 shadow-lg hover:shadow-xl hover:-translate-y-0.5"
        >
          {{ locale === 'fr' ? 'Voir mes projets' : 'View my projects' }}
        </button>
        <button
          @click="scrollTo('contact')"
          class="px-7 py-3 bg-transparent border border-white/50 text-white text-sm font-semibold rounded-full hover:bg-white/10 hover:border-white transition-all duration-300 backdrop-blur-sm"
        >
          {{ locale === 'fr' ? 'Me contacter' : 'Contact me' }}
        </button>
      </div>

      <!-- Stats row -->
      <div class="flex gap-10 mt-16 pt-8 border-t border-white/20" data-aos="fade-up" data-aos-delay="300">
        <div v-for="stat in stats" :key="stat.label" class="flex flex-col items-center">
          <span class="text-2xl font-bold text-white">{{ stat.value }}{{ stat.plus ? '+' : '' }}</span>
          <span class="text-xs text-white/50 mt-0.5 font-light tracking-wide">{{ stat.label }}</span>
        </div>
      </div>
    </div>

    <!-- Scroll indicator -->
    <div
      class="absolute bottom-8 left-1/2 -translate-x-1/2 flex flex-col items-center gap-2 cursor-pointer z-10 opacity-60 hover:opacity-100 transition-opacity"
      @click="scrollTo('about')"
    >
      <span class="text-[10px] text-white/60 tracking-[0.2em] uppercase font-light">Scroll</span>
      <div class="mouse-scroll">
        <div class="mouse-wheel"></div>
      </div>
    </div>
  </section>
</template>

<script setup>
import { ref, onMounted, onUnmounted, computed, watch } from 'vue'
import { useI18n } from 'vue-i18n'

const { t, locale } = useI18n()

const roles = computed(() => [
  t('hero.roles.fullstack'),
  locale.value === 'fr' ? 'Infographiste & Designer' : 'Graphic Designer',
  locale.value === 'fr' ? 'Expert en Systèmes d\'Information (SI)' : 'Information Systems (IS) Expert',
  t('hero.roles.itSecurity'),
  t('hero.roles.webMobile'),
  t('hero.roles.game'),
])

const currentRole = ref('')
let roleIndex = 0
let roleInterval = null

const stats = computed(() => [
  { value: '2',   label: t('hero.stats.experience'), plus: true },
  { value: '15',  label: t('hero.stats.technologies'), plus: true },
  { value: '10',  label: t('hero.stats.projects'), plus: true },
])

const rotateRoles = () => {
  roleInterval = setInterval(() => {
    roleIndex = (roleIndex + 1) % roles.value.length
    currentRole.value = roles.value[roleIndex]
  }, 3000)
}

watch(locale, () => {
  clearInterval(roleInterval)
  roleIndex = 0
  currentRole.value = roles.value[0]
  rotateRoles()
})

const scrollTo = (id) => {
  const el = document.getElementById(id)
  if (el) {
    const offset = 64
    const top = el.getBoundingClientRect().top + window.pageYOffset - offset
    window.scrollTo({ top, behavior: 'smooth' })
  }
}

onMounted(() => {
  currentRole.value = roles.value[0]
  setTimeout(rotateRoles, 3000)
})

onUnmounted(() => {
  clearInterval(roleInterval)
})
</script>

<style scoped>
/* Nom hero — Inter Black ultra-condensé */

.hero-name {
  font-family: 'Inter', sans-serif;
  font-style: normal;
  font-weight: 900;
  letter-spacing: -0.04em;
  text-shadow: 0 2px 30px rgba(0,0,0,0.5);
  line-height: 1.05;
}

/* Badge glassmorphism */
.glass-badge {
  background: rgba(255, 255, 255, 0.1);
  backdrop-filter: blur(12px);
  -webkit-backdrop-filter: blur(12px);
  border: 1px solid rgba(255, 255, 255, 0.2);
  border-radius: 9999px;
  padding: 12px 32px;
  min-width: 260px;
  text-align: center;
}

/* Icône souris scroll */
.mouse-scroll {
  width: 22px;
  height: 34px;
  border: 2px solid rgba(255,255,255,0.4);
  border-radius: 11px;
  display: flex;
  justify-content: center;
  padding-top: 6px;
}

.mouse-wheel {
  width: 3px;
  height: 6px;
  background: rgba(255,255,255,0.6);
  border-radius: 9999px;
  animation: scrollWheel 1.5s ease infinite;
}

@keyframes scrollWheel {
  0%   { transform: translateY(0); opacity: 1; }
  100% { transform: translateY(10px); opacity: 0; }
}

/* Transitions des rôles */
.role-enter-active, .role-leave-active {
  transition: opacity 0.35s ease, transform 0.35s ease;
}
.role-enter-from { opacity: 0; transform: translateY(8px); }
.role-leave-to   { opacity: 0; transform: translateY(-8px); }
</style>
