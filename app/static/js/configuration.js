function closeForm(evt){
    var forms = document.getElementsByClassName("modal");
    for (let index = 0; index < forms.length; index++) {
        const element = forms[index];
        element.style.display = "none";
    }
}

function showMenu(evt){
    document.getElementById("menu").style.display = "flex";
}   


function setColor(evt, nro){
    console.log("Cambiadno el color" + nro + " a " + evt.value);
    var formdata= new FormData();
    formdata.append("color"+nro, evt.value);
    var request = new XMLHttpRequest();
    request.open("POST", base_url + "/set/color"+nro);

    request.onload = function(data){
        window.location = base_url;
    }
    
    request.send(formdata);

}

function setCriterio(evt){
    console.log("Cambiando el criterio a" + evt.value);
    var formdata= new FormData();
    formdata.append("criterio", evt.value);
    var request = new XMLHttpRequest();
    request.open("POST", base_url + "/set/criterio");

    request.onload = function(data){
        window.location = base_url;
    }
    
    request.send(formdata);

}