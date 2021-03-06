const initialLat = -34.9187;
const initialLng = -57.956;
const mapLayerUrl =  'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png';
 
export class Map{

    #drawItems;
    #crear;
    #edita;
    #mostrar;
    #crearPoli;
    #crearRecta;
    #crearPoligono;

    constructor({selector,crearPolyline=false,crearRectangle=false, crearPoligono=false,longitudes,latitudes,create=false,update=false,show=false,color}){
        this.#drawItems = new L.FeatureGroup();
        this.crearPoli = crearPolyline;
        this.crearRecta = crearRectangle;
        this.crearPoligono = crearPoligono;
        this.#crear=create;
        this.#edita=update;
        this.#mostrar=show;
        this.#initializeMap(selector,longitudes,latitudes,update,show,color);

        if(create){
            this.map.on(L.Draw.Event.CREATED,(e)=>{
                this.#eventHandler(e,this.map,this.#drawItems,this.editControls,this.createControls)
            });
            this.map.on('draw:deleted',()=>{
                this.#deleteHandler(this.map,this.editControls,this.createControls)
            });
        }
    }

    #initializeMap(selector,longitudes,latitudes,update,show,color){
        this.map = L.map(selector).setView([initialLat,initialLng],13);
        L.tileLayer(mapLayerUrl).addTo(this.map);
        this.map.addLayer(this.#drawItems);
        this.map.addControl(this.createControls);
        if(update || show){
            let latlngs=[];
            for (let i=0;i<longitudes.length;i++){
                    let lalg=[latitudes[i].value,longitudes[i].value];
                    latlngs.push(lalg);
            }
            let poli;
            if(this.crearPoli){
                poli= L.polyline(latlngs,{color:'red'}).addTo(this.map);
            }
            if(this.crearPoligono){
                var polygon=L.polygon(latlngs,{color:color}).addTo(this.map);
            }
            if(update){
                poli.editing.enable();
                this.#drawItems.addLayer(poli);
            }
        }
    };

    #eventHandler(e,map,drawItems,editControls,createControls){
        const existingZones= Object.values(drawItems._layers);
        if (existingZones.length == 0){
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
        if(this.#edita || this.#crear){
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
        if(this.#crear){
            return this.createControlsToolbar ||= new L.Control.Draw({
                draw:{
                    circle:false,
                    circlemarker:false,
                    marker:false,
                    polyline: this.crearPoli,
                    rectangle: this.crearRecta,
                    polygon: this.crearPoligono
    
                }
            });
        }
        else{
            return this.createControlsToolbar ||= new L.Control.Draw({
                draw:false
            });
        }
    }
}


