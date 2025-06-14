import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView,
    },
    {
      path: '/login',
      name: 'login',
      component: () => import('../views/Login.vue'),
    },
    {
      path: '/signup',
      name: 'signup',
      component: () => import('../views/Signup.vue'),
    },
    {
      path: '/industry',
      name: 'industry',
      component: () => import('../views/Industry.vue'),
    },
    {
      path: '/news',
      name: 'news-list',
      component: () => import('../views/NewsList.vue'),
    },
    {
      path: '/news/:id',
      name: 'news-detail',
      component: () => import('../views/NewsDetail.vue'),
    },
    {
      path: '/news/compliance',
      name: 'news-compliance',
      component: () => import('../views/NewsCompliance.vue'),
    },
    {
      path: '/products',
      name: 'product-list',
      component: () => import('../views/ProductList.vue'),
    },
    {
      path: '/support',
      name: 'support',
      component: () => import('../views/Support.vue'),
    },
  ],
})

export default router
