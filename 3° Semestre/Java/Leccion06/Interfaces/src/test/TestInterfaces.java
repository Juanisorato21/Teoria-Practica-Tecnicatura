package test;

import accesodatos.*;

public class TestInterfaces {
    public static void main(String[] args) {
        I_AccesoDatos datos = new ImplementacionMySql();
        //datos.listar();
        //imprimir(datos);
        datos = new ImplementacionOracle();
        //datos.listar();
        imprimir(datos);
    }
    
    public static void imprimir(I_AccesoDatos datos){
        datos.listar();
    }
}
