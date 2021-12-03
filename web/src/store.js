import { createStore } from "vuex";

const store = createStore({
    state(){
        return {
            color1 : "",
            color2 : "",
            color3 : "",
            mainURL : "http://127.0.0.1:5000/api",
            registerURL : "none"
        }
    },
    mutations: {
        setURLs(state){
            if (process.env.NODE_ENV == "development"){
                state.registerURL = "http://127.0.0.1:5000/logingoogle";
                state.mainURL = "http://127.0.0.1:5000/api";
            }else{
                state.mainURL = "https://grupo40.proyecto2021.linti.unlp.edu.ar/";
                state.registerURL = "https://admin-grupo40.proyecto2021.linti.unlp.edu.ar/logingoogle";
            }
        }
    }
})

export default store