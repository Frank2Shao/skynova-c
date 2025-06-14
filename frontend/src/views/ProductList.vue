<template>
    <div class="row">
      <!-- 左侧分类栏 -->
      <aside class="col-md-2">
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
                :src="prod.img"
                class="card-img-top"
                :alt="prod.name"
                style="height: 200px; object-fit: cover;"
              />
              <div class="card-body">
                <h5 class="card-title" style="color: var(--heading-color)">
                  {{ prod.name }}
                </h5>
                <p class="card-text" style="color: var(--text-color)">
                  {{ prod.desc }}
                </p>
                <router-link
                  to="#"
                  class="btn"
                  :style="{
                    backgroundColor: 'var(--btn-bg)',
                    color: 'var(--btn-color)'
                  }"
                >
                  查看详情
                </router-link>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script setup>
  import { ref } from 'vue'

  const products = ref([
    { 
      id: 1, 
      name: 'AgriFly 100', 
      desc: '农业植保专家', 
      img: 'https://via.placeholder.com/300x200/1e90ff/ffffff?text=AgriFly+100'
    },
    { 
      id: 2, 
      name: 'InspectEye X', 
      desc: '巡检全覆盖', 
      img: 'https://via.placeholder.com/300x200/1e90ff/ffffff?text=InspectEye+X'
    },
    { 
      id: 3, 
      name: 'SkyShot Pro', 
      desc: '高清航拍', 
      img: 'https://via.placeholder.com/300x200/1e90ff/ffffff?text=SkyShot+Pro'
    }
  ])
  </script>
  
  <style scoped>
  /* 需要时可在此添加局部样式 */
  </style>
  