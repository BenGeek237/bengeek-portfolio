<template>
  <nav class="fixed top-0 w-full z-50 border-b transition-colors duration-300"
       :class="themeStore.darkMode
         ? 'bg-gray-950/95 border-gray-800 backdrop-blur-sm'
         : 'bg-white/95 border-gray-200 backdrop-blur-sm'">
    <div class="container mx-auto px-6 sm:px-8">
      <div class="flex justify-between items-center h-16">

        <!-- Logo -->
        <router-link to="/" class="flex items-center gap-2.5 group">
          <img
            src="/logo/bg.png"
            alt="BenGeek Logo"
            class="w-9 h-9 rounded-lg object-contain"
            :class="themeStore.darkMode ? 'bg-white/10' : 'bg-gray-100'"
          />
          <div class="flex flex-col leading-none">
            <span class="text-sm font-semibold text-gray-900 dark:text-white">Mamoudou Bia</span>
            <span class="text-[11px] text-gray-400 dark:text-gray-500 font-normal">Fullstack Developer</span>
          </div>
        </router-link>

        <!-- Navigation Desktop -->
        <div class="hidden md:flex items-center gap-1">
          <template v-for="item in navItems" :key="item.name">
            <router-link
              v-if="item.id === 'projects'"
              to="/projects"
              class="px-3 py-1.5 text-sm font-medium rounded-md transition-colors duration-150"
              :class="route.path.includes('/projects')
                ? 'text-gray-900 dark:text-white bg-gray-100 dark:bg-gray-800'
                : 'text-gray-500 dark:text-gray-400 hover:text-gray-900 dark:hover:text-white hover:bg-gray-50 dark:hover:bg-gray-800/60'"
            >{{ item.name }}</router-link>

            <button
              v-else
              @click="scrollToSection(item.id)"
              class="px-3 py-1.5 text-sm font-medium rounded-md transition-colors duration-150"
              :class="activeSection === item.id
                ? 'text-gray-900 dark:text-white bg-gray-100 dark:bg-gray-800'
                : 'text-gray-500 dark:text-gray-400 hover:text-gray-900 dark:hover:text-white hover:bg-gray-50 dark:hover:bg-gray-800/60'"
            >{{ item.name }}</button>
          </template>

          <div class="w-px h-4 bg-gray-200 dark:bg-gray-800 mx-1"></div>

          <router-link
            to="/blog"
            class="px-3 py-1.5 text-sm font-medium rounded-md transition-colors duration-150"
            :class="route.path.includes('/blog')
              ? 'text-gray-900 dark:text-white bg-gray-100 dark:bg-gray-800'
              : 'text-gray-500 dark:text-gray-400 hover:text-gray-900 dark:hover:text-white hover:bg-gray-50 dark:hover:bg-gray-800/60'"
          >Blog</router-link>
        </div>

        <!-- Actions -->
        <div class="hidden md:flex items-center gap-2">
          <!-- Toggle langue -->
          <button
            @click="toggleLanguage"
            class="px-3 py-1.5 text-xs font-semibold rounded-md transition-colors duration-150"
            :class="themeStore.darkMode
              ? 'text-gray-400 hover:text-white hover:bg-gray-800'
              : 'text-gray-500 hover:text-gray-900 hover:bg-gray-100'"
            aria-label="Toggle language"
          >
            <transition name="lang" mode="out-in">
              <span :key="locale">{{ locale.toUpperCase() }}</span>
            </transition>
          </button>

          <!-- Toggle thème -->
          <button
            @click="toggleTheme"
            class="p-2 rounded-md transition-colors duration-150"
            :class="themeStore.darkMode
              ? 'text-gray-400 hover:text-white hover:bg-gray-800'
              : 'text-gray-500 hover:text-gray-900 hover:bg-gray-100'"
            aria-label="Toggle theme"
          >
            <svg v-if="themeStore.darkMode" class="w-4 h-4" fill="currentColor" viewBox="0 0 20 20">
              <path fill-rule="evenodd" d="M10 2a1 1 0 011 1v1a1 1 0 11-2 0V3a1 1 0 011-1zm4 8a4 4 0 11-8 0 4 4 0 018 0zm-.464 4.95l.707.707a1 1 0 001.414-1.414l-.707-.707a1 1 0 00-1.414 1.414zm2.12-10.607a1 1 0 010 1.414l-.706.707a1 1 0 11-1.414-1.414l.707-.707a1 1 0 011.414 0zM17 11a1 1 0 100-2h-1a1 1 0 100 2h1zm-7 4a1 1 0 011 1v1a1 1 0 11-2 0v-1a1 1 0 011-1zM5.05 6.464A1 1 0 106.465 5.05l-.708-.707a1 1 0 00-1.414 1.414l.707.707zm1.414 8.486l-.707.707a1 1 0 01-1.414-1.414l.707-.707a1 1 0 011.414 1.414zM4 11a1 1 0 100-2H3a1 1 0 000 2h1z" clip-rule="evenodd" />
            </svg>
            <svg v-else class="w-4 h-4" fill="currentColor" viewBox="0 0 20 20">
              <path d="M17.293 13.293A8 8 0 016.707 2.707a8.001 8.001 0 1010.586 10.586z" />
            </svg>
          </button>

          <!-- CTA Contact -->
          <button
            @click="scrollToSection('contact')"
            class="btn-primary ml-1"
          >
            {{ t('nav.contact') }}
          </button>
        </div>

        <!-- Hamburger Mobile -->
        <button
          @click="isMobileMenuOpen = !isMobileMenuOpen"
          class="md:hidden p-2 rounded-md transition-colors"
          :class="themeStore.darkMode ? 'text-gray-400 hover:bg-gray-800' : 'text-gray-500 hover:bg-gray-100'"
          aria-label="Menu mobile"
        >
          <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path v-if="!isMobileMenuOpen" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"/>
            <path v-else stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"/>
          </svg>
        </button>
      </div>

      <!-- Menu Mobile -->
      <transition
        enter-active-class="transition-all duration-200 ease-out"
        enter-from-class="opacity-0 -translate-y-2"
        enter-to-class="opacity-100 translate-y-0"
        leave-active-class="transition-all duration-150 ease-in"
        leave-from-class="opacity-100 translate-y-0"
        leave-to-class="opacity-0 -translate-y-2"
      >
        <div
          v-if="isMobileMenuOpen"
          class="md:hidden border-t py-3 space-y-0.5"
          :class="themeStore.darkMode ? 'border-gray-800' : 'border-gray-200'"
        >
          <template v-for="item in navItems" :key="item.name">
            <router-link
              v-if="item.id === 'projects'"
              to="/projects"
              @click="isMobileMenuOpen = false"
              class="block px-3 py-2.5 text-sm font-medium rounded-md transition-colors"
              :class="route.path.includes('/projects')
                ? 'text-gray-900 dark:text-white bg-gray-100 dark:bg-gray-800'
                : 'text-gray-500 dark:text-gray-400 hover:text-gray-900 dark:hover:text-white'"
            >{{ item.name }}</router-link>

            <button
              v-else
              @click="scrollToSection(item.id); isMobileMenuOpen = false"
              class="block w-full text-left px-3 py-2.5 text-sm font-medium rounded-md transition-colors"
              :class="activeSection === item.id
                ? 'text-gray-900 dark:text-white bg-gray-100 dark:bg-gray-800'
                : 'text-gray-500 dark:text-gray-400 hover:text-gray-900 dark:hover:text-white'"
            >{{ item.name }}</button>
          </template>

          <router-link
            to="/blog"
            @click="isMobileMenuOpen = false"
            class="block px-3 py-2.5 text-sm font-medium rounded-md transition-colors"
            :class="route.path.includes('/blog')
              ? 'text-gray-900 dark:text-white bg-gray-100 dark:bg-gray-800'
              : 'text-gray-500 dark:text-gray-400 hover:text-gray-900 dark:hover:text-white'"
          >Blog</router-link>

          <div class="pt-2 mt-2 border-t flex items-center gap-2 px-3"
               :class="themeStore.darkMode ? 'border-gray-800' : 'border-gray-200'">
            <button @click="toggleLanguage"
              class="px-3 py-2 text-xs font-semibold rounded-md"
              :class="themeStore.darkMode ? 'text-gray-400 hover:bg-gray-800' : 'text-gray-500 hover:bg-gray-100'"
            >{{ locale.toUpperCase() }}</button>
            <button @click="toggleTheme"
              class="p-2 rounded-md"
              :class="themeStore.darkMode ? 'text-gray-400 hover:bg-gray-800' : 'text-gray-500 hover:bg-gray-100'"
            >
              <svg v-if="themeStore.darkMode" class="w-4 h-4" fill="currentColor" viewBox="0 0 20 20">
                <path fill-rule="evenodd" d="M10 2a1 1 0 011 1v1a1 1 0 11-2 0V3a1 1 0 011-1zm4 8a4 4 0 11-8 0 4 4 0 018 0zm-.464 4.95l.707.707a1 1 0 001.414-1.414l-.707-.707a1 1 0 00-1.414 1.414zm2.12-10.607a1 1 0 010 1.414l-.706.707a1 1 0 11-1.414-1.414l.707-.707a1 1 0 011.414 0zM17 11a1 1 0 100-2h-1a1 1 0 100 2h1zm-7 4a1 1 0 011 1v1a1 1 0 11-2 0v-1a1 1 0 011-1zM5.05 6.464A1 1 0 106.465 5.05l-.708-.707a1 1 0 00-1.414 1.414l.707.707zm1.414 8.486l-.707.707a1 1 0 01-1.414-1.414l.707-.707a1 1 0 011.414 1.414zM4 11a1 1 0 100-2H3a1 1 0 000 2h1z" clip-rule="evenodd" />
              </svg>
              <svg v-else class="w-4 h-4" fill="currentColor" viewBox="0 0 20 20">
                <path d="M17.293 13.293A8 8 0 016.707 2.707a8.001 8.001 0 1010.586 10.586z" />
              </svg>
            </button>
            <button
              @click="scrollToSection('contact'); isMobileMenuOpen = false"
              class="flex-1 btn-primary text-center"
            >{{ t('nav.contact') }}</button>
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

const router = useRouter()
const route = useRoute()
const themeStore = useThemeStore()
const { t, locale } = useI18n()
const languageStore = useLanguageStore()

const isMobileMenuOpen = ref(false)
const activeSection = ref('hero')

const navItems = computed(() => [
  { name: t('nav.home'),     id: 'hero' },
  { name: t('nav.about'),    id: 'about' },
  { name: t('nav.projects'), id: 'projects' },
  { name: t('nav.skills'),   id: 'skills' },
])

const toggleLanguage = () => {
  const newLocale = languageStore.toggleLocale()
  locale.value = newLocale
}

const scrollToSection = (sectionId) => {
  if (route.path !== '/') {
    router.push('/')
    setTimeout(() => scrollToElement(sectionId), 100)
  } else {
    scrollToElement(sectionId)
  }
  isMobileMenuOpen.value = false
}

const scrollToElement = (elementId) => {
  const el = document.getElementById(elementId)
  if (el) {
    const offset = 72
    const top = el.getBoundingClientRect().top + window.pageYOffset - offset
    window.scrollTo({ top, behavior: 'smooth' })
  }
}

const handleScroll = () => {
  if (route.path !== '/') return
  const sections = navItems.value.map(item => document.getElementById(item.id))
  const scrollY = window.scrollY + 100
  for (let i = sections.length - 1; i >= 0; i--) {
    if (sections[i] && scrollY >= sections[i].offsetTop) {
      activeSection.value = navItems.value[i].id
      break
    }
  }
}

const handleKeydown = (e) => {
  if (e.key === 'Escape' && isMobileMenuOpen.value) isMobileMenuOpen.value = false
}

const toggleTheme = () => themeStore.toggleTheme()

onMounted(() => {
  window.addEventListener('scroll', handleScroll, { passive: true })
  window.addEventListener('keydown', handleKeydown)
  setTimeout(handleScroll, 100)
})

onUnmounted(() => {
  window.removeEventListener('scroll', handleScroll)
  window.removeEventListener('keydown', handleKeydown)
})
</script>

<style scoped>
.lang-enter-active, .lang-leave-active { transition: opacity 0.15s ease; }
.lang-enter-from, .lang-leave-to { opacity: 0; }
</style>