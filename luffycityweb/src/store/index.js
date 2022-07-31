import { createStore } from 'vuex'
import createPersistedState from 'vuex-persistedstate'

// 实例化一个 vuex 存储库
export default createStore({
    // 调用永久存储vuex数据的插件 localstorage 里会多一个叫vuex的key，里面就是vuex的值
    plugins: [createPersistedState()],
    // 数据存储位置
    state() {
        return {
            user: {},
        }
    },
    getters: {
        getUserInfo(state) {
            // 从jwt的载荷中提取用户信息
            let now = parseInt((new Date() - 0) / 1000) // js获取时间戳的方案 秒时间戳
            if (state.user.exp === undefined) {
                // 没登录
                state.user = {}
                localStorage.token = null
                sessionStorage.token = null
                return null
            }
            if (parseInt(state.user.exp) < now) {
                // 过期处理
                state.user = {}
                localStorage.token = null
                sessionStorage.token = null
                return null
            }

            return state.user
        },
    },
    // 操作数据的方法
    mutations: {
        login(state, payload) {
            state.user = payload
        },
    },
})
