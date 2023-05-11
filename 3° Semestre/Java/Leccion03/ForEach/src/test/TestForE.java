package test;

import domain.Persona;

public class TestForE {
    public static void main(String[] args) {
        int edades [] = {5,6,8,9}; //sintaxis resumida
        for (int edad: edades) { //Sintaxis del ForEach
            System.out.println("edad = "+edad);
        }
        
        
        Persona personas[] = {new Persona('Juan'), new Persona('Marcos'),new Persona('Rodolfo')};
    
        //ForEach
         for(Persona persona: personas){
            System.out.println('Persona = '+persona);
}
    }
    

