function validarLogin(){
    var correo, clave;
    correo = document.getElementById("correo").value;
    clave = document.getElementById("clave").value;


    validarCorreo = /\w+@\w+\.+[a-z]/;

    if (correo == "") {
        alert("Debe ingresar su correo");
        return false;
    }
    
    if(clave == ""){
        alert("Debe ingresar su su contraseña");
        return false;
    }
}




