import { defineStore } from 'pinia'
import { ref } from 'vue'
import { useI18n } from 'vue-i18n'

export const useLanguageStore = defineStore('language', () => {
    const currentLocale = ref(localStorage.getItem('locale') || 'fr')

    const setLocale = (locale) => {
        currentLocale.value = locale
        localStorage.setItem('locale', locale)
    }

    const toggleLocale = () => {
        const newLocale = currentLocale.value === 'fr' ? 'en' : 'fr'
        setLocale(newLocale)
        return newLocale
    }

    return {
        currentLocale,
        setLocale,
        toggleLocale
    }
})
