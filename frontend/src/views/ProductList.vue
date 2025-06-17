<template>
  <div class="product-page container-fluid">
    <div class="row h-100">
      <!-- 左侧分类栏 -->
      <aside class="col-md-2 sidebar">
        <ul class="nav flex-column">
          <li class="nav-item">
            <router-link class="nav-link" to="#">农业无人机</router-link>
          </li>
          <li class="nav-item">
            <router-link class="nav-link" to="#">巡检无人机</router-link>
          </li>
          <li class="nav-item">
            <router-link class="nav-link" to="#">航拍无人机</router-link>
          </li>
        </ul>
      </aside>

      <!-- 产品卡片列表 -->
      <div class="col-md-10">
        <div class="row">
          <div
            class="col-lg-4 mb-4"
            v-for="prod in products"
            :key="prod.id"
          >
            <div class="card h-100">
              <img
                :src="prod.image ? `http://127.0.0.1:8000${prod.image}` : 'https://via.placeholder.com/300x200/1e90ff/ffffff?text=No+Image'"
                class="card-img-top"
                :alt="prod.title"
                style="height: 200px; object-fit: cover;"
              />
              <div class="card-body">
                <h5 class="card-title" style="color: var(--heading-color)">
                  {{ prod.title }}
                </h5>
                <p class="card-text" style="color: var(--text-color)">
                  {{ prod.description }}
                </p>
                <RouterLink :to="{ name: 'product-detail', params: { sku: prod.sku } }" class="btn" :style="{ backgroundColor: 'var(--btn-bg)', color: 'var(--btn-color)' }">
                  查看详情
                </RouterLink>
              </div>
            </div>
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

const products = ref([])

onMounted(async () => {
  try {
    const response = await axios.get('/api/products/')
    products.value = response.data.products
  } catch (error) {
    console.error('Error fetching products:', error)
  }
})
</script>

<style scoped>
.product-page {
  min-height: calc(100vh - 56px);
  padding: 2rem 0;
}

.sidebar {
  background-color: #2a2a2b;
  padding: 1rem;
  height: 100%;
}

.sidebar .nav-link {
  color: #dbe0e4;
  padding: 0.8rem 1rem;
  border-radius: 4px;
  transition: all 0.3s ease;
}

.sidebar .nav-link:hover {
  background-color: #e9ecef;
  color: #212529;
}

.sidebar .nav-link.active {
  background-color: #e9ecef;
  color: #212529;
  font-weight: 500;
}
</style>
  