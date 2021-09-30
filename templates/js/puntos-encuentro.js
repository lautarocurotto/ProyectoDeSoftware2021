function showNewForm(evt){
    document.getElementById("new-pto-modal").style.display = "flex";
}

function closeForm(evt){
    var forms = document.getElementsByClassName("modal");
    for (let index = 0; index < forms.length; index++) {
        const element = forms[index];
        element.style.display = "none";
    }
}

function showSearchForm(evt){
    document.getElementById("search-form").style.display = "flex";
}

function showPublished(evt){
    fixbtns(evt);
    evt.disabled = true;
    console.log("mostrando puntos de encuentro publicados");
}

function showUnpublished(evt){
    fixbtns(evt);
    evt.disabled = true;
    console.log("mostrando puntos de encuentro sin publicar");
}

function fixbtns(evt){
    var filterBtns = document.getElementsByClassName("filterbtn");

    for (let index = 0; index < filterBtns.length; index++) {
        const element = filterBtns[index];
        element.disabled = false;
    }
}

function clearFilters(evt){
    fixbtns();
    
    //quitar filtros de la lista
}

function showMenu(evt){
    document.getElementById("menu").style.display = "flex";
}   