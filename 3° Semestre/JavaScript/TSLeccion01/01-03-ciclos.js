// While : mientras 
let contador = 0; //creamos la variable contador
while(contador < 10){
    console.log(contador);
    contador++;
}
console.log('Fin del ciclo while')

////////////////////////////////////////////////////////////////////////////////////////////////////////
//Do While: 
//se ejecuta todo el codigo y luego la condicion 

let conteo = 0;
do{
    console.log(conteo);
    conteo++;
}while(conteo < 10);
console.log('Fin del ciclo DoWhile');

////////////////////////////////////////////////////////////////////////////////////////////////////////
//For
for(let contando = 0;contando < 10 ;contando++){
    console.log(contando);
}
console.log('Fin del ciclo For');

////////////////////////////////////////////////////////////////////////////////////////////////////////
//Palabra reservada break: rompe la estructura
//Ejercicio para encontrar solo el primer numero par
for(let contando = 0 ; contando <= 10; contando++){
    if(contando % 2 == 0){
        console.log(contando); //Muestra todos los pares
        break; // solo muestra el primer numero par
    }
}
console.log('Termina ciclo al encontrar el primer numero par')
////////////////////////////////////////////////////////////////////////////////////////////////////////
//Palabra reservada Continue y uso de etiquetas Labels: 
inicio:
for(let contando = 0; contando <10; contando++){
    if(contando % 2!=0){ //si es impar lo saltea o ignora
        continue inicio; //esto va a continuar a la siguiente iteracion
    }
    console.log(contando);
}
console.log('Termina ciclo')

////////////////////////////////////////////////////////////////////////////////////////////////////////
//Ejercitacion 

//Ciclo While
//A1. Buscar numeros pares con ciclo while
let contador_par = 0;
while (contador_par <10){
    contador_par++;
    if(contador_par %2==0){
        console.log(contador_par)
    }
}
console.log('Termina ejercicio A1: numeros par')

//A2. Buscar numeros impar con ciclo while
let contador_impar =0;
while(contador_impar <10){
    contador_impar++;
    if(contador_impar %2!=0){
        console.log(contador_impar);
    }
}
console.log('Termina ejercicio A2: numeros impar');

//B1. Buscar numeros par con ciclo do while
let conteo_par = 0;
do{
    conteo_par++;
    if(conteo_par %2 == 0){
        console.log(conteo_par);
    };
    
}while(conteo_par <10);
console.log('Termina ejercicio B1: numeros par')

//B2. Buscar numeros impar con ciclo do while
let conteo_impar = 0;
do{
    conteo_impar++;
    if(conteo_impar %2 !=0){
        console.log(conteo_impar);
    };

}while(conteo_impar <10)
console.log('Termina ejercicio B1: numeros impar')

//C1. Buscar numeros par con ciclo for
for(let contando = 0 ; contando <= 10; contando++){
    if(contando % 2 == 0){
        console.log(contando); //Muestra todos los pares
    }
}
console.log('Termina ejercicio C1: numeros par')

//C2. Buscar numeros impar con ciclo for
for(let contando = 0; contando <10; contando++){
    if(contando % 2!=0){
        console.log(contando); //Muestra todos los impares
    }
}
console.log('Termina ejercicio C2: numeros impares')


