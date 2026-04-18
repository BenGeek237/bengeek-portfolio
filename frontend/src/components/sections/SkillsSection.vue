<template>
  <section id="skills" class="py-24 bg-white dark:bg-gray-950 section-diagonal-top section-diagonal-bottom">
    <div class="container mx-auto px-6 sm:px-8">

      <!-- Titre stylisé -->
      <h2 class="section-styled-title" data-aos="fade-up">
        -{{ locale === 'fr' ? 'Compétences' : 'Skills' }}-
      </h2>

      <!-- Onglets -->
      <div class="mt-12" data-aos="fade-up" data-aos-delay="100">
        <div class="grid grid-cols-2 sm:grid-cols-4 gap-3 mb-10">
          <button
            v-for="cat in categories"
            :key="cat.id"
            @click="activeCategory = cat.id"
            class="py-3 px-4 rounded-xl text-sm font-semibold transition-all duration-200 border"
            :class="activeCategory === cat.id
              ? 'bg-gray-900 dark:bg-white text-white dark:text-gray-900 border-gray-900 dark:border-white shadow-md'
              : 'bg-gray-50 dark:bg-gray-900 text-gray-500 dark:text-gray-400 border-gray-200 dark:border-gray-800 hover:border-gray-400 dark:hover:border-gray-600'"
          >
            <span class="mr-2">{{ cat.emoji }}</span>{{ cat.label }}
          </button>
        </div>

        <!-- Grille des skills -->
        <Transition name="skills-fade" mode="out-in">
          <div :key="activeCategory" class="grid grid-cols-3 sm:grid-cols-4 md:grid-cols-5 lg:grid-cols-6 gap-4">
            <div
              v-for="(skill, i) in currentSkills"
              :key="skill.name"
              class="flex flex-col items-center gap-2.5 py-5 px-3 rounded-xl border border-gray-100 dark:border-gray-800 bg-gray-50 dark:bg-gray-900 hover:border-gray-300 dark:hover:border-gray-600 hover:bg-white dark:hover:bg-gray-800 hover:-translate-y-1 transition-all duration-200 cursor-default group"
              data-aos="fade-up"
              :data-aos-delay="i * 40"
            >
              <!-- Icône -->
              <div class="text-3xl leading-none group-hover:scale-110 transition-transform duration-200">
                <i v-if="typeof skill.icon === 'string'" :class="skill.icon"></i>
                <span v-else>{{ skill.emoji }}</span>
              </div>
              <!-- Nom -->
              <span class="text-[11px] font-medium text-gray-600 dark:text-gray-400 text-center leading-tight">
                {{ skill.name }}
              </span>
            </div>
          </div>
        </Transition>
      </div>

    </div>
  </section>
</template>

<script setup>
import { ref, computed } from 'vue'
import { useI18n } from 'vue-i18n'

const { locale } = useI18n()
const activeCategory = ref('web')

const categories = computed(() => [
  { id: 'web',     label: 'Web',        emoji: '🌐' },
  { id: 'mobile',  label: 'Mobile',     emoji: '📱' },
  { id: 'backend', label: 'Backend',    emoji: '⚙️' },
  { id: 'autres',  label: locale.value === 'fr' ? 'Autres' : 'Others', emoji: '🛠️' },
])

const skillsByCategory = {
  web: [
    { name: 'Vue.js',        icon: 'devicon-vuejs-plain colored' },
    { name: 'React',         icon: 'devicon-react-original colored' },
    { name: 'HTML5',         icon: 'devicon-html5-plain colored' },
    { name: 'CSS3',          icon: 'devicon-css3-plain colored' },
    { name: 'Tailwind CSS',  icon: 'devicon-tailwindcss-original colored' },
    { name: 'WordPress',     icon: 'devicon-wordpress-plain colored' },
    { name: 'JavaScript',    icon: 'devicon-javascript-plain colored' },
    { name: 'Figma',         icon: 'devicon-figma-plain colored' },
  ],
  mobile: [
    { name: 'Flutter',       icon: 'devicon-flutter-plain colored' },
    { name: 'Dart',          icon: 'devicon-dart-plain colored' },
    { name: 'Godot Engine',  icon: 'devicon-godot-plain colored' },
    { name: 'Pygame',        icon: 'devicon-python-plain colored' },
    { name: 'Android',       icon: 'devicon-android-plain colored' },
  ],
  backend: [
    { name: 'Django',        icon: 'devicon-django-plain colored' },
    { name: 'Python',        icon: 'devicon-python-plain colored' },
    { name: 'PostgreSQL',    icon: 'devicon-postgresql-plain colored' },
    { name: 'SQLite',        icon: 'devicon-sqldeveloper-plain colored' },
    { name: 'REST API',      emoji: '🔌', icon: false },
    { name: 'Git',           icon: 'devicon-git-plain colored' },
    { name: 'Docker',        icon: 'devicon-docker-plain colored' },
    { name: 'Linux',         icon: 'devicon-linux-plain colored' },
  ],
  autres: [
    { name: 'VS Code',       icon: 'devicon-vscode-plain colored' },
    { name: 'Photoshop',     icon: 'devicon-photoshop-plain colored' },
    { name: 'Illustrator',   icon: 'devicon-illustrator-plain colored' },
    { name: 'Canva',         icon: 'devicon-canva-original colored' },
    { name: 'UX/UI Design',  emoji: '🎨', icon: false },
    { name: 'IT Support',    emoji: '🔧', icon: false },
    { name: 'Réseaux',       emoji: '📡', icon: false },
    { name: 'Sys. Info (SI)',emoji: '🗄️', icon: false },
    { name: 'Cybersécurité', emoji: '🔒', icon: false },
  ],
}

const currentSkills = computed(() => skillsByCategory[activeCategory.value] || [])
</script>

<style scoped>
.skills-fade-enter-active, .skills-fade-leave-active { transition: opacity 0.25s ease, transform 0.25s ease; }
.skills-fade-enter-from { opacity: 0; transform: translateY(8px); }
.skills-fade-leave-to   { opacity: 0; transform: translateY(-4px); }
</style>