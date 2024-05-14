from paquete_principal.model.Class_Usuario import Usuario


class Libreria:
    def __init__(self, tiempo: int, libros: list[dict], usuario: Usuario):
        self.tiempo = tiempo
        self.libros = libros
        self.usuario = usuario

    def mostrar_lista(self):
        pass

    def verificar_sesion(self, usuario: str, password: str) -> bool:
        pass

    def iniciar_sesion(self, usuario: str, password: str) -> bool:
        pass

    def registrar_usuario(self, usuario: str, password: str):
        pass