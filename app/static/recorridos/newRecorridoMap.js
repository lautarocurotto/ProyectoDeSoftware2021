import { Map } from './MapMultipleMarker.js';


const submitHandler = (event,map) => {
    event.preventDefault();
    if (!map.hasValidZone()){
        alert('Selecciona minimo de puntos para aceptar el recorrido');
    }
    else {
        const name=document.querySelector('#nombre').value;
        const description=document.querySelector('#descripcion').value;
        const status=document.querySelector('#status').value;
        
        const coodinates=map.drawnlayers[0].getLatLngs().flat().map(coordinate =>{
            return {lat:coordinate.lat ,lng:coordinate.lng }
        });

        console.log(coodinates);

    
      
        fetch('/recorridos/nuevo', {
            method: 'POST',
            body: JSON.stringify({name:name,description:description,status:status,coodinates:coodinates}),
            headers: {
                'Content-Type':'application/json'
            }

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