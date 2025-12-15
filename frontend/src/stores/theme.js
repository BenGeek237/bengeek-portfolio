import { ref, computed } from 'vue'
import { defineStore } from 'pinia'

export const useThemeStore = defineStore('theme', () => {
    const darkMode = ref(true) // Mode sombre par défaut

    // Récupérer le thème depuis localStorage au démarrage
    if (typeof window !== 'undefined') {
        const savedTheme = localStorage.getItem('darkMode')
        if (savedTheme !== null) {
            darkMode.value = savedTheme === 'true'
        } else {
            // Préférer le mode sombre par défaut (style geek)
            darkMode.value = true
        }
    }

    // Appliquer le thème au document
    const applyTheme = () => {
        if (darkMode.value) {
            document.documentElement.classList.add('dark')
        } else {
            document.documentElement.classList.remove('dark')
        }
        localStorage.setItem('darkMode', darkMode.value)
    }

    // Toggle du thème
    const toggleTheme = () => {
        // Utiliser l'API View Transitions pour une animation fluide si supportée
        if (typeof document !== 'undefined' && document.startViewTransition) {
            document.startViewTransition(() => {
                darkMode.value = !darkMode.value
                applyTheme()
            })
        } else {
            // Fallback classique
            darkMode.value = !darkMode.value
            applyTheme()
        }
    }

    // Appeler applyTheme au démarrage
    if (typeof window !== 'undefined') {
        applyTheme()
    }

    return {
        darkMode: computed(() => darkMode.value),
        toggleTheme,
    }
})