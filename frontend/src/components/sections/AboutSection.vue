<template>
  <section id="about" class="py-24 bg-gray-50 dark:bg-gray-900 section-diagonal-bottom">
    <div class="container mx-auto px-6 sm:px-8">

      <!-- Titre stylisé -->
      <h2 class="section-styled-title" data-aos="fade-up">
        -{{ locale === 'fr' ? 'À propos' : 'About me' }}-
      </h2>

      <!-- Grid photo + texte -->
      <div class="grid grid-cols-1 md:grid-cols-5 gap-12 lg:gap-20 items-start mt-14">

        <!-- Photo avec cadres décalés -->
        <div class="md:col-span-2 flex justify-center" data-aos="fade-right">
          <div class="relative w-56 h-64 md:w-64 md:h-80 flex-shrink-0">
            <!-- Cadre décoratif 1 — derrière, décalé en bas-droite -->
            <div class="absolute inset-0 rounded-xl border-2 border-gray-300 dark:border-gray-600 translate-x-4 translate-y-4"></div>
            <!-- Cadre décoratif 2 — encore plus derrière -->
            <div class="absolute inset-0 rounded-xl border-2 border-gray-200 dark:border-gray-700 translate-x-8 translate-y-8 opacity-50"></div>
            <!-- Photo principale -->
            <div class="relative rounded-xl overflow-hidden border-2 border-white dark:border-gray-800 shadow-xl z-10">
              <img
                src="/images/profile.jpeg"
                alt="Mamoudou Bia"
                class="w-full h-full object-cover object-top"
              />
            </div>
            <!-- Badge disponibilité -->
            <div class="absolute -bottom-5 left-1/2 -translate-x-1/2 z-20 bg-white dark:bg-gray-900 border border-gray-200 dark:border-gray-700 rounded-full px-4 py-1.5 shadow-md flex items-center gap-2 whitespace-nowrap">
              <span class="relative flex h-2 w-2">
                <span class="animate-ping absolute inline-flex h-full w-full rounded-full bg-emerald-400 opacity-75"></span>
                <span class="relative inline-flex rounded-full h-2 w-2 bg-emerald-500"></span>
              </span>
              <span class="text-xs font-semibold text-gray-700 dark:text-gray-300">Open to Work</span>
            </div>
          </div>
        </div>

        <!-- Texte + Onglets -->
        <div class="md:col-span-3" data-aos="fade-left">

          <!-- Texte intro -->
          <p class="text-base md:text-lg text-gray-600 dark:text-gray-300 leading-relaxed mb-4" v-html="introText"></p>
          <p class="text-base text-gray-500 dark:text-gray-400 leading-relaxed mb-8" v-html="approachText"></p>

          <!-- Onglets : Langages / Soft Skills / Loisirs -->
          <div class="mb-4">
            <div class="flex gap-2 flex-wrap mb-5">
              <button
                v-for="tab in tabs"
                :key="tab.id"
                @click="activeTab = tab.id"
                class="px-4 py-2 text-sm rounded-full border transition-all duration-200 font-medium"
                :class="activeTab === tab.id
                  ? 'bg-gray-900 dark:bg-white text-white dark:text-gray-900 border-gray-900 dark:border-white'
                  : 'border-gray-300 dark:border-gray-700 text-gray-500 dark:text-gray-400 hover:border-gray-500 dark:hover:border-gray-500'"
              >
                {{ tab.label }}
              </button>
            </div>

            <!-- Contenu onglet -->
            <Transition name="tab-fade" mode="out-in">
              <div :key="activeTab">
                <!-- Langages -->
                <div v-if="activeTab === 'languages'" class="flex flex-wrap gap-2">
                  <span v-for="lang in languages" :key="lang.name"
                    class="flex items-center gap-2 px-3 py-1.5 rounded-full border border-gray-200 dark:border-gray-700 bg-white dark:bg-gray-900 text-sm text-gray-700 dark:text-gray-300">
                    <i :class="lang.icon + ' text-base'"></i>
                    {{ lang.name }}
                  </span>
                </div>

                <!-- Soft Skills -->
                <div v-else-if="activeTab === 'softskills'" class="flex flex-wrap gap-2">
                  <span v-for="skill in softSkills" :key="skill"
                    class="px-3 py-1.5 rounded-full border border-gray-200 dark:border-gray-700 bg-white dark:bg-gray-900 text-sm text-gray-600 dark:text-gray-400">
                    {{ skill }}
                  </span>
                </div>

                <!-- Loisirs -->
                <div v-else-if="activeTab === 'hobbies'" class="flex flex-wrap gap-2">
                  <span v-for="hobby in hobbies" :key="hobby.name"
                    class="flex items-center gap-2 px-3 py-1.5 rounded-full border border-gray-200 dark:border-gray-700 bg-white dark:bg-gray-900 text-sm text-gray-600 dark:text-gray-400">
                    <span>{{ hobby.emoji }}</span>
                    {{ hobby.name }}
                  </span>
                </div>
              </div>
            </Transition>
          </div>

          <!-- Section Formation (Restored) -->
          <div class="mt-8 mb-6 bg-white dark:bg-gray-800 rounded-xl p-5 border border-gray-100 dark:border-gray-700 shadow-sm flex items-start gap-4">
            <div class="flex-shrink-0 w-12 h-12 bg-emerald-100 dark:bg-emerald-900/30 rounded-full flex items-center justify-center text-emerald-600 dark:text-emerald-400">
              <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 14l9-5-9-5-9 5 9 5z"></path>
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 14l6.16-3.422a12.083 12.083 0 01.665 6.479A11.952 11.952 0 0012 20.055a11.952 11.952 0 00-6.824-2.998 12.078 12.078 0 01.665-6.479L12 14z"></path>
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 14v6"></path>
              </svg>
            </div>
            <div>
              <h4 class="text-sm font-bold text-gray-500 dark:text-gray-400 uppercase tracking-wider mb-1">{{ $t('about.education.title') }}</h4>
              <p class="text-lg font-bold text-gray-900 dark:text-white">{{ $t('about.education.degree') }}</p>
              <div class="flex flex-col sm:flex-row sm:items-center gap-1 sm:gap-3 text-sm text-gray-600 dark:text-gray-400 mt-1">
                <span class="font-medium">{{ $t('about.education.university') }}</span>
                <span class="hidden sm:inline">•</span>
                <span class="text-emerald-600 dark:text-emerald-400 font-semibold">{{ $t('about.education.year') }}</span>
              </div>
            </div>
          </div>

          <!-- Bouton CV -->
          <a
            href="/cv/Mamoudou_Bia_CV.pdf"
            download="Mamoudou_Bia_CV.pdf"
            class="inline-flex items-center gap-2 mt-6 px-5 py-2.5 border border-gray-900 dark:border-white text-gray-900 dark:text-white text-sm font-semibold rounded-full hover:bg-gray-900 hover:text-white dark:hover:bg-white dark:hover:text-gray-900 transition-all duration-200"
          >
            <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 10v6m0 0l-3-3m3 3l3-3m2 8H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" />
            </svg>
            {{ locale === 'fr' ? 'Télécharger mon CV' : 'Download my CV' }}
          </a>
        </div>
      </div>

    </div>
  </section>
</template>

<script setup>
import { ref, computed } from 'vue'
import { useI18n } from 'vue-i18n'

const { locale } = useI18n()

const activeTab = ref('languages')

const tabs = computed(() => [
  { id: 'languages',  label: locale.value === 'fr' ? 'Langages' : 'Languages' },
  { id: 'softskills', label: 'Soft Skills' },
  { id: 'hobbies',    label: locale.value === 'fr' ? 'Loisirs' : 'Hobbies' },
])

const introText = computed(() => locale.value === 'fr'
  ? 'Je suis <strong>Mamoudou Bia</strong>, développeur Fullstack passionné par la création d\'applications web et mobile robustes. Je maîtrise l\'ensemble de la chaîne de développement, de la conception à la mise en production.'
  : 'I\'m <strong>Mamoudou Bia</strong>, a Fullstack developer passionate about building robust web and mobile applications. I master the entire development chain, from design to deployment.')

const approachText = computed(() => locale.value === 'fr'
  ? 'Mon approche : comprendre le problème métier avant d\'écrire la première ligne de code. Que ce soit avec Django, Vue.js, Flutter ou Godot, je m\'adapte aux besoins du projet avec rigueur et créativité.'
  : 'My approach: understand the business problem before writing the first line of code. Whether with Django, Vue.js, Flutter or Godot, I adapt to project needs with rigor and creativity.')

const languages = [
  { name: 'Python',      icon: 'devicon-python-plain colored' },
  { name: 'JavaScript',  icon: 'devicon-javascript-plain colored' },
  { name: 'Dart',        icon: 'devicon-dart-plain colored' },
  { name: 'HTML/CSS',    icon: 'devicon-html5-plain colored' },
  { name: 'SQL',         icon: 'devicon-postgresql-plain colored' },
  { name: 'GDScript',    icon: 'devicon-godot-plain colored' },
]

const softSkills = computed(() => locale.value === 'fr'
  ? ['Autonomie', 'Rigueur', 'Créativité', 'Travail en équipe', 'Adaptabilité', 'Communication', 'Curiosité', 'Résolution de problèmes']
  : ['Autonomy', 'Rigor', 'Creativity', 'Teamwork', 'Adaptability', 'Communication', 'Curiosity', 'Problem solving'])

const hobbies = computed(() => locale.value === 'fr'
  ? [
      { emoji: '🎮', name: 'Développement de jeux' },
      { emoji: '📚', name: 'Lecture tech' },
      { emoji: '🎵', name: 'Musique' },
      { emoji: '⚽', name: 'Football' },
      { emoji: '🌍', name: 'Geopolitique' },
      { emoji: '🤖', name: 'IA & ML' },
    ]
  : [
      { emoji: '🎮', name: 'Game dev' },
      { emoji: '📚', name: 'Tech reading' },
      { emoji: '🎵', name: 'Music' },
      { emoji: '⚽', name: 'Football' },
      { emoji: '🌍', name: 'Geopolitics' },
      { emoji: '🤖', name: 'AI & ML' },
    ])
</script>

<style scoped>
.tab-fade-enter-active, .tab-fade-leave-active { transition: opacity 0.2s ease, transform 0.2s ease; }
.tab-fade-enter-from { opacity: 0; transform: translateY(6px); }
.tab-fade-leave-to   { opacity: 0; transform: translateY(-6px); }
</style>