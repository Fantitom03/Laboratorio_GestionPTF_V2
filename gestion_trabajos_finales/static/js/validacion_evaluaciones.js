let fechaEvaluacionInput = document.getElementById("id_fecha_evaluacion");
let observacionesTextarea = document.getElementById("id_observaciones");

fechaEvaluacionInput.addEventListener('change', function validarFecha() {
    let fechaEvaluacion = new Date(fechaEvaluacionInput.value);
    let today = new Date();

    if (fechaEvaluacion > today) {
        fechaEvaluacionInput.classList.add('is-invalid');
    } else {
        fechaEvaluacionInput.classList.remove('is-invalid');
    }
});

let estadoSelect = document.getElementById("id_estado");

observacionesTextarea.disabled = true;
document.getElementById('id_observaciones').innerHTML = "Pendiente";

estadoSelect.addEventListener('change', function calificar() {
    let opcionSeleccionada = estadoSelect.value;
    // Usar el ID generado por Django para el campo de observaciones
    let observacionesTextarea = document.getElementById("id_observaciones");

    switch (opcionSeleccionada) {
        case "aprobado":
            document.getElementById('id_observaciones').innerHTML = "CSFT-Aprobado";
            observacionesTextarea.disabled = true;
            break;
        case "rechazado":
            document.getElementById('id_observaciones').innerHTML = "CSFT-Rechazado";
            observacionesTextarea.disabled = true;
            break;
        case "observado":
            document.getElementById('id_observaciones').innerHTML = "CSFT-Observado";
            observacionesTextarea.disabled = false;
            break;
        default:
            document.getElementById('id_observaciones').innerHTML = "Pendiente";
            observacionesTextarea.disabled = true;
            break;
    }
});