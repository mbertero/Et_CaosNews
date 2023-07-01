document.addEventListener("DOMContentLoaded", function() {
    // Adicionando fecha actual
    const obtenerFecha = () => {
      let fecha = new Date();
      let dia = fecha.getDate();
      let mes = fecha.getMonth() + 1; //Enero es 0
      let anio = fecha.getFullYear();
  
      // Formateando fecha (ej Miércoles, 25 de Noviembre de 2020)
      let fechaActual = new Intl.DateTimeFormat("es-CL", {
        weekday: "long",
        day: "numeric",
        month: "long",
        year: "numeric"
        }).format(fecha);
    
  
      // Actualiza el contenido del elemento HTML con la fecha actual
      document.getElementById('fecha-actual').textContent = fechaActual;
    }
  
    // Llama a la función obtenerFecha una vez que el contenido de la página se haya cargado completamente
    obtenerFecha();
  });