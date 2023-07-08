//Que botón buscar limpie el formulario
$(document).ready(function(){
    $('#search-form').click(function(){
        $('#busqueda').val('');
    });
});

//Confirmar la eliminacion de la noticia 

function confirmDelete() {
    return confirm('¿Estás seguro de que deseas eliminar esta noticia?');
}


//Validaciones del formulario con JQuery


//Validación 1 (submit):
//Al presionar submit, se debe validar que los campos no estén vacíos


$(document).ready(function(){
    $('#submit-form').click(function(){
        //rut
        let rut = $('#rut-form').val();
        //nombre completo
        let nombre = $('#nombre-form').val();
        //email
        let email = $('#email-form').val();
        //contraseña 1
        let pass1 = $('#pass-form1').val();
        //contraseña 2
        let pass2 = $('#pass-form2').val();


        if (rut.length == 0){
            alert('El campo rut no puede estar vacío');
        } else if (nombre.length == 0){
            alert('El campo nombre no puede estar vacío');
        } else if (email.length == 0){
            alert('El campo email no puede estar vacío');
        } else if (pass1.length == 0){
            alert('El campo contraseña no puede estar vacío');
        } else if (pass2.length == 0){
            alert('El campo contraseña no puede estar vacío');
        }
    });
});






//Validación 2 (rut):
//1. Que el rut no esté vacío
//2. Que el rut tenga un largo mínimo de 9 caracteres
//3. Cambiar el color del borde del input a rojo si no cumple con las condiciones anteriores


$(document).ready(function(){
    $('#rut-form').keyup(function(){
        let rut = $('#rut-form').val();
        if (rut.length == 0){
            $('#rut-form').css('border-color', 'red');
        } else if (rut.length < 9){
            $('#rut-form').css('border-color', 'red');
        } else if (rut.length > 9){
            $('#rut-form').css('border-color', 'red');
        } else if (rut.length == 9){
            $('#rut-form').css('border-color', 'green');
        }
    });
});




//Validación 3 (nombre):
//1. Que el nombre no esté vacío
//2. Que el nombre tenga un largo mínimo de 3 caracteres
//3. Cambiar el color del borde del input a rojo si no cumple con las condiciones anteriores
//4. Que sólo se puedan ingresar letras


$(document).ready(function(){
    $('#nombre-form').keyup(function(){
        let nombre = $('#nombre-form').val();
        if (nombre.length == 0){
            $('#nombre-form').css('border-color', 'red');
        } else if (nombre.length < 3){
            $('#nombre-form').css('border-color', 'red');
        } else if (nombre.length > 3){
            $('#nombre-form').css('border-color', 'green');
        }
    });
});




//Validación 4 (email):
//1. Que el email no esté vacío
//2. Que el email tenga un largo mínimo de 3 caracteres
//3. Que contenga un @ y  un .
//4. Cambiar el color del borde del input a rojo si no cumple con las condiciones anteriores


$(document).ready(function(){
    $('#email-form').keyup(function(){
        let email = $('#email-form').val();
        if (email.length == 0){
            $('#email-form').css('border-color', 'red');
        } else if (email.length < 3){
            $('#email-form').css('border-color', 'red');
        } else if (email.length > 3){
            $('#email-form').css('border-color', 'green');
        }


        if (email.includes('@') && email.includes('.')){
            $('#email-form').css('border-color', 'green');
        } else {
            $('#email-form').css('border-color', 'red');
        }
    });
});

// Api

