import { createI18n } from 'vue-i18n'
import fr from './locales/fr.json'
import en from './locales/en.json'

// Récupérer la langue sauvegardée ou utiliser le français par défaut
const savedLocale = localStorage.getItem('locale') || 'fr'

const i18n = createI18n({
  legacy: false, // Mode Composition API
  locale: savedLocale,
  fallbackLocale: 'fr',
  messages: {
    fr,
    en
  }
})

export default i18n
