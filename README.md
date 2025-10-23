Comparativa y Explicación de Códigos - Sistema de
Biblioteca en Python
■ Descripción General
Este documento compara dos versiones del sistema de gestión de biblioteca desarrollado en Python
con conexión a MySQL.
Ambas versiones permiten manejar **libros, usuarios y préstamos**, pero difieren en su **estructura**,
**nivel de modularidad** y **alcance funcional**.
---
■ PRIMER CÓDIGO: Versión Orientada a Clases Internas
■ Funcionalidad
Esta primera versión utiliza un enfoque totalmente orientado a objetos (POO). Las clases **Libro**,
**Usuario**, **Prestamo** y **Biblioteca** están diseñadas para trabajar **en memoria** con los datos
cargados desde la base de datos.
- La clase `Biblioteca` actúa como contenedor central de datos.
- Los métodos `listar_libros`, `listar_usuarios` y `listar_prestamos` imprimen la información
almacenada.
- No permite registrar, actualizar o eliminar registros directamente desde el código (solo lectura).
- Se enfoca en cargar y visualizar información.
■ Características Técnicas
- Uso de POO con encapsulación (`__atributos`).
- Conexión MySQL persistente mediante `mysql.connector`.
- Uso de `fetch=True` para traer los datos como diccionarios.
- Ideal para análisis y visualización de datos de la base de datos.
■■ Limitaciones
- No se pueden agregar nuevos libros, usuarios o préstamos desde el programa.
- No hay interacción dinámica con el usuario (sin menú).
- La devolución de libros solo se simula en memoria, sin reflejarse en la base de datos.
---
■ SEGUNDO CÓDIGO: Versión Interactiva con Menú
■ Funcionalidad
Esta versión amplía las capacidades del sistema para permitir **registro, préstamo y devolución de
libros**, además de listar datos.
Introduce una **interfaz por consola** para la interacción del usuario.
■ Mejoras Clave Respecto al Primer Código
| Aspecto | Primer Código | Segundo Código |
|----------|----------------|----------------|
| **Interacción** | No interactivo | Menú con opciones dinámicas |
| **Registros** | Solo lectura | Permite agregar libros, usuarios y préstamos |
| **Actualización BD** | No se actualiza la base | Modifica directamente la base (INSERT, UPDATE) |
| **Devolución de libros** | Solo lógica interna | Actualiza `fecha_devolucion` y `disponible` en la BD |
| **Modularidad** | Todo en clases | Combina POO y funciones prácticas |
| **Usabilidad** | Uso programático | Uso directo desde consola |
■ Funciones principales del Menú
1. **Registrar libro** – Inserta un nuevo libro en la tabla `libros`.
2. **Registrar usuario** – Inserta un nuevo usuario en la tabla `usuarios`.
3. **Registrar préstamo** – Crea un préstamo y actualiza el estado del libro a “no disponible”.
4. **Devolver libro** – Marca el préstamo como devuelto y vuelve a habilitar el libro.
5. **Listar libros/usuarios/préstamos** – Muestra los registros almacenados.
6. **Salir** – Cierra la conexión con MySQL de manera segura.
■ Beneficios
- Total integración con la base de datos.
- Estructura más flexible para ampliaciones.
- Ideal para un sistema de gestión real o prototipo funcional.
---
■ Conclusión
El **primer código** es un diseño inicial, útil para representar la lógica y estructura base del sistema.
El **segundo código** representa una **evolución completa**, integrando la lógica orientada a objetos
con un sistema interactivo y persistencia real de datos.
**En resumen:**
> El segundo código convierte una maqueta funcional en un sistema real de gestión de biblioteca con
base de datos MySQL.
---
✍■ **Autor:** Eduardo
■■ **Fecha:** Octubre 2025
