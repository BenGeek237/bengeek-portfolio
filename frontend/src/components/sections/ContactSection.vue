<template>
  <section id="contact" class="section-light section-padded">
    <div class="contact-container">
      <!-- Header -->
      <div data-aos="fade-up">
        <h2 class="section-heading">Contact</h2>
        <div class="section-divider"></div>
        <p class="contact-subtitle">
          {{ locale === 'fr' ? 'N\'hésitez pas à me contacter.' : 'Feel free to get in touch.' }}
        </p>
      </div>

      <!-- Form -->
      <form @submit.prevent="submitForm" class="contact-form" data-aos="fade-up" data-aos-delay="100">
        <div class="form-row">
          <!-- Left col -->
          <div class="form-col">
            <label for="contact-name" class="contact-label">
              <span class="contact-label-icon">
                <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" fill="currentColor" viewBox="0 0 24 24">
                  <path d="M12 12a5 5 0 100-10 5 5 0 000 10zm0 2c-5.33 0-8 2.67-8 4v1h16v-1c0-1.33-2.67-4-8-4z"/>
                </svg>
              </span>
              {{ locale === 'fr' ? 'Nom et prénom' : 'Full name' }} *
            </label>
            <input
              id="contact-name"
              type="text"
              v-model="form.name"
              required
              class="contact-input"
              :placeholder="locale === 'fr' ? 'Nom et Prénom *' : 'Full Name *'"
            />

            <label for="contact-email" class="contact-label" style="margin-top: 1.5rem;">
              <span class="contact-label-icon">
                <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" fill="currentColor" viewBox="0 0 24 24">
                  <path d="M20 4H4a2 2 0 00-2 2v12a2 2 0 002 2h16a2 2 0 002-2V6a2 2 0 00-2-2zm0 4l-8 5-8-5V6l8 5 8-5v2z"/>
                </svg>
              </span>
              Email *
            </label>
            <input
              id="contact-email"
              type="email"
              v-model="form.email"
              required
              class="contact-input"
              :placeholder="locale === 'fr' ? 'Saisissez votre email *' : 'Enter your email *'"
            />

            <!-- Divider under left col -->
            <div style="height: 3px; background: linear-gradient(90deg, #6366f1, #818cf8); width: 3.5rem; margin-top: 1.25rem; border-radius: 2px;"></div>
          </div>

          <!-- Right col -->
          <div class="form-col">
            <label for="contact-message" class="contact-label">
              <span class="contact-label-icon">
                <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" fill="currentColor" viewBox="0 0 24 24">
                  <path d="M20 2H4a2 2 0 00-2 2v18l4-4h14a2 2 0 002-2V4a2 2 0 00-2-2z"/>
                </svg>
              </span>
              Message *
            </label>
            <textarea
              id="contact-message"
              v-model="form.message"
              required
              rows="8"
              class="contact-input"
              style="resize: vertical; min-height: 200px;"
              :placeholder="locale === 'fr' ? 'Saisissez votre message *' : 'Enter your message *'"
            ></textarea>
          </div>
        </div>

        <!-- Status message -->
        <div v-if="status.message" :class="['status-msg', status.type === 'success' ? 'status-success' : 'status-error']">
          {{ status.message }}
        </div>

        <!-- Submit button -->
        <div class="form-submit">
          <button
            type="submit"
            :disabled="loading"
            class="btn-accent"
            :class="{ 'btn-loading': loading }"
          >
            <span v-if="loading">
              <span class="btn-spinner"></span>
              {{ locale === 'fr' ? 'Envoi...' : 'Sending...' }}
            </span>
            <span v-else>ENVOYER</span>
          </button>
        </div>
      </form>
    </div>
  </section>
</template>

<script setup>
import { ref, reactive } from 'vue'
import { useI18n } from 'vue-i18n'
import emailjs from '@emailjs/browser'

const { locale } = useI18n()

const form = reactive({ name: '', email: '', message: '' })
const loading = ref(false)
const status = reactive({ type: '', message: '' })

const submitForm = async () => {
  loading.value = true
  status.message = ''

  const serviceID  = import.meta.env.VITE_EMAILJS_SERVICE_ID
  const templateID = import.meta.env.VITE_EMAILJS_TEMPLATE_ID
  const publicKey  = import.meta.env.VITE_EMAILJS_PUBLIC_KEY

  const templateParams = {
    from_name:  form.name,
    from_email: form.email,
    subject:    `Message de ${form.name}`,
    message:    form.message,
    to_name:    'Mamoudou Bia',
  }

  try {
    if (!serviceID || !templateID || !publicKey) {
      throw new Error('Configuration EmailJS manquante.')
    }
    await emailjs.send(serviceID, templateID, templateParams, publicKey)
    status.type = 'success'
    status.message = locale.value === 'fr'
      ? 'Message envoyé avec succès ! Je vous répondrai rapidement.'
      : 'Message sent successfully! I will reply shortly.'
    form.name = ''
    form.email = ''
    form.message = ''
  } catch (err) {
    status.type = 'error'
    status.message = locale.value === 'fr'
      ? 'Erreur lors de l\'envoi. Vérifiez la configuration ou réessayez.'
      : 'Error sending message. Check configuration or try again.'
  } finally {
    loading.value = false
    setTimeout(() => { status.message = '' }, 6000)
  }
}
</script>

<style scoped>
.contact-container {
  max-width: 960px;
  margin: 0 auto;
  padding: 0 1.5rem;
  text-align: center;
}

.contact-subtitle {
  font-family: 'Merriweather', serif;
  font-size: 0.95rem;
  color: #6c757d;
  margin-bottom: 2.5rem;
}

/* Form layout */
.contact-form {
  text-align: left;
}

.form-row {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 2rem;
  margin-bottom: 1.5rem;
}

@media (max-width: 640px) {
  .form-row {
    grid-template-columns: 1fr;
  }
}

.form-col {
  display: flex;
  flex-direction: column;
}

/* Label */
.contact-label {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  font-family: 'Open Sans', sans-serif;
  font-weight: 600;
  font-size: 0.9rem;
  color: #212529;
  margin-bottom: 0.5rem;
}

.contact-label-icon {
  width: 2rem;
  height: 2rem;
  border-radius: 50%;
  background: linear-gradient(135deg, var(--accent), var(--accent-hover));
  color: #fff;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
}

/* Input */
.contact-input {
  width: 100%;
  padding: 0.75rem 1rem;
  border: 1px solid #dee2e6;
  border-radius: 4px;
  font-family: 'Merriweather', serif;
  font-size: 0.88rem;
  color: #212529;
  background: #fff;
  transition: border-color 0.2s ease, box-shadow 0.2s ease;
  outline: none;
}

.contact-input:focus {
  border-color: var(--accent);
  box-shadow: 0 0 0 3px rgba(99, 102, 241, 0.15);
}

/* Status */
.status-msg {
  padding: 0.875rem 1.25rem;
  border-radius: 6px;
  font-family: 'Open Sans', sans-serif;
  font-size: 0.88rem;
  font-weight: 600;
  margin-bottom: 1rem;
  text-align: center;
}

.status-success {
  background: #d4edda;
  color: #155724;
  border: 1px solid #c3e6cb;
}

.status-error {
  background: #f8d7da;
  color: #721c24;
  border: 1px solid #f5c6cb;
}

/* Submit */
.form-submit {
  display: flex;
  justify-content: flex-end;
}

/* Spinner */
.btn-loading {
  opacity: 0.75;
  cursor: not-allowed;
}

.btn-spinner {
  display: inline-block;
  width: 14px;
  height: 14px;
  border: 2px solid rgba(255,255,255,0.5);
  border-top-color: #fff;
  border-radius: 50%;
  animation: spin 0.7s linear infinite;
  margin-right: 6px;
  vertical-align: middle;
}

@keyframes spin {
  to { transform: rotate(360deg); }
}
</style>