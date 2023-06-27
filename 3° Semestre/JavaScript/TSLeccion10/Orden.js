

class Producto {
    constructor(idProducto, nombre, precio) {
      this.idProducto = idProducto;
      this.nombre = nombre;
      this.precio = precio;
      this.contadorProductos = 0;
    }
  
    getIdProducto() {
      return this.idProducto;
    }
  
    getNombre() {
      return this.nombre;
    }
  
    setNombre(nombre) {
      this.nombre = nombre;
    }
  
    getPrecio() {
      return this.precio;
    }
  
    setPrecio(precio) {
      this.precio = precio;
    }
  
    toString() {
      return `ID: ${this.idProducto}, Nombre: ${this.nombre}, Precio: ${this.precio}`;
    }
  }
  
  class VentasTest {
    ejecutarPrueba() {
      const producto1 = new Producto(1, "Producto 1", 10);
      const producto2 = new Producto(2, "Producto 2", 20);
      const producto3 = new Producto(3, "Producto 3", 30);
  
      const orden = new Orden(1);
      orden.agregarProducto(producto1);
      orden.agregarProducto(producto2);
      orden.agregarProducto(producto3);
      orden.mostrarOrden();
    }
  }
  
  // Ejecutar la prueba
  const ventasTest = new VentasTest();
  ventasTest.ejecutarPrueba();
  
  
  
  
  
  
  