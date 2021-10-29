import { Map } from './MapMultipleMarker.js';

const submitHandler = (event,map) => {
   
    if (map.marker.length<3){
        event.preventDefault();
        alert('Selecciona minimo 3 puntos para aceptar el recorrido');
    }
    else {
        let latlng;
        for (punto in map.marker){
            latlng=punto.getLatLng();
            console.log(latlng);
            "document.getElementById('lat').setAttribute('value',latlng.lat);"
            "document.getElementById('lng').setAttribute('value',latlng.lng);"
        }
      
    }
}

const resetHandler = (event,map) => {

    while (map.marker,length>0) map.marker.pop();
}

window.onload = () => {
    
    
    let map = new Map('mapid');
    let form = document.getElementById('create-recorrido-form');
    let res=form.addEventListener('submit', (event)=> submitHandler(event,map));
    let res2=form.addEventListener('reset', (event)=> resetHandler(event,map));

}