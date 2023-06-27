import java.sql.SQLOutput;
import java.util.Scanner;

public class CalculadoraUTN {

    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        while (true){ //Ciclo infinito
            System.out.println("******* Aplicacion Calculadora *******");
            mostrarMenu(); //Llamamos al metodo

            try{
                var operacion = Integer.parseInt(entrada.nextLine());
                if(operacion >= 1 && operacion <= 4){

                    ejercutarOperacion(operacion, entrada);
                } //Fin if
                else if (operacion == 5) {
                    System.out.println("Hasta pronto");
                    System.out.println("© CalculadoraUTN. Todos los derechos reservados a Juan S. ");
                    break; //Rompe el ciclo while
                } //Fin else-if
                else{
                    System.out.println("Opción erronea: "+operacion);
                } //Fin else
                //Imprimimos un salta de linea antes de repetir el menú
                System.out.println();

            } catch (Exception e){ //fin del try, comienzo del catch
                System.out.println("Ocurrio un error: "+e.getMessage());
                System.out.println();
            } //fin del catch



        } //fin while


    } //Fin main

    private static void mostrarMenu(){ //Funcion mostrar menú
        //Mostramos el menú
        System.out.println("""
                1. Sumar
                2. Restar
                3. Multiplicacion
                4. Division
                5. Salir
                """);
        System.out.print("Operación a realizar?: ");
    }// fin metodo mostrar menu

    private static void ejercutarOperacion(int operacion, Scanner entrada){
        System.out.print("Digite el valor para el operando1: ");
        var operando1 = Double.parseDouble(entrada.nextLine());
        System.out.print("Digite el valor para el operando2: ");
        var operando2 = Double.parseDouble(entrada.nextLine());

        Double resultado;
        switch(operacion){
            case 1 -> { //Suma
                resultado = operando1 + operando2;
                System.out.println("Resultado de la suma: "+resultado);
            }
            case 2 -> { //Resta
                resultado = operando1 - operando2;
                System.out.println("Resultado de la resta: "+resultado);
            }
            case 3 -> { //Multiplicación
                resultado = operando1 * operando2;
                System.out.println("Resultado de la multiplicacion es: "+resultado);
            }
            case 4 -> { //División
                resultado = operando1 / operando2;
                System.out.println("Resultado de la division es: "+resultado);
            }
            default -> System.out.println("Opción erronea"+operacion);

        } // Fin switch
    } //Fin metodo ejecutar operacion


} //Fin class



// Try catch -> para las excepciones
// While -> ciclo infinito, para terminar una operacion y seguir
// If else -> para delimitar las opciones: si es mayor a 1 y menor a 4 entra al menu, si no da ,ensaje de error
// Switch -> elegir la opcion
