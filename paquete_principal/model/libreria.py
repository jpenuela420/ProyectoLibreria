import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import datetime


class Contenido:
    def __init__(self, sinopsis: str, analisis_ia: str):
        self.sinopsis = sinopsis
        self.analisis_ia = analisis_ia
    # Esta clase no se ha implentado


class Libro:
    def __init__(self, titulo: str, nombre_autor: str, categoria: str):
        self.titulo = titulo
        self.nombre_autor = nombre_autor
        self.categoria = categoria
        self.disponible: bool = True


class Usuario:
    lista_usuarios = []
    lista_passwords = []

    def __init__(self, nombre: str, correo: str):
        self.nombre = nombre
        self.correo = correo
        self.reservas: int = 3
        self.libro: Libro
        self.mis_libros: dict[str: Libro] = {}

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
    def __init__(self, libro: Libro, usuario: Usuario):
        self.libro = libro
        self.libros: dict[str, libro] = {}
        self.usuario = usuario
        self.libros_disponibles: dict[str, Libro] = {}

    def filtrar_libros(self, titulo: str = None, autor: str = None, categoria: str = None, disponible: bool = None):
        resultado = list(self.libros.values())
        if titulo and autor and categoria and disponible is None:
            print(f"{self.libros}")

        if titulo is not None:
            resultado = [i for i in resultado if titulo == self.libros.values()]

        elif autor is not None:
            resultado = [i for i in resultado if autor == self.libros.values()]

        elif categoria is not None:
            resultado = [i for i in resultado if categoria == self.libros.values()]

        elif disponible is not None:
            resultado = [i for i in resultado if disponible == self.libros.values()]

        return f"Los libros resultado de tu busqueda son: {resultado}"

    def agregar_disponible(self):
        self.libros = {self.libro.titulo: self.libro for self.libro in range(10)}

    def verificar_disponibilidad(self, titulo_libro: str):
        if titulo_libro in self.libros_disponibles.values():
            return True
        else:
            return False

    def hacer_resenia(self):
        pass

    def reservar_libro(self, titulo: str):
        if self.usuario.reservas > 0:
            if self.verificar_disponibilidad(titulo):
                self.usuario.mis_libros[self.libro.titulo] = self.libro
                self.reservar_libro_correo(self.libro, self.usuario, self.usuario.correo)
                self.usuario.reservas -= 1
        else:
            print(f"El usuario no tiene reservas disponibles")

    @staticmethod
    def enviar_correo(destinatario, asunto, mensaje):
        servidor_smtp = 'smtp.gmail.com'
        puerto_smtp = 587
        remitente = 'tomatolibraryeduco@gmail.com'
        password = 'ngjq zhsg zbhn clso'

        msg = MIMEMultipart()
        msg['From'] = remitente
        msg['To'] = destinatario
        msg['Subject'] = asunto

        # Adjunta el mensaje al cuerpo del correo
        msg.attach(MIMEText(mensaje, 'plain'))

        servidor = smtplib.SMTP(host=servidor_smtp, port=puerto_smtp)
        servidor.starttls()
        servidor.login(remitente, password)

        servidor.send_message(msg)
        servidor.quit()

    def reservar_libro_correo(self, libro, usuario, correo_usuario):
        tiempo_devolucion = datetime.datetime.now() + datetime.timedelta(days=10)
        mensaje = f"¡Hola {usuario}!\n\nHas reservado el libro '{libro}'.\n\nPor favor, devuélvelo antes de: {tiempo_devolucion}"
        self.enviar_correo(correo_usuario, "Reserva de libro", mensaje)

    def libro_disponible(self, libro, usuario, correo_usuario):
        mensaje = f"¡Hola {usuario}!\n\nEl libro '{libro}' que estabas esperando ya está disponible para su reserva."
        self.enviar_correo(correo_usuario, "Libro disponible", mensaje)

        libro_devuelto = "" #Aqui se almacena el nombre del libro devuelto
        usuarios_esperando = []  #Esta lista va a contener los correos de las personas que asignaron un libro a la lista de favoritos

        for usuario, correo_usuario in usuarios_esperando:
            self.libro_disponible(libro_devuelto, usuario, correo_usuario)
