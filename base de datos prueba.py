import mysql.connector
from datetime import datetime

# =====================================================
# Clase de Conexión a la Base de Datos
# =====================================================
class ConexionBD:
    def __init__(self):
        try:
            self.conexion = mysql.connector.connect(
                host="localhost",
                user="root",
                password="toor",  # Cambiar si tu contraseña es diferente
                database="biblioteca",
                buffered=True
            )
            self.cursor = self.conexion.cursor(dictionary=True, buffered=True)
            print("✅ Conexión establecida correctamente.")
        except mysql.connector.Error as e:
            print("❌ Error al conectar con la base de datos:", e)
            self.conexion = None
            self.cursor = None

    def ejecutar(self, query, valores=None, fetch=False):
        try:
            cursor = self.conexion.cursor(dictionary=True, buffered=True)
            cursor.execute(query, valores or ())
            if fetch:
                return cursor.fetchall()
            self.conexion.commit()
            return cursor
        except mysql.connector.Error as e:
            print("⚠️ Error en la consulta:", e)
            return None

    def cerrar(self):
        if self.cursor:
            self.cursor.close()
        if self.conexion:
            self.conexion.close()

# =====================================================
# Clases base
# =====================================================
class Libro:
    def __init__(self, id, titulo, autor, anio, disponible=True):
        self.id = id
        self.__titulo = titulo
        self.__autor = autor
        self.__anio = anio
        self.__disponible = disponible

    def get_titulo(self): return self.__titulo
    def get_autor(self): return self.__autor
    def get_anio(self): return self.__anio
    def get_disponible(self): return self.__disponible
    def set_disponible(self, disponible): self.__disponible = disponible

    def __str__(self):
        estado = "Disponible ✅" if self.__disponible else "Prestado ❌"
        return f"[{self.id}] {self.__titulo} - {self.__autor} ({self.__anio}) → {estado}"


class Usuario:
    def __init__(self, id, nombre, tipo):
        self.id = id
        self.__nombre = nombre
        self.__tipo = tipo

    def get_nombre(self): return self.__nombre
    def get_tipo(self): return self.__tipo

    def __str__(self):
        return f"[{self.id}] {self.__nombre} - Tipo: {self.__tipo}"


class Prestamo:
    def __init__(self, id, usuario, libro, fecha_prestamo, fecha_devolucion=None):
        self.id = id
        self.__usuario = usuario
        self.__libro = libro
        self.__fecha_prestamo = fecha_prestamo
        self.__fecha_devolucion = fecha_devolucion

    def devolver(self):
        if self.__fecha_devolucion:
            print("⚠️ Este préstamo ya fue devuelto.")
        else:
            self.__fecha_devolucion = datetime.now().strftime('%Y-%m-%d')
            self.__libro.set_disponible(True)
            print(f"✅ Libro devuelto correctamente: {self.__libro.get_titulo()}")

    def __str__(self):
        fecha_dev = self.__fecha_devolucion if self.__fecha_devolucion else "Pendiente"
        return f"#{self.id} | {self.__usuario.get_nombre()} → {self.__libro.get_titulo()} | Prestado: {self.__fecha_prestamo} | Dev: {fecha_dev}"

# =====================================================
# Clase Biblioteca (usa la base de datos)
# =====================================================
class Biblioteca:
    def __init__(self, conexion):
        self.conexion = conexion
        self.libros = []
        self.usuarios = []
        self.prestamos = []

    def cargar_datos(self):
        # Cargar usuarios
        usuarios_bd = self.conexion.ejecutar("SELECT * FROM usuarios", fetch=True)
        for u in usuarios_bd:
            self.usuarios.append(Usuario(u["id"], u["nombre"], u["tipo"]))

        # Cargar libros
        libros_bd = self.conexion.ejecutar("SELECT * FROM libros", fetch=True)
        for l in libros_bd:
            self.libros.append(Libro(l["id"], l["titulo"], l["autor"], l["anio"], l["disponible"]))

        # Cargar préstamos
        prestamos_bd = self.conexion.ejecutar("SELECT * FROM prestamos", fetch=True)
        for p in prestamos_bd:
            usuario = next((u for u in self.usuarios if u.id == p["id_usuario"]), None)
            libro = next((l for l in self.libros if l.id == p["id_libro"]), None)
            if usuario and libro:
                self.prestamos.append(Prestamo(p["id"], usuario, libro, p["fecha_prestamo"], p["fecha_devolucion"]))

    def listar_libros(self):
        print("\n📚 Lista de Libros:")
        if not self.libros:
            print("No hay libros registrados.")
            return
        for l in self.libros:
            print(l)

    def listar_usuarios(self):
        print("\n👥 Lista de Usuarios:")
        if not self.usuarios:
            print("No hay usuarios registrados.")
            return
        for u in self.usuarios:
            print(u)

    def listar_prestamos(self):
        print("\n📖 Lista de Préstamos:")
        if not self.prestamos:
            print("No hay préstamos registrados.")
            return
        for p in self.prestamos:
            print(p)

# =====================================================
# Ejecución automática
# =====================================================
if __name__ == "__main__":
    conexion = ConexionBD()
    if conexion.conexion:
        biblioteca = Biblioteca(conexion)
        biblioteca.cargar_datos()
        biblioteca.listar_usuarios()
        biblioteca.listar_libros()
        biblioteca.listar_prestamos()
        conexion.cerrar()
        print("\n🔚 Ejecución finalizada (con base de datos).")
