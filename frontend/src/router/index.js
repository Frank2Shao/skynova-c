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
    // Authentication popup routes
    {
      path: '/auth/login',
      name: 'auth-login',
      component: () => import('../views/AuthLogin.vue'),
    },
    {
      path: '/auth/signup',
      name: 'auth-signup',
      component: () => import('../views/AuthSignup.vue'),
    },
    {
      path: '/industry',
      name: 'industry-solution-list',
      component: () => import('../views/IndustrySolutionList.vue'),
    },
    {
      path: '/news',
      name: 'news-list',
      component: () => import('../views/NewsList.vue'),
    },
    {
      path: '/news/:slug',
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
      path: '/products/:sku',
      name: 'product-detail',
      component: () => import('../views/ProductDetail.vue'),
    },
    {
      path: '/support',
      name: 'support',
      component: () => import('../views/Support.vue'),
    },
    {
      path: '/solutions/:id',
      name: 'solution-detail',
      component: () => import('../views/SolutionDetail.vue'),
    },
  ],
})

export default router
