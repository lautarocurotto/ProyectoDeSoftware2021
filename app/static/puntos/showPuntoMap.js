import { Map } from './MapSingleMarkerShow.js';



window.onload = () => {
    
    let latitud = document.getElementById('lat');
    let longitud = document.getElementById('lng');
    let map = new Map('mapid',latitud.getAttribute('value'), longitud.getAttribute('value'));
    
};
