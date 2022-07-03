import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import Components from 'unplugin-vue-components/vite'
import { ElementPlusResolver } from 'unplugin-vue-components/resolvers'

// https://vitejs.dev/config/
export default defineConfig({
    plugins: [
        vue(),
        // 配置elementplus 组件按需加载
        Components({
            resolvers: [ElementPlusResolver()],
        }),
    ],
    // server: {
    //     port: '3000',
    //     host: '127.0.0.1',
    //     // 跨域代理
    //     proxy: {
    //         '/api': {
    //             // 凡是遇到 /api 路径的请求都映射到 target 属性
    //             target: 'http:127.0.0.1:8000',
    //             changeOrigin: true,
    //             ws: true, // 是否支持webscoket跨域
    //             rewrite: path => path.replace(/^\/api/, ''),
    //         },
    //     },
    // },
})
