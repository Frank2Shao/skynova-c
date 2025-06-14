<script setup>
import { RouterView } from 'vue-router'
import NavBar from '@/components/NavBar.vue'
</script>

<template>
  <div>
    <!-- 全局导航栏 -->
    <NavBar />

    <!-- 主体内容，padding-top 用来抵消固定导航高度 -->
    <div class="container-fluid p-0" style="padding-top:56px;">
      <RouterView />
    </div>
  </div>
</template>

<style>
/* 这里写全局样式，若没特殊需求可留空 */
</style>
