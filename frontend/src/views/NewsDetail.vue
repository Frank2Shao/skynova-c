<template>
    <article class="container py-5">
      <h1>{{ post.title }}</h1>
      <p class="text-muted">
        {{ formatDate(new Date(post.created_at)) }}
      </p>
      <div class="mt-4" v-html="post.content"></div>
      <RouterLink to="/news" class="btn btn-secondary mt-4">
        ← 返回新闻列表
      </RouterLink>
    </article>
  </template>
  
  <script setup>
  import { ref, onMounted } from 'vue'
  import { useRoute, RouterLink } from 'vue-router'
  import axios from 'axios'
  
  const route = useRoute()
  const post = ref({ title: '', created_at: '', content: '' })
  
  onMounted(async () => {
    const slug = route.params.slug
    const res = await axios.get(`/api/news/${slug}/`)
    post.value = res.data
  })
  
  function formatDate(dt) {
    const y = dt.getFullYear()
    const m = String(dt.getMonth() + 1).padStart(2, '0')
    const d = String(dt.getDate()).padStart(2, '0')
    const hh = String(dt.getHours()).padStart(2, '0')
    const mm = String(dt.getMinutes()).padStart(2, '0')
    return `${y}-${m}-${d} ${hh}:${mm}`
  }
  </script>
  
  <style>
  /* Ensure all article content is dark to override theme */
  article.container,
  article.container * {
    color: #222222 !important;
  }
  </style>
  