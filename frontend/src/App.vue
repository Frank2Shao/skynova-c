<script setup>
import { RouterView } from 'vue-router'
import NavBar from '@/components/NavBar.vue'
import { ref } from 'vue'

const showNavBar = ref(false)
</script>

<template>
  <div>
    <!-- 全局导航栏 -->
    <NavBar v-show="showNavBar" />

    <!-- 主体内容 -->
    <div class="content-wrapper container-fluid d-flex justify-content-center">
      <RouterView @video-playing="showNavBar = true" />
    </div>
  </div>
</template>

<style>
/* Global styles */
body {
  background-color: #ffffff;
  color: #333333;
}

.content-wrapper {
  width: 80vw;
  margin: 0 auto;
}

/* Style for all pages except home */
.router-view-container {
  min-height: calc(100vh - 56px);
  background-color: #ffffff;
}

/* Ensure proper contrast for text */
h1, h2, h3, h4, h5, h6 {
  color: #222222;
}

/* Style for cards and containers */
.card {
  background-color: #ffffff;
  border: 1px solid #e0e0e0;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

/* Style for links */
a {
  color: #0066cc;
  text-decoration: none;
}

a:hover {
  color: #004499;
  text-decoration: underline;
}

/* Add white background to all views except home */
.router-view-container > *:not(.hero) {
  background-color: #ffffff;
}
</style>
