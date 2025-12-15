<template>
  <div class="min-h-screen">
    <!-- Sections One-Page -->
    <HeroSection id="hero" />
    <AboutSection id="about" />
    <ProjectsSection id="projects" :limit="3" />
    <SkillsSection id="skills" />
    <BlogPreview id="blog-preview" />
    <ContactSection id="contact" />
  </div>
</template>

<script setup>
// Import des sections
import HeroSection from '@/components/sections/HeroSection.vue'
import AboutSection from '@/components/sections/AboutSection.vue'
import ProjectsSection from '@/components/sections/ProjectsSection.vue'
import SkillsSection from '@/components/sections/SkillsSection.vue'
import BlogPreview from '@/components/sections/BlogPreview.vue'
import ContactSection from '@/components/sections/ContactSection.vue'
</script>

<style scoped>
/* Smooth scrolling pour les ancres */
html {
  scroll-behavior: smooth;
}
</style>