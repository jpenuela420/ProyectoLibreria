from paquete_principal.model import libreria
def main():
    l1 = libreria.Libro("el principito", "jovany vasquez", "aventura")
    l2 = libreria.Libro("la princesa y el sapo", "samanta espinal", "romance")
    l3 = libreria.Libro("el rayo mcqueen", "jh de la cruz", "accion")
    ln = [l1,l2,l3]
    usuario_nombre = input("Ingrese un nombre de usuario:")
    usuario_correo = input("Ingrese una direccion de correo:")
    usuario = libreria.Usuario(usuario_nombre, usuario_correo)
    password = input("Ingrese una contraseña:")
    libreria.Usuario.registrar_usuario(usuario, usuario_nombre, password)
    opcion1 = int(input("Ingrese 1 para iniciar sesion:"))
    if opcion1 == 1:
        usuario_nombre = input("Ingrese su nombre de usuario:")
        password = input("Ingrese su contraseña:")
    else:
        exit()
    libreria.Usuario.iniciar_sesion(usuario, usuario_nombre, password)
    biblioteca = libreria.Biblioteca(ln, usuario)
    print(f"Bienvenido esta es la biblioteca Tomato Library")
    print(f"- Para consultar nuestros libros presione 1")
    print(f"- Para filtrar los libros por titulo, autor o categoria presione 2")
    print(f"- Para reservar un libro presione 3")
    opcion = int(input("ingrese una opción:"))
    if opcion == 1:
        biblioteca.agregar_disponible()
    elif opcion == 2:
        titulo = input("Ingrese un titulo:") or None
        categoria = input("Ingrese una categoria:") or None
        autor = input("Ingrese el nombre de un autor:") or None
        libreria.Biblioteca.filtrar_libros(biblioteca, titulo=titulo, categoria=categoria, autor=autor)
    elif opcion == 3:
        titulo = input("Ingrese el titulo del libro que desea reservar")
        libreria.Biblioteca.reservar_libro(biblioteca, titulo)
main()