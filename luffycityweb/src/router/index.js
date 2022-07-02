import { createRouter, createWebHistory } from 'vue-router'

// 路由列表
const routes = []

// 路由对象实例化
const router = createRouter({
    // 路由的模式 没有#
    history: createWebHistory,
    // 路由列表
    routes,
})

// 暴露路由对象
export default router
