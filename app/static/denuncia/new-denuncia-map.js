import { Map } from './MapSingleMarker.js';

const submitHandler = (event,map) => {

    if (!map.marker){
        event.preventDefault();
        alert('Selecciona una ubicacion por favor');
    }
    else {
        let latlng= map.marker.getLatLng();
        console.log(latlng.lat);
        document.getElementById('lat').setAttribute('value',latlng.lat);
        document.getElementById('lng').setAttribute('value',latlng.lng);
    }
}

const resetHandler = (event,map) => {

    if (map.marker){
        map.marker.remove();
        
    }
}

window.onload = () => {
    
    let latitud = document.getElementById('lat');
    let longitud = document.getElementById('lng');
    let map = new Map('mapid', latitud.getAttribute('value'), longitud.getAttribute('value'));
    let form = document.getElementById('new-denuncia-form');
    let res=form.addEventListener('submit', (event)=> submitHandler(event,map));
    let res2=form.addEventListener('reset', (event)=> resetHandler(event,map));

}