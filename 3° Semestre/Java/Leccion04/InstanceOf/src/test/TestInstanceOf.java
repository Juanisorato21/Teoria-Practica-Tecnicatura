
package test;

import domain.*;


public class TestInstanceOf {
    public static void main(String[] args) {
        Empleado empleado1 = new Empleado("Sabrina",10000);
        determinarTipo(empleado1);
        empleado1 = new Gerente("Joaquin",5500,"sistemas");
        
    }
    
    public static void determinarTipo(Empleado empleado){
        if(empleado instanceof Gerente){
            System.out.println("Es de tipo Gerente");
            Gerente gerente = (Gerente)empleado;
            gerente.getDepartamento();
        }
        else if(empleado instanceof Empleado){
            System.out.println("Es de tipo Empleado");
            //Gerente gerente = (Gerente)empleado;
            //gerente.getDepartamento();
        }
        else if(empleado instanceof Object){
            System.out.println("Es de tipo Object");
        }
    }
}
