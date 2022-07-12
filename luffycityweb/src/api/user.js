// 导航的请求api

import http from '../utils/http'
import { reactive, ref } from 'vue'

const user = reactive({
    // 登录账号
    account: '',
    // 密码
    password: '',
    // 登录弹框默认显示
    login_type: 0,
    // 是否记住账号
    remember: false,
    // 手机号码
    mobile: '',
    // 验证码
    code: '',
    login() {
        // 用户登录
        return http.post('/users/login/', {
            username: this.account,
            password: this.password,
        })
    },
})

export default user
