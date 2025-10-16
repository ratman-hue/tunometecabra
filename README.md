# Sistema de Biblioteca en Python (Con y Sin Base de Datos)
Este proyecto es un **sistema de gestión de biblioteca** desarrollado en Python, que incluye dos
versiones:
una **de prueba (sin base de datos)** y una **versión real con conexión MySQL**.
---
## ■ Versión de Prueba (Sin Base de Datos)
Esta versión usa **listas internas** como almacenamiento temporal, simulando una base de datos.
Ideal para aprendizaje de Programación Orientada a Objetos (POO) sin necesidad de instalación de
MySQL.
### Estructura
- **Libro:** Contiene título, autor, año y disponibilidad.
- **Usuario:** Registra nombre y tipo de usuario.
- **Prestamo:** Controla la relación entre libro y usuario, con fechas de préstamo y devolución.
- **Biblioteca:** Gestiona los registros de usuarios, libros y préstamos en memoria.
### Ventajas
- Rápida ejecución, sin dependencias externas.
- Código simple y claro para entender POO.
- Perfecto para pruebas o entornos educativos.
---
## ■■ Versión Real (Conexión MySQL)
Esta versión implementa **persistencia de datos** mediante una base de datos MySQL.
Integra todas las operaciones de la versión de prueba, pero con consultas SQL reales y validaciones
más sólidas.
### Componentes
- **Clase `ConexionBD`:** Crea y administra la conexión a MySQL.
- **Clases `Libro`, `Usuario`, `Prestamo`:** Incluyen métodos para insertar y actualizar datos en tablas
reales.
- **Menú interactivo:** Permite ejecutar operaciones desde consola de forma dinámica.
### Tablas requeridas
```sql
CREATE TABLE usuarios (
id INT AUTO_INCREMENT PRIMARY KEY,
nombre VARCHAR(100),
tipo VARCHAR(50)
);
CREATE TABLE libros (
id INT AUTO_INCREMENT PRIMARY KEY,
titulo VARCHAR(150),
autor VARCHAR(100),
anio INT,
disponible BOOLEAN DEFAULT TRUE
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
```
---
## ■ Comparativa y Mejoras entre Versiones
| Aspecto | Código de Prueba (Sin BD) | Código Real (Con MySQL) |
|----------|----------------------------|--------------------------|
| **Almacenamiento** | Listas en memoria | Tablas persistentes en MySQL |
| **Persistencia** | Los datos se pierden al cerrar el programa | Los datos permanecen guardados |
| **Ejecución** | Automática, sin menú | Menú interactivo para elegir acciones |
| **Validaciones** | Limitadas (solo por lógica local) | Reales con consultas SQL (existencia,
disponibilidad) |
| **Actualización del estado del libro** | Cambia en memoria | Se actualiza en la base de datos |
| **Listados** | Muestra objetos creados en memoria | Muestra datos con consultas `JOIN` |
| **Escalabilidad** | Limitada a una sesión | Preparada para múltiples usuarios reales |
| **Código modular** | Todo contenido en una sola clase central | Dividido en clases independientes +
capa de conexión |
| **Uso educativo** | Ideal para practicar POO básica | Ideal para practicar CRUD y POO aplicada a BD
|
---
## ■■ Ejecución
### Versión de Prueba
```bash
python base de datos.py
```
### Versión Real
```bash
python base de datos prueba.py
```
> **Nota:** Antes de ejecutar la versión con MySQL, crea la base de datos `biblioteca` y ajusta las
credenciales:
```python
host="localhost",
user="root",
password="tu_contraseña",
database="biblioteca"
```
---
## ■ Mejoras Técnicas Implementadas
1. **Conexión persistente a base de datos** mediante `mysql.connector`.
2. **Consultas parametrizadas** para evitar inyección SQL.
3. **Separación de responsabilidades:** cada clase maneja su propia lógica.
4. **Sistema de menú interactivo** que facilita la navegación y evita ejecuciones automáticas.
5. **Gestión de errores** mediante excepciones (`try/except`) en conexión y consultas.
6. **Validación de existencia de registros** antes de ejecutar préstamos o devoluciones.
7. **Actualización automática** del estado de los libros al devolverlos.
8. **Consultas con `JOIN`** para mostrar información combinada de usuarios, libros y préstamos.
9. **Cierre seguro** de la conexión a la base de datos al salir del sistema.
10. **Preparación para futuras expansiones** (roles, multas, historial, etc.).
---
## ■ Conclusión
El proyecto evoluciona desde una simulación simple hasta un sistema completo con persistencia real.
Demuestra **el uso de POO, SQL y manejo de datos en Python**, siendo una excelente base para un
sistema de biblioteca profesional.
---
■ **Autor:** Proyecto educativo
■ **Lenguaje:** Python 3.x
■ **Base de Datos:** MySQL
■ **Versión:** 2.1 (comparativa mejorada)
