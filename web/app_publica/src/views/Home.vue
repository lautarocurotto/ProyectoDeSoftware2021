<template>
    <div>
      <div class="container-fluid" v-bind:style="{'background-image' : 'url(https://images.unsplash.com/photo-1485617359743-4dc5d2e53c89?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=774&q=80)', 'height' : '250px' }" style="background-repeat: no-repeat; background-size: cover; background-position: center;">
          <div class="row align-items-center h-100">
              <div class="col-6"></div>
              <div class="col-md-6 col-sm-12">
                  <p style="padding: 20px; background: rgba(255, 255, 255, 0.8); border-radius: 6px;">Esta aplicación nace con el objetivo de proveer a la ciudad de La Plata con herramientas para informarse y ser informantes de las zonas de inundación.</p>
              </div>
              
          </div>
      </div>
      <div class="container px-4 py-5" id="featured-3">
          <h2 class="pb-2">Ponemos a tu disposición...</h2>
          <div class="row g-4 py-5 row-cols-1 row-cols-lg-3">
            <div class="feature col">
              <div class="feature-icon h1">
                <i class="fas fa-water"></i>
              </div>
              <h2>Zonas inundables</h2>
              <p>Paragraph of text beneath the heading to explain the heading. We'll add onto it with another sentence and probably just keep going until we run out of words.</p>
              <router-link class="icon-link btn btn-outline-primary" to="/mapaZonasInundables">Ver las zonas de inundación</router-link>
            </div>
            <div class="feature col">
              <div class="feature-icon h1">
                <i class="fas fa-route"></i>
              </div>
              <h2>Recorridos de evacuación</h2>
              <p>Paragraph of text beneath the heading to explain the heading. We'll add onto it with another sentence and probably just keep going until we run out of words.</p>
              <router-link class="icon-link btn btn-outline-primary" to="/mapaRecorridosPuntos">Mapa de recorridos y puntos de evacuacion</router-link>
            </div>
            <div class="feature col">
              <div class="feature-icon h1">
                <i class="fas fa-map-marked-alt"></i>
              </div>
              <h2>Puntos de encuentro</h2>
              <p>Paragraph of text beneath the heading to explain the heading. We'll add onto it with another sentence and probably just keep going until we run out of words.</p>
              <a href="#" class="icon-link btn btn-outline-primary">
                Ver
              </a>
            </div>
          </div>
      </div>
      <div class="" id="denunciar">
        <div class="container-fluid" style="background-color: rgb(238, 202, 0); height: 200px;">
          <div class="row align-items-center h-100">
              <div class="col-6" style="text-align: right;">
                  <h5>¿Conoces una zona que puede ser riesgosa en la ciudad?</h5>
                  <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Eveniet voluptatum vero perspiciatis possimus. Nemo fuga sapiente magni odio qui ullam sunt velit minus, aliquid sequi amet? Omnis rerum fugiat nesciunt!</p>
              </div>
              <div class="col-6" style="text-align: left;">
                  <router-link class="btn btn-lg btn-light" to="/denunciar">REALIZAR DENUNCIA</router-link>
              </div>
          </div>
        </div>
      </div>
    </div>
</template>

<script>

export default {
  name: 'Home'
}
</script>

<style scoped>
    .feature{
        height: 320px;
    }
</style>