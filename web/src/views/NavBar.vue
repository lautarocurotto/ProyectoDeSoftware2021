<template>
    <nav>
        <div class="container">
            <header class="d-flex flex-wrap justify-content-center py-3 mb-4">
              <a href="/" class="d-flex align-items-center mb-3 mb-md-0 me-md-auto text-dark text-decoration-none">
                <img src="../assets/laplatacorazon.png" height="40" width="50" alt="">
                <span class="fs-4">Zonas Inundables</span>
              </a>
        
              <ul class="nav">
                <li class="nav-item"><a href="#denunciar" class="nav-link">Denunciar</a></li>
                <li class="nav-item">
                  <a v-bind:href="$store.state.registerURL" class="btn btn-outline-primary"> Ingresar con Google <i class="fab fa-google"></i></a>
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