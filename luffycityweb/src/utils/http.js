import axios from 'axios'

const http = axios.create({
    // 设置api服务端默认地址
    baseURL: 'http://127.0.0.1:8000',
    // 请求超时时，有大文件上传需要关闭这个配置
    // timeout: 2500,
    // 是否允许客户端携带cookie
    withCredentials: false,
})

// 设置请求拦截器
http.interceptors.request.use(
    config => {
        console.log('http请求之前')
        return config
    },
    error => {
        console.log('http请求错误')
        return Promise.reject(error)
    }
)

// 响应拦截器
http.interceptors.response.use(
    response => {
        console.log('服务端响应数据成功后,返回结果给客户端的第一时间,执行then之前')
        return response
    },
    error => {
        console.log('服务端响应错误内容的时候')
        return Promise.reject(error)
    }
)

export default http
