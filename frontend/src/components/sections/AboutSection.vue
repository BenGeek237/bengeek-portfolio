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

                <!-- Certifications -->
                <div v-else-if="activeTab === 'certifications'" class="flex flex-col gap-3">
                  <a v-for="(cert, index) in certificationsList" :key="index"
                    :href="cert.file" target="_blank"
                    class="flex items-center gap-3 px-4 py-3 rounded-xl border border-gray-100 dark:border-gray-700 bg-gray-50 dark:bg-gray-800/50 text-sm text-gray-700 dark:text-gray-300 shadow-sm hover:border-emerald-500 dark:hover:border-emerald-500 transition-colors group cursor-pointer">
                    <CheckBadgeIcon class="w-5 h-5 text-emerald-500 flex-shrink-0" />
                    <span class="font-medium flex-grow">{{ cert.name }}</span>
                    <ArrowTopRightOnSquareIcon class="w-4 h-4 text-gray-400 group-hover:text-emerald-500 transition-colors" />
                  </a>
                </div>

                <!-- Loisirs -->
                <div v-else-if="activeTab === 'hobbies'" class="flex flex-wrap gap-2">
                  <span v-for="hobby in hobbies" :key="hobby.name"
                    class="flex items-center gap-2 px-3 py-1.5 rounded-full border border-gray-200 dark:border-gray-700 bg-white dark:bg-gray-900 text-sm text-gray-600 dark:text-gray-400">
                    <component :is="hobby.iconComponent" class="w-4 h-4 text-emerald-500" />
                    {{ hobby.name }}
                  </span>
                </div>
              </div>
            </Transition>
          </div>

          <!-- Section Formation (Restored) -->
          <div class="mt-8 mb-6 bg-white dark:bg-gray-800 rounded-xl p-5 border border-gray-100 dark:border-gray-700 shadow-sm flex items-start gap-4">
            <div class="flex-shrink-0 w-12 h-12 bg-emerald-100 dark:bg-emerald-900/30 rounded-full flex items-center justify-center text-emerald-600 dark:text-emerald-400">
              <AcademicCapIcon class="w-6 h-6" />
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
            <DocumentArrowDownIcon class="w-4 h-4" />
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
import { 
  AcademicCapIcon, 
  CheckBadgeIcon, 
  ArrowTopRightOnSquareIcon, 
  DocumentArrowDownIcon, 
  PuzzlePieceIcon, 
  BookOpenIcon, 
  MusicalNoteIcon, 
  TrophyIcon, 
  GlobeAltIcon, 
  CpuChipIcon 
} from '@heroicons/vue/24/outline'

const { locale } = useI18n()

const activeTab = ref('languages')

const tabs = computed(() => [
  { id: 'languages',  label: locale.value === 'fr' ? 'Langages' : 'Languages' },
  { id: 'softskills', label: 'Soft Skills' },
  { id: 'certifications', label: 'Certifications' },
  { id: 'hobbies',    label: locale.value === 'fr' ? 'Loisirs' : 'Hobbies' },
])

const introText = computed(() => locale.value === 'fr'
  ? 'Je suis <strong>Mamoudou Bia</strong>, véritable couteau suisse du numérique. Si j\'excelle en tant que développeur Fullstack, mon expertise couvre bien d\'autres domaines : <strong>Infographie</strong>, <strong>Support IT</strong>, et conception de <strong>Systèmes d\'Information (SI)</strong> complexes.'
  : 'I\'m <strong>Mamoudou Bia</strong>, a true digital Swiss Army knife. While I excel as a Fullstack developer, my expertise covers many other areas: <strong>Infography</strong>, <strong>IT Support</strong>, and designing complex <strong>Information Systems (IS)</strong>.')

const approachText = computed(() => locale.value === 'fr'
  ? 'Mon approche : être polyvalent pour résoudre tout problème informatique. Qu\'il s\'agisse de coder une application avec Django ou Vue.js, de concevoir une identité visuelle percutante, ou de gérer une infrastructure IT, j\'aborde chaque projet avec rigueur et créativité globale.'
  : 'My approach: be versatile to solve any IT problem. Whether it\'s coding an application with Django or Vue.js, designing a striking visual identity, or managing an IT infrastructure, I approach each project with global rigor and creativity.')

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

const certificationsList = computed(() => [
  { name: 'Introduction to Back-End Development', file: '/certifications/Certificat Introduction to backend.pdf' },
  { name: 'Introduction to Front-End Development', file: '/certifications/Certificat Introduction to frontend.pdf' },
  { name: 'Programming in Python (Coursera)', file: '/certifications/Coursera python VV742X8SGV4P.pdf' },
  { name: 'Django Web Framework (Coursera)', file: '/certifications/Coursera Django 00FK52IFSUVK.pdf' },
  { name: 'Version Control (Coursera)', file: '/certifications/Coursera FRCXJJNKWB70.pdf' },
  { name: 'Databases for Back-End (Coursera)', file: '/certifications/Coursera H5KWTX2W5D1M.pdf' },
  { name: 'APIs (Coursera)', file: '/certifications/Coursera LBWKCW614D4T.pdf' },
  { name: 'The Full Stack (Coursera)', file: '/certifications/Coursera LBWKCW614D4T_2.pdf' },
])

const hobbies = computed(() => locale.value === 'fr'
  ? [
      { iconComponent: PuzzlePieceIcon, name: 'Développement de jeux' },
      { iconComponent: BookOpenIcon, name: 'Lecture tech' },
      { iconComponent: MusicalNoteIcon, name: 'Musique' },
      { iconComponent: TrophyIcon, name: 'Football' },
      { iconComponent: GlobeAltIcon, name: 'Geopolitique' },
      { iconComponent: CpuChipIcon, name: 'IA & ML' },
    ]
  : [
      { iconComponent: PuzzlePieceIcon, name: 'Game dev' },
      { iconComponent: BookOpenIcon, name: 'Tech reading' },
      { iconComponent: MusicalNoteIcon, name: 'Music' },
      { iconComponent: TrophyIcon, name: 'Football' },
      { iconComponent: GlobeAltIcon, name: 'Geopolitics' },
      { iconComponent: CpuChipIcon, name: 'AI & ML' },
    ])
</script>

<style scoped>
.tab-fade-enter-active, .tab-fade-leave-active { transition: opacity 0.2s ease, transform 0.2s ease; }
.tab-fade-enter-from { opacity: 0; transform: translateY(6px); }
.tab-fade-leave-to   { opacity: 0; transform: translateY(-6px); }
</style>