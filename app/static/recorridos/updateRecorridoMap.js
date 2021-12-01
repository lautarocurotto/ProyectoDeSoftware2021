import { Map } from './MapMultipleMarkerUpdate.js';

 
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
    
    let latitud = document.getElementsByName('lat');
    let longitud = document.getElementsByName('lng');
    
    let map = new Map({
        selector:'mapid',
        longitudes: longitud,
        latitudes:latitud

    })
    let form = document.getElementById('formulario-update');
    let res=form.addEventListener('submit', (event)=> submitHandler(event,map));
    

}

