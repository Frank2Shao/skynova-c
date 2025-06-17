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
                <template v-if="isAuthenticated">
                  <li><RouterLink class="dropdown-item" to="/profile">我的主页</RouterLink></li>
                  <li><hr class="dropdown-divider" /></li>
                  <li><a class="dropdown-item" href="#" @click="logout">退出登录</a></li>
                </template>
                <template v-else>
                  <li><a class="dropdown-item" href="#" @click.prevent="openLoginPopup">登录</a></li>
                  <li><a class="dropdown-item" href="#" @click.prevent="openSignupPopup">注册</a></li>
                </template>
              </ul>
            </li>
          </ul>
        </div>
      </div>
    </nav>
  </template>
  
  <script setup>
  import { ref, onMounted } from 'vue'
  import { RouterLink } from 'vue-router'
  import AuthService from '../services/auth.js'

  const isAuthenticated = ref(false)
  const currentUser = ref(null)
  const avatarUrl = ref('/static/media/default_avatar.png')

  // Check user authentication status on component mount
  onMounted(async () => {
    try {
      const status = await AuthService.getUserStatus()
      if (status.authenticated) {
        isAuthenticated.value = true
        currentUser.value = status.user
      } else {
        isAuthenticated.value = false
        currentUser.value = null
      }
    } catch (error) {
      console.error('Failed to check user status:', error)
      // If status check fails, assume not authenticated
      isAuthenticated.value = false
      currentUser.value = null
    }
  })

  const openLoginPopup = async () => {
    try {
      const user = await AuthService.openAuthPopup('login')
      isAuthenticated.value = true
      currentUser.value = user
      console.log('Login successful:', user)
    } catch (error) {
      console.error('Login failed:', error.message)
    }
  }

  const openSignupPopup = async () => {
    try {
      const user = await AuthService.openAuthPopup('signup')
      // Note: For signup, user might not be immediately authenticated
      // if email verification is required
      console.log('Signup initiated:', user)
    } catch (error) {
      console.error('Signup failed:', error.message)
    }
  }

  const logout = async () => {
    try {
      await AuthService.logout()
      isAuthenticated.value = false
      currentUser.value = null
      console.log('Logout successful')
    } catch (error) {
      console.error('Logout failed:', error)
    }
  }
  </script>
  
  <style scoped>
  .navbar-brand h1 {
    font-weight: 600;
    color: #ffffff;
  }
  </style>
  