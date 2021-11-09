import { Map } from './MapMultipleMarkerUpdate.js';

 
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
        const id=document.getElementById('idReco');

      
        fetch('/recorridos/update/'+id, {
            method: 'POST',
            body: JSON.stringify({name:name,description:description,status:status,coodinates:coodinates}),
            headers: {
                'Content-Type':'application/json'
            }

        }).then(data => location.reload());
      
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

