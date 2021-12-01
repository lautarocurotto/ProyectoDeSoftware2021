import { Map } from './MapMultipleMarkerCUS.js';


window.onload = () => {
    
    let latitud = document.getElementsByName('lat');
    let longitud = document.getElementsByName('lng');
    let map = new Map({
        selector:'mapid',
        longitudes: longitud,
        latitudes:latitud,
        crearPolyline:true,
        show:true
    })
    
    

}