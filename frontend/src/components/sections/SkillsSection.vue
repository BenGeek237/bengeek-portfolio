<template>
  <section id="skills" class="py-8 bg-white dark:bg-gray-800 overflow-hidden">
    <div class="container mx-auto px-4 sm:px-6 lg:px-8">
      <div class="text-center mb-8" data-aos="fade-up">
        <h2 class="section-title">{{ t('skills.title') }}</h2>
        <p class="section-subtitle">
          {{ t('skills.subtitle') }}
        </p>
      </div>

      <!-- Compétences en ligne unique -->
      <div class="relative">
        <!-- Conteneur avec défilement horizontal -->
        <div 
          ref="scrollContainer"
          class="overflow-x-auto scrollbar-thin scrollbar-thumb-primary-600 scrollbar-track-gray-200 dark:scrollbar-track-gray-700 pb-4 select-none transition-all duration-300"
          :class="{ 
            'cursor-grabbing scale-[0.98]': isDragging, 
            'cursor-grab': !isDragging,
            'dragging-active': isDragging
          }"
          @mousedown="startDrag"
          @mousemove="onDrag"
          @mouseup="stopDrag"
          @mouseleave="stopDrag"
        >
          <div class="flex gap-4 px-2 sm:px-4 min-w-max">
            <div 
              v-for="(skill, index) in allSkills"
              :key="index"
              class="skill-card group relative bg-gray-50 dark:bg-gray-900 rounded-xl p-3 md:p-4 text-center hover:bg-gradient-to-br hover:from-primary-50 hover:to-purple-50 dark:hover:from-gray-800 dark:hover:to-gray-700 transition-all duration-300 border border-transparent hover:border-primary-200 dark:hover:border-primary-800 w-[120px] sm:w-[140px] flex-shrink-0"
              :class="{ 
                'pointer-events-none': isDragging,
                'hover:scale-110 hover:shadow-xl': !isDragging,
                'dragging-tilt': isDragging,
                'scale-95 opacity-90': isDragging
              }"
              :style="isDragging ? `transition-delay: ${index * 10}ms` : ''"
            >
              <!-- Icône -->
              <div 
                class="text-2xl md:text-3xl mb-1.5 md:mb-2 transition-transform duration-300"
                :class="{ 'group-hover:scale-110': !isDragging, 'scale-90': isDragging }"
              >
                {{ skill.icon }}
              </div>
              
              <!-- Nom -->
              <div class="font-semibold text-gray-900 dark:text-white text-[10px] md:text-xs group-hover:text-primary-600 dark:group-hover:text-primary-400 transition-colors">
                {{ skill.name }}
              </div>
              
              <!-- Badge niveau (visible au survol) -->
              <div v-if="skill.level" class="absolute top-2 right-2 opacity-0 group-hover:opacity-100 transition-opacity duration-300">
                <span class="px-2 py-0.5 bg-primary-600 text-white text-[10px] rounded-full">
                  {{ skill.level }}%
                </span>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>




<script setup>
import { ref } from 'vue'
import { useI18n } from 'vue-i18n'

const { t } = useI18n()

const allSkills = [
  // Développement Web
  { name: 'Django', icon: '🐍', level: 95 },
  { name: 'Vue.js', icon: '⚡', level: 90 },
  { name: 'React', icon: '⚛️', level: 80 },
  { name: 'Python', icon: '🐍', level: 95 },
  { name: 'Tailwind CSS', icon: '🎨', level: 95 },

  // Game Dev & IA
  { name: 'Godot Engine', icon: '🎮', level: 85 },
  { name: 'Pygame', icon: '👾', level: 90 },
  { name: 'Intelligence Artificielle', icon: '🤖', level: 80 },

  // Cybersécurité & IT
  { name: 'Cybersécurité', icon: '🔒', level: 85 },
  { name: 'Google IT Support', icon: '💻', level: 90 },
  { name: 'Linux', icon: '🐧', level: 85 },
  { name: 'Réseaux', icon: '🌐', level: 80 },

  // Design & Création
  { name: 'Google UX Design', icon: '✨', level: 85 },
  { name: 'Figma', icon: '🖌️', level: 80 },
  { name: 'Canva', icon: '🎨', level: 95 },
  { name: 'CapCut', icon: '🎬', level: 90 },

  // Outils
  { name: 'Suite Office', icon: '📊', level: 100 },
  { name: 'Git & GitHub', icon: '🐙', level: 90 },
  { name: 'Docker', icon: '🐳', level: 75 },
  { name: 'VS Code', icon: '📝', level: 95 },
]

// Drag to scroll avec momentum
const scrollContainer = ref(null)
const isDragging = ref(false)
const startX = ref(0)
const scrollLeft = ref(0)
const lastX = ref(0)
const velocity = ref(0)
const lastTime = ref(0)

const startDrag = (e) => {
  if (!scrollContainer.value) return
  
  isDragging.value = true
  startX.value = e.pageX - scrollContainer.value.offsetLeft
  scrollLeft.value = scrollContainer.value.scrollLeft
  lastX.value = e.pageX
  lastTime.value = Date.now()
  velocity.value = 0
  
  // Ajouter une classe pour l'animation
  scrollContainer.value.style.scrollBehavior = 'auto'
}

const onDrag = (e) => {
  if (!isDragging.value || !scrollContainer.value) return
  
  e.preventDefault()
  const x = e.pageX - scrollContainer.value.offsetLeft
  const walk = (x - startX.value) * 2.5 // Multiplier pour un défilement plus rapide
  scrollContainer.value.scrollLeft = scrollLeft.value - walk
  
  // Calculer la vélocité pour l'effet de momentum
  const now = Date.now()
  const dt = now - lastTime.value
  if (dt > 0) {
    velocity.value = (e.pageX - lastX.value) / dt
  }
  lastX.value = e.pageX
  lastTime.value = now
}

const stopDrag = () => {
  if (!isDragging.value || !scrollContainer.value) return
  
  isDragging.value = false
  
  // Appliquer l'effet de momentum
  applyMomentum()
}

const applyMomentum = () => {
  if (!scrollContainer.value) return
  
  let currentVelocity = velocity.value * 30 // Facteur de momentum
  const friction = 0.92 // Friction pour ralentir progressivement
  
  const animate = () => {
    if (Math.abs(currentVelocity) < 0.5 || !scrollContainer.value) {
      scrollContainer.value.style.scrollBehavior = 'smooth'
      return
    }
    
    scrollContainer.value.scrollLeft -= currentVelocity
    currentVelocity *= friction
    
    requestAnimationFrame(animate)
  }
  
  if (Math.abs(currentVelocity) > 0.5) {
    requestAnimationFrame(animate)
  } else {
    scrollContainer.value.style.scrollBehavior = 'smooth'
  }
}
</script>


<style scoped>
/* Animations */
@keyframes float {
  0%, 100% { transform: translateY(0px); }
  50% { transform: translateY(-5px); }
}

@keyframes bounce-subtle {
  0%, 100% { transform: translateY(0px); }
  50% { transform: translateY(-3px); }
}

.animate-bounce-subtle {
  animation: bounce-subtle 2s ease-in-out infinite;
}

.group:hover {
  animation: float 2s ease-in-out infinite;
}

/* Animation de tilt pendant le drag */
@keyframes tilt {
  0%, 100% { transform: rotate(0deg) scale(0.95); }
  25% { transform: rotate(-1deg) scale(0.95); }
  75% { transform: rotate(1deg) scale(0.95); }
}

.dragging-tilt {
  animation: tilt 0.3s ease-in-out;
}

/* Effet de glow pendant le drag */
.dragging-active {
  position: relative;
}

.dragging-active::before {
  content: '';
  position: absolute;
  top: -2px;
  left: -2px;
  right: -2px;
  bottom: -2px;
  background: linear-gradient(45deg, 
    rgba(var(--color-primary-600), 0.3),
    rgba(var(--color-secondary-500), 0.3),
    rgba(var(--color-primary-600), 0.3)
  );
  border-radius: 1rem;
  filter: blur(10px);
  opacity: 0.5;
  z-index: -1;
  animation: glow-pulse 1.5s ease-in-out infinite;
}

@keyframes glow-pulse {
  0%, 100% { opacity: 0.3; }
  50% { opacity: 0.6; }
}

/* Transition fluide pour les cartes */
.skill-card {
  will-change: transform, opacity;
  backface-visibility: hidden;
  -webkit-backface-visibility: hidden;
  transform: translateZ(0);
  -webkit-transform: translateZ(0);
}

/* Scrollbar personnalisée */
.overflow-x-auto {
  scrollbar-width: thin;
  scrollbar-color: rgb(var(--color-primary-600) / 0.5) rgb(229 231 235);
  scroll-behavior: smooth;
}

.dark .overflow-x-auto {
  scrollbar-color: rgb(var(--color-primary-600) / 0.5) rgb(55 65 81);
}

.overflow-x-auto::-webkit-scrollbar {
  height: 8px;
}

.overflow-x-auto::-webkit-scrollbar-track {
  background: rgb(229 231 235);
  border-radius: 4px;
}

.dark .overflow-x-auto::-webkit-scrollbar-track {
  background: rgb(55 65 81);
}

.overflow-x-auto::-webkit-scrollbar-thumb {
  background: rgb(var(--color-primary-600) / 0.5);
  border-radius: 4px;
  transition: background 0.3s ease;
}

.overflow-x-auto::-webkit-scrollbar-thumb:hover {
  background: rgb(var(--color-primary-600) / 0.8);
}

/* Animation de la scrollbar pendant le drag */
.dragging-active::-webkit-scrollbar-thumb {
  background: rgb(var(--color-primary-600) / 0.9);
  box-shadow: 0 0 10px rgba(var(--color-primary-600), 0.5);
}
</style>