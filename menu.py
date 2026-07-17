"""
Modulo: menu.py

Contiene una funcion por cada rol del sistema (Jugador,
Desarrolladora, Administrador). Cada funcion muestra el menu
correspondiente en un ciclo, pide la opcion elegida y llama a la
funcion de funciones.py que resuelve esa opcion.
"""

import inputs
import prints
import funciones


def menu_jugador(nombre_usuario):
    """
    Ejecuta el ciclo de menu del rol Jugador hasta que el usuario
    elige la opcion de salir.

    Parametros:
        nombre_usuario (str): nombre del usuario logueado.
    """
    continuar_en_menu = True

    while continuar_en_menu == True:
        prints.mostrar_menu_jugador(nombre_usuario)
        opcion_elegida = inputs.pedir_opcion_menu(
            "Elija una opcion: ", 1, 3)

        if opcion_elegida == 1:
            funciones.ver_perfil_jugador()
        elif opcion_elegida == 2:
            funciones.explorar_catalogo()
        elif opcion_elegida == 3:
            prints.mostrar_mensaje("Cerrando sesion del Jugador...")
            continuar_en_menu = False


def menu_desarrolladora(nombre_usuario):
    """
    Ejecuta el ciclo de menu del rol Desarrolladora hasta que el
    usuario elige la opcion de salir.

    Parametros:
        nombre_usuario (str): nombre del usuario logueado.
    """
    nombre_estudio = funciones.DATOS_ESTUDIO["nombre_estudio"]
    continuar_en_menu = True

    while continuar_en_menu == True:
        prints.mostrar_menu_desarrolladora(
            nombre_usuario, nombre_estudio)
        opcion_elegida = inputs.pedir_opcion_menu(
            "Elija una opcion: ", 1, 4)

        if opcion_elegida == 1:
            funciones.ver_datos_estudio()
        elif opcion_elegida == 2:
            funciones.publicar_juego()
        elif opcion_elegida == 3:
            funciones.ver_ventas()
        elif opcion_elegida == 4:
            prints.mostrar_mensaje(
                "Cerrando sesion de la Desarrolladora...")
            continuar_en_menu = False


def menu_administrador(nombre_usuario, lista_usuarios):
    """
    Ejecuta el ciclo de menu del rol Administrador hasta que el
    usuario elige la opcion de salir.

    Parametros:
        nombre_usuario (str): nombre del usuario logueado.
        lista_usuarios (list): lista de usuarios del sistema.

    Retorna:
        list: lista de usuarios, posiblemente actualizada si se
        crearon nuevos usuarios durante la sesion.
    """
    continuar_en_menu = True

    while continuar_en_menu == True:
        prints.mostrar_menu_administrador(nombre_usuario)
        opcion_elegida = inputs.pedir_opcion_menu(
            "Elija una opcion: ", 1, 4)

        if opcion_elegida == 1:
            lista_usuarios = funciones.crear_usuario(lista_usuarios)
        elif opcion_elegida == 2:
            funciones.borrar_usuario()
        elif opcion_elegida == 3:
            funciones.ver_info_sistema()
        elif opcion_elegida == 4:
            prints.mostrar_mensaje(
                "Cerrando sesion del Administrador...")
            continuar_en_menu = False

    return lista_usuarios
