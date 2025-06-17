<template>
  <div class="hero" id="hero">
    <video id="bg-video" autoplay muted loop>
      <source :src="flightVideo" type="video/mp4" />
    </video>
    <div class="hero-content" :class="{ 'fade-in': isContentVisible }">
      <h1>标语</h1>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import flightVideo from '@/assets/flight.mp4'

const isContentVisible = ref(false)
const emit = defineEmits(['video-playing'])

onMounted(() => {
  // Wait for video to start playing
  const video = document.getElementById('bg-video')
  video.addEventListener('playing', () => {
    // After video starts playing, wait 1 second then fade video and show content
  setTimeout(() => {
    video.classList.add('fade-out')
      isContentVisible.value = true
      emit('video-playing')
  }, 1000)
  })
})
</script>

<style scoped>
.hero {
  position: fixed;
  top: 0;
  left: 0;
  width: 100vw;
  height: 100vh;
  overflow: hidden;
  background-color: #000;
  z-index: 0;
}

#bg-video {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
  z-index: 0;
  opacity: 1;
  transition: opacity 2s ease;
}

#bg-video.fade-out {
  opacity: 0.3;
}

.hero-content {
  position: relative;
  z-index: 1;
  color: white;
  text-align: center;
  padding: 2rem;
  height: 100vh;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  opacity: 0;
  transform: translateY(20px);
  transition: opacity 1s ease, transform 1s ease;
}

.hero-content.fade-in {
  opacity: 1;
  transform: translateY(0);
}

.card-container {
  display: flex;
  gap: 2rem;
  margin-top: 2rem;
  flex-wrap: wrap;
  justify-content: center;
}

.card {
  width: 300px;
  transition: transform 0.3s ease;
  text-decoration: none;
  background-color: rgba(0, 0, 0, 0.7) !important;
}

.card:hover {
  transform: translateY(-5px);
}

.card-body {
  padding: 2rem;
}

.card-title {
  margin-bottom: 1rem;
}

.description {
  font-size: 1.1rem;
  opacity: 0.8;
}

#hero.active {
  /* 如果主题 CSS 中已有激活样式可省略此处 */
}
</style>
