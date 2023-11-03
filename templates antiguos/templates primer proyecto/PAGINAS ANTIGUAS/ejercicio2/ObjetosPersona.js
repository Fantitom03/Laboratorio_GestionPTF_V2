class Persona{
    constructor(apellido, nombre, genero){
        this.apellido = apellido;
        this.nombre = nombre;
        this.genero = genero;
        this.nombre_completo = nombre + " " + apellido;
    }

    obtDetalles(){
        console.log("Nombre: "+this.nombre_completo);
        console.log("Genero: "+this.genero);
    }
}

let formulario = document.getElementById("form-container");
formulario.addEventListener("submit", e => {
    e.preventDefault();
    let nombre = document.getElementById("Nombre").value;
    let apellido = document.getElementById("Apellido").value;
    let genero = document.getElementById("Genero").value;

    let personas = [];
    personas.push(new Persona(apellido, nombre, genero));
    console.log(personas);

    // Create a button element
    let boton = document.createElement("button");
    boton.innerHTML = "X";

    // Create a new table row
    let fila = document.createElement("tr");

    // Create table cells (td) for the data
    let cellNombre = document.createElement("td");
    cellNombre.textContent = nombre;
    let cellApellido = document.createElement("td");
    cellApellido.textContent = apellido;
    let cellGenero = document.createElement("td");
    cellGenero.textContent = genero;

    // Append the cells and button to the row
    fila.appendChild(cellNombre);
    fila.appendChild(cellApellido);
    fila.appendChild(cellGenero);
    fila.appendChild(boton);

    // Append the row to the tbody
    document.getElementById("tibody").appendChild(fila);

    boton.onclick = function (){
        let filaAEliminar = boton.parentNode;
        filaAEliminar.parentNode.removeChild(filaAEliminar);

    }
})