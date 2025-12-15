<template>
  <div class="group">
    <div class="flex justify-between items-center mb-2">
      <span class="font-medium text-gray-900 dark:text-white group-hover:text-primary-600 transition-colors">
        {{ skill.name }}
      </span>
      <span class="text-sm text-gray-600 dark:text-gray-400">
        {{ skill.level }}%
      </span>
    </div>
    <div class="h-2 bg-gray-200 dark:bg-gray-700 rounded-full overflow-hidden">
      <div 
        class="h-full rounded-full bg-gradient-to-r transition-all duration-1000 ease-out"
        :class="skill.color"
        :style="{ width: skill.level + '%' }"
      ></div>
    </div>
  </div>
</template>

<script setup>
defineProps({
  skill: {
    type: Object,
    required: true
  }
})
</script>