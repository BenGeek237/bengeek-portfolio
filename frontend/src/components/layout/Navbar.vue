<template>
  <nav class="fixed top-0 w-full backdrop-blur-lg z-50 border-b transition-all duration-300"
       :class="themeStore.darkMode ? 'bg-gray-900/90 border-gray-800/50' : 'bg-white/90 border-gray-200/50'">
    <div class="container mx-auto px-4 sm:px-6 lg:px-8">
      <div class="flex justify-between items-center h-16">
        <!-- Logo Amélioré -->
        <router-link to="/" class="flex items-center space-x-3 group">
          <div class="relative">
            <div class="w-10 h-10 bg-gradient-to-br from-primary-600 to-purple-600 rounded-lg flex items-center justify-center shadow-lg group-hover:shadow-primary-500/50 transition-all duration-300 group-hover:scale-110">
              <span class="text-white font-black text-lg">BG</span>
            </div>
            <div class="absolute -top-1 -right-1 w-3 h-3 bg-green-500 rounded-full border-2 border-white dark:border-gray-900 animate-pulse"></div>
          </div>
          <div class="flex flex-col">
            <span class="text-xl font-black tracking-tight"
                  :class="themeStore.darkMode ? 'text-white' : 'text-gray-900'">
              <span class="text-transparent bg-clip-text bg-gradient-to-r from-primary-600 to-purple-600">BenGeek</span>
              
            </span>
            
            <span class="text-[10px] font-sans tracking-wider font-medium"
                  :class="themeStore.darkMode ? 'text-gray-500' : 'text-gray-400'">
              // fullstack developer
            </span>
          </div>
        </router-link>

        <!-- Navigation Desktop Centrée -->
        <div class="hidden md:flex items-center justify-center flex-1 space-x-1">
          <template v-for="item in navItems" :key="item.name">
            <!-- Lien Projects vers la page -->
            <router-link
              v-if="item.id === 'projects'"
              to="/projects"
              class="px-4 py-2 rounded-lg font-sans text-sm font-medium transition-all duration-300 relative group"
              :class="route.path.includes('/projects')
                ? 'text-primary-600 dark:text-primary-400 bg-primary-50 dark:bg-primary-900/20' 
                : 'text-gray-600 dark:text-gray-300 hover:text-primary-600 dark:hover:text-primary-400 hover:bg-gray-100 dark:hover:bg-gray-800/50'"
            >
              {{ item.name }}
              <span v-if="route.path.includes('/projects')" 
                    class="absolute bottom-0 left-1/2 -translate-x-1/2 w-1 h-1 bg-primary-600 dark:bg-primary-400 rounded-full"></span>
            </router-link>
            
            <!-- Autres liens avec scroll -->
            <button
              v-else
              @click="scrollToSection(item.id)"
              class="px-4 py-2 rounded-lg font-sans text-sm font-medium transition-all duration-300 relative group"
              :class="activeSection === item.id 
                ? 'text-primary-600 dark:text-primary-400 bg-primary-50 dark:bg-primary-900/20' 
                : 'text-gray-600 dark:text-gray-300 hover:text-primary-600 dark:hover:text-primary-400 hover:bg-gray-100 dark:hover:bg-gray-800/50'"
            >
              {{ item.name }}
              <!-- Indicateur actif -->
              <span v-if="activeSection === item.id" 
                    class="absolute bottom-0 left-1/2 -translate-x-1/2 w-1 h-1 bg-primary-600 dark:bg-primary-400 rounded-full"></span>
            </button>
          </template>
          
          <!-- Séparateur -->
          <div class="h-6 w-px bg-gray-300 dark:bg-gray-700 mx-2"></div>
          
          <!-- Lien Blog -->
          <router-link 
            to="/blog"
            class="px-4 py-2 rounded-lg font-sans text-sm font-medium transition-all duration-300"
            :class="route.path.includes('/blog')
              ? 'text-green-600 dark:text-green-400 bg-green-50 dark:bg-green-900/20'
              : 'text-gray-600 dark:text-gray-300 hover:text-green-600 dark:hover:text-green-400 hover:bg-gray-100 dark:hover:bg-gray-800/50'"
          >
            BLOG
          </router-link>
        </div>

        <!-- Actions à droite -->
        <div class="hidden md:flex items-center space-x-2">
          
          <!-- Toggle Langue -->
          <button 
            @click="toggleLanguage"
            class="p-2.5 rounded-lg transition-all duration-300 group relative overflow-hidden"
            :class="themeStore.darkMode 
              ? 'bg-gray-800 hover:bg-gray-700' 
              : 'bg-gray-100 hover:bg-gray-200'"
            aria-label="Toggle language"
            title="Changer de langue / Change language"
          >
            <div class="relative w-5 h-5 flex items-center justify-center">
              <transition
                enter-active-class="transition-all duration-300"
                enter-from-class="opacity-0 scale-50 rotate-180"
                enter-to-class="opacity-100 scale-100 rotate-0"
                leave-active-class="transition-all duration-300"
                leave-from-class="opacity-100 scale-100 rotate-0"
                leave-to-class="opacity-0 scale-50 -rotate-180"
                mode="out-in"
              >
                <span v-if="locale === 'fr'" key="fr" class="font-bold font-mono">FR</span>
                <span v-else key="en" class="font-bold font-mono">EN</span>
              </transition>
            </div>
          </button>
          
          <!-- Toggle Thème -->
          <button 
            @click="toggleTheme"
            class="p-2.5 rounded-lg transition-all duration-300 group relative"
            :class="themeStore.darkMode 
              ? 'bg-gray-800 hover:bg-gray-700 text-yellow-400' 
              : 'bg-gray-100 hover:bg-gray-200 text-gray-700'"
            aria-label="Toggle theme"
            title="Toggle theme (Ctrl+T)"
          >
            <svg v-if="themeStore.darkMode" class="w-5 h-5 transition-transform group-hover:rotate-180 duration-500" fill="currentColor" viewBox="0 0 20 20">
              <path d="M17.293 13.293A8 8 0 016.707 2.707a8.001 8.001 0 1010.586 10.586z" />
            </svg>
            <svg v-else class="w-5 h-5 transition-transform group-hover:rotate-180 duration-500" fill="currentColor" viewBox="0 0 20 20">
              <path fill-rule="evenodd" d="M10 2a1 1 0 011 1v1a1 1 0 11-2 0V3a1 1 0 011-1zm4 8a4 4 0 11-8 0 4 4 0 018 0zm-.464 4.95l.707.707a1 1 0 001.414-1.414l-.707-.707a1 1 0 00-1.414 1.414zm2.12-10.607a1 1 0 010 1.414l-.706.707a1 1 0 11-1.414-1.414l.707-.707a1 1 0 011.414 0zM17 11a1 1 0 100-2h-1a1 1 0 100 2h1zm-7 4a1 1 0 011 1v1a1 1 0 11-2 0v-1a1 1 0 011-1zM5.05 6.464A1 1 0 106.465 5.05l-.708-.707a1 1 0 00-1.414 1.414l.707.707zm1.414 8.486l-.707.707a1 1 0 01-1.414-1.414l.707-.707a1 1 0 011.414 1.414zM4 11a1 1 0 100-2H3a1 1 0 000 2h1z" clip-rule="evenodd" />
            </svg>
          </button>
          
          <!-- Bouton Contact -->
          <button 
            @click="scrollToSection('contact')"
            class="ml-2 px-5 py-2.5 rounded-lg font-sans text-sm font-bold bg-gradient-to-r from-primary-600 to-purple-600 hover:from-primary-700 hover:to-purple-700 text-white shadow-lg hover:shadow-xl hover:shadow-primary-500/50 transition-all duration-300 hover:-translate-y-0.5 flex items-center gap-2"
          >
            <span>{{ t('nav.contact').toUpperCase() }}</span>
            <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 7l5 5m0 0l-5 5m5-5H6" />
            </svg>
          </button>
        </div>

        <!-- Hamburger Menu Mobile Amélioré -->
        <button 
          @click="isMobileMenuOpen = !isMobileMenuOpen"
          class="md:hidden p-2 rounded-lg transition-all duration-300 relative group"
          :class="themeStore.darkMode 
            ? 'bg-gray-800 hover:bg-gray-700' 
            : 'bg-gray-100 hover:bg-gray-200'"
          aria-label="Menu mobile"
          aria-expanded="isMobileMenuOpen"
        >
          <div class="w-6 h-5 flex flex-col justify-between">
            <span class="w-full h-0.5 rounded-full transition-all duration-300"
                  :class="[
                    isMobileMenuOpen ? 'rotate-45 translate-y-2' : '',
                    themeStore.darkMode ? 'bg-gray-300' : 'bg-gray-700'
                  ]"></span>
            <span class="w-full h-0.5 rounded-full transition-all duration-300"
                  :class="[
                    isMobileMenuOpen ? 'opacity-0' : '',
                    themeStore.darkMode ? 'bg-gray-300' : 'bg-gray-700'
                  ]"></span>
            <span class="w-full h-0.5 rounded-full transition-all duration-300"
                  :class="[
                    isMobileMenuOpen ? '-rotate-45 -translate-y-2' : '',
                    themeStore.darkMode ? 'bg-gray-300' : 'bg-gray-700'
                  ]"></span>
          </div>
        </button>
      </div>

      <!-- Menu Mobile avec Animation -->
      <transition
        enter-active-class="transition-all duration-300 ease-out"
        enter-from-class="opacity-0 -translate-y-4"
        enter-to-class="opacity-100 translate-y-0"
        leave-active-class="transition-all duration-200 ease-in"
        leave-from-class="opacity-100 translate-y-0"
        leave-to-class="opacity-0 -translate-y-4"
      >
        <div 
          v-if="isMobileMenuOpen" 
          class="md:hidden border-t"
          :class="themeStore.darkMode ? 'bg-gray-900/95 border-gray-800' : 'bg-white/95 border-gray-200'"
        >
          <div class="px-4 py-4 space-y-1">
            <!-- Liens mobile -->
            <template v-for="item in navItems" :key="item.name">
              <!-- Lien Projects vers la page -->
              <router-link
                v-if="item.id === 'projects'"
                to="/projects"
                @click="isMobileMenuOpen = false"
                class="block w-full text-left py-3 px-4 rounded-lg font-sans text-sm font-medium transition-all duration-200"
                :class="route.path.includes('/projects')
                  ? 'text-primary-600 dark:text-primary-400 bg-primary-50 dark:bg-primary-900/20'
                  : 'text-gray-600 dark:text-gray-300 hover:bg-gray-100 dark:hover:bg-gray-800/50'"
              >
                <div class="flex items-center justify-between">
                  <span>{{ item.name }}</span>
                  <svg v-if="route.path.includes('/projects')" class="w-4 h-4" fill="currentColor" viewBox="0 0 20 20">
                    <path fill-rule="evenodd" d="M7.293 14.707a1 1 0 010-1.414L10.586 10 7.293 6.707a1 1 0 011.414-1.414l4 4a1 1 0 010 1.414l-4 4a1 1 0 01-1.414 0z" clip-rule="evenodd" />
                  </svg>
                </div>
              </router-link>
              
              <!-- Autres liens avec scroll -->
              <button
                v-else
                @click="scrollToSection(item.id); isMobileMenuOpen = false"
                class="block w-full text-left py-3 px-4 rounded-lg font-sans text-sm font-medium transition-all duration-200"
                :class="activeSection === item.id
                  ? 'text-primary-600 dark:text-primary-400 bg-primary-50 dark:bg-primary-900/20'
                  : 'text-gray-600 dark:text-gray-300 hover:bg-gray-100 dark:hover:bg-gray-800/50'"
              >
                <div class="flex items-center justify-between">
                  <span>{{ item.name }}</span>
                  <svg v-if="activeSection === item.id" class="w-4 h-4" fill="currentColor" viewBox="0 0 20 20">
                    <path fill-rule="evenodd" d="M7.293 14.707a1 1 0 010-1.414L10.586 10 7.293 6.707a1 1 0 011.414-1.414l4 4a1 1 0 010 1.414l-4 4a1 1 0 01-1.414 0z" clip-rule="evenodd" />
                  </svg>
                </div>
              </button>
            </template>
            
            <router-link 
              to="/blog"
              class="block py-3 px-4 rounded-lg font-sans text-sm font-medium transition-all duration-200"
              :class="route.path.includes('/blog')
                ? 'text-green-600 dark:text-green-400 bg-green-50 dark:bg-green-900/20'
                : 'text-gray-600 dark:text-gray-300 hover:bg-gray-100 dark:hover:bg-gray-800/50'"
              @click="isMobileMenuOpen = false"
            >
              {{ t('nav.blog').toUpperCase() }}
            </router-link>
            
            <!-- Séparateur -->
            <div class="h-px bg-gray-200 dark:bg-gray-800 my-2"></div>
            
            <!-- Toggle langue mobile -->
            <button 
              @click="toggleLanguage"
              class="flex items-center justify-between w-full py-3 px-4 rounded-lg font-sans text-sm font-medium transition-all duration-200"
              :class="themeStore.darkMode
                ? 'text-gray-300 hover:bg-gray-800/50'
                : 'text-gray-600 hover:bg-gray-100'"
            >
              <div class="flex items-center gap-3">
                <span v-if="locale === 'fr'" class="font-bold font-mono">FR</span>
                <span v-else class="font-bold font-mono">EN</span>
                {{ locale === 'fr' ? 'FRANÇAIS' : 'ENGLISH' }}
              </div>
              <span class="text-xs opacity-50">{{ locale === 'fr' ? 'FR' : 'EN' }}</span>
            </button>
            
            <!-- Toggle thème mobile -->
            <button 
              @click="toggleTheme"
              class="flex items-center justify-between w-full py-3 px-4 rounded-lg font-sans text-sm font-medium transition-all duration-200"
              :class="themeStore.darkMode
                ? 'text-gray-300 hover:bg-gray-800/50'
                : 'text-gray-600 hover:bg-gray-100'"
            >
              <div class="flex items-center gap-3">
                <MoonIcon v-if="themeStore.darkMode" class="w-5 h-5 text-yellow-400" />
                <SunIcon v-else class="w-5 h-5 text-yellow-500" />
                {{ themeStore.darkMode ? (locale === 'fr' ? 'MODE CLAIR' : 'LIGHT MODE') : (locale === 'fr' ? 'MODE SOMBRE' : 'DARK MODE') }}
              </div>
              <span class="text-xs opacity-50">CTRL+T</span>
            </button>
            
            <!-- Contact mobile -->
            <button 
              @click="scrollToSection('contact'); isMobileMenuOpen = false"
              class="block w-full text-left py-3 px-4 mt-2 rounded-lg font-sans text-sm font-bold bg-gradient-to-r from-primary-600 to-purple-600 text-white shadow-lg transition-all duration-300 flex items-center justify-between"
            >
              <span>{{ t('nav.contact').toUpperCase() }}</span>
              <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 7l5 5m0 0l-5 5m5-5H6" />
              </svg>
            </button>
          </div>
        </div>
      </transition>
    </div>
  </nav>
</template>

<script setup>
import { ref, onMounted, onUnmounted, computed } from 'vue'
import { useRouter, useRoute } from 'vue-router'
import { useThemeStore } from '@/stores/theme'
import { useI18n } from 'vue-i18n'
import { useLanguageStore } from '@/stores/language'
import { MoonIcon, SunIcon } from '@heroicons/vue/24/outline'

const router = useRouter()
const route = useRoute()
const themeStore = useThemeStore()
const { t, locale } = useI18n()
const languageStore = useLanguageStore()

const isMobileMenuOpen = ref(false)
const activeSection = ref('hero')

// Items de navigation avec traductions
const navItems = computed(() => [
  { name: t('nav.home').toUpperCase(), id: 'hero' },
  { name: t('nav.about').toUpperCase(), id: 'about' },
  { name: t('nav.projects').toUpperCase(), id: 'projects' },
  { name: t('nav.skills').toUpperCase(), id: 'skills' },
])

// Fonction pour changer de langue
const toggleLanguage = () => {
  const newLocale = languageStore.toggleLocale()
  locale.value = newLocale
}

// Fonction pour scroller vers une section
const scrollToSection = (sectionId) => {
  if (route.path !== '/') {
    router.push('/')
    setTimeout(() => {
      scrollToElement(sectionId)
    }, 100)
  } else {
    scrollToElement(sectionId)
  }
  isMobileMenuOpen.value = false
}

// Fonction utilitaire pour scroller
const scrollToElement = (elementId) => {
  const element = document.getElementById(elementId)
  if (element) {
    const offset = 80
    const elementPosition = element.getBoundingClientRect().top
    const offsetPosition = elementPosition + window.pageYOffset - offset
    
    window.scrollTo({
      top: offsetPosition,
      behavior: 'smooth'
    })
  }
}

// Détecter la section active pendant le scroll
const handleScroll = () => {
  if (route.path !== '/') return
  
  const sections = navItems.map(item => document.getElementById(item.id))
  const scrollPosition = window.scrollY + 100
  
  for (let i = sections.length - 1; i >= 0; i--) {
    if (sections[i] && scrollPosition >= sections[i].offsetTop) {
      activeSection.value = navItems[i].id
      break
    }
  }
}

// Gestion des raccourcis clavier
const handleKeydown = (e) => {
  if ((e.ctrlKey || e.metaKey) && e.key === 't') {
    e.preventDefault()
    toggleTheme()
  }
  
  if (e.key === 'Escape' && isMobileMenuOpen.value) {
    isMobileMenuOpen.value = false
  }
}

const toggleTheme = () => {
  themeStore.toggleTheme()
}

// Ajouter les écouteurs
onMounted(() => {
  window.addEventListener('scroll', handleScroll)
  window.addEventListener('keydown', handleKeydown)
  setTimeout(handleScroll, 100)
})

onUnmounted(() => {
  window.removeEventListener('scroll', handleScroll)
  window.removeEventListener('keydown', handleKeydown)
})
</script>

<style scoped>
/* Effet de bordure animée */
nav::after {
  content: '';
  position: absolute;
  bottom: 0;
  left: 0;
  width: 100%;
  height: 1px;
  background: linear-gradient(90deg, 
    transparent, 
    theme('colors.primary.500'), 
    theme('colors.purple.500'), 
    transparent
  );
  opacity: 0.3;
}
</style>