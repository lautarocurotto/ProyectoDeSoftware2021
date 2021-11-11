const initialLat = -34.9187;
const initialLng = -57.956;
const mapLayerUrl =  'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png';

export class Map{

    #drawItems;
 


    constructor({selector,longitudes,latitudes}){
        this.#drawItems = new L.FeatureGroup();

        this.#initializeMap(selector,longitudes,latitudes);

      
        
    }

    #initializeMap(selector,longitudes,latitudes){
        this.map = L.map(selector).setView([initialLat,initialLng],13);
        L.tileLayer(mapLayerUrl).addTo(this.map);
        
        this.map.addLayer(this.#drawItems);

        this.map.addControl(this.createControls);
        let latlngs=[];
        for (let i=0;i<longitudes.length;i++){
               let lalg=[latitudes[i].value,longitudes[i].value];
                latlngs.push(lalg);
        }
     
        var polygon=L.polygon(latlngs,{color:'red'}).addTo(this.map);
    };

    
    
    hasValidZone(){
        return this.drawnlayers.length ===1;
    }

    get drawnlayers(){
        return Object.values(this.#drawItems._layers);
    }

    get editControls(){
        return this.editControlsToolbar ||= new L.Control.Draw({
            draw:false,
            edit:false
        });
    }

    get createControls(){
        return this.createControlsToolbar ||= new L.Control.Draw({
            draw:false,
            edit:false
        });
    }
}