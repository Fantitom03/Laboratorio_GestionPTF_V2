const formulario1 = document.getElementById("formulario_PTF");

formulario1.addEventListener("submit", function(e){
   let inputFecha = document.getElementById("fecha_presentacion").value;
   let fechaActual = new Date();
   let fechaForm = new Date(inputFecha);

   if(fechaForm > fechaActual){
      e.preventDefault();
      alert('Error. La fecha es posterior a la actual');
   }
});
 