<?php
// Configura la conexión a la base de datos MySQL
$servername = "localhost";
$username = "root";
$password = "";
$dbname = "biblioteca";

// Conexión a la base de datos
$conn = new mysqli($localhost, $root, $root, $biblioteca);

// Verifica la conexión
if ($conn->connect_error) {
    die("Conexión fallida: " . $conn->connect_error);
}

// Obtiene los datos del formulario
$nombre = $_POST['nombre'];
$email = $_POST['email'];

// Inserta los datos en la base de datos
$sql = "INSERT INTO tabla_datos (nombre, email) VALUES ('$nombre', '$email')";

if ($conn->query($sql) === TRUE) {
    echo "Datos guardados exitosamente.";
} else {
    echo "Error al guardar los datos: " . $conn->error;
}

// Cierra la conexión
$conn->close();
?>
