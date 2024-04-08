class Contenido():
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
        return

    def verificar_sesion(self, usuario: str, password: str) -> bool:
        for i in self.__class__.lista_passwords:
            if usuario == self.__class__.lista_usuarios[i] and password == self.__class__.lista_passwords[i]:
                return True
            else:
                return False

    def iniciar_sesion(self, usuario: str, password: str) -> bool:
        inicio_de_sesion = self.verificar_sesion(usuario, password)
        return inicio_de_sesion


class Libreria:
    def __init__(self, tiempo: int, libros: list[dict], usuario: Usuario):
        self.tiempo = tiempo
        self.libros = libros
        self.usuario = usuario

    def mostrar_lista(self):
        pass