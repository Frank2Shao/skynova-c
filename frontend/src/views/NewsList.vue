<template>
    <div class="container py-5">
      <h1 class="mb-4">新闻动态</h1>
  
      <input
        v-model="query"
        class="form-control mb-3"
        placeholder="搜索新闻标题…"
      />
  
      <div class="row">
        <div
          class="col-md-4 mb-4"
          v-for="post in filtered"
          :key="post.slug"
        >
          <div class="card h-100">
            <div class="card-body">
              <h5 class="card-title">
                <RouterLink :to="`/news/${post.slug}`">
                  {{ post.title }}
                </RouterLink>
              </h5>
              <p class="card-text">{{ post.description }}</p>
            </div>
            <div class="card-footer text-muted">
              {{ formatDate(new Date(post.created_at)) }}
            </div>
          </div>
        </div>
        <div v-if="filtered.length === 0" class="col-12">
          <p class="text-center">暂无匹配的新闻。</p>
        </div>
      </div>
    </div>
  </template>
  
  <script setup>
  import { ref, computed, onMounted } from 'vue'
  import axios from 'axios'
  import { RouterLink } from 'vue-router'
  
  const posts = ref([])
  const query = ref('')
  
  onMounted(async () => {
    const res = await axios.get('/api/news/')
    posts.value = res.data.news
  })
  
  const filtered = computed(() => {
    const q = query.value.trim().toLowerCase()
    if (!q) return posts.value
    return posts.value.filter(p =>
      p.title.toLowerCase().includes(q) ||
      p.description.toLowerCase().includes(q)
    )
  })
  
  function formatDate(dt) {
    const y = dt.getFullYear()
    const m = String(dt.getMonth() + 1).padStart(2, '0')
    const d = String(dt.getDate()).padStart(2, '0')
    return `${y}-${m}-${d}`
  }
  </script>
  
  <style scoped>
  /* 页面级样式，可根据需要补充 */
  </style>
  