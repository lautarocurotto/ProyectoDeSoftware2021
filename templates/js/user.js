function showNewUserForm(evt){
    document.getElementById("new-user-modal").style.display = "flex";
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

function filterUsers(evt){
    console.log("Se esta realizando una busqueda de usuarios con query " + document.getElementById("user-query").value);
    //codigo para filtrar la tabla con criterio del query aqui
}

function showActiveUsers(evt){
    fixbtns(evt);
    evt.disabled = true;
    //filter users (active)
}

function showInactiveUsers(evt){
    fixbtns(evt);
    evt.disabled = true;
    //filter users (inactive)
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