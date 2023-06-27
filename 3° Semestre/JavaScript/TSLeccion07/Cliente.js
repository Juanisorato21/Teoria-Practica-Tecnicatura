class Cliente extends Persona{
    static contadorClientes = 0;

    constructor(nombre, apellido, edad, fecharegistro){
        super(nombre, apellido, edad); //Llamamos al contructor de la clase Persona
        this.idCliente = ++Cliente.contadorClientes;
        this.fecharegistro = fecharegistro;
    }

    get idCliente(){
        return this._idCliente;
    }

    get fecharegistro(){
        return this._fecharegistro;
    }

    set fecharegistro(fecharegistro){
        this._fecharegistro = fecharegistro;
    }

    toString(){
        return `
        ${super.toString()} 
        ${this._idCliente} 
        ${this._fecharegistro}`;
    }
}