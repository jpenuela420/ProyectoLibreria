import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import datetime

def enviar_correo(destinatario, asunto, mensaje):
    servidor_smtp = 'smtp.gmail.com'
    puerto_smtp = 587
    remitente = 'tomatolibraryeduco@gmail.com'
    contraseña = 'ngjq zhsg zbhn clso'

    msg = MIMEMultipart()
    msg['From'] = remitente
    msg['To'] = destinatario
    msg['Subject'] = asunto


    msg.attach(MIMEText(mensaje, 'plain'))

    servidor = smtplib.SMTP(host=servidor_smtp, port=puerto_smtp)
    servidor.starttls()
    servidor.login(remitente, contraseña)

    servidor.send_message(msg)
    servidor.quit()

def reservar_libro(libro, usuario, correo_usuario):
    tiempo_devolucion = datetime.datetime.now() + datetime.timedelta(days=7)  # Ejemplo: 7 días de plazo
    mensaje = f"¡Hola {usuario}!\n\nHas reservado el libro '{libro}'.\n\nPor favor, devuélvelo antes de: {tiempo_devolucion}"
    enviar_correo(correo_usuario, "Reserva de libro", mensaje)

def libro_disponible(libro, usuario, correo_usuario):
    # Notifica al usuario que el libro está disponible para su reserva
    mensaje = f"¡Hola {usuario}!\n\nEl libro '{libro}' que estabas esperando ya está disponible para su reserva."
    enviar_correo(correo_usuario, "Libro disponible", mensaje)


libro_devuelto = "Python for Beginners"
usuarios_esperando = [("Maria", "mjhincapie18@gmail.com")]

for usuario, correo_usuario in usuarios_esperando:
    libro_disponible(libro_devuelto, usuario, correo_usuario)
