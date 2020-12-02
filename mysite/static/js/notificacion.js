//Titulo de la notificación
Push.create("Mobike App Web", {

    //Texto del cuerpo de la notificación
    body: "Leonardo Farkas se culió a Daniela Chavez",

    icon: "../img/Logotipo.png", //Icono de la notificación
    timeout: 6000, //Tiempo de duración de la notificación


    onClick: function() {
        //Función que se cumple al realizar clic cobre la notificación
        window.location = "localhost:8000"; //Redirige a la siguiente web
        this.close(); //Cierra la notificación
    },
});
