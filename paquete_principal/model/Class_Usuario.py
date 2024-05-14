from paquete_principal.model.class_Libro import Libro


class Usuario:
    def __init__(self, nombre: str, correo: str):
        self.nombre = nombre
        self.correo = correo
        self.reservas: int = 3
        self.libro: Libro
        self.mis_libros: list[dict] = dict[str: Libro]