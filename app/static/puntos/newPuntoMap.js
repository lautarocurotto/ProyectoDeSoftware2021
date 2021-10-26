import { Map } from '../MapSingleMarker.js';

const submitHandler = (event,map) => {

    if (!map.marker){
        event.preventDefault();
        alert('Selecciona una ubicacion por favor');
    }
    else {
        latlng= map.marker.getLatLng();
        document.getElementById('lat').setAttribute('value',latlng.lat);
        document.getElementById('lng').setAttribute('value',latlng.lng);

    }

}

window.onload = () => {
    
    const map = new Map({
        selector: 'mapid'
    });
    const form = document.getElementById('create-punto-form');
    form.addEventListener('submit', (event)=> submitHandler(event,map));

}