from datetime import datetime

# =====================================================
# Clases base
# =====================================================
class Libro:
    _contador_id = 1
    def __init__(self, titulo, autor, anio, disponible=True):
        self.id = Libro._contador_id
        Libro._contador_id += 1
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
    _contador_id = 1
    def __init__(self, nombre, tipo):
        self.id = Usuario._contador_id
        Usuario._contador_id += 1
        self.__nombre = nombre
        self.__tipo = tipo

    def get_nombre(self): return self.__nombre
    def get_tipo(self): return self.__tipo

    def __str__(self):
        return f"[{self.id}] {self.__nombre} - Tipo: {self.__tipo}"


class Prestamo:
    _contador_id = 1
    def __init__(self, usuario, libro, fecha_prestamo=None, fecha_devolucion=None):
        self.id = Prestamo._contador_id
        Prestamo._contador_id += 1
        self.__usuario = usuario
        self.__libro = libro
        self.__fecha_prestamo = fecha_prestamo or datetime.now().strftime('%Y-%m-%d')
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
# Clase Biblioteca (simula la base de datos)
# =====================================================
class Biblioteca:
    def __init__(self):
        self.libros = []
        self.usuarios = []
        self.prestamos = []

    # ---------- Registrar ----------
    def registrar_libro(self, titulo, autor, anio):
        libro = Libro(titulo, autor, anio)
        self.libros.append(libro)
        print(f"✅ Libro registrado: {libro.get_titulo()}")

    def registrar_usuario(self, nombre, tipo):
        usuario = Usuario(nombre, tipo)
        self.usuarios.append(usuario)
        print(f"✅ Usuario registrado: {usuario.get_nombre()}")

    def registrar_prestamo(self, id_usuario, id_libro):
        usuario = next((u for u in self.usuarios if u.id == id_usuario), None)
        libro = next((l for l in self.libros if l.id == id_libro), None)

        if not usuario:
            print("❌ El usuario no existe.")
            return
        if not libro:
            print("❌ El libro no existe.")
            return
        if not libro.get_disponible():
            print("⚠️ El libro no está disponible.")
            return

        libro.set_disponible(False)
        prestamo = Prestamo(usuario, libro)
        self.prestamos.append(prestamo)
        print(f"📚 Préstamo registrado: {usuario.get_nombre()} → {libro.get_titulo()}")

    def devolver_libro(self, id_prestamo):
        prestamo = next((p for p in self.prestamos if p.id == id_prestamo), None)
        if not prestamo:
            print("❌ No se encontró el préstamo.")
            return
        prestamo.devolver()

    # ---------- Listar ----------
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
# Ejecución automática (sin conexión, sin menú)
# =====================================================
if __name__ == "__main__":
    biblioteca = Biblioteca()

    # 1️⃣ Registrar usuarios
    biblioteca.registrar_usuario("Ana López", "Estudiante")
    biblioteca.registrar_usuario("Luis Pérez", "Profesor")
    biblioteca.registrar_usuario("María Torres", "Visitante")

    # 2️⃣ Registrar libros
    biblioteca.registrar_libro("Cien años de soledad", "Gabriel García Márquez", 1967)
    biblioteca.registrar_libro("El Principito", "Antoine de Saint-Exupéry", 1943)
    biblioteca.registrar_libro("1984", "George Orwell", 1949)

    # 3️⃣ Registrar préstamos
    biblioteca.registrar_prestamo(1, 1)
    biblioteca.registrar_prestamo(2, 2)

    # 4️⃣ Devolver un libro
    biblioteca.devolver_libro(1)

    # 5️⃣ Listar todo
    biblioteca.listar_usuarios()
    biblioteca.listar_libros()
    biblioteca.listar_prestamos()

    print("\n🔚 Ejecución finalizada (sin base de datos).")
