<template>
  <div class="container py-5">
    <h1 class="mb-4">行业解决方案</h1>
    <div class="row">
      <div
        class="col-lg-4 mb-4"
        v-for="sol in solutions"
        :key="sol.id"
      >
        <div class="card h-100">
          <img
            v-if="sol.image"
            :src="`http://127.0.0.1:8000${sol.image}`"
            class="card-img-top"
            :alt="sol.title"
            style="height:200px;object-fit:cover;"
          />
          <div class="card-body d-flex flex-column gap-2">
            <h5 class="card-title">{{ sol.title }}</h5>
            <p class="card-text">{{ sol.description }}</p>
            <RouterLink
              :to="{ name: 'solution-detail', params: { id: sol.id } }"
              class="btn btn-primary mt-auto"
            >
              查看详情
            </RouterLink>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { RouterLink } from 'vue-router'
import axios from 'axios'

const solutions = ref([])

onMounted(async () => {
  try {
    const res = await axios.get('/api/solutions/')
    solutions.value = res.data.solutions
  } catch (err) {
    console.error('Failed to load solutions', err)
  }
})
</script>

<style>
.card-title {
  color: var(--heading-color, #0056b3);
}
</style> 