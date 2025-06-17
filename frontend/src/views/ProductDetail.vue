<template>
  <article class="container py-5">
    <h1>{{ product.title }}</h1>
    <p class="text-muted">价格: ¥{{ product.price }}</p>
    <img
      v-if="product.image"
      :src="`http://127.0.0.1:8000${product.image}`"
      class="img-fluid mb-4"
      :alt="product.title"
      style="max-height: 400px; object-fit: cover; width:100%;"
    />
    <p>{{ product.description }}</p>
    <h3 class="mt-4">产品参数</h3>
    <table class="table table-bordered">
      <tbody>
        <tr v-for="param in product.parameters" :key="param.key">
          <th>{{ param.key }}</th>
          <td>{{ param.value }}</td>
        </tr>
      </tbody>
    </table>
    <RouterLink to="/products" class="btn btn-secondary mt-4">← 返回产品列表</RouterLink>
  </article>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRoute, RouterLink } from 'vue-router'
import axios from 'axios'

const route = useRoute()
const product = ref({ title: '', price: '', description: '', image: '', parameters: [] })

onMounted(async () => {
  const sku = route.params.sku
  try {
    const res = await axios.get(`/api/products/${sku}/`)
    product.value = res.data
  } catch (err) {
    console.error('Failed to load product:', err)
  }
})
</script>

<style>
/* Ensure dark text on white background */
article.container,
article.container * {
  color: #222222 !important;
}
</style> 