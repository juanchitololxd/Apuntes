function setStyles(){
    
    var estilos = document.getElementById("style");
    if(estilos.getAttribute("href") == "./../estilos/dark.css")
        estilos.href = "./../estilos/oscuro.css";
    else
        estilos.href = "./../estilos/dark.css";
    
  }