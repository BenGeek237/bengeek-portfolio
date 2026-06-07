<template>
  <footer class="site-footer">
    <div class="footer-container">
      <!-- Social links -->
      <div class="footer-socials">
        <a
          v-for="social in socialLinks"
          :key="social.name"
          :href="social.url"
          target="_blank"
          :aria-label="social.name"
          class="footer-social-link"
        >
          <span v-html="social.icon"></span>
        </a>
      </div>

      <!-- Copyright -->
      <p class="footer-copy">
        &copy; {{ currentYear }} MAMOUDOU BIA
      </p>
    </div>
  </footer>
</template>

<script setup>
const currentYear = new Date().getFullYear()

const socialLinks = [
  {
    name: 'GitHub',
    url: 'https://github.com/BenGeek237/bengeek-portfolio',
    icon: `<svg viewBox="0 0 24 24" fill="currentColor" width="20" height="20"><path fill-rule="evenodd" d="M12 2C6.477 2 2 6.484 2 12.017c0 4.425 2.865 8.18 6.839 9.504.5.092.682-.217.682-.483 0-.237-.008-.868-.013-1.703-2.782.605-3.369-1.343-3.369-1.343-.454-1.158-1.11-1.466-1.11-1.466-.908-.62.069-.608.069-.608 1.003.07 1.531 1.032 1.531 1.032.892 1.53 2.341 1.088 2.91.832.092-.647.35-1.088.636-1.338-2.22-.253-4.555-1.113-4.555-4.951 0-1.093.39-1.988 1.029-2.688-.103-.253-.446-1.272.098-2.65 0 0 .84-.27 2.75 1.026A9.564 9.564 0 0112 6.844c.85.004 1.705.115 2.504.337 1.909-1.296 2.747-1.027 2.747-1.027.546 1.379.202 2.398.1 2.651.64.7 1.028 1.595 1.028 2.688 0 3.848-2.339 4.695-4.566 4.943.359.309.678.92.678 1.855 0 1.338-.012 2.419-.012 2.747 0 .268.18.58.688.482A10.019 10.019 0 0022 12.017C22 6.484 17.522 2 12 2z" clip-rule="evenodd"/></svg>`,
  },
  {
    name: 'LinkedIn',
    url: 'https://www.linkedin.com/in/bengeek237',
    icon: `<svg viewBox="0 0 24 24" fill="currentColor" width="20" height="20"><path d="M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433c-1.144 0-2.063-.926-2.063-2.065 0-1.138.92-2.063 2.063-2.063 1.14 0 2.064.925 2.064 2.063 0 1.139-.925 2.065-2.064 2.065zm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.222 0h.003z"/></svg>`,
  },
  {
    name: 'WhatsApp',
    url: 'https://wa.me/237698340664',
    icon: `<svg viewBox="0 0 24 24" fill="currentColor" width="20" height="20"><path fill-rule="evenodd" d="M12 2C6.48 2 2 6.48 2 12c0 1.93.53 3.74 1.45 5.31L2.1 22l4.89-1.28A9.97 9.97 0 0012 22c5.52 0 10-4.48 10-10S17.52 2 12 2zm0 18c-1.74 0-3.37-.5-4.79-1.36l-.34-.2-3.56.93.95-3.47-.22-.35A8.006 8.006 0 014 12c0-4.41 3.59-8 8-8 4.41 0 8 3.59 8 8s-3.59 8-8 8zm4.55-5.96c-.25-.13-1.48-.73-1.71-.82-.23-.08-.39-.12-.56.13-.17.25-.65.82-.79.99-.15.17-.3.19-.55.07-.25-.13-1.07-.39-2.03-1.25-.75-.67-1.26-1.5-1.41-1.75-.15-.25-.02-.38.11-.51.11-.11.25-.29.37-.43.13-.15.17-.25.25-.42.08-.17.04-.32-.02-.45-.06-.13-.56-1.35-.77-1.84-.2-.48-.41-.42-.56-.43h-.48c-.17 0-.44.06-.67.31-.23.25-.88.86-.88 2.1 0 1.25.91 2.45 1.03 2.62.13.17 3.59 5.48 7.37 7.09 2.45 1.05 3.01.99 3.57.94.97-.09 1.91-.79 2.18-1.55.27-.76.27-1.41.19-1.55-.08-.13-.3-.21-.55-.34z" clip-rule="evenodd"/></svg>`,
  },
]
</script>

<style scoped>
.site-footer {
  background-color: #212529;
  padding: 2rem 0;
}

.footer-container {
  max-width: 1140px;
  margin: 0 auto;
  padding: 0 1.5rem;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 1rem;
}

.footer-socials {
  display: flex;
  gap: 0.75rem;
}

.footer-social-link {
  width: 2.25rem;
  height: 2.25rem;
  border-radius: 50%;
  background: #343a40;
  color: #adb5bd;
  display: flex;
  align-items: center;
  justify-content: center;
  text-decoration: none;
  transition: background 0.2s ease, color 0.2s ease;
}

.footer-social-link:hover {
  background: var(--accent);
  color: #ffffff;
}

.footer-copy {
  font-family: 'Open Sans', sans-serif;
  font-size: 0.8rem;
  color: #6c757d;
  letter-spacing: 0.05em;
}
</style>