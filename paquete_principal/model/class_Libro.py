from paquete_principal.model.Class_Contenido import Contenido


class Libro:
    def __init__(self, titulo: str, nombre_autor: str, categoria: str, contenido: Contenido):
        self.titulo = titulo
        self.nombre_autor = nombre_autor
        self.categoria = categoria
        self.contenido = contenido
        self.disponible: bool = True

