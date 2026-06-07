<template>
  <canvas
    ref="canvasRef"
    class="particles-canvas"
    :style="{ opacity: opacity }"
  ></canvas>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue'

const props = defineProps({
  opacity: { type: Number, default: 1 },
  color: { type: String, default: '#ffffff' },
  particleCount: { type: Number, default: 80 },
})

const canvasRef = ref(null)
let animationId = null
let particles = []

const getCanvas = () => canvasRef.value
const getCtx = () => canvasRef.value?.getContext('2d')

function resize() {
  const canvas = getCanvas()
  if (!canvas) return
  canvas.width = canvas.offsetWidth
  canvas.height = canvas.offsetHeight
}

function createParticles() {
  const canvas = getCanvas()
  if (!canvas) return
  particles = []
  for (let i = 0; i < props.particleCount; i++) {
    particles.push({
      x: Math.random() * canvas.width,
      y: Math.random() * canvas.height,
      vx: (Math.random() - 0.5) * 0.5,
      vy: (Math.random() - 0.5) * 0.5,
      radius: Math.random() * 2 + 1,
    })
  }
}

function draw() {
  const canvas = getCanvas()
  const ctx = getCtx()
  if (!canvas || !ctx) return

  ctx.clearRect(0, 0, canvas.width, canvas.height)

  // Move particles
  for (const p of particles) {
    p.x += p.vx
    p.y += p.vy
    if (p.x < 0 || p.x > canvas.width) p.vx *= -1
    if (p.y < 0 || p.y > canvas.height) p.vy *= -1
  }

  // Draw connections
  for (let i = 0; i < particles.length; i++) {
    for (let j = i + 1; j < particles.length; j++) {
      const dx = particles[i].x - particles[j].x
      const dy = particles[i].y - particles[j].y
      const dist = Math.sqrt(dx * dx + dy * dy)
      const maxDist = 130
      if (dist < maxDist) {
        ctx.beginPath()
        ctx.strokeStyle = props.color
        ctx.globalAlpha = (1 - dist / maxDist) * 0.35
        ctx.lineWidth = 0.8
        ctx.moveTo(particles[i].x, particles[i].y)
        ctx.lineTo(particles[j].x, particles[j].y)
        ctx.stroke()
      }
    }
  }

  // Draw dots
  for (const p of particles) {
    ctx.beginPath()
    ctx.globalAlpha = 0.7
    ctx.fillStyle = props.color
    ctx.arc(p.x, p.y, p.radius, 0, Math.PI * 2)
    ctx.fill()
  }

  ctx.globalAlpha = 1
  animationId = requestAnimationFrame(draw)
}

onMounted(() => {
  resize()
  createParticles()
  draw()
  window.addEventListener('resize', () => {
    resize()
    createParticles()
  })
})

onUnmounted(() => {
  if (animationId) cancelAnimationFrame(animationId)
  window.removeEventListener('resize', resize)
})
</script>

<style scoped>
.particles-canvas {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  pointer-events: none;
  z-index: 0;
}
</style>
