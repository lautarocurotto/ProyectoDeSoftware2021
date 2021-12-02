import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import MapaRP from '../views/MapaRP.vue'
import MapaZonas from '../views/MapaZonas.vue'
import MapaZonaUnica from '../views/MapaZonaUnica.vue'
import Denuncia from '../views/Denuncia.vue'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/mapaRecorridosPuntos',
    name: 'mapaRecorridosPuntos',
    component: MapaRP
  },
  {
    path: '/mapaZonasInundables',
    name: 'mapaZonasInundables',
    component: MapaZonas
  },
  {
    path: '/mapaZonasInundables/:id',
    name: 'mapaZonaInundable',
    component: MapaZonaUnica
  },
  {
    path: '/denunciar',
    name: 'Denuncia',
    component: Denuncia
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
