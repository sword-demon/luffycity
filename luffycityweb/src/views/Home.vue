<script setup>
import Header from "../components/Header.vue";
import Footer from "../components/Footer.vue";
import http from "../utils/http";

http.get("/home/test").then((response) => {
    console.log(response.data);
});
</script>

<template>
    <div class="home">
        <Header />
        <Footer />
    </div>
</template>

<style scoped></style>
