import { Map } from './MapMultipleMarker.js';

const submitHandler = (event,map) => {
    event.preventDefault();
    if (map.hasValidZone()){
        alert('Selecciona minimo de puntos para aceptar el recorrido');
    }
    else {
        const name=document.querySelector('#zone_name').ariaValueMax;
        const coodinates=map.drawlayers[0].getLatLngs().flat().map(coordinate =>{
            return {lat:coodinates.lat,lng:coordinate.lng}
        });

        const formData=new FormData();
        formData.append('name',name);
        formData.append('coordinates',JSON.stringify(coodinates));

        fetch('/recorridos/nuevo', {
            method: 'POST',
            body: formData
        })
      
    }
}
     
    


window.onload = () => {
    
    
    let map = new Map({
        selector:'mapid',
        crearRectangle:false,
        crearPolyline:true,
        crearPoligono:false

    })
    let form = document.getElementById('create-recorrido-form');
    let res=form.addEventListener('submit', (event)=> submitHandler(event,map));
    

}