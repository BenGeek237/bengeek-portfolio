<template>
  <div class="flex flex-col items-center justify-center min-h-[60vh] px-4 text-center">
    <h1 class="text-6xl font-bold text-indigo-600 dark:text-indigo-400 mb-4">404</h1>
    <h2 class="text-2xl font-semibold text-gray-800 dark:text-gray-200 mb-6">Page non trouvée</h2>
    <p class="text-gray-600 dark:text-gray-400 mb-8 max-w-md">
      Désolé, la page que vous recherchez n'existe pas ou a été déplacée.
    </p>
    <router-link 
      to="/" 
      class="px-6 py-3 bg-indigo-600 hover:bg-indigo-700 text-white rounded-lg transition-colors duration-300 font-medium"
    >
      Retour à l'accueil
    </router-link>
  </div>
</template>

<script setup>
// Pas de logique spécifique nécessaire
</script>
