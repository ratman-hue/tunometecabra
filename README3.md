Sistema de Biblioteca en Python con MySQL

Este proyecto consiste en un sistema de biblioteca hecho en Python que se conecta a una base de datos MySQL.
Permite registrar libros, usuarios y préstamos, además de listar y devolver libros.

Está hecho usando Programación Orientada a Objetos (POO) con clases que representan cada parte del sistema.

Objetivo del proyecto

El propósito es aplicar conceptos de POO (como encapsulamiento y clases relacionadas) para crear un sistema que pueda guardar y manejar información real desde una base de datos MySQL.
El programa usa un menú en consola donde se pueden realizar las operaciones principales del sistema.

Estructura del proyecto

ConexionBD: maneja la conexión con MySQL y ejecuta las consultas SQL.

Libro: representa un libro con sus atributos (título, autor, año y si está disponible).

Usuario: representa un usuario de la biblioteca (nombre y tipo).

Prestamo: gestiona los préstamos entre usuarios y libros, y permite registrar devoluciones.

Funciones del menú: permiten registrar, listar o actualizar los datos de forma interactiva.

Tablas utilizadas en MySQL
CREATE TABLE libros (
    id INT AUTO_INCREMENT PRIMARY KEY,
    titulo VARCHAR(100),
    autor VARCHAR(100),
    anio INT,
    disponible BOOLEAN
);

CREATE TABLE usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100),
    tipo VARCHAR(50)
);

CREATE TABLE prestamos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    id_usuario INT,
    id_libro INT,
    fecha_prestamo DATE,
    fecha_devolucion DATE,
    FOREIGN KEY (id_usuario) REFERENCES usuarios(id),
    FOREIGN KEY (id_libro) REFERENCES libros(id)
);

Ejecución

Para usar el sistema se necesita tener Python y MySQL instalados, además del conector:

pip install mysql-connector-python


Luego se ejecuta el archivo principal:

python base_de_datos.py

Diferencias respecto a la versión beta

La versión beta del código era una simulación sin base de datos: todo se guardaba en memoria y los datos se perdían al cerrar el programa.
Esta nueva versión mejora eso al usar una conexión real a MySQL, lo que permite guardar la información de forma permanente.

Característica	Versión Beta	Versión Final
Base de datos	No usa	Sí usa MySQL
Persistencia	No guarda datos	Guarda datos reales
Ejecución	Automática	Menú interactivo
Validaciones	Básicas	Verifica existencia de usuario/libro
Escalabilidad	Limitada	Puede ampliarse fácilmente
Conclusión

La versión final es más completa y realista.
Permite trabajar con datos reales y demuestra cómo se puede pasar de un modelo básico (versión beta) a un sistema funcional usando una base de datos relacional.

Es un buen ejemplo de cómo aplicar POO con Python y conectar el programa a MySQL.