class Contenido:
    def __init__(self, sinopsis: str, analisis_ia: str):
        self.sinopsis = sinopsis
        self.analisis_ia = analisis_ia


class Libro:
    def __init__(self, titulo: str, nombre_autor: str, categoria: str, contenido: Contenido):
        self.titulo = titulo
        self.nombre_autor = nombre_autor
        self.categoria = categoria
        self.contenido = contenido
        self.disponible: bool = True


class Usuario:
    lista_usuarios = []
    lista_passwords = []

    def __init__(self, nombre: str, correo: str):
        self.nombre = nombre
        self.correo = correo
        self.reservas: int = 3
        self.libro: Libro
        self.mis_libros: list[dict] = dict[str: Libro]

    def registrar_usuario(self, usuario: str, password: str):
        self.__class__.lista_usuarios.append(usuario)
        self.__class__.lista_passwords.append(password)


    def verificar_sesion(self, usuario: str, password: str) -> bool:
        for i in self.__class__.lista_passwords:
            if usuario == self.__class__.lista_usuarios[i] and password == self.__class__.lista_passwords[i]:
                return True
            else:
                return False

    def iniciar_sesion(self, usuario: str, password: str) -> bool:
        inicio_de_sesion = self.verificar_sesion(usuario, password)
        return inicio_de_sesion


class Biblioteca:
    def __init__(self, libros: dict[str, Libro], usuario: Usuario):
        self.libros = libros
        self.usuario = usuario
        self.libros_disponibles: dict[str, bool] = {}

    def filtrar_libros(self, titulo: str = None, autor: str = None, categoria: str = None, disponible: bool = None):
        resultado = list(self.libros.values())
        if titulo and autor and categoria and disponible is None:
            print(f"{self.libros}")

        if titulo is not None:
            resultado = [i for i in resultado]


    def verificar_disponibilidad(self, titulo_libro: str):
        pass

    def hacer_resenia(self):
        pass

    def reservar_libro(self):
        pass