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