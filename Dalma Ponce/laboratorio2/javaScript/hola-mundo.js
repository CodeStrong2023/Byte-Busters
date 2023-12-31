var nombre = "Dalma";
nombre = "Dalma \nFlorencia ";
var apellido = "Ponce";
//console.log(nombre + apellido);
//console.log(apellido);
console.log(nombre + apellido);
var holaMundo = "Hola mundo desde JavaScript ";
console.log(holaMundo);

// --- CLase 3 ---
// Funcion alert()  
// alert("Hola Mundo!");

var nombre = "Dalma"; // tipo str
console.log(nombre)
var numero = 1996; // tipo numerico
console.log(numero);
var objeto = {      // tipo objeto
    nombre: "Dalma",
    apellido: "Ponce",
    edad: 27
};
console.log(objeto);

// --- CLase 4 ---
/* 
Las variables son reutilizables
 */
var nombre = "Dalma"; // tipo str
console.log(typeof nombre)
nombre = 7;
console.log(typeof nombre)
nombre = 12.3;
console.log(typeof nombre)
nombre = true;
console.log(typeof nombre)

// typo boolean
var bandera = true;
console.log(bandera);

// tipo funcion  --> nos permite reutilizar codigo
function miFuncion() {
};
console.log(typeof miFuncion);

// tipo symbol
//var simbolo = Symbol("mi simbolo");
//console.log(typeof simbolo);

// tipo clase
class Persona {
    constructor(nombre, apellido) {
        this.nombre = nombre;
        this.apellido = apellido;
    }
}
console.log(typeof Persona);

// tipo undefined  --> dato asignado a variable no inicializada
var x;
console.log(typeof x);

// null --> ausencia de valor
var y = null; // null no es un tipo de dato, pero su origen es object
console.log(typeof y);

// tipo array y Empty String
var auto = ['citroen', 'Audi', 'Ford'];
console.log(typeof auto);

var z = "";
console.log(typeof z);


// Concatenar Cadenas
var nombre = "Samuel";
var apellido = ' Montes';
var nombreCompleto = nombre + " " + apellido;  // primera forma de concatenar
console.log(nombreCompleto);

var nombreCompleto2 = 'Javier' + " " + 'Martinez'; // segunda forma de concatenar
console.log(nombreCompleto2);

var juntos = nombre + 219; // Los numeros los une al string como cadena
console.log(juntos);

juntos = nombre + 78 + 17;
juntos = 78 + 17 + nombre;
console.log(juntos);

nombre += apellido; // tercer forma de concatenar
console.log(nombre);

/* let x, y;  // se pueden declarar y asignar varias variables en una linea
x = 17, y = 21;
let z = x + y; */

let _1num = 31; // no utilizar numeros al inicio para nombrar a variable

// Ejercicio 1:
// Encontrar numeros pares e impares
let numParImpar = 22;
if (numParImpar % 2 == 0) {

    console.log("El numero es par");

} else {

    console.log("El numero es impar");
}


// Ejercicio 2:
//Es mayor de edad
let edad = 18;

if (edad >= 18) {
    console.log("Es mayor de edad")

} else {

    console.log("Es menor de edad")

}


//Ejercicio 3
// Dentro de un rango
let dentroRango = 5;
let valMin = 0, valMax = 10;

if (dentroRango >= valMin && dentroRango <= valMax) {

    console.log("Se encuentra dentro de rango");

} else {

    console.log("Se encuentra fuera de rango");

}

// var, let, const

// Ya no se recomienda el usa de var, solo let
let nombre_ = "José";
console.log(nombre_);

const apellido_ = "Parco"; // las constantes no se pueden modificar

// Ejercicio 4:
// Padre puede asistir al juego de su hijo
/* let vacaciones = false, diaDescanso = true;
if (vacaciones || diaDescanso) {

    conosole.log("Puede asistir");

} else {

    console.log("No puede asistir");

} */

//Operador ternario
let resultado_ = 3 > 2 ? "verdadero" : "falso";
console.log(resultado_);
let _num = 8;
resultado_ = _num % 2 == 0 ? "Es numero par" : "Es numero impar";

//convertir String a number
let miNumero = "11";
console.log(typeof miNumero);
let edad2 = Number(miNumero); // funcion
console.log(typeof edad2);
if (isNaN(edad2)) {

    console.log("Esta variable no contiene un numero")

} else {

    if (edad2 >= 18) {

        console.log("Puede votar");

    } else {

        console.log("No puede votar");

    }
}

//Operador ternario
let resultado3 = edad2 >= 18 ? "Puede votar" : "No puede votar";
console.log(resultado3);

//Funcion isNaN --> devuelve un booleano (NaN --> Not at Number)


// Ejercicios
//Calcular estacion del año
let mes = 8;
let estacion;

switch (mes) {
    case 12:
    case 1:
    case 2:
        estacion = "verano";
        console.log("Es la estacion de: " + estacion);
        break;

    case 3:
    case 4:
    case 5:
        estacion = "otoño";
        console.log("Es la estacion de: " + estacion);
        break;

    case 6:
    case 7:
    case 8:
        estacion = "invierno";
        console.log("Es la estacion de: " + estacion);
        break;

    case 9:
    case 10:
    case 11:
        estacion = "primavera";
        console.log("Es la estacion de: " + estacion);
        break;

    default:
        estacion = "No existe mes";
        console.log(estacion);
        break;
}


//Hora del dia 
let hora = 12;
let actividad;
if (hora >= 0 && hora < 7) {

    actividad = "duermo";
    console.log("En este horario " + actividad);
} else if (hora >= 7 && hora < 11) {
    actividad = "desayuno";
    console.log("En este horario " + actividad);
} else if (hora >= 11 && hora < 14) {

    actividad = "almuerzo";
    console.log("En este horario " + actividad);
} else if (hora >= 14 && hora < 17) {

    actividad = "dormir siesta";
    console.log("En este horario " + actividad);
} else if (hora >= 17 && hora < 19) {

    actividad = "meriendo";
    console.log("En este horario " + actividad);
} else if (hora >= 19 && hora < 21) {

    actividad = "estudio";
    console.log("En este horario " + actividad);
} else if (hora >= 21 && hora <= 23) {
    actividad = "ceno";
    console.log("En este horario " + actividad);
} else {
    actividad = "Hora no existe"
    console.log(actividad);
}

