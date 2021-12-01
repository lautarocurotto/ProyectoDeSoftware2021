<template>
    <div>
        <div class="text-center denuncia">
            <h2>Estás a punto de realizar una denuncia</h2>
            <p>Primero te tomaremos los datos sobre el lugar y de qué se trata el problema.</p>
            <p>Luego te pediremos información personal.</p>
            <p>Puedes ser contactado por alguno de nuestros operadores para validar información.</p>
        </div>
        <form v-on:submit="mandarDenuncia">
            <div class="text-center denuncia">
                <h2>¿De qué se trata?</h2>
                <div class="mb-3">
                    <label>En breves palabras, ¿De qué se trata el problema?
                    <input v-model="nuevadenuncia.titulo" required name="titulo" type="text" class="form-control" placeholder="Título">
                    </label>
                </div>
                <div class="mb-3">
                    <label>Describí un poco más el problema que querés denunciar
                    <textarea class="form-control" v-model="nuevadenuncia.descripcion" name="descripcion" required></textarea>
                    </label>
                </div>
                <div class="mb-3">
                    <label>Dentro de qué categoría entraría
                    <select v-model="nuevadenuncia.categoria_id" class="form-control" name="categoria_id" required>
                        <option value=" "> </option>
                        <option v-for="(categoria, index) in categorias" v-bind:value="categoria.id" v-bind:key="index">{{categoria.name}}</option>
                    </select>
                    </label>
                </div>
            </div>
            <div class="text-center denuncia">
                <h2>Marcá en el mapa la ubicación de lo que querés denunciar</h2>
                <l-map style="height: 300px; width: 100%;" :zoom="mapa.zoom" :center="mapa.center" v-on:click="addMarker">
                    <l-tile-layer :url="mapa.url" :attribution="mapa.attribution"></l-tile-layer>
                    <l-marker v-if="mapa.marker" :lat-lng="mapa.marker"></l-marker>
                </l-map>
            </div>
            <div class="text-center denuncia">
                <h2>Sus datos personales</h2>
                <div class="mb-3">
                    <label>Nombre
                    <input v-model="nuevadenuncia.nombre_denunciante" required name="nombre_denunciante" type="text" class="form-control" placeholder="Nombre">
                    </label>
                </div>
                <div class="mb-3">
                    <label>Apellido
                    <input v-model="nuevadenuncia.apellido_denunciante" required name="apellido_denunciante" type="text" class="form-control" placeholder="Apellido">
                    </label>
                </div>
                <div class="mb-3">
                    <label>Teléfono
                    <input v-model="nuevadenuncia.telcel_denunciante" required name="telcel_denunciante" type="text" class="form-control" placeholder="Número telefónico">
                    </label>
                </div>
                <div class="mb-3">
                    <label>Email
                    <input v-model="nuevadenuncia.email_denunciante" required name="email_denunciante" type="email" class="form-control" placeholder="Email">
                    </label>
                </div>
                <input class="btn btn-outline-success" type="submit" value="Listo, Mandar denuncia">
            </div>
        </form>
    </div>
</template>


<script>
import {LMap, LTileLayer, LMarker} from '@vue-leaflet/vue-leaflet';

var userlat = -34.9187
var userlng = -57.956

export default {
    name : 'Denuncia',
    data() {
        return {
            categorias : [],
            nuevadenuncia : {
                categoria_id : -1,
                apellido_denunciante : "",
                nombre_denunciante : "",
                telcel_denunciante : "",
                email_denunciante : "",
                titulo : "",
                descripcion : "",
                coordenadas : ""
            },
            mapa : {
                url: 'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',
                attribution: '&copy; <a target="_blank" href="http://osm.org/copyright">OpenStreetMap</a> contributors',
                zoom: 13,
                center: [userlat, userlng],
                marker: null
            }
        }
    },
    methods: {
        mandarDenuncia(evt){
            evt.preventDefault();
            this.nuevadenuncia.coordenadas = this.mapa.marker.lat + ", " + this.mapa.marker.lng;
            console.log(JSON.stringify(this.nuevadenuncia))
            fetch(this.$store.state.mainURL + "/denuncias",{
                method : "POST",
                body : JSON.stringify(this.nuevadenuncia)
            })
            .then(res => res.json())
            .then(data => {
                console.log(data);
            })
            .catch(error => {
                console.log(error);
            });
        },
        addMarker(evt){
            this.mapa.marker = evt.latlng;
            console.log("lat: " + this.mapa.marker.lat + " lng: " + this.mapa.marker.lng)
        }
    },
    created(){
        // obtener categorias
        fetch(this.$store.state.mainURL + "/denuncias/get-categorias")
            .then(response => response.json())
            .then(data => this.categorias = data.categorias);

        navigator.geolocation.getCurrentPosition((position) => {
            userlat = position.coords.latitude;
            userlng = position.coords.lng;
        });
    },
    components: {
        LMap,
        LTileLayer,
        LMarker
    }
}

</script>

<style scoped>
    textarea{
        display: block;
    }

    .denuncia{
        padding: 20px;
    }
</style>