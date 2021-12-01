const initialLat = -34.9187;
const initialLng = -57.956;
const mapLayerUrl =  'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png';
 
export class Map{

    #drawItems;
    #edita;

    constructor({selector,longitudes,latitudes,update}){
        this.#drawItems = new L.FeatureGroup();
        this.#edita=update;
        this.#initializeMap(selector,longitudes,latitudes,update);
    }

    #initializeMap(selector,longitudes,latitudes,update){
        this.map = L.map(selector).setView([initialLat,initialLng],13);
        L.tileLayer(mapLayerUrl).addTo(this.map);
        this.map.addLayer(this.#drawItems);
        this.map.addControl(this.createControls);
        let latlngs=[];
        for (let i=0;i<longitudes.length;i++){
               let lalg=[latitudes[i].value,longitudes[i].value];
                latlngs.push(lalg);
        }
        let poli= L.polyline(latlngs,{color:'red'}).addTo(this.map);
        if(update){
            poli.editing.enable();
            this.#drawItems.addLayer(poli);
        }
    };

    hasValidZone(){
        return this.drawnlayers.length ===1;
    }

    get drawnlayers(){
        return Object.values(this.#drawItems._layers);
    }

    get editControls(){
        if(this.#edita){
            return this.editControlsToolbar ||= new L.Control.Draw({
                draw:false,
                edit:{
                    featureGroup: this.#drawItems
                }
            });
        }
        else{
            return this.editControlsToolbar ||= new L.Control.Draw({
                draw:false,
                edit:false
            });
        }
    }

    get createControls(){
        return this.createControlsToolbar ||= new L.Control.Draw({
            draw:false
        });
    }
}


