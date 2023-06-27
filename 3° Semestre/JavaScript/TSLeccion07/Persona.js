class Persona{
    static contadorPersona = 0; //Vairable statica

    //Método Construcotr
    contrucotr(nombre, apellido, edad){
        this._idPersona = ++Persona.contadorPersona;
        this._nombre = nombre;
        this._apellido = apellido;
        this._edad = edad;
    }

 // get -> obtener
    get idPersona(){
        return this._idPersona;
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
        return this._apellido;
    }

    get edad(){
        return this.edad;
    }
    set edad(edad){
        return this.edad;
    }

    toString(){
        return `
        ${this._idPersona}
        ${this._nombre}
        ${this._apellido}
        ${this.edad}`;
    }


}