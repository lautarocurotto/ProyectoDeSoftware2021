import { Map } from '../mapa/MapMultipleMarkerCUS.js';

window.onload = () => {
    
    let latitud = document.getElementsByName('lat');
    let longitud = document.getElementsByName('lng');
    let color = document.getElementById('color').value;
    console.log(color);
    let map = new Map({
        selector:'mapid',
        longitudes: longitud,
        latitudes:latitud,
        crearPoligono:true,
        show:true,
        color:color

    })
}