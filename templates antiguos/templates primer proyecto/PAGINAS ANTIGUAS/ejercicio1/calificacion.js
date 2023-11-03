let select = document.getElementById("calificacion");
let textarea = document.getElementById("floatingTextarea");

select.addEventListener('change', function calificar() {
let opcionSeleccionada = select.value;

switch (opcionSeleccionada) {
    case "aprobado":
        document.getElementById('Ej1').innerHTML = "CSFT-Aprobado";
        textarea.disabled = true;
        break;
    case "rechazado":
        document.getElementById('Ej1').innerHTML = "CSFT-Rechazado";
        textarea.disabled = true;
        break;
    case "observado":
        document.getElementById('Ej1').innerHTML = "CSFT-Observado";
        textarea.disabled = false;
        break;
    default:
        document.getElementById('Ej1').innerHTML = "Pendiente";
        textarea.disabled = true;
        break;
    }
});

let select2 = document.getElementById("calificacion2");
let textarea2 = document.getElementById("floatingTextarea2");

select2.addEventListener('change', function calificar2() {
let opcionSeleccionada2 = select2.value;
    
    switch (opcionSeleccionada2) {
        case "aprobado":
            document.getElementById('Ej2').innerHTML = "CSFT-Aprobado";
            textarea2.disabled = true;
            break;
        case "rechazado":
            document.getElementById('Ej2').innerHTML = "CSFT-Rechazado";
            textarea2.disabled = true;
            break;
        case "observado":
            document.getElementById('Ej2').innerHTML = "CSFT-Observado";
            textarea2.disabled = false;
            break;
        default:
            document.getElementById('Ej2').innerHTML = "Pendiente";
            textarea2.disabled = true;
            break;
        }
});

let select3 = document.getElementById("calificacion3");
let textarea3 = document.getElementById("floatingTextarea3");

select3.addEventListener('change', function calificar3() {
let opcionSeleccionada3 = select3.value;
    
    switch (opcionSeleccionada3) {
        case "aprobado":
            document.getElementById('Ej3').innerHTML = "CSFT-Aprobado";
            textarea3.disabled = true;
            break;
        case "rechazado":
            document.getElementById('Ej3').innerHTML = "CSFT-Rechazado";
            textarea3.disabled = true;
            break;
        case "observado":
            document.getElementById('Ej3').innerHTML = "CSFT-Observado";
            textarea3.disabled = false;
            break;
        default:
            document.getElementById('Ej3').innerHTML = "Pendiente";
            textarea3.disabled = true;
            break;
        }
});


// let i = 1;
// for(i=1; i<4; i++){
//     let select = document.getElementById("calificacion"+parseString(i));
//     let textarea = document.getElementById("floatingTextarea"+parseString(i));

//     select.addEventListener('change', function calificar() {
//     let opcionSeleccionada = select.value;
    
//     switch (opcionSeleccionada) {
//         case "aprobado":
//             document.getElementById('Ej'+parseString(i)).innerHTML = "CSFT-Aprobado";
//             textarea.disabled = true;
//             break;
//         case "rechazado":
//             document.getElementById('Ej'+parseString(i)).innerHTML = "CSFT-Rechazado";
//             textarea.disabled = true;
//             break;
//         case "observado":
//             document.getElementById('Ej'+parseString(i)).innerHTML = "CSFT-Observado";
//             textarea.disabled = false;
//             break;
//         default:
//             document.getElementById('Ej'+parseString(i)).innerHTML = "Pendiente";
//             textarea.disabled = true;
//             break;
//         }
// });
// }
    