<template>
  <article class="container py-5">
    <h1>{{ sol.title }}</h1>
    <p class="text-muted">价格: ¥{{ sol.price }}</p>
    <img
      v-if="sol.image"
      :src="`http://127.0.0.1:8000${sol.image}`"
      class="img-fluid mb-4"
      :alt="sol.title"
      style="max-height: 400px; object-fit: cover; width:100%;"
    />
    <p>{{ sol.description }}</p>

    <h3 class="mt-4">建议的产品</h3>
    <ul class="list-group mb-4">
      <li class="list-group-item" v-for="item in sol.suggested_products" :key="item.name">
        <strong>{{ item.name }}</strong>
        <span v-if="item.note"> - {{ item.note }}</span>
      </li>
      <li v-if="!sol.suggested_products.length" class="list-group-item">暂无建议产品。</li>
    </ul>

    <RouterLink to="/industry" class="btn btn-secondary">← 返回解决方案列表</RouterLink>
  </article>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRoute, RouterLink } from 'vue-router'
import axios from 'axios'

const route = useRoute()
const sol = ref({ title: '', price: '', description: '', image: '', suggested_products: [] })

onMounted(async () => {
  const id = route.params.id
  try {
    const res = await axios.get(`/api/solutions/${id}/`)
    sol.value = res.data
  } catch (err) {
    console.error('Failed to load solution:', err)
  }
})
</script>

<style>
article.container,
article.container * {
  color: #222222 !important;
}
</style> 