<template>
  <div class="min-h-screen pt-24 pb-16">
    <div class="container mx-auto px-4 sm:px-6 lg:px-8 mb-12 text-center">
      <h1 class="text-4xl md:text-5xl font-bold text-gray-900 dark:text-white mb-4">
        Mes Projets
      </h1>
      <p class="text-xl text-gray-600 dark:text-gray-400 max-w-2xl mx-auto">
        Découvrez l'ensemble de mes réalisations, des sites vitrines aux applications web complexes.
      </p>
    </div>
    
    <!-- On réutilise la section existante qui gère déjà l'affichage et les filtres -->
    <ProjectsSection />
  </div>
</template>

<script setup>
import ProjectsSection from '@/components/sections/ProjectsSection.vue'
</script>
