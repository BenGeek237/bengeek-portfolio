import './assets/main.css'

import { createApp } from 'vue'
import { createPinia } from 'pinia'

import App from './App.vue'
import router from './router'
import i18n from './i18n'

const app = createApp(App)

app.use(createPinia())
app.use(router)
app.use(i18n)

app.mount('#app')

import AOS from 'aos'
import 'aos/dist/aos.css'

AOS.init({
    duration: 800,
    easing: 'slide',
    once: true,
})
