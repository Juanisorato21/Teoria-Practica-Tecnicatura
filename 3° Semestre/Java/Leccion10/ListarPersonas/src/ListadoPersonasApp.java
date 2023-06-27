import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class ListadoPersonasApp {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        //Definimos la lista fuera del ciclo while
        List<Persona> personas = new ArrayList<>(); //definimos un alista como array
        //Empezamos con el menú

        var salir = false;
        while(!salir){
            mostrarMenu();
            try{
                salir = ejecutarOperacion(entrada, personas);
            }catch(Exception e) {
                System.out.println("Ocurrio un error: "+e.getMessage());
            }
            System.out.println();

        }//fin ciclo while

    }//fin método main

    private static void mostrarMenu(){
        //mostramos las opciones
        System.out.print("""
                ****** Listado de personas ******
                1. Agregar 
                2. Listar
                3. Salir 
                """);
        System.out.println("Digite una de las opciones: ");
    }//Fin método mostrar menú
    private static boolean ejecutarOperacion(Scanner entrada, List<Persona> personas){
        var opcion = Integer.parseInt(entrada.nextLine());
        var salir = false;

        //Revisamos la opcion digitada a través de un switch
        switch (opcion){
            case 1 -> { //Agregar una persona a la lista
                System.out.print("Digite el nombre: ");
                var nombre = entrada.nextLine();
                System.out.print("Digite el telefono: ");
                var tel = entrada.nextLine();
                System.out.print("Digite el email: ");
                var email = entrada.nextLine();
                //Creamos el objeto Persona
                var persona = new Persona(nombre, tel, email); //creamos un objeto de la clase persona
                //Agregamos persona a la lista
                personas.add(persona); //agregamos el objeto en la lista
                System.out.println("La lista tiene: "+personas.size()+" elementos");
            }//Fin caso 1

            case 2 -> { //Listar personas
                System.out.println("Listado de personas: ");
                //Mejoras con lambda y el método de referencia
                //personas.forEach((persona) -> System.out.println(persona));
                personas.forEach(System.out::println);
            } //Fin caso 2

            case 3 -> { //Salir del ciclo
                System.out.println("Hasta pronto...");
                salir = true;
            } //Fin caso 3
            default -> System.out.println("Opcion Incorrecta: "+opcion);

        }//Fin del switch
        return salir;
    }//Fin método ejecutarOperaciones
}//Fin de la clase ListadoPersonasApp