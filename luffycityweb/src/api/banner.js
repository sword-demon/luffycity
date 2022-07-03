// 轮播图的请求api

import http from '../utils/http'
import { reactive, ref } from 'vue'

const banner = reactive({
    // 轮播图列表
    banner_list: [],

    get_banner() {
        return http.get('/home/banner/')
    },
})

export default banner
