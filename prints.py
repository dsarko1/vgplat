"""
Modulo: prints.py

Contiene todas las funciones encargadas de mostrar informacion
por pantalla: presentacion del sistema, menues de cada rol y
mensajes informativos.
"""


def mostrar_presentacion():
    """Muestra el nombre del sistema, su descripcion y objetivo."""
    print("=" * 40)
    print("=== Bienvenido a GameParadise ===")
    print("La mejor plataforma de videojuegos online.")
    print("Conectate con jugadores y desarrolladores de todo el mundo.")
    print("=" * 40)
    print("Objetivo: simular el funcionamiento basico de una")
    print("plataforma online de videojuegos, con distintos tipos")
    print("de usuario (Jugador, Desarrolladora y Administrador).")
    print("=" * 40)
    print()


def mostrar_menu_jugador(usuario):
    """
    Muestra el menu de opciones correspondiente al rol Jugador.

    Parametros:
        usuario (str): nombre de usuario logueado.
    """
    print("-" * 40)
    print(f"Usuario: {usuario}")
    print("Tipo:    Jugador")
    print("-" * 40)
    print("1. Ver perfil")
    print("2. Explorar catalogo (simulado)")
    print("3. Salir")
    print("-" * 40)


def mostrar_menu_desarrolladora(usuario, estudio):
    """
    Muestra el menu de opciones correspondiente al rol
    Desarrolladora.

    Parametros:
        usuario (str): nombre de usuario logueado.
        estudio (str): nombre del estudio desarrollador.
    """
    print("-" * 40)
    print(f"Usuario: {usuario}")
    print("Tipo:    Desarrolladora")
    print(f"Estudio: {estudio}")
    print("-" * 40)
    print("1. Ver datos del estudio")
    print("2. Publicar juego (simulado)")
    print("3. Ver ventas (simulado)")
    print("4. Salir")
    print("-" * 40)


def mostrar_menu_administrador(usuario):
    """
    Muestra el menu de opciones correspondiente al rol
    Administrador.

    Parametros:
        usuario (str): nombre de usuario logueado.
    """
    print("-" * 40)
    print(f"Usuario: {usuario}")
    print("Tipo:    Administrador")
    print("-" * 40)
    print("1. Crear usuario (simulado)")
    print("2. Borrar usuario (simulado)")
    print("3. Ver informacion del sistema")
    print("4. Salir")
    print("-" * 40)


def mostrar_perfil_jugador(datos_jugador):
    """
    Muestra en pantalla los datos del perfil de un jugador.

    Parametros:
        datos_jugador (dict): diccionario con los datos
        hardcodeados del jugador.
    """
    print("-" * 40)
    print("PERFIL DEL JUGADOR")
    print("-" * 40)
    print(f"Nombre:               {datos_jugador['nombre']}")
    print(f"Apodo (nickname):     {datos_jugador['apodo']}")
    print(f"Pais:                 {datos_jugador['pais']}")
    print(f"Plataforma favorita:  {datos_jugador['plataforma']}")
    print(f"Horas jugadas:        {datos_jugador['horas_jugadas']}")
    print(f"Juegos comprados:     {datos_jugador['juegos_comprados']}")
    print(f"Nivel de cuenta:      {datos_jugador['nivel']}")
    print("-" * 40)


def mostrar_datos_estudio(datos_estudio):
    """
    Muestra en pantalla los datos de la desarrolladora.

    Parametros:
        datos_estudio (dict): diccionario con los datos
        hardcodeados del estudio.
    """
    print("-" * 40)
    print("DATOS DEL ESTUDIO")
    print("-" * 40)
    print(f"Nombre del estudio:      {datos_estudio['nombre_estudio']}")
    print(f"Pais de origen:          {datos_estudio['pais']}")
    print(f"Sitio web:               {datos_estudio['sitio_web']}")
    print(f"Juegos publicados:       "
          f"{datos_estudio['juegos_publicados']}")
    print(f"Empleados:               {datos_estudio['empleados']}")
    print(f"Anio de fundacion:       {datos_estudio['anio_fundacion']}")
    print("-" * 40)


def mostrar_catalogo(lista_juegos, empresa):
    """
    Muestra el listado de juegos disponibles de una empresa, con
    su precio.

    Parametros:
        lista_juegos (list): lista de tuplas (titulo, precio).
        empresa (str): nombre de la empresa buscada.
    """
    print("-" * 40)
    print(f"Catalogo de {empresa}")
    print("-" * 40)

    for i in range(len(lista_juegos)):
        titulo = lista_juegos[i][0]
        precio = lista_juegos[i][1]
        print(f"{i + 1}. {titulo} - $ {precio}")

    print("-" * 40)


def mostrar_metodos_pago():
    """Muestra el submenu de metodos de pago disponibles."""
    print("-" * 40)
    print("Metodos de pago disponibles")
    print("-" * 40)
    print("1. Tarjeta de credito")
    print("2. Tarjeta de debito")
    print("0. Ninguno (cancelar compra)")
    print("-" * 40)


def mostrar_info_sistema():
    """
    Muestra la informacion general del sistema: integrantes del
    grupo, descripcion del proyecto y funcionalidades extra
    propuestas para cada rol.
    """
    print("-" * 40)
    print("INFORMACION DEL SISTEMA")
    print("-" * 40)
    print("Integrantes del grupo:")
    print("- Integrante 1")
    print("- Integrante 2")
    print("- Integrante 3")
    print("- Integrante 4")
    print("-" * 40)
    print("Descripcion del sistema:")
    print("GameParadise es una plataforma online de videojuegos que")
    print("conecta a jugadores con estudios desarrolladores.")
    print("Resuelve el problema de centralizar en un unico lugar")
    print("la compra de juegos, la publicacion de titulos por")
    print("parte de las desarrolladoras y la administracion")
    print("general de la plataforma.")
    print("Tipos de usuario: Jugador, Desarrolladora y")
    print("Administrador.")
    print("-" * 40)
    print("Funcionalidades extra propuestas:")
    print("Jugador:")
    print("  1. Lista de deseados (wishlist) de juegos.")
    print("  2. Sistema de resenas y puntuacion de juegos.")
    print("  3. Historial de compras realizadas.")
    print("Desarrolladora:")
    print("  1. Estadisticas de descargas por juego publicado.")
    print("  2. Posibilidad de aplicar descuentos a un juego.")
    print("Administrador:")
    print("  1. Listado general de usuarios registrados.")
    print("  2. Reportes de actividad de la plataforma.")
    print("-" * 40)


def mostrar_mensaje(mensaje):
    """
    Muestra un mensaje generico por pantalla.

    Parametros:
        mensaje (str): texto a mostrar.
    """
    print(mensaje)
