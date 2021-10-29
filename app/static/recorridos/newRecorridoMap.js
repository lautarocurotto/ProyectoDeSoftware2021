import { Map } from './MapMultipleMarker.js';

const submitHandler = (event,map) => {
   
    if (map.marker.length<1){
        event.preventDefault();
        alert('Selecciona minimo de puntos para aceptar el recorrido');
    }
    else {
        let latlng;
        for (punto in map.marker){
            latlng=punto.getLatLng();
            console.log(latlng);
            document.getElementById('lat').setAttribute('value',latlng.lat);
            document.getElementById('lng').setAttribute('value',latlng.lng);
        }
      
    }
}

const resetHandler = (event,map) => {
    console.log(map.marker.length);
    for (let punto in map.marker) {
        console.log(punto);
     }
     
    
}

window.onload = () => {
    
    
    let map = new Map('mapid');
    let form = document.getElementById('create-recorrido-form');
    let res=form.addEventListener('submit', (event)=> submitHandler(event,map));
    let res2=form.addEventListener('reset', (event)=> resetHandler(event,map));

}