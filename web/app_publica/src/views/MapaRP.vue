<template>
  <l-map style="height: 700px" :zoom="zoom" :center="center" >
    <l-tile-layer :url="url" :attribution="attribution"></l-tile-layer>
    <l-marker :lat-lng="markerLatLng"></l-marker>
  </l-map>
</template>

<script>
import {LMap, LTileLayer, LMarker} from '@vue-leaflet/vue-leaflet';

export default {
  components: {
    LMap,
    LTileLayer,
    LMarker
  },
  data () {
    return {
      url: 'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',
      attribution:
        '&copy; <a target="_blank" href="http://osm.org/copyright">OpenStreetMap</a> contributors',
      zoom: 13,
      center: [-34.9187,-57.956],
      markerLatLng: []
    };
  },
  created(){
      fetch('http://127.0.0.1:5000/api/puntos-encuentro').then((response) =>{
          return response.json();
      }).then((json) => {
          this.puntos = json.puntos_encuentro;
      }).catch((e) => {
        console.log(e);
      })
  }
  
}
</script>
