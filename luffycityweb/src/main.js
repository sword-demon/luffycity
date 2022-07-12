import { createApp } from 'vue'
import App from './App.vue'
import router from './router/index'
import 'element-plus/dist/index.css'

const app = createApp(App)
// 注册全局路由对象
app.use(router)
app.mount('#app')
