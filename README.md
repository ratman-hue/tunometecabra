Sistema de Biblioteca en Python con MySQL
🧩 Descripción del proyecto

Este proyecto consiste en un sistema de biblioteca desarrollado en Python que se conecta a una base de datos MySQL.
Permite registrar libros, usuarios y préstamos, además de listar y devolver libros desde un menú interactivo en consola.

El código está basado en Programación Orientada a Objetos (POO), utilizando clases que representan las distintas partes del sistema.

🎯 Objetivo del proyecto

El objetivo principal es aplicar conceptos de POO (como encapsulamiento y relaciones entre clases) para construir un sistema funcional que maneje información real a través de una base de datos MySQL.

De esta forma, el programa puede guardar, consultar y actualizar datos de manera persistente.

🏗️ Estructura del proyecto

1. ConexionBD
Encargada de manejar la conexión con MySQL y ejecutar las consultas SQL.

2. Libro
Representa un libro con sus atributos: título, autor, año y disponibilidad.

3. Usuario
Define a un usuario de la biblioteca con su nombre y tipo (por ejemplo, estudiante o profesor).

4. Prestamo
Gestiona los préstamos entre usuarios y libros, además de permitir registrar devoluciones.

5. Funciones del menú
Permiten registrar, listar y actualizar datos mediante opciones interactivas desde la consola.

🗄️ Tablas utilizadas en MySQL
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

⚙️ Ejecución
Requisitos

Python 3.x

MySQL instalado y en ejecución

Conector de MySQL para Python

Instalación del conector:

pip install mysql-connector-python

Ejecución del programa

Desde la consola, ejecuta:

python base_de_datos.py

🔁 Diferencias respecto a la versión beta
Característica	Versión Beta	Versión Final
Base de datos	No usa	Usa MySQL
Persistencia	No guarda datos	Guarda datos reales
Ejecución	Automática	Menú interactivo
Validaciones	Básicas	Verifica existencia de usuario/libro
Escalabilidad	Limitada	Fácil de ampliar

La versión final reemplaza el sistema en memoria por una base de datos real, lo que permite guardar información de forma permanente y mejorar la organización y validación de los datos.

🧠 Conclusión

La versión final del sistema es más completa y realista.
Permite trabajar con datos reales y demuestra cómo se puede pasar de un modelo simple a un sistema funcional con base de datos relacional, aplicando principios de POO en Python.
