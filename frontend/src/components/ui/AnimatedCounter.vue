<template>
  <div class="inline-block">
    <span class="tabular-nums">{{ displayValue }}</span>
    <span v-if="suffix">{{ suffix }}</span>
  </div>
</template>

<script setup>
import { ref, onMounted, watch } from 'vue'

const props = defineProps({
  end: {
    type: [Number, String],
    required: true
  },
  duration: {
    type: Number,
    default: 2000
  },
  suffix: {
    type: String,
    default: ''
  },
  prefix: {
    type: String,
    default: ''
  },
  decimals: {
    type: Number,
    default: 0
  },
  start: {
    type: Number,
    default: 0
  }
})

const displayValue = ref(props.prefix + props.start)
const observer = ref(null)
const hasAnimated = ref(false)

const animateValue = () => {
  if (hasAnimated.value) return
  hasAnimated.value = true

  const endValue = typeof props.end === 'string' ? parseFloat(props.end.replace(/[^0-9.]/g, '')) : props.end
  const startValue = props.start
  const duration = props.duration
  const startTime = Date.now()

  const updateValue = () => {
    const currentTime = Date.now()
    const elapsed = currentTime - startTime
    const progress = Math.min(elapsed / duration, 1)

    // Easing function (easeOutExpo)
    const easeOutExpo = progress === 1 ? 1 : 1 - Math.pow(2, -10 * progress)
    
    const currentValue = startValue + (endValue - startValue) * easeOutExpo
    
    displayValue.value = props.prefix + currentValue.toFixed(props.decimals)

    if (progress < 1) {
      requestAnimationFrame(updateValue)
    } else {
      displayValue.value = props.prefix + endValue.toFixed(props.decimals)
    }
  }

  requestAnimationFrame(updateValue)
}

onMounted(() => {
  // Intersection Observer pour démarrer l'animation quand visible
  observer.value = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          animateValue()
        }
      })
    },
    { threshold: 0.5 }
  )

  // Observer le parent
  const element = document.querySelector('.counter-trigger')
  if (element) {
    observer.value.observe(element)
  } else {
    // Si pas de trigger, animer directement
    setTimeout(animateValue, 100)
  }
})

watch(() => props.end, () => {
  hasAnimated.value = false
  animateValue()
})
</script>

<style scoped>
.tabular-nums {
  font-variant-numeric: tabular-nums;
}
</style>
