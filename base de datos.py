import mysql.connector
from datetime import datetime

class ConexionBD:
    def __init__(self):
        try:
            self.conexion = mysql.connector.connect(
                host="localhost",
                user="root",
                password="toor",  # ⚠️ cambia a tu contraseña real
                database="biblioteca",
                buffered=True  # 👈 ESTA LÍNEA ES CLAVE
            )
            self.cursor = self.conexion.cursor(dictionary=True, buffered=True)
            print("✅ Conexión establecida correctamente.")
        except mysql.connector.Error as e:
            print("❌ Error al conectar con la base de datos:", e)
            self.conexion = None
            self.cursor = None

    def ejecutar(self, query, valores=None, fetch=False):
        """
        Ejecuta una consulta SQL.
        Si fetch=True, devuelve los resultados del SELECT.
        """
        try:
            cursor = self.conexion.cursor(dictionary=True, buffered=True)
            cursor.execute(query, valores or ())
            if fetch:
                resultado = cursor.fetchall()
                return resultado
            else:
                self.conexion.commit()
            return cursor
        except mysql.connector.Error as e:
            print("⚠️ Error al ejecutar la consulta:", e)
            return None

    def cerrar(self):
        if self.cursor:
            self.cursor.close()
        if self.conexion:
            self.conexion.close()


# =====================================================
# Clase Libro
# =====================================================
class Libro:
    def __init__(self, titulo, autor, anio, disponible=True):
        self.__titulo = titulo
        self.__autor = autor
        self.__anio = anio
        self.__disponible = disponible

    def get_titulo(self): return self.__titulo
    def get_autor(self): return self.__autor
    def get_anio(self): return self.__anio
    def get_disponible(self): return self.__disponible
    def set_disponible(self, disponible): self.__disponible = disponible

    def guardar(self, conexion):
        conexion.ejecutar(
            "INSERT INTO libros (titulo, autor, anio, disponible) VALUES (%s, %s, %s, %s)",
            (self.__titulo, self.__autor, self.__anio, self.__disponible)
        )
        print("✅ Libro registrado correctamente.")

# =====================================================
# Clase Usuario
# =====================================================
class Usuario:
    def __init__(self, nombre, tipo):
        self.__nombre = nombre
        self.__tipo = tipo

    def get_nombre(self): return self.__nombre
    def get_tipo(self): return self.__tipo

    def guardar(self, conexion):
        conexion.ejecutar(
            "INSERT INTO usuarios (nombre, tipo) VALUES (%s, %s)",
            (self.__nombre, self.__tipo)
        )
        print("✅ Usuario registrado correctamente.")

# =====================================================
# Clase Prestamo
# =====================================================
class Prestamo:
    def __init__(self, id_usuario, id_libro, fecha_prestamo=None, fecha_devolucion=None):
        self.__id_usuario = id_usuario
        self.__id_libro = id_libro
        self.__fecha_prestamo = fecha_prestamo or datetime.now().strftime('%Y-%m-%d')
        self.__fecha_devolucion = fecha_devolucion

    def registrar(self, conexion):
        # Verificar si el usuario existe
        cursor_u = conexion.ejecutar("SELECT * FROM usuarios WHERE id = %s", (self.__id_usuario,))
        usuario = cursor_u.fetchone()
        if not usuario:
            print("❌ El usuario no existe.")
            return

        # Verificar si el libro existe y está disponible
        cursor_l = conexion.ejecutar("SELECT * FROM libros WHERE id = %s", (self.__id_libro,))
        libro = cursor_l.fetchone()
        if not libro:
            print("❌ El libro no existe.")
            return
        if not libro["disponible"]:
            print("⚠️ El libro no está disponible.")
            return

        # Registrar préstamo
        conexion.ejecutar(
            "INSERT INTO prestamos (id_usuario, id_libro, fecha_prestamo, fecha_devolucion) VALUES (%s, %s, %s, %s)",
            (self.__id_usuario, self.__id_libro, self.__fecha_prestamo, self.__fecha_devolucion)
        )

        # Cambiar estado del libro
        conexion.ejecutar("UPDATE libros SET disponible = 0 WHERE id = %s", (self.__id_libro,))
        print("📚 Préstamo registrado correctamente.")

# =====================================================
# Funciones del Menú
# =====================================================
def registrar_libro(conexion):
    titulo = input("Título del libro: ")
    autor = input("Autor: ")
    anio = input("Año de publicación: ")
    libro = Libro(titulo, autor, anio)
    libro.guardar(conexion)

def registrar_usuario(conexion):
    nombre = input("Nombre del usuario: ")
    tipo = input("Tipo de usuario (Ej: estudiante, profesor, visitante): ")
    usuario = Usuario(nombre, tipo)
    usuario.guardar(conexion)

def registrar_prestamo(conexion):
    id_usuario = input("ID del usuario: ")
    id_libro = input("ID del libro: ")
    prestamo = Prestamo(id_usuario, id_libro)
    prestamo.registrar(conexion)

def devolver_libro(conexion):
    id_prestamo = input("ID del préstamo a devolver: ")

    cursor = conexion.ejecutar("SELECT * FROM prestamos WHERE id = %s", (id_prestamo,))
    prestamo = cursor.fetchone()

    if not prestamo:
        print("❌ No se encontró el préstamo.")
        return

    if prestamo["fecha_devolucion"]:
        print("⚠️ Este préstamo ya fue devuelto.")
        return

    # Actualizar fecha de devolución y disponibilidad del libro
    fecha_actual = datetime.now().strftime('%Y-%m-%d')
    conexion.ejecutar("UPDATE prestamos SET fecha_devolucion = %s WHERE id = %s", (fecha_actual, id_prestamo))
    conexion.ejecutar("UPDATE libros SET disponible = 1 WHERE id = %s", (prestamo["id_libro"],))
    print("✅ Libro devuelto correctamente.")

def listar_libros(conexion):
    print("\n📚 Lista de Libros:")
    libros = conexion.ejecutar("SELECT * FROM libros", fetch=True)
    if not libros:
        print("No hay libros registrados.")
        return
    for libro in libros:
        estado = "Disponible ✅" if libro["disponible"] else "Prestado ❌"
        print(f'[{libro["id"]}] {libro["titulo"]} - {libro["autor"]} ({libro["anio"]}) → {estado}')

def listar_prestamos(conexion):
    print("\n📖 Lista de Préstamos:")
    prestamos = conexion.ejecutar("""
        SELECT p.id, u.nombre AS usuario, l.titulo AS libro, p.fecha_prestamo, p.fecha_devolucion
        FROM prestamos p
        JOIN usuarios u ON p.id_usuario = u.id
        JOIN libros l ON p.id_libro = l.id
    """, fetch=True)
    if not prestamos:
        print("No hay préstamos registrados.")
        return
    for p in prestamos:
        devolucion = p["fecha_devolucion"] if p["fecha_devolucion"] else "Pendiente"
        print(f'#{p["id"]} | {p["usuario"]} → {p["libro"]} | Prestado: {p["fecha_prestamo"]} | Dev: {devolucion}')

def listar_usuarios(conexion):
    print("\n👥 Lista de Usuarios:")
    usuarios = conexion.ejecutar("SELECT * FROM usuarios", fetch=True)
    if not usuarios:
        print("No hay usuarios registrados.")
        return
    for u in usuarios:
        print(f'[{u["id"]}] {u["nombre"]} - Tipo: {u["tipo"]}')


# =====================================================
# Menú Principal
# =====================================================
def menu():
    conexion = ConexionBD()
    while True:
        print("""
===== 📘 MENÚ BIBLIOTECA =====
1. Registrar libro
2. Registrar usuario
3. Registrar préstamo
4. Devolver libro
5. Listar libros
6. Listar usuarios
7. Listar préstamos
8. Salir
""")
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            registrar_libro(conexion)
        elif opcion == "2":
            registrar_usuario(conexion)
        elif opcion == "3":
            registrar_prestamo(conexion)
        elif opcion == "4":
            devolver_libro(conexion)
        elif opcion == "5":
            listar_libros(conexion)
        elif opcion == "6":
            listar_usuarios(conexion)
        elif opcion == "7":
            listar_prestamos(conexion)
        elif opcion == "8":
            conexion.cerrar()
            print("👋 ¡Hasta luego!")
            break
        else:
            print("❌ Opción inválida.")

# =====================================================
# Ejecución del programa
# =====================================================
if __name__ == "__main__":
    menu()
