import './assets/main.css'

import { createApp } from 'vue'
import { createPinia } from 'pinia'

import App from './App.vue'
import router from './router'

// 引入自定义全局样式
import './assets/css/custom.css'
import './assets/css/theme-dark.css'

// 执行全局脚本（如全局组件/插件注册）
import './plugins/app.js'

const app = createApp(App)

app.use(createPinia())
app.use(router)

app.mount('#app')
