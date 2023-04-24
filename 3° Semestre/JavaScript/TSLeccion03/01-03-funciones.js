
miFuncion(8, 2); // Esto se lo conoce como hosting se puede llamar antes de definirla.

function miFuncion(a, b) {

   console.log("Sumamos: "+ (a + b));
   //return a + b;
}

//Llamamos la funcion.
miFuncion(5, 4);

let resultado = miFuncion(6, 7);
console.log(resultado);

//#########################################################################################################
//Declaramos una funcion de tipo expresion o anonima
let x = function(a, b){return a+b}; //necesita cierre con ; (punto y coma)

resultado = x(5 , 6) //al llamar se pone la variable y parentesis
console.log("El resultado es: "+ resultado);


//#########################################################################################################
//Funciones de tipo self y invoking
//(function(a, b){
    //console.log('Ejecutando la funcion: '(+a+b));
//})(9 , 6);


console.log(typeof miFuncion);
function miFuncionDos(a, b){
    console.log(arguments)
    console.log(arguments.length)

}

miFuncionDos(8, 7, 6, 4)
//################################################################################################

//toString
var miFuncionTexto = miFuncionDos.toString();
console.log(miFuncionTexto);

//################################################################################################
//Funciones flecha
const sumarFuncionFlecha = (a , b ) => a + b;
resultado = sumarFuncionFlecha(8, 2); //Asignamos el valor a una variable.
console.log(resultado);

let sumar = function(a = 4, b = 8){
    console.log(arguments[0]); // Muestra el parametro de: a
    console.log(arguments[1]); //Muestra el parametro de: b
    console.log(arguments[2]);
    return a + b;
}
resultado = sumar(3, 6);
console.log(resultado);

//Sumar todos los argumentos
let respuesta = sumarTodo(5, 4, 13, 10, 9);
console.log(respuesta);
function sumarTodo(){
    let suma = 0;
    for(let i = 0; i < arguments.length; i++){
        suma += arguments[i]; //arguments es para arreglos.
    }
    return suma;
}


//#########################################################################################
//Tipo primitivos
let g = 10;
function cambiarValor(a){ //paso por valor
    a = 20
}
cambiarValor(g);
console.log(g)

//Paso por rferencia
const persona = {
    nombre: 'Mateo',
    apellido: 'Magallanes'
}

function cambiarValorObjeto(p1){
    p1.nombre = 'Ignacio'
    p1.apellido = 'Mondino'
}
cambiarValorObjeto(persona);
console.log(persona)

