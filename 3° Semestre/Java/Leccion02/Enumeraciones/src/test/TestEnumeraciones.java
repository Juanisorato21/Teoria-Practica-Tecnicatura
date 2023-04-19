
package test;

import enumeraciones.Continentes;
import enumeraciones.Dias;


public class TestEnumeraciones {
    public static void main(String[] args) {
        // EJERCITACION N°1 DIAS
       //-> System.out.println("Dia 1: "+Dias.LUNES);
       //-> indicarDiaSemana(Dias.JUEVES); //Las enumeraciones se tratan como cadenas
        //Ahora no se deben utilizar comillas, se accede a través de el operador de punto
        
        // EJERCITACION N°2 CONTINENTES
        // Imprimimos los continentes sus paises y la cantidad de habitantes
        System.out.println("Continentes No. 1: "+Continentes.AFRICA);
        System.out.println("No. de paises en el 1er. continente: "+Continentes.AFRICA.getHabitantes());
        System.out.println("************************************************************************************************");
        System.out.println("Continentes No. 2: "+Continentes.EUROPA);
        System.out.println("No. de paises en el 2do. continente: "+Continentes.EUROPA.getHabitantes());
        System.out.println("************************************************************************************************");
        System.out.println("Continentes No. 3: "+Continentes.ASIA);
        System.out.println("No. de paises en el 3ro. continente: "+Continentes.ASIA.getHabitantes());
        System.out.println("************************************************************************************************");
        System.out.println("Continentes No. 4: "+Continentes.AMERICA);
        System.out.println("No. de paises en el 4to. continente: "+Continentes.AMERICA.getHabitantes());
        System.out.println("************************************************************************************************");
        System.out.println("Continentes No. 5: "+Continentes.OCEANIA);
        System.out.println("No. de paises en el 5to. continente: "+Continentes.OCEANIA.getHabitantes());
    }
    
    
    private static void indicarDiaSemana(Dias dias){
        switch(dias){
            case LUNES:
                System.out.println("Primer día de la semana");
                break;
            case MARTES:
                System.out.println("Segundo día de la semana");
                break;
            case MIERCOLES:
                System.out.println("Tercer día de la semana");
                break;
            case JUEVES:
                System.out.println("Cuarto día de la semana");
                break;
            case VIERNES:
                System.out.println("Quinto día de la semana");
                break;
            case SABADO:
                System.out.println("Sexto día de la semana");
                break;
            case DOMINGO:
                System.out.println("Septimo día de la semana");
                break;
            default:
                System.out.println("El valor proporcionado no es valido");
        }
    }
}
