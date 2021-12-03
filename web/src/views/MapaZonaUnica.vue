<template>
    <div>
        <l-map style= "height: 65vh" :zoom="zoom" :center="center">
        <l-tile-layer :url="url"></l-tile-layer>
        <l-polygon :lat-lngs="[zona[0].coordenadas]" :color="zona[0].color" :fill="true" :fillColor="zona[0].color" :fillOpacity="0.5"/>
        </l-map>
        <div class="card">
            <div class="card-body">
            <h5 class="card-title">{{zona[0].nombre}}</h5>
            <h6 class="card-subtitle mb-2 text-muted">Id: {{zona[0].id}}</h6>
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
            zona: [],
        };
    },
  created(){
    fetch(this.$store.state.mainURL + '/consultas/'+ this.$route.params.id).then((response) =>{
        console.log(response);
        return response.json();
    }).then((json)=>{
        console.log(json);
        this.zona.push(json.Zonas);
        console.log(json.Zonas)
        console.log(json.Zonas.coordenadas)   
    }).catch((e) => {
                console.log(e);
            });        
    }
}

</script>