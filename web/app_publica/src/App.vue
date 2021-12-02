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
  },
  created() {
    // obtener configs globales 
    fetch(this.$store.state.mainURL + "/configuracion/get-configs")
      .then(res => res.json())
      .then(data => {
        this.$store.commit('setConfigs', data);
      })
      .then(() => {
        this.applyStyles("h2", this.$store.state.configs.color1);
        this.applyStyles("h1", this.$store.state.configs.color1);
        this.applyStyles("h3", this.$store.state.configs.color1);
        this.applyStyles("h4", this.$store.state.configs.color1);
        this.applyStyles("a", this.$store.state.configs.color3);
      });
  },
  methods : {
    applyStyles(tagname, color){
      var elements = document.getElementsByTagName(tagname);
      for (let index = 0; index < elements.length; index++) {
        const element = elements[index];
        element.style.color = color;
      }
    }
  }
}
</script>


<style>
  h1,h2,h3,h4,h5{
    color: var('--this.$store.state.configs.color2');
  }
</style>