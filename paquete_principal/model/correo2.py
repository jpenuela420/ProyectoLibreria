import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import datetime

def enviar_correo(destinatario, asunto, mensaje):
    # Configura los detalles del servidor SMTP
    servidor_smtp = 'smtp.gmail.com'
    puerto_smtp = 587
    remitente = 'tomatolibraryeduco@gmail.com'
    contraseña = 'ngjq zhsg zbhn clso'

    # Crea el objeto de mensaje Multipart
    msg = MIMEMultipart()
    msg['From'] = remitente
    msg['To'] = destinatario
    msg['Subject'] = asunto

    # Adjunta el mensaje al cuerpo del correo
    msg.attach(MIMEText(mensaje, 'plain'))

    # Inicia una conexión con el servidor SMTP
    servidor = smtplib.SMTP(host=servidor_smtp, port=puerto_smtp)
    servidor.starttls()
    servidor.login(remitente, contraseña)

    # Envía el correo electrónico
    servidor.send_message(msg)
    servidor.quit()

def reservar_libro(libro, usuario, correo_usuario):
    # Simula la reserva del libro
    tiempo_devolucion = datetime.datetime.now() + datetime.timedelta(days=7)  # Ejemplo: 7 días de plazo
    mensaje = f"¡Hola {usuario}!\n\nHas reservado el libro '{libro}'.\n\nPor favor, devuélvelo antes de: {tiempo_devolucion}"
    enviar_correo(correo_usuario, "Reserva de libro", mensaje)

# Ejemplo de uso
reservar_libro("Python for Beginners", "Juan", "kevincanizales07@gmail.com")
