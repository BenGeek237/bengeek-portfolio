<template>
  <nav
    id="mainNav"
    class="navbar"
    :class="{ 'navbar-scrolled': isScrolled }"
  >
    <div class="nav-container">
      <!-- Brand -->
      <router-link to="/" class="navbar-brand" @click="goHome">
        MAMOUDOU BIA
      </router-link>

      <!-- Desktop links -->
      <ul class="nav-links" :class="{ 'nav-open': isMobileMenuOpen }">
        <li v-for="item in navItems" :key="item.id">
          <a
            href="#"
            @click.prevent="scrollToSection(item.id)"
            class="nav-link"
            :class="{ 'nav-link-active': activeSection === item.id }"
          >
            {{ item.name }}
          </a>
        </li>
      </ul>

      <!-- Hamburger -->
      <button
        class="hamburger"
        :class="{ open: isMobileMenuOpen }"
        @click="isMobileMenuOpen = !isMobileMenuOpen"
        aria-label="Menu mobile"
      >
        <span></span>
        <span></span>
        <span></span>
      </button>
    </div>
  </nav>
</template>

<script setup>
import { ref, computed, onMounted, onUnmounted } from 'vue'
import { useRouter, useRoute } from 'vue-router'

const router = useRouter()
const route = useRoute()

const isScrolled = ref(false)
const isMobileMenuOpen = ref(false)
const activeSection = ref('hero')

const navItems = [
  { name: 'À PROPOS',  id: 'about' },
  { name: 'SERVICES',  id: 'services' },
  { name: 'PORTFOLIO', id: 'projects' },
  { name: 'FORMATION', id: 'formation' },
  { name: 'CONTACT',   id: 'contact' },
]

const handleScroll = () => {
  isScrolled.value = window.scrollY > 50
  if (route.path !== '/') return
  const sections = navItems.map(item => document.getElementById(item.id))
  const scrollY = window.scrollY + 100
  for (let i = sections.length - 1; i >= 0; i--) {
    if (sections[i] && scrollY >= sections[i].offsetTop) {
      activeSection.value = navItems[i].id
      break
    }
  }
}

const scrollToSection = (id) => {
  isMobileMenuOpen.value = false
  if (route.path !== '/') {
    router.push('/').then(() => {
      setTimeout(() => scrollToElement(id), 150)
    })
  } else {
    scrollToElement(id)
  }
}

const scrollToElement = (id) => {
  const el = document.getElementById(id)
  if (el) {
    const offset = 70
    const top = el.getBoundingClientRect().top + window.pageYOffset - offset
    window.scrollTo({ top, behavior: 'smooth' })
  }
}

const goHome = () => {
  isMobileMenuOpen.value = false
  if (route.path !== '/') router.push('/')
  else window.scrollTo({ top: 0, behavior: 'smooth' })
}

const handleKeydown = (e) => {
  if (e.key === 'Escape') isMobileMenuOpen.value = false
}

onMounted(() => {
  window.addEventListener('scroll', handleScroll, { passive: true })
  window.addEventListener('keydown', handleKeydown)
  setTimeout(handleScroll, 100)
})

onUnmounted(() => {
  window.removeEventListener('scroll', handleScroll)
  window.removeEventListener('keydown', handleKeydown)
})
</script>

<style scoped>
/* ---- Navbar base ---- */
.navbar {
  position: fixed;
  top: 0;
  width: 100%;
  z-index: 100;
  padding: 1.2rem 0;
  background: transparent;
  transition: background 0.35s ease, padding 0.35s ease, box-shadow 0.35s ease;
}

/* Après scroll : fond blanc */
.navbar-scrolled {
  background: #ffffff;
  padding: 0.6rem 0;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.08);
}

.nav-container {
  max-width: 1140px;
  margin: 0 auto;
  padding: 0 1.5rem;
  display: flex;
  align-items: center;
  justify-content: space-between;
}

/* ---- Brand ---- */
.navbar-brand {
  font-family: 'Open Sans', sans-serif;
  font-weight: 800;
  font-size: 1.1rem;
  letter-spacing: 0.05em;
  color: var(--accent);
  text-decoration: none;
  text-transform: uppercase;
  transition: color 0.2s ease;
}

.navbar-brand:hover {
  color: var(--accent-hover);
}

/* ---- Nav links ---- */
.nav-links {
  display: flex;
  align-items: center;
  gap: 0.25rem;
  list-style: none;
  margin: 0;
  padding: 0;
}

.nav-link {
  font-family: 'Open Sans', sans-serif;
  font-weight: 700;
  font-size: 0.78rem;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  text-decoration: none;
  color: rgba(255, 255, 255, 0.85);
  padding: 0.5rem 0.85rem;
  border-radius: 4px;
  transition: color 0.2s ease;
  display: block;
}

.navbar-scrolled .nav-link {
  color: #212529;
}

.nav-link:hover,
.nav-link-active {
  color: #6366f1;
}

/* ---- Hamburger ---- */
.hamburger {
  display: none;
  flex-direction: column;
  gap: 5px;
  background: transparent;
  border: none;
  cursor: pointer;
  padding: 0.25rem;
}

.hamburger span {
  display: block;
  width: 24px;
  height: 2px;
  background: rgba(255,255,255,0.85);
  border-radius: 2px;
  transition: all 0.25s ease;
}

.navbar-scrolled .hamburger span {
  background: #212529;
}

.hamburger.open span:nth-child(1) { transform: translateY(7px) rotate(45deg); }
.hamburger.open span:nth-child(2) { opacity: 0; }
.hamburger.open span:nth-child(3) { transform: translateY(-7px) rotate(-45deg); }

/* ---- Mobile ---- */
@media (max-width: 768px) {
  .hamburger {
    display: flex;
  }

  .nav-links {
    position: fixed;
    top: 0;
    right: 0;
    bottom: 0;
    width: 280px;
    background: #212529;
    flex-direction: column;
    align-items: flex-start;
    justify-content: center;
    padding: 2rem;
    gap: 0.5rem;
    transform: translateX(100%);
    transition: transform 0.3s ease;
    z-index: 200;
  }

  .nav-links.nav-open {
    transform: translateX(0);
  }

  .nav-link {
    font-size: 1rem;
    color: rgba(255,255,255,0.85) !important;
    padding: 0.75rem 0;
    width: 100%;
  }

  .nav-link:hover,
  .nav-link-active {
  color: var(--accent) !important;
  }
}
</style>