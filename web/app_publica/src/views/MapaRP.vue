<template>
  <l-map style="height: 700px" :zoom="zoom" :center="center" >
    <l-tile-layer :url="url" :attribution="attribution"></l-tile-layer>
    <div v-for="(marker,index) in markers" :key="index" >
      <l-marker :lat-lng=[marker.lat,marker.long]></l-marker>
    </div>
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
      markers: []
    };
  },
  created(){
      fetch('http://127.0.0.1:5000/api/puntos-encuentro').then((response) =>{
          return response.json();
      }).then((json) => {
          for (var i=1;i<=json.total;i++){
             fetch('http://127.0.0.1:5000/api/puntos-encuentro?page='+i).then((response2) =>{
                return response2.json();
             }).then((json2) => {
                for (var i=0;i<json2.puntos_encuentro.length;i++){
                    this.markers.push(json2.puntos_encuentro[i]);
                }
              }
          )} 
      }).catch((e) => {
        console.log(e);
      })
  }
  
}
</script>
