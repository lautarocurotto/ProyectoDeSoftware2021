const initialLat = -34.9187;
const initialLng = -57.956;
const mapLayerUrl =  'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png';

export class Map{

    #drawItems;
    #crearPoli;
    #crearRecta;
    #crearPoligono;


    constructor({selector,crearPolyline,crearRectangle, crearPoligono}){
        this.#drawItems = new L.FeatureGroup();

        this.crearPoli = crearPolyline;
        this.crearRecta = crearRectangle;
        this.crearPoligono = crearPoligono;

        this.#initializeMap(selector);

        this.map.on(L.Draw.Event.CREATED,(e)=>{
            this.#eventHandler(e,this.map,this.#drawItems,this.editControls,this.createControls)
        });
        this.map.on('draw:deleted',()=>{
            this.#deleteHandler(this.map,this.editControls,this.createControls)
        });
    }

    #initializeMap(selector){
        this.map = L.map(selector).setView([initialLat,initialLng],13);
        L.tileLayer(mapLayerUrl).addTo(this.map);
        
        this.map.addLayer(this.#drawItems);

        this.map.addControl(this.createControls);
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
        createControls.addTo(map);
        editControls.remove();
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
            edit:{
                featureGroup: this.#drawItems
            }
        });
    }

    get createControls(){
        return this.createControlsToolbar ||= new L.Control.Draw({
            draw:{
                circle:false,
                marker:false,
                polyline: this.crearPoli,
                rectangle: this.crearRecta,
                polygon: this.crearPoligono

            }
        });
    }
}