let x = 10; //Variable de tipo primitiva
console.log(x.length);
console.log('Tipos primitivos');
//###############################################################################################
//Objeto
let persona = {
    nombre: 'Carlos',
    apellido: 'Villalon',
    email: 'carlitosvilla@mail.com',
    edad: 30,
    idioma: 'ES',
    get lang(){
        return this.idioma.toUpperCase();  //Convierte las minusculas a mayusculas
    },
    set lang(lang){
        this.idioma = lang.toUpperCase();
    },
    nombreCompleto: function(){ //método o funcion en JS 
        return this.nombre+' '+this.apellido;
    },
    datosCompletos: function(){ //Segunda funcion
        return this.nombre+' '+this.apellido+' '+this.email;
    }, 
    get nombreEdad(){ //Este es el metodo get
        return 'El nombre es: '+ this.nombre+',  edad: '+this.edad
    }
   
    
}


//Mostramos los datos del objeto
console.log(persona);
//Mostramos datos especifico del objeto
console.log(persona.nombre);
console.log(persona.email)

console.log(persona.nombreCompleto());
console.log(persona.datosCompletos())
console.log('Ejecutando con un objeto')

//###############################################################################################
//Creamos un segundo objeto
let persona2 = new Object(); //Debe crear un nuevo objeto en memoria
persona2.nombre = 'Juliana';
persona2.apellido = 'Escudero';
persona2.direccion = 'Esmeralda 125'
persona2.telefono = 2604001122
console.log('Creamos un nuevo objeto')
//###############################################################################################
console.log(persona2);


console.log(persona['apellido'])

//for in accedemos al objeto como si fuera un arreglo
for(propiedad in persona){
    console.log(propiedad)
    console.log(persona[propiedad])
}


// persona.apellido = 'Aguilera' --> //Cambiamos dinamicamente un valor del objeto
// delete persona.apellido --> eliminamos la propiedad (apellido) y el valor ('Aguilera)
console.log(persona)


//Distintas formas de imprimir un objeto

//--> Numero 1: la más sencilla: concatenar cada valor de cada propiedad.
console.log('Distintas formas de imprimir un objeto: Forma 1')

console.log(persona.nombre+' , '+persona.edad);

//--> Numero 2: a travez del ciclo for in
console.log('Distintas formas de imprimir un objeto: Forma 2')

for(nombrePropiedad in persona){
    console.log(persona[nombrePropiedad]);
}

//--> Numero 3: La función Object.values()
console.log('Distintas formas de imprimir un objeto: Forma 3')

let personaArray = Object.values(persona);
console.log(personaArray);


//--> Numero 4: Utilizamos el método JSON.stringify
console.log('Distintas formas de imprimir un objeto: Forma 4')

let personaString = JSON.stringify(persona)
console.log(personaString);


console.log('Comenzamos a utilizar el metodo get');
console.log(persona.nombreEdad)

console.log('Comenzamos con el metodo get para idiomas');
persona.lang = 'en';
console.log(persona.lang);



 //############################################################################################################

function Persona3(nombre, apellido, email){
    this.nombre = nombre;
    this.apellido = apellido;
    this.email = email;
    this.nombreCompleto = function(){
        return this.nombre+' '+this.apellido
    }
}
let padre = new Persona3('Leo', 'Miranda', 'LMiranda@mail.com');
padre.telefono = '2604842588'
console.log(padre);
console.log(padre.nombreCompleto());


let madre = new Persona3('Laura','Contrera','ContreraL@mail.com');
console.log(madre);
console.log(madre.telefono) //La propiedad no esta definida
console.log(madre.nombreCompleto());


//Diferentes formas de crear objetos
//Caso N°1
let miObjeto = new Object(); //Esta es una opcion formal
//Caso N°2
let miObjeto2 = {}; //Esta opcion es breve y recomendada

//Caso String 1 
let miCaddena1 = new String('Hola')
//Caso String 2
let miCaddena2 = 'HOLA'; //Esta la sintaxis simplificada y recomendada

//Caso 1 con numero 
let miNumero = new Number(1); //Esta forma no recomendable
//Caso 2 con numero
let miNumero2 = 1; //Sintaxis recomendada

//Caso 1 boolean
let miBoolean1 = new Boolean(true); //Forma1
//Caso 2 boolean
let miBolean2 = false; //Sintaxis recomendada

//Caso 1 Arreglos
//let miArreglo = new Array(); //Forma1
//Caso 2 Arreglos
let miArreglo = [];

//Caso 1 function
let miFuncion1 = new function(){}; //Todo despues de new es considerado objeto
//Caso 2 function
let miFuncion2 = function(){}; //Notacion simplificada y recomandada

//Uso de prototype
Persona3.prototype.telefono = '2604887799'
console.log(padre);
console.log(madre.telefono);
madre.telefono = '5492604887799'
console.log(madre.telefono);

//Uso de call
let persona4 = { //-> objeto
    nombre: 'Juan',
    apellido: 'Perez',
    nombreCompleto2: function(titulo, telefono){
        return titulo+': '+this.nombre+' '+this.apellido+' '+telefono;
       // return this.nombre+' '+this.apellido;
    }
}

let persona5  = { 
    nombre: 'Carlos',
    apellido: 'Marculi'
}

console.log(persona4.nombreCompleto2('Lic.','5492604001122'));

console.log(persona4.nombreCompleto2.call(persona5,'Ing.','5492604779988'));

//Metodo Apply
let arreglo = ['Ing.','5492604585859'];
console.log(persona4.nombreCompleto2.apply(persona5,arreglo));



