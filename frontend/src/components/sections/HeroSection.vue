<template>
  <section class="pt-20 pb-12 md:pt-24 md:pb-16 relative overflow-hidden">
    <!-- BACKGROUND GEEK ULTIMATE - Matrice + Circuit Board -->
    <div class="absolute inset-0 z-0 overflow-hidden transition-colors duration-300"
         :class="themeStore.darkMode ? 'bg-black' : 'bg-white'">
      <!-- Couche 1: Circuit Board (base) -->
      <div class="absolute inset-0 opacity-[0.15]">
        <svg class="w-full h-full">
          <defs>
            <pattern id="circuitPattern" width="80" height="80" patternUnits="userSpaceOnUse">
              <circle cx="40" cy="40" r="2" fill="#10b981" fill-opacity="0.5" />
              <circle cx="40" cy="40" r="4" fill="none" stroke="#3b82f6" stroke-width="0.5" stroke-opacity="0.3" />
              <path d="M40,0 V80 M0,40 H80" stroke="#10b981" stroke-width="0.8" stroke-opacity="0.2" stroke-dasharray="4,4" />
            </pattern>
          </defs>
          <rect width="100%" height="100%" fill="url(#circuitPattern)" />
        </svg>
      </div>

      <!-- Couche 2: Code Matrix Falling (vert) -->
      <div class="matrix-container absolute inset-0">
        <div
          v-for="i in matrixColumns"
          :key="i.id"
          class="matrix-column absolute top-0 font-mono text-green-400/40 text-sm md:text-base whitespace-nowrap"
          :style="{
            left: `${i.position}%`,
            animationDuration: `${i.speed}s`,
            animationDelay: `${i.delay}s`
          }"
          v-html="i.content"
        />
      </div>

      <!-- Couche 3: Points de connexion réseau -->
      <div class="absolute inset-0">
        <div
          v-for="(node, idx) in networkNodes"
          :key="idx"
          class="network-node absolute rounded-full"
          :class="[
            node.size === 'sm' ? 'w-1.5 h-1.5' :
            node.size === 'md' ? 'w-2.5 h-2.5' : 'w-1 h-1'
          ]"
          :style="{
            left: `${node.x}%`,
            top: `${node.y}%`,
            backgroundColor: `rgba(16, 185, 129, ${node.opacity})`,
            border: `1px solid rgba(59, 130, 246, ${node.opacity * 0.5})`,
            animationDelay: `${idx * 0.2}s`
          }"
        >
          <div
            v-if="node.size === 'md'"
            class="absolute inset-0 rounded-full animate-ping"
            :style="{ backgroundColor: `rgba(16, 185, 129, ${node.opacity * 0.3})` }"
          />
        </div>
      </div>

      <!-- Couche 4: Lignes de connexion entre points -->
      <svg class="absolute inset-0 w-full h-full opacity-10 pointer-events-none">
        <defs>
          <linearGradient id="lineGradient" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" stop-color="#10b981" stop-opacity="0.5" />
            <stop offset="100%" stop-color="#3b82f6" stop-opacity="0.5" />
          </linearGradient>
          <filter id="glow">
            <feGaussianBlur stdDeviation="1" result="coloredBlur"/>
            <feMerge>
              <feMergeNode in="coloredBlur"/>
              <feMergeNode in="SourceGraphic"/>
            </feMerge>
          </filter>
        </defs>

        <!-- Lignes principales (moins nombreuses) -->
        <line
          v-for="(line, idx) in connectionLines"
          :key="`line-${idx}`"
          :x1="`${line.x1}%`"
          :y1="`${line.y1}%`"
          :x2="`${line.x2}%`"
          :y2="`${line.y2}%`"
          stroke="url(#lineGradient)"
          stroke-width="0.8"
          stroke-dasharray="6,4"
          filter="url(#glow)"
          class="connection-line"
          :style="{
            animationDelay: `${idx * 0.5}s`
          }"
        />
      </svg>

      <!-- Couche 5: Effet de scanline très subtil -->
      <div class="absolute inset-0 scanlines opacity-[0.03]"></div>
    </div>

    <!-- CONTENU PRINCIPAL -->
    <div class="container mx-auto px-6 sm:px-8 lg:px-12 relative z-10">
      <div class="max-w-4xl mx-auto text-center">

        <!-- Titre principal -->
        <div class="mb-8" data-aos="fade-down" data-aos-delay="200">
          <h1 class="hero-title font-bold px-2">
            <span class="greeting-text text-gray-700 dark:text-gray-300 font-['Inter']">{{ t('hero.greeting') }}</span>
            <br class="mobile-break" />
            <span class="name-text text-transparent bg-clip-text bg-gradient-to-r from-blue-400 to-green-400 font-['Inter']">
              {{ displayedName }}<span class="text-green-400">|</span>
            </span>
          </h1>
        </div>

        <!-- Rôles rotatifs -->
        <div class="text-xl md:text-2xl text-gray-600 dark:text-gray-400 font-['Inter'] min-h-[40px] mt-4 mb-8">
          <span class="text-green-400 mr-2">&gt;</span>
          <span>{{ currentRole }}</span>
        </div>

        <!-- Boutons -->
        <div class="flex flex-col sm:flex-row gap-4 justify-center mb-12" data-aos="fade-up" data-aos-delay="600">
          <router-link to="#projects"
            class="px-7 py-4 text-lg bg-gradient-to-r from-blue-600/80 to-green-500/80 text-white font-mono rounded-lg hover:shadow-lg hover:shadow-green-500/30 backdrop-blur-sm border border-green-500/20 transition-all duration-300 hover:scale-105">
            <span class="flex items-center justify-center">
              <span class="mr-2">🚀</span>
              {{ t('hero.exploreProjects') }}
            </span>
          </router-link>

          <a href="mailto:mamoudoubiya3@gmail.com"
            class="hire-me-btn px-7 py-4 text-lg font-mono rounded-lg backdrop-blur-sm transition-all duration-300 hover:scale-105 relative overflow-hidden group">
            <span class="flex items-center justify-center relative z-10 text-white">
              <span class="mr-2">💼</span>
              {{ t('hero.hireMe') }}
            </span>
            <!-- Gradient de fond animé -->
            <span class="absolute inset-0 bg-gradient-to-r from-blue-600 via-green-500 to-blue-600 bg-[length:200%_100%] animate-gradient"></span>
            <!-- Bordure lumineuse tournante -->
            <span class="absolute inset-0 rounded-lg opacity-75 blur-sm bg-gradient-to-r from-blue-400 via-green-400 to-blue-400 bg-[length:200%_100%] animate-gradient"></span>
            <!-- Effet de glow externe -->
            <span class="absolute -inset-1 rounded-lg opacity-30 blur-md bg-gradient-to-r from-blue-500 via-green-500 to-blue-500 bg-[length:200%_100%] animate-gradient -z-10"></span>
            <!-- Particules brillantes au survol -->
            <span class="absolute inset-0 opacity-0 group-hover:opacity-100 transition-opacity duration-500">
              <span class="absolute top-1/4 left-1/4 w-1 h-1 bg-white rounded-full animate-sparkle"></span>
              <span class="absolute top-3/4 left-2/3 w-1 h-1 bg-white rounded-full animate-sparkle" style="animation-delay: 0.2s"></span>
              <span class="absolute top-1/2 left-3/4 w-1 h-1 bg-white rounded-full animate-sparkle" style="animation-delay: 0.4s"></span>
            </span>
          </a>
        </div>

        <!-- Stats -->
        <div class="grid grid-cols-2 md:grid-cols-4 gap-2 md:gap-3 max-w-2xl mx-auto mt-8">
          <div v-for="stat in stats" :key="stat.label"
               class="bg-gray-900/40 border border-gray-800/50 rounded-lg p-2 md:p-3 group hover:border-green-500/50 hover:bg-gray-900/60 backdrop-blur-sm transition-all duration-500">
            <div class="text-2xl md:text-3xl font-mono font-bold text-green-400 mb-1 group-hover:scale-110 transition-transform duration-500">
              {{ stat.value }}{{ stat.plus ? '+' : '' }}
            </div>
            <div class="text-xs md:text-sm text-gray-400 font-mono uppercase tracking-wider break-words">
              {{ stat.label }}
            </div>
            <div class="h-0.5 w-0 bg-gradient-to-r from-green-500 to-blue-500 group-hover:w-full transition-all duration-700 mt-2"></div>
          </div>
        </div>

        <!-- Scroll indicator -->
        <div class="mt-12">
          <div class="text-gray-500 text-base font-mono mb-2">{{ t('hero.scrollDown') }}</div>
          <div class="w-6 h-10 border-2 border-gray-700 rounded-full mx-auto flex justify-center">
            <div class="w-1 h-3 bg-green-400 rounded-full mt-2 animate-pulse"></div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
import { ref, onMounted, onUnmounted, computed, watch } from 'vue'
import { useThemeStore } from '@/stores/theme'
import { useI18n } from 'vue-i18n'

const themeStore = useThemeStore()
const { t, locale } = useI18n()

// Animation typing
const fullName = 'MAMOUDOU BIA'
const displayedName = ref('')

// Rôles rotatifs avec traductions
const roles = computed(() => [
  t('hero.roles.webMobile'),
  t('hero.roles.game'),
  t('hero.roles.uiux'),
  t('hero.roles.itSecurity'),
  t('hero.roles.ai'),
  t('hero.roles.fullstack')
])
const currentRole = ref('')
let roleIndex = 0
let roleInterval = null

// Stats avec traductions - Données réelles et pertinentes
const stats = computed(() => [
  { value: '2', label: t('hero.stats.experience'), plus: true },
  { value: '15', label: t('hero.stats.technologies'), plus: true },
  { value: '10', label: t('hero.stats.projects'), plus: true },
  { value: '✓', label: t('hero.stats.availability'), plus: false },
])

// ===== BACKGROUND GEEK =====
// Colonnes de code Matrix
const matrixColumns = ref([])

// Points de réseau
const networkNodes = ref([])

// Lignes de connexion
const connectionLines = ref([])

// Générer une colonne de code Matrix
const generateMatrixColumn = () => {
  const chars = '01アイウエオカキクケコABCDEF0123456789<>{}[]()'
  let column = ''
  const length = 15 + Math.floor(Math.random() * 10)

  for (let i = 0; i < length; i++) {
    const char = chars[Math.floor(Math.random() * chars.length)]
    // Alterner opacité pour effet dégradé
    const opacity = 0.2 + (i / length) * 0.6
    column += `<span style="opacity: ${opacity}">${char}</span>`
  }
  return column
}

// Initialiser le background geek
const initGeekBackground = () => {
  // Générer 25 colonnes Matrix
  matrixColumns.value = Array.from({ length: 25 }, (_, i) => ({
    id: i,
    position: (i * 4), // Espacement régulier
    speed: 10 + Math.random() * 15, // Vitesse variable
    delay: Math.random() * 10, // Décalage aléatoire
    content: generateMatrixColumn()
  }))

  // Générer 40 points de réseau
  networkNodes.value = Array.from({ length: 40 }, (_, i) => ({
    x: Math.random() * 100,
    y: Math.random() * 100,
    size: i % 5 === 0 ? 'md' : i % 3 === 0 ? 'sm' : 'xs',
    opacity: 0.2 + Math.random() * 0.4
  }))

  // Générer 15 lignes de connexion
  connectionLines.value = Array.from({ length: 15 }, (_, i) => {
    const x1 = Math.random() * 100
    const y1 = Math.random() * 100
    return {
      x1,
      y1,
      x2: Math.min(100, Math.max(0, x1 + (Math.random() * 40 - 20))),
      y2: Math.min(100, Math.max(0, y1 + (Math.random() * 40 - 20)))
    }
  })
}

// Variable pour stocker le timeout de l'animation des rôles
let roleAnimationTimeout = null

// Animation typing pour les rôles
const typeRole = () => {
  const role = roles.value[roleIndex]
  let charIndex = 0
  let isDeleting = false

  const type = () => {
    if (isDeleting) {
      currentRole.value = role.substring(0, charIndex - 1)
      charIndex--
    } else {
      currentRole.value = role.substring(0, charIndex + 1)
      charIndex++
    }

    let typeSpeed = isDeleting ? 50 : 100

    if (!isDeleting && charIndex === role.length) {
      isDeleting = true
      typeSpeed = 2000 // Pause à la fin
    } else if (isDeleting && charIndex === 0) {
      // Passer au rôle suivant
      roleIndex = (roleIndex + 1) % roles.value.length
      // Recommencer l'animation avec le nouveau rôle
      roleAnimationTimeout = setTimeout(typeRole, 500)
      return
    }

    roleAnimationTimeout = setTimeout(type, typeSpeed)
  }

  type()
}

// Watcher pour réinitialiser l'animation des rôles quand la langue change
watch(locale, () => {
  // Arrêter l'animation en cours
  if (roleAnimationTimeout) {
    clearTimeout(roleAnimationTimeout)
  }
  // Réinitialiser et redémarrer
  roleIndex = 0
  currentRole.value = ''
  setTimeout(typeRole, 500)
})

// Animation typing
onMounted(() => {
  // Initialiser le background
  initGeekBackground()

  // Animation du nom
  let index = 0
  const typingInterval = setInterval(() => {
    if (index < fullName.length) {
      displayedName.value += fullName[index]
      index++
    } else {
      clearInterval(typingInterval)
    }
  }, 150)

  // Démarrer l'animation des rôles après celle du nom  
  setTimeout(() => {
    currentRole.value = ''
    typeRole()
  }, 2000)
})

onUnmounted(() => {
  // Nettoyage si nécessaire
})
</script>

<style>
/* Police Inter déjà importée dans main.css */


/* Curseur clignotant */
.text-green-400:last-child {
  animation: blink 1s infinite;
}

@keyframes blink {
  0%, 100% { opacity: 1; }
  50% { opacity: 0; }
}

/* Animation de gradient pour le bouton Hire Me */
@keyframes gradient {
  0% {
    background-position: 0% 50%;
  }
  50% {
    background-position: 100% 50%;
  }
  100% {
    background-position: 0% 50%;
  }
}

.animate-gradient {
  animation: gradient 3s ease infinite;
}

/* Animation de particules scintillantes */
@keyframes sparkle {
  0%, 100% {
    opacity: 0;
    transform: scale(0);
  }
  50% {
    opacity: 1;
    transform: scale(1.5);
  }
}

.animate-sparkle {
  animation: sparkle 1.5s ease-in-out infinite;
}

/* Style du bouton Hire Me */
.hire-me-btn {
  box-shadow: 0 0 20px rgba(16, 185, 129, 0.3);
  transition: all 0.3s ease;
}

.hire-me-btn:hover {
  box-shadow: 0 0 30px rgba(16, 185, 129, 0.5), 0 0 60px rgba(59, 130, 246, 0.3);
}

/* ===== ANIMATIONS BACKGROUND GEEK ===== */

/* Chute des colonnes Matrix */
@keyframes matrixFall {
  from {
    transform: translateY(-100%);
    opacity: 0;
  }
  10% { opacity: 0.5; }
  to {
    transform: translateY(100vh);
    opacity: 0;
  }
}

.matrix-column {
  animation: matrixFall linear infinite;
  line-height: 1.8;
}

/* Pulsation des points réseau */
@keyframes nodePulse {
  0%, 100% {
    transform: scale(1);
    opacity: 0.3;
  }
  50% {
    transform: scale(1.1);
    opacity: 0.6;
  }
}

.network-node {
  animation: nodePulse 3s ease-in-out infinite;
}

/* Animation des lignes de connexion */
@keyframes lineFlow {
  0% { stroke-dashoffset: 0; }
  100% { stroke-dashoffset: 20; }
}

.connection-line {
  stroke-dasharray: 10, 5;
  animation: lineFlow 3s linear infinite;
}

/* Effet scanlines */
.scanlines {
  background: linear-gradient(
    to bottom,
    transparent 50%,
    rgba(0, 255, 0, 0.03) 51%
  );
  background-size: 100% 8px;
}

/* Assombrir légèrement le background pour mieux voir le texte */
.bg-black {
  background: linear-gradient(to bottom, #000000 0%, #0a0a0a 100%);
}

/* Animation fade pour les rôles */
.font-share-tech span {
  transition: opacity 0.5s ease-in-out;
}

/* Garantir une ligne sur tous les écrans */
.whitespace-nowrap {
  white-space: nowrap;
}

/* ===== HERO TITLE RESPONSIVE ===== */

/* Base styles pour le titre */
.hero-title {
  font-size: 2rem; /* 32px base */
  line-height: 1.2;
}

.greeting-text {
  display: inline;
}

.name-text {
  display: inline;
  white-space: nowrap;
}

/* Mobile break - caché par défaut, visible uniquement sur mobile */
.mobile-break {
  display: none; /* CACHÉ PAR DÉFAUT */
}

/* Mobile (très petits écrans) */
@media (max-width: 374px) {
  .hero-title {
    font-size: 1.5rem !important; /* 24px */
  }
  
  .mobile-break {
    display: block !important; /* Saut de ligne sur très petit mobile */
  }
}

/* Mobile standard */
@media (max-width: 640px) {
  .hero-title {
    font-size: 1.875rem; /* 30px */
    line-height: 1.3;
  }
  
  .mobile-break {
    display: block !important; /* Saut de ligne sur mobile */
  }

  /* Réduire le nombre de colonnes Matrix sur mobile */
  .matrix-column {
    font-size: 0.7rem !important;
  }
}

/* Tablettes - UNE SEULE LIGNE */
@media (min-width: 641px) and (max-width: 768px) {
  .hero-title {
    font-size: 2rem; /* 32px - RÉDUIT */
  }
  
  .mobile-break {
    display: none !important; /* PAS de saut de ligne */
  }
}

/* Desktop petit - UNE SEULE LIGNE */
@media (min-width: 769px) and (max-width: 1023px) {
  .hero-title {
    font-size: 2.5rem; /* 40px - RÉDUIT */
  }
  
  .mobile-break {
    display: none !important; /* PAS de saut de ligne */
  }
}

/* Desktop moyen - UNE SEULE LIGNE */
@media (min-width: 1024px) and (max-width: 1279px) {
  .hero-title {
    font-size: 3rem; /* 48px - RÉDUIT */
  }
  
  .mobile-break {
    display: none !important; /* PAS de saut de ligne */
  }
}

/* Desktop large - UNE SEULE LIGNE */
@media (min-width: 1280px) and (max-width: 1535px) {
  .hero-title {
    font-size: 3.5rem; /* 56px - RÉDUIT */
  }
  
  .mobile-break {
    display: none !important; /* PAS de saut de ligne */
  }
}

/* Extra large screens - UNE SEULE LIGNE */
@media (min-width: 1536px) {
  .hero-title {
    font-size: 4rem; /* 64px - RÉDUIT */
  }
  
  .mobile-break {
    display: none !important; /* PAS de saut de ligne */
  }
}



</style>
