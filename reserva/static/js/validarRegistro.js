function validarRegistro(){
    var rut, nombre, correo, validarNombre, validarCorreo, clave, clave2;
    rut = document.getElementById("rut").value;
    nombre = document.getElementById("nombre").value;
    correo = document.getElementById("correo").value;
    clave = document.getElementById("clave").value;
    clave2 = document.getElementById("clave2").value;


    validarCorreo = /\w+@\w+\.+[a-z]/;
    validarNombre = /[a-z]/;

    if (rut == "") {
        alert("El rut esta vacio");
        return false;
    }
    if (rut.length < 8 || rut.length > 10 ) {
        alert("El rut ingresado no es valido")
        return false;
    }

    if (nombre == "") {
        alert("El nombre esta vacio");
        return false;
    }
    if (!validarNombre.test(nombre)) {
        alert("El nombre ingresado no es valido")
        return false;
    }
    if (correo == "") {
        alert("El correo esta vacio");
        return false;
    }
    if (!validarCorreo.test(correo)) {
        alert("El correo no es valido")
        return false;
    }

    if (clave == "") {
        alert("Debe ingresar una contraseña");
        return false;
    }
    if (clave2 == "") {
        alert("Debe volver a ingresar su contraseña");
        return false;
    }
    if(clave!=clave2){
        alert("Las contraseñas no coinciden")
        return false;
    }


}