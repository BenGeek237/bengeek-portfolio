<template>
  <div>
    <HeroSection />
    <AboutSection />
    <ServicesSection />
    <ProjectsSection :limit="6" />
    <TimelineSection />
    <BlogPreview />
    <BannerCv />
    <ContactSection />
  </div>
</template>

<script setup>
import HeroSection    from '@/components/sections/HeroSection.vue'
import AboutSection   from '@/components/sections/AboutSection.vue'
import ServicesSection from '@/components/sections/ServicesSection.vue'
import ProjectsSection from '@/components/sections/ProjectsSection.vue'
import TimelineSection from '@/components/sections/TimelineSection.vue'
import BlogPreview    from '@/components/sections/BlogPreview.vue'
import BannerCv       from '@/components/sections/BannerCv.vue'
import ContactSection from '@/components/sections/ContactSection.vue'
</script>