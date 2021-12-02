<template>
    <nav>
        <div class="container" v-bind:style="{'background-color' : $store.state.configs.color2}">
            <header class="d-flex flex-wrap justify-content-center py-3 mb-4">
              <a href="/" class="d-flex align-items-center mb-3 mb-md-0 me-md-auto text-dark text-decoration-none">
                <img src="../assets/laplatacorazon.png" height="40" width="50" alt="">
                <span class="fs-4">Zonas Inundables</span>
              </a>
        
              <ul class="nav">
                <!-- <li class="nav-item"><a href="#" class="nav-link active" aria-current="page">Home</a></li> -->
                <li class="nav-item"><a href="#denunciar" class="nav-link">Denunciar</a></li>
                <li class="nav-item">
                  <a href="#" class="btn btn-outline-primary"><i class="fas fa-user-plus"></i> Registrarse</a>
                </li>
              </ul>
            </header>
          </div>
    </nav>
</template>

<script>
export default {
  name: 'NavBar'
}
</script>