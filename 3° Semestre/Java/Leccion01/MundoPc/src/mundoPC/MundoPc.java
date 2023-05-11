package mundoPC;

import ar.com.system2023.mundopc.*;

public class MundoPc {
    public static void main(String[] args) {
        Monitor monitorHP = new Monitor("HP",13); //Importar la clase  
        Teclado tecladoHP = new Teclado("Bluetooth", "HP");
        Raton ratonHP = new Raton("Bluetooth","HP");
        Computadora computadoraHP =new Computadora("Computadora HP", monitorHP, tecladoHP, ratonHP);
        
        //Creamos otros objetos con distintas marcas
        Monitor monitorLG = new Monitor("LG",13);   
        Teclado tecladoLG = new Teclado("Bluetooth", "LG");
        Raton ratonLG = new Raton("Bluetooth","LG");
        Computadora computadoraLG =new Computadora("Computadora LG", monitorLG, tecladoLG, ratonLG);
        
        //Creamos otros objetos con distintas marcas
        Monitor monitorSM = new Monitor("SM",13);   
        Teclado tecladoSM = new Teclado("Bluetooth", "SM");
        Raton ratonSM = new Raton("Bluetooth","SM");
        Computadora computadoraSM =new Computadora("Computadora SM", monitorSM, tecladoSM, ratonSM);
        
        //
        
        //Creamos otros objetos con distintas marcas
        Computadora computadoraVarias = new Computadora("PC diferente marcas", monitorHP, tecladoLG, ratonSM);
        
        
        
        Orden orden1 = new Orden(); //iniciamos el arreglo vacio
        Orden orden2 = new Orden(); //Una nueva lista para el objeto orden2
        
        orden1.agregarComputadora(computadoraHP);
        orden1.agregarComputadora(computadoraLG);
        orden1.agregarComputadora(computadoraSM);
        orden1.mostrarOrden();
        
        orden2.agregarComputadora(computadoraVarias);
        orden2.mostrarOrden();
    }
    
    
    //Tarea:
    //A -> Crear mas objetos de tipo computadora con todos sus elemenos
    //B -> Completar una lista con el objeto orden1 que llegue a los 10 elemntos 
    //C -> Probar de este manera los metodos al maximo rendimiento
    
}
