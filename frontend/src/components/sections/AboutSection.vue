<template>
  <section id="about" class="py-8 bg-white dark:bg-gray-800">
    <div class="container mx-auto px-4 sm:px-6 lg:px-8">
      <!-- Introduction / Qui suis-je -->
      <div class="max-w-5xl mx-auto mb-16" data-aos="fade-up">
        <h2 class="section-title text-center mb-10">{{ t('about.whoAmI') }}</h2>
        
        <div class="grid grid-cols-1 md:grid-cols-3 gap-8 items-center">
          
          <!-- Colonne Gauche : Photo & Sociaux -->
          <div class="md:col-span-1 flex flex-col items-center">
            <!-- Photo de profil -->
            <div class="relative w-56 h-56 md:w-64 md:h-64 mb-6 group">
              <div class="absolute inset-0 bg-gradient-to-tr from-primary-500 to-blue-600 rounded-full blur opacity-75 group-hover:opacity-100 transition-opacity duration-300 animate-pulse"></div>
              <img 
                src="/images/profile.jpeg" 
                alt="Mamoudou Bia"
                class="relative w-full h-full object-cover rounded-full border-4 border-white dark:border-gray-900 shadow-xl z-10"
              />
              <!-- Status online -->
              <div class="absolute bottom-3 right-3 w-6 h-6 bg-green-500 border-4 border-white dark:border-gray-900 rounded-full z-20" title="Disponible pour de nouveaux projets"></div>
            </div>

            <!-- Réseaux Sociaux -->
            <div class="flex justify-center gap-4">
              <a href="https://github.com/BenGeek237/bengeek-portfolio" target="_blank" class="text-gray-400 hover:text-gray-900 dark:hover:text-white hover:scale-110 transition-all duration-300">
                <span class="sr-only">GitHub</span>
                <svg class="h-6 w-6" fill="currentColor" viewBox="0 0 24 24" aria-hidden="true">
                  <path fill-rule="evenodd" d="M12 2C6.477 2 2 6.484 2 12.017c0 4.425 2.865 8.18 6.839 9.504.5.092.682-.217.682-.483 0-.237-.008-.868-.013-1.703-2.782.605-3.369-1.343-3.369-1.343-.454-1.158-1.11-1.466-1.11-1.466-.908-.62.069-.608.069-.608 1.003.07 1.531 1.032 1.531 1.032.892 1.53 2.341 1.088 2.91.832.092-.647.35-1.088.636-1.338-2.22-.253-4.555-1.113-4.555-4.951 0-1.093.39-1.988 1.029-2.688-.103-.253-.446-1.272.098-2.65 0 0 .84-.27 2.75 1.026A9.564 9.564 0 0112 6.844c.85.004 1.705.115 2.504.337 1.909-1.296 2.747-1.027 2.747-1.027.546 1.379.202 2.398.1 2.651.64.7 1.028 1.595 1.028 2.688 0 3.848-2.339 4.695-4.566 4.943.359.309.678.92.678 1.855 0 1.338-.012 2.419-.012 2.747 0 .268.18.58.688.482A10.019 10.019 0 0022 12.017C22 6.484 17.522 2 12 2z" clip-rule="evenodd" />
                </svg>
              </a>
              <a href="https://www.linkedin.com/in/bengeek237" target="_blank" class="text-gray-400 hover:text-blue-600 hover:scale-110 transition-all duration-300">
                <span class="sr-only">LinkedIn</span>
                <svg class="h-6 w-6" fill="currentColor" viewBox="0 0 24 24" aria-hidden="true">
                  <path fill-rule="evenodd" d="M19 0h-14c-2.761 0-5 2.239-5 5v14c0 2.761 2.239 5 5 5h14c2.762 0 5-2.239 5-5v-14c0-2.761-2.239-5-5-5zm-11 19h-3v-11h3v11zm-1.5-12.268c-.966 0-1.75-.79-1.75-1.764s.784-1.764 1.75-1.764 1.75.79 1.75 1.764-.783 1.764-1.75 1.764zm13.5 12.268h-3v-5.604c0-3.368-4-3.113-4 0v5.604h-3v-11h3v1.765c1.396-2.586 7-2.777 7 2.476v6.759z" clip-rule="evenodd" />
                </svg>
              </a>
              <a href="https://wa.me/+237698340664" target="_blank" class="text-gray-400 hover:text-green-500 hover:scale-110 transition-all duration-300">
                <span class="sr-only">WhatsApp</span>
                <svg class="h-6 w-6" fill="currentColor" viewBox="0 0 24 24" aria-hidden="true">
                  <path fill-rule="evenodd" d="M12.04 2c-5.46 0-9.91 4.45-9.91 9.91 0 1.75.46 3.45 1.32 4.95L2.05 22l5.25-1.38c1.45.79 3.08 1.21 4.74 1.21 5.46 0 9.91-4.45 9.91-9.91 0-2.65-1.03-5.14-2.9-7.01C17.17 3.03 14.68 2 12.04 2zM12.05 20.21c-1.5 0-2.96-.39-4.25-1.15l-.3-.18-3.11.82.83-3.04-.2-.31a8.13 8.13 0 0113.15-5.96c1.6 1.6 2.48 3.73 2.48 5.96 0 4.52-3.69 8.2-8.22 8.2l-.38-.34zM16.48 14.5c-.24-.12-1.43-.71-1.65-.79-.22-.08-.39-.12-.55.12-.17.24-.65.82-.79.99-.15.17-.3.19-.55.07-.25-.13-1.07-.39-2.03-1.25-.75-.67-1.26-1.5-1.41-1.75-.15-.25-.02-.38.11-.51.11-.11.25-.29.37-.43.13-.15.17-.25.25-.42.08-.17.04-.32-.02-.45-.06-.13-.56-1.35-.77-1.84-.2-.48-.41-.42-.56-.43h-.48c-.17 0-.44.06-.67.31-.23.25-.88.86-.88 2.1 0 1.25.91 2.45 1.03 2.62.13.17 3.59 5.48 7.37 7.09 2.45 1.05 3.01.99 3.57.94.97-.09 1.91-.79 2.18-1.55.27-.76.27-1.41.19-1.55-.08-.13-.3-.21-.55-.34z" clip-rule="evenodd" />
                </svg>
              </a>
              <a href="/rss.xml" target="_blank" class="text-gray-400 hover:text-orange-500 hover:scale-110 transition-all duration-300">
                <span class="sr-only">RSS</span>
                <svg class="h-6 w-6" fill="currentColor" viewBox="0 0 24 24" aria-hidden="true">
                  <path d="M6.18 15.64a2.18 2.18 0 0 1 2.18 2.18C8.36 19.02 7.38 20 6.18 20C4.98 20 4 19.02 4 17.82a2.18 2.18 0 0 1 2.18-2.18M4 4.44v2.83c7.03 0 12.73 5.7 12.73 12.73h2.83c0-8.59-6.97-15.56-15.56-15.56M4 10.1v2.83c2.76 0 5 2.24 5 5h2.83c0-4.28-3.47-7.75-7.75-7.75Z"/>
                </svg>
              </a>
            </div>
          </div>

          <!-- Colonne Droite : Texte -->
          <div class="md:col-span-2 text-lg text-gray-600 dark:text-gray-300 leading-relaxed font-light text-left">
            <p class="mb-6 first-letter:text-4xl first-letter:font-bold first-letter:text-primary-600 dark:first-letter:text-primary-400 first-letter:mr-1 float-left" v-html="introText"></p>
            <p v-html="approachText"></p>
            
            <!-- Bouton Télécharger CV -->
            <div class="mt-8">
              <a 
                href="/cv/Mamoudou_Bia_CV.pdf" 
                download="Mamoudou_Bia_CV.pdf"
                class="inline-flex items-center gap-3 px-6 py-3.5 bg-gradient-to-r from-primary-600 to-purple-600 hover:from-primary-700 hover:to-purple-700 text-white font-bold rounded-xl shadow-lg hover:shadow-xl hover:shadow-primary-500/50 transition-all duration-300 hover:-translate-y-1 group"
              >
                <!-- Icône Download -->
                <svg class="w-5 h-5 group-hover:animate-bounce" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 10v6m0 0l-3-3m3 3l3-3m2 8H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" />
                </svg>
                <span>{{ locale === 'fr' ? 'Télécharger mon CV' : 'Download my CV' }}</span>
                <!-- Icône Arrow -->
                <svg class="w-4 h-4 group-hover:translate-x-1 transition-transform duration-300" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7" />
                </svg>
              </a>
            </div>
          </div>
        </div>
      </div>

      <div class="w-full h-px bg-gray-200 dark:bg-gray-700 my-12 max-w-2xl mx-auto"></div>

      <!-- Titre Formation -->
      <div class="text-center mb-10" data-aos="fade-up">
        <h3 class="text-2xl md:text-3xl font-bold text-gray-900 dark:text-white mb-2">{{ locale === 'fr' ? 'Ma Formation' : 'My Education' }}</h3>
        <p class="section-subtitle text-base">
          {{ locale === 'fr' ? 'Mon parcours académique et mes certifications' : 'My academic background and certifications' }}
        </p>
      </div>

      <!-- Formation Centrée -->
      <div class="max-w-3xl mx-auto" data-aos="fade-up">
        <div class="flex items-center mb-6">
          <div class="p-2 bg-green-100 dark:bg-green-900/30 rounded-lg mr-3">
            <AcademicCapIcon class="w-5 h-5 text-green-600 dark:text-green-400" />
          </div>
          <h3 class="text-xl font-bold text-gray-900 dark:text-white">{{ locale === 'fr' ? 'Formation' : 'Education' }}</h3>
        </div>

        <div class="relative border-l-2 border-green-200 dark:border-green-900 ml-5 space-y-6">
          <div 
            v-for="(edu, index) in education" 
            :key="index"
            class="relative pl-6 group"
          >
            <!-- Point Timeline -->
            <div class="absolute -left-[9px] top-2 w-4 h-4 rounded-full border-2 border-white dark:border-gray-800 bg-green-500 group-hover:scale-125 transition-transform duration-300"></div>
            
            <!-- Contenu -->
            <div class="bg-gray-50 dark:bg-gray-900 p-4 rounded-xl hover:shadow-md transition-all duration-300 border border-transparent hover:border-green-100 dark:hover:border-green-900">
              <span class="inline-block px-2 py-0.5 bg-green-100 dark:bg-green-900/30 text-green-700 dark:text-green-300 text-[10px] uppercase tracking-wide font-bold rounded-full mb-2">
                {{ edu.period }}
              </span>
              <h4 class="text-lg font-bold text-gray-900 dark:text-white mb-0.5">{{ edu.degree }}</h4>
              <div class="text-green-600 dark:text-green-400 text-sm font-medium mb-2">{{ edu.school }}</div>
              <p class="text-gray-600 dark:text-gray-400 text-xs leading-relaxed">
                {{ edu.description }}
              </p>
              <div v-if="edu.link" class="mt-2 pt-2 border-t border-gray-200 dark:border-gray-800">
                <a :href="edu.link" target="_blank" class="inline-flex items-center text-xs text-primary-600 hover:text-primary-700 font-medium transition-colors">
                  <LinkIcon class="w-3 h-3 mr-1" />
                  {{ locale === 'fr' ? 'Voir le certificat' : 'View certificate' }}
                </a>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
import { AcademicCapIcon, LinkIcon } from '@heroicons/vue/24/outline'
import { useI18n } from 'vue-i18n'
import { computed } from 'vue'

const { t, locale } = useI18n()

const introText = computed(() => {
  if (locale.value === 'fr') {
    return 'Salut ! Je suis <span class="text-primary-600 dark:text-primary-400 font-bold">Mamoudou Bia</span>, un véritable couteau suisse du numérique. Développeur <span class="font-semibold text-gray-900 dark:text-white">Fullstack</span>, créateur de <span class="font-semibold text-gray-900 dark:text-white">Jeux Vidéo</span> et développeur <span class="font-semibold text-gray-900 dark:text-white">Mobile</span>, je navigue avec aisance entre le code pur, la <span class="font-semibold text-gray-900 dark:text-white">Cybersécurité</span> et le <span class="font-semibold text-gray-900 dark:text-white">Design UX</span>.'
  } else {
    return 'Hi! I\'m <span class="text-primary-600 dark:text-primary-400 font-bold">Mamoudou Bia</span>, a true digital Swiss Army knife. <span class="font-semibold text-gray-900 dark:text-white">Fullstack</span> Developer, <span class="font-semibold text-gray-900 dark:text-white">Video Game</span> creator and <span class="font-semibold text-gray-900 dark:text-white">Mobile</span> developer, I navigate with ease between pure code, <span class="font-semibold text-gray-900 dark:text-white">Cybersecurity</span> and <span class="font-semibold text-gray-900 dark:text-white">UX Design</span>.'
  }
})

const approachText = computed(() => {
  if (locale.value === 'fr') {
    return 'Mon approche est simple : <span class="italic font-medium text-gray-900 dark:text-white">"Si ça peut être codé, je peux le créer."</span>. Que ce soit pour bâtir une architecture web robuste avec Django/Vue, développer des applications mobiles avec Flutter, créer des sites WordPress performants, concevoir un univers ludique sur Godot, ou sécuriser des infrastructures, j\'apporte une vision technique globale et une touche de créativité à chaque projet.'
  } else {
    return 'My approach is simple: <span class="italic font-medium text-gray-900 dark:text-white">"If it can be coded, I can create it."</span>. Whether it\'s building a robust web architecture with Django/Vue, developing mobile apps with Flutter, creating high-performance WordPress sites, designing a playful universe on Godot, or securing infrastructures, I bring a global technical vision and a touch of creativity to each project.'
  }
})


const education = computed(() => [
  {
    degree: locale.value === 'fr' ? "Certificat Django Web Framework" : "Django Web Framework Certificate",
    school: "Coursera",
    period: locale.value === 'fr' ? "Vérifié" : "Verified",
    description: locale.value === 'fr' 
      ? "Maîtrise du framework Django, ORM, authentification et déploiement."
      : "Mastery of Django framework, ORM, authentication and deployment.",
    link: "https://coursera.org/verify/00FK52IFSUVK"
  },
  {
    degree: locale.value === 'fr' ? "Certificat Python for Everybody" : "Python for Everybody Certificate",
    school: "Coursera",
    period: locale.value === 'fr' ? "Vérifié" : "Verified",
    description: locale.value === 'fr'
      ? "Programmation avancée en Python, structures de données et gestion de bases de données."
      : "Advanced Python programming, data structures and database management.",
    link: "https://coursera.org/verify/VV742X8SGV4P"
  },
  {
    degree: locale.value === 'fr' ? "Licence en Informatique" : "Bachelor's in Computer Science",
    school: locale.value === 'fr' ? "Université de Ngaoundéré" : "University of Ngaoundéré",
    period: "2021 - 2022",
    description: locale.value === 'fr'
      ? "Bases solides en algorithmique, structures de données et génie logiciel."
      : "Strong foundation in algorithms, data structures and software engineering."
  },
  {
    degree: locale.value === 'fr' ? "Baccalauréat Scientifique" : "Scientific Baccalaureate",
    school: locale.value === 'fr' ? "Lycée Classique" : "Classical High School",
    period: "2018 - 2019",
    description: locale.value === 'fr'
      ? "Option Mathématiques et Sciences Physiques. Mention Bien."
      : "Mathematics and Physical Sciences option. With Honors."
  }
])
</script>