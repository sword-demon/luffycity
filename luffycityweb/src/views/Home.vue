<script setup>
import { reactive } from "vue";
const store = reactive({
    value2: null,
    colors: ["#99A9BF", "#F7BA2A", "#FF9900"],
});
</script>

<template>
    <h1>首页</h1>
    <el-row class="mb-4">
        <el-button type="primary">Primary</el-button>
        <el-rate v-model="store.value2" :colors="store.colors"></el-rate>
    </el-row>
</template>

<style scoped></style>
