<template>
  <div class="hero" id="hero">
    <video id="bg-video" autoplay muted loop>
      <source :src="flightVideo" type="video/mp4" />
    </video>
    <div class="hero-content">
      <h1>标语</h1>
      <div class="card-container">
        <router-link to="/products" class="card text-white bg-dark">
          <div class="card-body d-flex flex-column align-items-center gap-2">
            <h3 class="card-title">产品中心</h3>
            <p class="discription">本公司的所有产品</p>
          </div>
        </router-link>
        <router-link to="/industry" class="card text-white bg-dark">
          <div class="card-body d-flex flex-column align-items-center gap-2">
            <h3 class="card-title">行业解决方案</h3>
            <p class="discription">针对不同行业的难题，我们提供了不同的解决方案</p>
          </div>
        </router-link>
        <router-link to="/news" class="card text-white bg-dark">
          <div class="card-body d-flex flex-column align-items-center gap-2">
            <h3 class="card-title">新闻动态</h3>
            <p class="discription">看看我们的最新成果！</p>
          </div>
        </router-link>
      </div>
    </div>
  </div>
</template>

<script setup>
import { onMounted } from 'vue'
import flightVideo from '@/assets/flight.mp4'

onMounted(() => {
  setTimeout(() => {
    const video = document.getElementById('bg-video')
    const hero = document.getElementById('hero')
    video.classList.add('fade-out')
    hero.classList.add('active')
  }, 1000)
})
</script>

<style scoped>
#bg-video.fade-out {
  opacity: 0;
  transition: opacity 1s ease;
}
#hero.active {
  /* 如果主题 CSS 中已有激活样式可省略此处 */
}
</style>
