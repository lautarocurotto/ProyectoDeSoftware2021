const initialLat = -34.9187;
const initialLng = -57.956;
const mapLayerUrl =  'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png';

export function Map (selector, lati,longi,create=false,update=false,show=false){

    let marker;
    let map;

    function initializeMap(selector){
        map = L.map(selector).setView([initialLat,initialLng],13);
        L.tileLayer(mapLayerUrl).addTo(map);
        if(update || show){
            marker = L.marker([parseFloat(lati),parseFloat(longi)]).addTo(map);
        }
    };
    initializeMap(selector);

    function addMarker({lat,lng}){
       if (marker) {
            marker.remove();
        };
        marker = L.marker([lat,lng]).addTo(map);
    };

    if (create || update){
        map.addEventListener('click', (e)=> {addMarker(e.latlng)});
        return {
            get marker() {return marker},
            addMarker: addMarker
        }; 
    }
    else{
        return {
            get marker() {return marker}
        }; 
    }
}