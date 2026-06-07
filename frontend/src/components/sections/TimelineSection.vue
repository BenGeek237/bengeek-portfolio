<template>
  <section id="formation" class="section-light section-padded">
    <div class="timeline-container">
      <div data-aos="fade-up">
        <h2 class="section-heading">
          {{ locale === 'fr' ? 'Formation' : 'Education' }}
        </h2>
        <div class="section-divider"></div>
      </div>

      <!-- Timeline -->
      <div class="timeline">
        <div
          v-for="(item, index) in timelineItems"
          :key="index"
          class="timeline-item"
          :class="index % 2 === 0 ? 'right' : 'left'"
          data-aos="fade-up"
          :data-aos-delay="index * 100"
        >
          <!-- Texte -->
          <div class="timeline-content" :class="index % 2 === 0 ? 'text-right-side' : 'text-left-side'">
            <p class="timeline-year">{{ item.years }}</p>
            <h3 class="timeline-title">{{ item.title }}</h3>
            <p class="timeline-desc">{{ item.desc }}</p>
          </div>

          <!-- Cercle central -->
          <div class="timeline-circle-wrap">
            <div class="timeline-circle">
              <img v-if="item.image" :src="item.image" :alt="item.title" />
              <div v-else class="timeline-circle-placeholder" v-html="item.icon">
              </div>
            </div>
          </div>

          <!-- Spacer (côté opposé au texte) -->
          <div class="timeline-spacer"></div>
        </div>

        <!-- Badge de fin -->
        <div class="timeline-end-badge" data-aos="fade-up">
          <div class="timeline-badge">
            {{ locale === 'fr' ? 'Début de mon Parcours !' : 'Start of my Journey!' }}
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
import { computed } from 'vue'
import { useI18n } from 'vue-i18n'

const { locale } = useI18n()

const timelineItems = computed(() => [
  {
    years: '2022',
    title: locale.value === 'fr'
      ? 'Licence Informatique — Génie Logiciel'
      : 'Bachelor\'s Degree — Software Engineering',
    desc: locale.value === 'fr'
      ? 'Formation en développement logiciel, conception de systèmes d\'information, gestion de bases de données et architecture web.'
      : 'Training in software development, information systems design, database management and web architecture.',
    image: null,
    icon: `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" class="timeline-svg"><path d="M11.7 2.805a.75.75 0 01.6 0A60.65 60.65 0 0122.83 8.72a.75.75 0 01-.231 1.337 49.949 49.949 0 00-9.902 3.912l-.003.002c-.114.06-.227.119-.34.18a.75.75 0 01-.707 0A50.88 50.88 0 007.5 12.173v-.224c0-.131.067-.248.172-.311a54.615 54.615 0 014.653-2.52.75.75 0 00-.65-1.352 56.123 56.123 0 00-4.78 2.589 1.858 1.858 0 00-.859 1.228 49.803 49.803 0 00-4.634-1.527.75.75 0 01-.231-1.337A60.653 60.653 0 0111.7 2.805z"/><path d="M13.06 15.473a48.45 48.45 0 017.666-3.282c.134 1.414.22 2.843.255 4.284a.75.75 0 01-.46.711 47.87 47.87 0 00-8.105 4.342.75.75 0 01-.832 0 47.87 47.87 0 00-8.104-4.342.75.75 0 01-.461-.71c.035-1.442.121-2.87.255-4.286A48.4 48.4 0 016 13.18v1.27a1.5 1.5 0 00-.14 2.508c-.09.38-.222.753-.397 1.11.452.213.901.434 1.346.66a6.727 6.727 0 00.551-1.607 1.5 1.5 0 00.14-2.67v-.645a48.549 48.549 0 013.44 1.667 2.25 2.25 0 002.12 0z"/><path d="M4.462 19.462c.42-.419.753-.89 1-1.395.453.214.902.435 1.347.662a6.742 6.742 0 01-1.286 1.794.75.75 0 01-1.06-1.06z"/></svg>`,
  },
  {
    years: '2021 - 2022',
    title: locale.value === 'fr'
      ? 'Certifications Meta & Coursera'
      : 'Meta & Coursera Certifications',
    desc: locale.value === 'fr'
      ? 'Introduction au développement Back-End et Front-End (Meta), Django Web Framework, Programming in Python, APIs, Version Control (Coursera).'
      : 'Introduction to Back-End and Front-End Development (Meta), Django Web Framework, Programming in Python, APIs, Version Control (Coursera).',
    image: null,
    icon: `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" class="timeline-svg"><path fill-rule="evenodd" d="M8.603 3.799A4.49 4.49 0 0112 2.25c1.357 0 2.573.6 3.397 1.549a4.49 4.49 0 013.498 1.307 4.491 4.491 0 011.307 3.497A4.49 4.49 0 0121.75 12a4.49 4.49 0 01-1.549 3.397 4.491 4.491 0 01-1.307 3.497 4.491 4.491 0 01-3.497 1.307A4.49 4.49 0 0112 21.75a4.49 4.49 0 01-3.397-1.549 4.49 4.49 0 01-3.498-1.306 4.491 4.491 0 01-1.307-3.498A4.49 4.49 0 012.25 12c0-1.357.6-2.573 1.549-3.397a4.49 4.49 0 011.307-3.497 4.49 4.49 0 013.497-1.307zm7.007 6.387a.75.75 0 10-1.22-.872l-3.236 4.53L9.53 12.22a.75.75 0 00-1.06 1.06l2.25 2.25a.75.75 0 001.14-.094l3.75-5.25z" clip-rule="evenodd"/></svg>`,
  },
  {
    years: '2019 - 2021',
    title: locale.value === 'fr'
      ? 'Formation en Infographie & Design'
      : 'Graphic Design & Infography Training',
    desc: locale.value === 'fr'
      ? 'Maîtrise de Photoshop, Illustrator, Canva et Figma. Création d\'identités visuelles, maquettes UI/UX et supports de communication.'
      : 'Mastery of Photoshop, Illustrator, Canva and Figma. Visual identity creation, UI/UX mockups and communication materials.',
    image: null,
    icon: `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" class="timeline-svg"><path fill-rule="evenodd" d="M20.599 1.5c-.376 0-.743.111-1.055.32l-5.08 3.385a18.747 18.747 0 00-3.471 2.987 10.04 10.04 0 014.815 4.815 18.748 18.748 0 002.987-3.472l3.386-5.079A1.902 1.902 0 0020.599 1.5zm-8.3 14.025a18.76 18.76 0 001.896-1.207 8.026 8.026 0 00-4.513-4.513A18.75 18.75 0 008.475 11.7l-.278.5a5.26 5.26 0 013.601 3.602l.5-.277z" clip-rule="evenodd"/><path fill-rule="evenodd" d="M10.832 20.019a.75.75 0 01-1.04-.265l-2.182-3.82a.75.75 0 01.265-1.04c.182-.104.385-.184.606-.234A6.767 6.767 0 0112 14.25c.186 0 .368.016.545.048.223.04.428.121.61.226a.75.75 0 01.265 1.04l-2.182 3.82a.75.75 0 01-1.04.265l-.366-.21zm-2.905-2.091l1.884 3.298a2.25 2.25 0 003.882-.001l1.884-3.297a8.272 8.272 0 00-1.89-1.002 8.274 8.274 0 00-1.886 1.002z" clip-rule="evenodd"/></svg>`,
  },
  {
    years: '2019',
    title: locale.value === 'fr'
      ? 'BAC TI'
      : 'High School Diploma in IT',
    desc: locale.value === 'fr'
      ? 'Lycée classique et moderne de Ngaoundéré.'
      : 'Lycée classique et moderne de Ngaoundéré.',
    image: null,
    icon: `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" class="timeline-svg"><path d="M12 3L1 9l4 2.18v6L12 21l7-3.82v-6l2-1.09V17h2V9L12 3zm6.82 6L12 12.72 5.18 9 12 5.28 18.82 9zM17 15.99l-5 2.73-5-2.73v-3.72l5 2.73 5-2.73v3.72z"/></svg>`,
  },
  {
    years: locale.value === 'fr' ? 'Autodidacte' : 'Self-taught',
    title: locale.value === 'fr'
      ? 'Passion pour le Développement & la Tech'
      : 'Passion for Development & Tech',
    desc: locale.value === 'fr'
      ? 'Apprentissage par la pratique : développement de jeux avec Godot et Pygame, exploration de l\'IA, cybersécurité et administration Linux.'
      : 'Learning by doing: game development with Godot and Pygame, AI exploration, cybersecurity and Linux administration.',
    image: null,
    icon: `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" class="timeline-svg"><path fill-rule="evenodd" d="M12.963 2.286a.75.75 0 00-1.071-.136 9.742 9.742 0 00-3.539 6.177A7.547 7.547 0 016.648 6.61a.75.75 0 00-1.152-.082A9 9 0 1015.68 4.534a7.46 7.46 0 01-2.717-2.248zM15.75 14.25a3.75 3.75 0 11-7.313-1.172c.628.465 1.35.81 2.133 1a5.99 5.99 0 011.925-3.545 3.75 3.75 0 013.255 3.717z" clip-rule="evenodd"/></svg>`,
  },
])
</script>

<style scoped>
.timeline-container {
  max-width: 900px;
  margin: 0 auto;
  padding: 0 1.5rem;
  text-align: center;
}

/* Timeline */
.timeline {
  position: relative;
  padding: 2rem 0 0;
}

.timeline::before {
  content: '';
  position: absolute;
  left: 50%;
  top: 0;
  bottom: 0;
  width: 2px;
  background: #dee2e6;
  transform: translateX(-50%);
}

/* Each item */
.timeline-item {
  display: grid;
  grid-template-columns: 1fr auto 1fr;
  align-items: center;
  gap: 2rem;
  margin-bottom: 3rem;
  position: relative;
}

/* When index is even: text on right, spacer on left */
.timeline-item.right .text-right-side { order: 3; text-align: left; }
.timeline-item.right .timeline-circle-wrap { order: 2; }
.timeline-item.right .timeline-spacer { order: 1; }

/* When index is odd: text on left, spacer on right */
.timeline-item.left .text-left-side { order: 1; text-align: right; }
.timeline-item.left .timeline-circle-wrap { order: 2; }
.timeline-item.left .timeline-spacer { order: 3; }

.timeline-content {
  flex: 1;
}

.timeline-spacer {
  flex: 1;
}

.timeline-year {
  font-family: 'Open Sans', sans-serif;
  font-weight: 800;
  font-size: 1rem;
  color: #212529;
  margin-bottom: 0.2rem;
}

.timeline-title {
  font-family: 'Open Sans', sans-serif;
  font-weight: 700;
  font-size: 1.2rem;
  color: #212529;
  line-height: 1.3;
  margin-bottom: 0.5rem;
}

.timeline-desc {
  font-family: 'Merriweather', serif;
  font-size: 0.82rem;
  color: #6c757d;
  line-height: 1.7;
}

/* Circle */
.timeline-circle-wrap {
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 1;
}

.timeline-circle {
  width: 130px;
  height: 130px;
  border-radius: 50%;
  border: 4px solid #dee2e6;
  overflow: hidden;
  background: #f8f9fa;
  flex-shrink: 0;
}

.timeline-circle img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.timeline-circle-placeholder {
  width: 100%;
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 2.5rem;
  font-weight: 800;
  font-family: 'Open Sans', sans-serif;
  background: linear-gradient(135deg, #eef2ff, #e0e7ff);
}

:deep(.timeline-svg) {
  width: 3.5rem;
  height: 3.5rem;
  color: var(--accent);
}

/* End badge */
.timeline-end-badge {
  display: flex;
  justify-content: center;
  padding-top: 1rem;
  position: relative;
  z-index: 1;
}

.timeline-badge {
  width: 130px;
  height: 130px;
  border-radius: 50%;
  background: linear-gradient(135deg, #f0ad4e, #e8962d);
  display: flex;
  align-items: center;
  justify-content: center;
  text-align: center;
  padding: 1rem;
  font-family: 'Open Sans', sans-serif;
  font-weight: 700;
  font-size: 0.75rem;
  color: #fff;
  line-height: 1.3;
  border: 4px solid #dee2e6;
  box-shadow: 0 4px 15px rgba(240, 173, 78, 0.3);
}

/* Mobile */
@media (max-width: 640px) {
  .timeline::before { left: 2rem; }

  .timeline-item,
  .timeline-item.right,
  .timeline-item.left {
    grid-template-columns: auto 1fr;
    gap: 1.25rem;
  }

  .timeline-item.right .text-right-side,
  .timeline-item.left .text-left-side {
    order: 2 !important;
    text-align: left !important;
  }

  .timeline-item.right .timeline-circle-wrap,
  .timeline-item.left .timeline-circle-wrap {
    order: 1 !important;
  }

  .timeline-spacer { display: none; }

  .timeline-circle {
    width: 80px;
    height: 80px;
  }

  .timeline-end-badge {
    justify-content: flex-start;
    padding-left: 0.5rem;
  }
}
</style>
