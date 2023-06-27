

class Persona{ //Clase padre

    static contadorObjetosPersona = 0; //Atributo estático 
    email = 'Valor default email'; //Atributo no estático


    constructor(nombre, apellido){
        this._nombre = nombre;
        this._apellido = apellido;
        Persona.contadorObjetosPersona++;
        console.log('Se incrementa el contador: '+Persona.contadorObjetosPersona);
    }

    get nombre(){
        return this._nombre;
    }
    set nombre(nombre){
        this._nombre = nombre;
    }
    get apellido(){
        return this._apellido;
    }
    set apellido(apellido){
        this._apellido = apellido;
    }
    static saludar(){
        console.log('Saludos desde este método static');
    }
    static saludar2(persona){
        console.log(persona.nombre+' '+persona.apellido);
    }
}

class Empleado extends Persona{ //Clase hija
    constructor(nombre, apellido, departamento){
        super(nombre, apellido);
        this._departamento = departamento;
    }

    get departamento(){
        return this._departamento
    }

    set departamento(departamento){
        this._departamento = departamento;
    }

    //Sobreescritura 
    nombreCompleto(){
        return this._nombre+' '+this._apellido+', '+this._departamento;
    }

}


let persona1 = new Persona('Tomas','Gutierrez');  //creamos un objeto
console.log(persona1.nombre);
persona1.nombre = 'Julian'
console.log(persona1.nombre)
//console.log(persona1);

let persona2 = new Persona('Martina','Tomasety') //creamos otro objeto
console.log(persona2.nombre);
persona2.nombre = 'Maria Laura'
console.log(persona2.nombre)
//console.log(persona2);

let empleado1 = new Empleado('Julio','Roca','Sistemas');
console.log(empleado1);

//persona1.saludar; //--> no se puede utilizar en un objeto, si en la clase misma

//console.log(empleado1.nombreCompleto());
Persona.saludar(); 
Persona.saludar2(persona1);

Empleado.saludar();
Empleado.saludar2(empleado1);

//console.log(persona1.contadorObjetosPersona);
console.log(Persona.contadorObjetosPersona);
console.log(Empleado.contadorObjetosPersona);




