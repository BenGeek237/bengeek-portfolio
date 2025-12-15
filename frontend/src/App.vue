<template>
  <div id="app" class="min-h-screen bg-gray-50 dark:bg-gray-900 flex flex-col">
    <Navbar />
    <main class="flex-grow relative overflow-hidden">
      <router-view v-slot="{ Component, route }">
        <transition 
          :name="getTransitionName(route)"
          mode="out-in"
          @before-enter="beforeEnter"
          @enter="enter"
          @leave="leave"
        >
          <component :is="Component" :key="route.path" />
        </transition>
      </router-view>
    </main>
    <Footer />
    <ScrollToTop />
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import Navbar from '@/components/layout/Navbar.vue'
import Footer from '@/components/layout/Footer.vue'
import ScrollToTop from '@/components/ui/ScrollToTop.vue'

const router = useRouter()
const previousRoute = ref(null)

// Déterminer le nom de la transition selon la direction
const getTransitionName = (route) => {
  if (!previousRoute.value) {
    previousRoute.value = route
    return 'fade'
  }

  const toIndex = route.meta?.index || 0
  const fromIndex = previousRoute.value.meta?.index || 0

  previousRoute.value = route

  // Si on va vers une page avec un index plus élevé, slide vers la gauche
  // Si on revient en arrière, slide vers la droite
  if (toIndex > fromIndex) {
    return 'slide-left'
  } else if (toIndex < fromIndex) {
    return 'slide-right'
  }

  return route.meta?.transition || 'fade'
}

// Hooks d'animation
const beforeEnter = (el) => {
  el.style.opacity = '0'
}

const enter = (el, done) => {
  el.offsetHeight // Force reflow
  el.style.transition = 'opacity 0.3s ease'
  el.style.opacity = '1'
  setTimeout(done, 300)
}

const leave = (el, done) => {
  el.style.transition = 'opacity 0.3s ease'
  el.style.opacity = '0'
  setTimeout(done, 300)
}
</script>

<style>
/* Fade Transition */
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.3s ease;
}

.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}

/* Slide Left Transition */
.slide-left-enter-active,
.slide-left-leave-active {
  transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);
}

.slide-left-enter-from {
  opacity: 0;
  transform: translateX(30px);
}

.slide-left-leave-to {
  opacity: 0;
  transform: translateX(-30px);
}

/* Slide Right Transition */
.slide-right-enter-active,
.slide-right-leave-active {
  transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);
}

.slide-right-enter-from {
  opacity: 0;
  transform: translateX(-30px);
}

.slide-right-leave-to {
  opacity: 0;
  transform: translateX(30px);
}

/* Slide Up Transition */
.slide-up-enter-active,
.slide-up-leave-active {
  transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);
}

.slide-up-enter-from {
  opacity: 0;
  transform: translateY(30px);
}

.slide-up-leave-to {
  opacity: 0;
  transform: translateY(-30px);
}

/* Scale Transition */
.scale-enter-active,
.scale-leave-active {
  transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
}

.scale-enter-from {
  opacity: 0;
  transform: scale(0.95);
}

.scale-leave-to {
  opacity: 0;
  transform: scale(1.05);
}
</style>