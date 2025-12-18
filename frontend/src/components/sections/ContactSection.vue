<template>
  <section id="contact" class="py-12 bg-white dark:bg-gray-800">
    <div class="container mx-auto px-4 sm:px-6 lg:px-8">
      <div class="text-center mb-8" data-aos="fade-up">
        <h2 class="section-title">{{ locale === 'fr' ? 'Travaillons Ensemble' : 'Let\'s Work Together' }}</h2>
        <p class="section-subtitle">
          {{ locale === 'fr' ? 'Vous avez un projet en tête ? Discutons-en !' : 'Have a project in mind? Let\'s discuss it!' }}
        </p>
      </div>

      <div class="grid grid-cols-1 lg:grid-cols-2 gap-8 max-w-5xl mx-auto">
        <!-- Informations de contact -->
        <div data-aos="fade-right">
          <h3 class="text-xl font-bold text-gray-900 dark:text-white mb-6">
            {{ locale === 'fr' ? 'Mes Coordonnées' : 'My Contact Information' }}
          </h3>
          
          <div class="space-y-4">
            <div class="flex items-start">
              <div class="flex-shrink-0 w-10 h-10 bg-primary-100 dark:bg-primary-900/30 rounded-lg flex items-center justify-center mr-3">
                <EnvelopeIcon class="w-6 h-6 text-primary-600 dark:text-primary-400" />
              </div>
              <div>
                <h4 class="font-semibold text-gray-900 dark:text-white text-sm">Email</h4>
                <p 
                  @click="copyEmail" 
                  class="text-gray-600 dark:text-gray-400 text-sm cursor-pointer hover:text-primary-500 transition-colors flex items-center group"
                  title="Cliquez pour copier"
                >
                  mamoudoubiya3@gmail.com
                  <span class="ml-2 opacity-0 group-hover:opacity-100 transition-opacity text-[10px] bg-gray-200 dark:bg-gray-700 px-1.5 py-0.5 rounded text-gray-600 dark:text-gray-300">
                    {{ copyFeedback }}
                  </span>
                </p>
                <p class="text-xs text-gray-500">{{ locale === 'fr' ? 'Réponse sous 24h' : 'Response within 24h' }}</p>
              </div>
            </div>

            <div class="flex items-start">
              <div class="flex-shrink-0 w-10 h-10 bg-primary-100 dark:bg-primary-900/30 rounded-lg flex items-center justify-center mr-3">
                <MapPinIcon class="w-6 h-6 text-primary-600 dark:text-primary-400" />
              </div>
              <div>
                <h4 class="font-semibold text-gray-900 dark:text-white text-sm">{{ locale === 'fr' ? 'Localisation' : 'Location' }}</h4>
                <p class="text-gray-600 dark:text-gray-400 text-sm">Ngaoundéré, Cameroun</p>
                <p class="text-xs text-gray-500">{{ locale === 'fr' ? 'Disponible en remote' : 'Available remotely' }}</p>
              </div>
            </div>

            <div class="flex items-start">
              <div class="flex-shrink-0 w-10 h-10 bg-primary-100 dark:bg-primary-900/30 rounded-lg flex items-center justify-center mr-3">
                <ClockIcon class="w-6 h-6 text-primary-600 dark:text-primary-400" />
              </div>
              <div>
                <h4 class="font-semibold text-gray-900 dark:text-white text-sm">{{ locale === 'fr' ? 'Disponibilité' : 'Availability' }}</h4>
                <p class="text-gray-600 dark:text-gray-400 text-sm">{{ locale === 'fr' ? 'Temps plein' : 'Full time' }}</p>
                <p class="text-xs text-gray-500">Freelance & {{ locale === 'fr' ? 'CDI' : 'Permanent' }}</p>
              </div>
            </div>
          </div>
        </div>

        <!-- Formulaire de contact -->
        <div class="bg-gray-50 dark:bg-gray-900 rounded-xl p-6" data-aos="fade-left">
          <h3 class="text-xl font-bold text-gray-900 dark:text-white mb-4">
            {{ locale === 'fr' ? 'Envoyez un message' : 'Send a Message' }}
          </h3>

          <form @submit.prevent="submitForm" class="space-y-4">
            <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
              <div>
                <label for="name" class="block text-xs font-medium text-gray-700 dark:text-gray-300 mb-1">
                  {{ locale === 'fr' ? 'Votre nom *' : 'Your name *' }}
                </label>
                <input
                  type="text"
                  id="name"
                  v-model="form.name"
                  required
                  class="w-full px-3 py-2 text-sm bg-white dark:bg-gray-800 border border-gray-300 dark:border-gray-700 rounded-lg focus:ring-2 focus:ring-primary-500 focus:border-transparent transition-all"
                  placeholder="ben geek"
                />
              </div>

              <div>
                <label for="email" class="block text-xs font-medium text-gray-700 dark:text-gray-300 mb-1">
                  {{ locale === 'fr' ? 'Votre email *' : 'Your email *' }}
                </label>
                <input
                  type="email"
                  id="email"
                  v-model="form.email"
                  required
                  class="w-full px-3 py-2 text-sm bg-white dark:bg-gray-800 border border-gray-300 dark:border-gray-700 rounded-lg focus:ring-2 focus:ring-primary-500 focus:border-transparent transition-all"
                  placeholder="mamoudoubiya3@gmail.com"
                />
              </div>
            </div>

            <div>
              <label for="subject" class="block text-xs font-medium text-gray-700 dark:text-gray-300 mb-1">
                {{ locale === 'fr' ? 'Sujet *' : 'Subject *' }}
              </label>
              <input
                type="text"
                id="subject"
                v-model="form.subject"
                required
                class="w-full px-3 py-2 text-sm bg-white dark:bg-gray-800 border border-gray-300 dark:border-gray-700 rounded-lg focus:ring-2 focus:ring-primary-500 focus:border-transparent transition-all"
                :placeholder="locale === 'fr' ? 'Proposition de projet' : 'Project proposal'"
              />
            </div>

            <div>
              <label for="message" class="block text-xs font-medium text-gray-700 dark:text-gray-300 mb-1">
                {{ locale === 'fr' ? 'Votre message *' : 'Your message *' }}
              </label>
              <textarea
                id="message"
                v-model="form.message"
                required
                rows="4"
                class="w-full px-3 py-2 text-sm bg-white dark:bg-gray-800 border border-gray-300 dark:border-gray-700 rounded-lg focus:ring-2 focus:ring-primary-500 focus:border-transparent transition-all resize-none"
                :placeholder="locale === 'fr' ? 'Décrivez votre projet...' : 'Describe your project...'"
              ></textarea>
            </div>

            <!-- Status message -->
            <div v-if="status.message" :class="['p-3 rounded-lg text-sm', status.type === 'success' ? 'bg-green-100 text-green-800' : 'bg-red-100 text-red-800']">
              {{ status.message }}
            </div>

            <button
              type="submit"
              :disabled="loading"
              class="w-full btn-primary py-3 flex items-center justify-center text-sm"
              :class="{'opacity-50 cursor-not-allowed': loading}"
            >
              <span v-if="loading" class="flex items-center">
                <div class="animate-spin rounded-full h-4 w-4 border-t-2 border-b-2 border-white mr-2"></div>
                {{ locale === 'fr' ? 'Envoi...' : 'Sending...' }}
              </span>
              <span v-else>
                {{ locale === 'fr' ? 'Envoyer le message' : 'Send Message' }}
                <PaperAirplaneIcon class="w-4 h-4 ml-2 inline" />
              </span>
            </button>
          </form>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
import { ref, reactive, computed } from 'vue'
import { PaperAirplaneIcon, EnvelopeIcon, MapPinIcon, ClockIcon } from '@heroicons/vue/24/outline'
import { useI18n } from 'vue-i18n'

const { t, locale } = useI18n()

const form = reactive({
  name: '',
  email: '',
  subject: '',
  message: ''
})

const loading = ref(false)
const status = reactive({
  type: '',
  message: ''
})

const copyFeedback = computed(() => locale.value === 'fr' ? 'Copier' : 'Copy')
const copyEmail = () => {
  navigator.clipboard.writeText('mamoudoubiya3@gmail.com').then(() => {
    copyFeedback.value = 'Copié !'
    setTimeout(() => {
      copyFeedback.value = 'Copier'
    }, 2000)
  })
}

const socialLinks = [
  { 
    name: 'GitHub', 
    url: 'https://github.com/BenGeek237/bengeek-portfolio', 
    icon: '<svg viewBox="0 0 24 24" fill="currentColor" class="w-6 h-6"><path fill-rule="evenodd" d="M12 2C6.477 2 2 6.484 2 12.017c0 4.425 2.865 8.18 6.839 9.504.5.092.682-.217.682-.483 0-.237-.008-.868-.013-1.703-2.782.605-3.369-1.343-3.369-1.343-.454-1.158-1.11-1.466-1.11-1.466-.908-.62.069-.608.069-.608 1.003.07 1.531 1.032 1.531 1.032.892 1.53 2.341 1.088 2.91.832.092-.647.35-1.088.636-1.338-2.22-.253-4.555-1.113-4.555-4.951 0-1.093.39-1.988 1.029-2.688-.103-.253-.446-1.272.098-2.65 0 0 .84-.27 2.75 1.026A9.564 9.564 0 0112 6.844c.85.004 1.705.115 2.504.337 1.909-1.296 2.747-1.027 2.747-1.027.546 1.379.202 2.398.1 2.651.64.7 1.028 1.595 1.028 2.688 0 3.848-2.339 4.695-4.566 4.943.359.309.678.92.678 1.855 0 1.338-.012 2.419-.012 2.747 0 .268.18.58.688.482A10.019 10.019 0 0022 12.017C22 6.484 17.522 2 12 2z" clip-rule="evenodd" /></svg>' 
  },
  { 
    name: 'LinkedIn', 
    url: 'https://www.linkedin.com/in/bengeek237',  
    icon: '<svg viewBox="0 0 24 24" fill="currentColor" class="w-6 h-6"><path d="M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433c-1.144 0-2.063-.926-2.063-2.065 0-1.138.92-2.063 2.063-2.063 1.14 0 2.064.925 2.064 2.063 0 1.139-.925 2.065-2.064 2.065zm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.222 0h.003z"/></svg>' 
  },
  { 
    name: 'WhatsApp', 
    url: 'https://wa.me/237698340664',  
    icon: '<svg viewBox="0 0 24 24" fill="currentColor" class="w-6 h-6"><path fill-rule="evenodd" d="M12 2C6.48 2 2 6.48 2 12c0 1.93.53 3.74 1.45 5.31L2.1 22l4.89-1.28A9.97 9.97 0 0012 22c5.52 0 10-4.48 10-10S17.52 2 12 2zm0 18c-1.74 0-3.37-.5-4.79-1.36l-.34-.2-3.56.93.95-3.47-.22-.35A8.006 8.006 0 014 12c0-4.41 3.59-8 8-8 4.41 0 8 3.59 8 8s-3.59 8-8 8zm4.55-5.96c-.25-.13-1.48-.73-1.71-.82-.23-.08-.39-.12-.56.13-.17.25-.65.82-.79.99-.15.17-.3.19-.55.07-.25-.13-1.07-.39-2.03-1.25-.75-.67-1.26-1.5-1.41-1.75-.15-.25-.02-.38.11-.51.11-.11.25-.29.37-.43.13-.15.17-.25.25-.42.08-.17.04-.32-.02-.45-.06-.13-.56-1.35-.77-1.84-.2-.48-.41-.42-.56-.43h-.48c-.17 0-.44.06-.67.31-.23.25-.88.86-.88 2.1 0 1.25.91 2.45 1.03 2.62.13.17 3.59 5.48 7.37 7.09 2.45 1.05 3.01.99 3.57.94.97-.09 1.91-.79 2.18-1.55.27-.76.27-1.41.19-1.55-.08-.13-.3-.21-.55-.34z" clip-rule="evenodd" /></svg>' 
  },
]

import emailjs from '@emailjs/browser'

const submitForm = async () => {
  loading.value = true
  status.message = ''
  
  // ⚠️ CONFIGURATION EMAILJS REQUISE ⚠️
  // 1. Créez un compte sur https://www.emailjs.com/
  // 2. Créez un Service email (ex: Gmail) -> Copiez le SERVICE_ID
  // 3. Créez un Template d'email -> Copiez le TEMPLATE_ID
  // 4. Allez dans Account -> Copiez la Public Key
  // 5. Ajoutez ces valeurs dans le fichier .env
  
  const serviceID = import.meta.env.VITE_EMAILJS_SERVICE_ID
  const templateID = import.meta.env.VITE_EMAILJS_TEMPLATE_ID
  const publicKey = import.meta.env.VITE_EMAILJS_PUBLIC_KEY
  
  // Debug pour vérifier si les clés sont là
  console.log('Tentative d\'envoi avec Service ID:', serviceID ? 'OK ' + serviceID.substring(0, 4) + '...' : 'MANQUANT')
  
  const templateParams = {
    from_name: form.name,
    from_email: form.email,
    subject: form.subject,
    message: form.message,
    to_name: 'BenGeek',
  }
  
  try {
    if (!serviceID || !templateID || !publicKey) {
      throw new Error('Configuration EmailJS manquante. Vérifiez les variables d\'environnement.')
    }

    await emailjs.send(serviceID, templateID, templateParams, publicKey)
    
    status.type = 'success'
    status.message = 'Message envoyé avec succès ! Je vous répondrai dans les plus brefs délais.'
    
    // Réinitialiser le formulaire
    form.name = ''
    form.email = ''
    form.subject = ''
    form.message = ''
    
  } catch (error) {
    console.error('Erreur EmailJS:', error)
    status.type = 'error'
    // Afficher un message plus clair selon l'erreur
    status.message = serviceID 
      ? 'Erreur lors de l\'envoi. Vérifiez la console (F12) pour plus de détails.' 
      : 'Erreur de configuration : Clés EmailJS introuvables.'
  } finally {
    loading.value = false
    
    // Effacer le message après 5 secondes
    setTimeout(() => {
      status.message = ''
    }, 5000)
  }
}
</script>