"""
Modulo: main.py

Archivo principal del sistema GameParadise.

Se encarga de:
    1. Mostrar la presentacion del sistema.
    2. Realizar el login del usuario, validando los datos y
       reintentando ante credenciales incorrectas.
    3. Derivar al usuario logueado al menu correspondiente segun
       su rol (Jugador, Desarrolladora o Administrador).
"""

import inputs
import prints
import funciones
import menu


def iniciar_sesion(lista_usuarios):
    """
    Pide nombre de usuario y contrasenia, los valida y vuelve a
    solicitarlos mientras las credenciales no coincidan con
    ningun usuario del sistema.

    Parametros:
        lista_usuarios (list): lista de usuarios del sistema.

    Retorna:
        dict: diccionario del usuario que inicio sesion
        correctamente.
    """
    sesion_iniciada = False
    usuario_encontrado = None

    while sesion_iniciada is False:
        print("-" * 40)
        print("INICIO DE SESION")
        print("-" * 40)

        nombre_usuario = inputs.pedir_texto_minimo(
            "Usuario (minimo 3 caracteres): ", 3)
        contrasenia = inputs.pedir_texto_minimo(
            "Contraseña (minimo 6 caracteres): ", 6)

        usuario_encontrado = funciones.validar_login(
            lista_usuarios, nombre_usuario, contrasenia)

        if usuario_encontrado is None:
            print("Error: usuario o contraseña incorrectos. "
                  "Intente nuevamente.")
        else:
            sesion_iniciada = True
            print(f"Bienvenido/a, {nombre_usuario}.")

    return usuario_encontrado


def main():
    """Funcion principal que orquesta la ejecucion del programa."""
    lista_usuarios = funciones.USUARIOS_PRECARGADOS

    prints.mostrar_presentacion()

    usuario_logueado = iniciar_sesion(lista_usuarios)
    tipo_de_usuario = usuario_logueado["tipo"]
    nombre_usuario = usuario_logueado["usuario"]

    if tipo_de_usuario == "Jugador":
        menu.menu_jugador(nombre_usuario)
    elif tipo_de_usuario == "Desarrolladora":
        menu.menu_desarrolladora(nombre_usuario)
    elif tipo_de_usuario == "Administrador":
        lista_usuarios = menu.menu_administrador(
            nombre_usuario, lista_usuarios)

    print("-" * 40)
    print("Gracias por usar GameParadise. Hasta la proxima!")
    print("-" * 40)


# Punto de entrada del programa.
if __name__ == "__main__":
    main()
