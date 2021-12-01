import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import MapaRP from '../views/MapaRP.vue'
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
