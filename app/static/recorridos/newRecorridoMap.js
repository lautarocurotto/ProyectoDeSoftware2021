import { Map } from '../mapa/MapMultipleMarkerCUS.js';


const submitHandler = (event,map) => {
   
    if (!map.hasValidZone()){
        event.preventDefault();
        alert('Selecciona minimo de puntos para aceptar el recorrido');
    }
    else { 
        const coodinates=map.drawnlayers[0].getLatLngs().flat().map(coordinate =>{
            return {lat:coordinate.lat ,lng:coordinate.lng }
        });
        const coordenadas=document.querySelector('#coordinates');
        coordenadas.value=JSON.stringify(coodinates);
    }
}
     
window.onload = () => {
    
    let map = new Map({
        selector:'mapid',
        crearPolyline:true,
        create:true,
    })
    let form = document.getElementById('create-recorrido-form');
    let res=form.addEventListener('submit', (event)=> submitHandler(event,map));
    

}