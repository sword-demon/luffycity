import { createApp } from 'vue'
import App from './App.vue'
import router from './router/index'

const app = createApp(App)
// 注册全局路由对象
app.use(router)
app.mount('#app')
