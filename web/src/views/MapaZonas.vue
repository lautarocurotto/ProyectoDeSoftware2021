<template>
    <div>
        <l-map style= "height: 65vh" :zoom="zoom" :center="center">
        <l-tile-layer :url="url"></l-tile-layer>
        <div v-for="(zone, index) in zonas" :key="{index}">
            <l-polygon :lat-lngs="[zone.coordenadas]" :color="zone.color" :fill="true" :fillColor="zone.color" :fillOpacity="0.5"/>
        </div>
        </l-map>
        <div class="col-md-6 border-bottom">
          <h4>Zonas</h4>
            <div class="card" v-for="(zone,index) in zonas" :key="index">
              <div class="card-body">
                <h5 class="card-title">{{zone.nombre}}</h5>
                <h6 class="card-subtitle mb-2 text-muted">Id: {{zone.id}}</h6>
                <router-link :to="{ path: '/mapaZonasInundables/' + zone.id}" class="btn btn-primary"><a>Ver Zona</a></router-link>
              </div>
            </div>
        </div>
    </div>
    
</template>


<script>
import { LMap, LTileLayer, LPolygon } from '@vue-leaflet/vue-leaflet'

export default{
    components: {
        LMap,
        LTileLayer,
        LPolygon,
    },
    data(){
        return{
            url: 'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',
            zoom: 13,
            center: [-34.9187,-57.956],
            zonas: [],
        };
    },
  created(){
        fetch(this.$store.state.mainURL + '/consultas').then((response) =>{
            return response.json();
        }).then((json) => {
            for (var i=1;i<=json.total;i++){
                fetch(this.$store.state.mainURL + '/consultas?page='+i).then((response2) =>{
                    return response2.json();
                }).then((json2) => {
                    for (var i=0;i<json2.zonas.length;i++){
                        this.zonas.push(json2.zonas[i]);
            
                    }
                    }
            )} 
            }).catch((e) => {
                console.log(e);
            });
    }
}

</script>