import { createStore } from "vuex";

const store = createStore({
    state(){
        return {
            color1 : "",
            color2 : "",
            color3 : "",
            mainURL : "http://127.0.0.1:5000/api"
        }
    }
})

export default store