//Ejercicio N° 1: Ingresar una palabra y que la imprima 10 veces.
let palabra = ("electroencefalografista"); //definimos la variable palabra

for (let i = 1; i <= 10; i++) {          //definimos i y le damos un rango
  console.log(palabra);
}
console.log('Fin ejercicio 1')

////////////////////////////////////////////////////////////////////////////////////////////////////////

//Ejercicio N° 2: Escribir una edad y muestre por pantalla todos 
//los años que ha cumplido (desde 1 hasta su edad).

let edad = 10;
for(let i = 1; i <= edad; i++){
    console.log(edad)
}
console.log('Fin ejercicio 2')

////////////////////////////////////////////////////////////////////////////////////////////////////////
//Ejercicio N°3: Escribir un número entero positivo y 
//muestre por pantalla la cuenta atrás desde ese número hasta cero separados por comas.

let num = 15;
for(let i = num; i >= 0; i--){  //>= Mayor o igual a 0
    console.log(i)
}
console.log('Fin ejercicio 3')

////////////////////////////////////////////////////////////////////////////////////////////////////////
//Ejercicio N° 4: Escribir un programa que contenga la cantidad a invertir, 
// el interés anual y el número de años, y muestre por pantalla el capital obtenido en 
// la inversión cada año que dura la inversión.

let inversion = 100000;
let interes = 55;
let años = 1;

let capital = inversion
for(let i = 1; i <=años; i++ ){
    capital += capital *(interes /100);
    console.log(capital);
}
console.log("Fin ejercicio 4")

////////////////////////////////////////////////////////////////////////////////////////////////////////
//Ejercicio N° 5: Escribir un programa que tenga un número entero y muestre por pantalla 
// un triángulo rectángulo como el de más abajo, de altura el número introducido.

let n = 8;
for(let i = 1; i <= n; i++){  
 let fila = "";
 for(let j = 1; j <= i ; j++){
    fila += "*";
 }
 console.log(fila);
}
console.log("Fin ejercicio 5")

////////////////////////////////////////////////////////////////////////////////////////////////////////
//Ejercicio N° 6: Escribir un programa que muestre por pantalla la tabla de multiplicar del 1 al 10. 
for(let i= 1; i <= 10; i++){
let fila = "";
for(let j = 1; j <= 10; j++){
fila += (i*j) + "\t";
}
console.log(fila)
}
console.log('Fin ejercicio 6')

////////////////////////////////////////////////////////////////////////////////////////////////////////

//Ejercicio N°7: Escribir un programa que tenga número entero y muestre por pantalla un 
//triángulo rectángulo como el de más abajo.

let num_7 = 20;
let fila = "";
for (let i = 0; i < num_7; i++) {
  fila += (i+1);
  console.log(fila);
}
console.log('Fin ejercicio 7')

////////////////////////////////////////////////////////////////////////////////////////////////////////

