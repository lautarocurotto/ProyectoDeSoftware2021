const initialLat = -34.9187;
const initialLng = -57.956;
const mapLayerUrl =  'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png';

export class Map{

    #drawItems;
 


    constructor({selector,longitudes,latitudes}){
        this.#drawItems = new L.FeatureGroup();

        this.#initializeMap(selector,longitudes,latitudes);

        this.map.on(L.Draw.Event.CREATED,(e)=>{
            this.#eventHandler(e,this.map,this.#drawItems,this.editControls,this.createControls)
        });
        this.map.on('draw:deleted',()=>{
            this.#deleteHandler(this.map,this.editControls,this.createControls)
        });
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
        console.log(latlngs);
        var polyline=L.polyline(latlngs,{color:'red'}).addTo(this.map);
    };

    #eventHandler(e,map,drawItems,editControls,createControls){
        const existingZones= Object.values(drawItems._layers);

        if (existingZones.length == 0){
            const type=e.layerType;
            const layer= e.layer;

            layer.editing.enable();
            drawItems.addLayer(layer);
            editControls.addTo(map);
            createControls.remove();
        }

    };

    #deleteHandler(map,editControls,createControls){
       
    }   
    
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