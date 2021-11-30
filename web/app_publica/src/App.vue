<template>
  <div>
    <NavBar />
    <router-view />
    <Footer />
  </div>
</template>

<script>
import "@/assets/css/bootstrap.min.css";
import NavBar from './views/NavBar.vue'
import Footer from './views/Footer.vue'

export default {
  name: 'App',
  components : {
    NavBar,
    Footer
  }
}
</script>
