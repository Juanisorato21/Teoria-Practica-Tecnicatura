class Empleado extends Persona{
    static contadorEmpleados = 0;

    Constructor(nombre, apellido, edad, sueldo){
        super(nombre, apellido, edad); //llama al constructor de la clase Persona
        this.idEmpleado = ++Empleado.contadorEmpleados;
        this._sueldo = sueldo;
    }

    get idEmpleado(){
        return this._idEmpleado;
    }

    get sueldo(){
        this._sueldo;
    }
    set sueldo(sueldo){
        this._sueldo = sueldo;
    }

    toString(){
        return `${super.toString()}  //Llamamos al toString de la clase Persona
        ${this.idEmpleado} 
        ${this._sueldo}`; 
    }
}