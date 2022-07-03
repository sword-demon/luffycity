<template>
    <div class="footer">
        <ul>
            <li v-for="navItem in nav.footer_nav_list" :key="navItem.id">
                <!-- 区分外网链接 -->
                <a :href="navItem.link" v-if="navItem.is_http">{{
                    navItem.name
                }}</a>
                <router-link v-else :to="navItem.link">{{
                    navItem.name
                }}</router-link>
            </li>
        </ul>
        <p>Copyright © 版权所有</p>
    </div>
</template>

<script setup>
import nav from "../api/nav";

// 获取底部导航列表
nav.get_footer_nav().then((res) => {
    nav.footer_nav_list = res.data;
});
</script>

<style scoped>
.footer {
    width: 100%;
    height: 128px;
    color: #545c63;
}
.footer ul {
    margin: 0 auto 16px;
    padding-top: 38px;
    width: 930px;
}
.footer ul li {
    float: left;
    width: 112px;
    margin: 0 10px;
    text-align: center;
    font-size: 14px;
}
.footer ul::after {
    content: "";
    display: block;
    clear: both;
}
.footer p {
    text-align: center;
    font-size: 12px;
}
</style>
