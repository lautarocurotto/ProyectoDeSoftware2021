<template>
  <div>
    <l-map style="height: 300px" :zoom="zoom" :center="center" >
      <l-tile-layer :url="url" :attribution="attribution"></l-tile-layer>
      <div v-for="(marker,index) in markers" :key="index" >
        <l-marker :lat-lng=[marker.lat,marker.long]>
          <l-popup>Nombre: {{marker.nombre}}. Direccion: {{marker.direccion}}. Telefono: {{marker.telefono}}. Email: {{marker.email}}  </l-popup>
        </l-marker>
      </div>
      <div v-for="(recorrido,index) in recorridos" :key="index" >
        <l-polyline :lat-lngs=[recorrido.coordenadas]></l-polyline>
      </div>
    </l-map>
    <div class="container">
      <div class="row">
        <div class="col-md-6 border-bottom">
          <h4>Puntos de encuentro</h4>
            <div class="card margin-bottom" style="width: 18rem;" v-for="(marker,index) in markers" :key="index">
              <div class="card-body">
                <h5 class="card-title">{{marker.nombre}}</h5>
                <h6 class="card-subtitle mb-2 text-muted">{{marker.direccion}}</h6>
                <p class="card-text">
                  <strong>Telefono</strong>: {{marker.telefono}} <br>
                  <strong>Email</strong>: {{marker.email}} 
                </p>
              </div>
            </div>
        </div>

        <div class="col-md-6 border-bottom">
          <h4>Recorridos</h4>
            <div class="card margin-bottom" style="width: 18rem;" v-for="(recorrido,index) in recorridos" :key="index">
              <div class="card-body">
                <h5 class="card-title">{{recorrido.nombre}}</h5>
                <p class="card-text">
                  {{recorrido.descripcion}}
                </p>
              </div>
            </div>
        </div>
      </div>
    </div>

  </div>
</template>

<script>
import {LMap, LTileLayer, LMarker, LPolyline, LPopup} from '@vue-leaflet/vue-leaflet';

export default {
  components: {
    LMap,
    LTileLayer,
    LMarker,
    LPolyline,
    LPopup
  },
  data () {
    return {
      url: 'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',
      attribution:
        '&copy; <a target="_blank" href="http://osm.org/copyright">OpenStreetMap</a> contributors',
      zoom: 13,
      center: [-34.9187,-57.956],
      markers: [],
      recorridos: [],
    };
  },
  created(){
      fetch(this.$store.state.mainURL + '/puntos-encuentro').then((response) =>{
          return response.json();
      }).then((json) => {
          for (var i=1;i<=json.total;i++){
             fetch(this.$store.state.mainURL + '/puntos-encuentro?page='+i).then((response2) =>{
                return response2.json();
             }).then((json2) => {
                for (var i=0;i<json2.puntos_encuentro.length;i++){
                    this.markers.push(json2.puntos_encuentro[i]);
                }
              }
          )} 
      }).catch((e) => {
        console.log(e);
      });

    fetch(this.$store.state.mainURL + '/recorridos-evacuacion').then((response) =>{
          return response.json();
      }).then((json) => {
          for (var i=1;i<=json.total;i++){
             fetch(this.$store.state.mainURL + '/recorridos-evacuacion?page='+i).then((response2) =>{
                return response2.json();
             }).then((json2) => {
                for (var i=0;i<json2.recorridos.length;i++){
                    this.recorridos.push(json2.recorridos[i]);
            
                }
              }
          )} 
      }).catch((e) => {
        console.log(e);
      });
  }
}
</script>
