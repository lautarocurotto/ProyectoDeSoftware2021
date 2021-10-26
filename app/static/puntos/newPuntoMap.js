import { Map } from '../MapSingleMarker.js';

const submitHandler = (event,map) => {

    if (!map.marker){
        event.preventDefault();
        alert('Selecciona una ubicacion por favor');
    }
    else {
        let latlng= map.marker.getLatLng();
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
    
    let map = new Map({selector:'mapid'});
    let form = document.getElementById('create-punto-form');
    form.addEventListener('submit', (event)=> submitHandler(event,map));
    form.addEventListener('reset', (event)=> resetHandler(event,map));

}