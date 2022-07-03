// 导航的请求api

import http from '../utils/http'
import { reactive, ref } from 'vue'

const nav = reactive({
    // 头部导航列表
    header_nav_list: [],
    // 底部导航列表
    footer_nav_list: [],

    get_header_nav() {
        return http.get('/home/nav/header/')
    },

    get_footer_nav() {
        return http.get('/home/nav/footer/')
    },
})

export default nav
