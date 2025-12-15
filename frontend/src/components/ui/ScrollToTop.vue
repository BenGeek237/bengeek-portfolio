<template>
  <Transition
    enter-active-class="transition duration-300 ease-out"
    enter-from-class="translate-y-10 opacity-0"
    enter-to-class="translate-y-0 opacity-100"
    leave-active-class="transition duration-200 ease-in"
    leave-from-class="translate-y-0 opacity-100"
    leave-to-class="translate-y-10 opacity-0"
  >
    <button
      v-if="showButton"
      @click="scrollToTop"
      class="fixed bottom-6 right-6 md:bottom-10 md:right-10 w-12 h-12 md:w-14 md:h-14 bg-gray-900 border border-primary-500/50 text-primary-400 rounded-lg shadow-lg shadow-primary-500/20 hover:shadow-primary-500/50 hover:border-primary-400 hover:text-white hover:-translate-y-1 transition-all duration-300 flex items-center justify-center z-40 group overflow-hidden"
      aria-label="Retour en haut"
    >
      <div class="absolute inset-0 bg-gradient-to-tr from-primary-600/20 to-secondary-500/20 opacity-0 group-hover:opacity-100 transition-opacity duration-300"></div>
      <ChevronUpIcon class="w-6 h-6 md:w-8 md:h-8 relative z-10 group-hover:animate-bounce" />
    </button>
  </Transition>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue'
import { ChevronUpIcon } from '@heroicons/vue/24/outline'

const showButton = ref(false)

const handleScroll = () => {
  showButton.value = window.scrollY > 300
}

const scrollToTop = () => {
  window.scrollTo({
    top: 0,
    behavior: 'smooth'
  })
}

onMounted(() => {
  window.addEventListener('scroll', handleScroll)
})

onUnmounted(() => {
  window.removeEventListener('scroll', handleScroll)
})
</script>