import { createStore } from "vuex";

const store = createStore({
    state(){
        return {
            mainURL : "http://127.0.0.1:5000/api",
            configs : {"color2" : ""}
        }
    },
    mutations : {
        setConfigs(state, configs){
            console.log("configurando configs : ");
            state.configs = configs;
            console.log(state.configs);
        }
    }
})

export default store