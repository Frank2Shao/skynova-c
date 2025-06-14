<template>
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark fixed-top">
      <div class="container d-flex align-items-center">
        <RouterLink class="navbar-brand d-flex align-items-center" to="/">
          <img src="@/assets/logo1.png" class="me-4" alt="SkyNova Logo" />
          <h1 class="strong">SkyNova</h1>
        </RouterLink>
        <button
          class="navbar-toggler"
          type="button"
          data-bs-toggle="collapse"
          data-bs-target="#navMenu"
          aria-controls="navMenu"
          aria-expanded="false"
          aria-label="Toggle navigation"
        >
          <span class="navbar-toggler-icon"></span>
        </button>
  
        <div class="collapse navbar-collapse" id="navMenu">
          <ul class="navbar-nav ms-auto">
            <li class="nav-item"><RouterLink class="nav-link" to="/products">产品中心</RouterLink></li>
            <li class="nav-item"><RouterLink class="nav-link" to="/industry">行业解决方案</RouterLink></li>
            <li class="nav-item"><RouterLink class="nav-link" to="/news">新闻动态</RouterLink></li>
            <li class="nav-item"><RouterLink class="nav-link" to="/support">支持服务</RouterLink></li>
          </ul>
          <ul class="navbar-nav">
            <li class="nav-item dropdown">
              <a
                class="nav-link dropdown-toggle d-flex align-items-center"
                href="#"
                id="userDropdown"
                role="button"
                data-bs-toggle="dropdown"
                aria-expanded="false"
              >
                <img
                  v-if="isAuthenticated"
                  :src="avatarUrl"
                  class="rounded-circle"
                  height="30"
                  alt="User Avatar"
                />
                <i v-else class="bi bi-person-circle" style="font-size:1.5rem;"></i>
              </a>
              <ul class="dropdown-menu dropdown-menu-end" aria-labelledby="userDropdown">
                <li v-if="isAuthenticated"><RouterLink class="dropdown-item" to="/profile">我的主页</RouterLink></li>
                <li v-if="isAuthenticated"><hr class="dropdown-divider" /></li>
                <li v-if="isAuthenticated"><a class="dropdown-item" href="#" @click="logout">退出登录</a></li>
                <li v-else-if="!isAuthenticated"><RouterLink class="dropdown-item" to="/login">登录</RouterLink></li>
                <li v-else><RouterLink class="dropdown-item" to="/signup">注册</RouterLink></li>
              </ul>
            </li>
          </ul>
        </div>
      </div>
    </nav>
  </template>
  
  <script>
  export default {
    name: 'NavBar',
    computed: {
      isAuthenticated() {
        // TODO: 接入实际认证状态，例如 Vuex 或 Pinia
        return false
      },
      avatarUrl() {
        // TODO: 用户头像逻辑
        return '/static/media/default_avatar.png'
      }
    },
    methods: {
      logout() {
        // TODO: 调用登出 API 或清除 Token
      }
    }
  }
  </script>
  
  <style scoped>
  /* 如需局部样式，可写在这里 */
  </style>
  