"""
Modulo: funciones.py

Contiene los datos hardcodeados del sistema (usuarios y catalogo
de juegos) y toda la logica de negocio: login, y una funcion por
cada opcion de los menues de Jugador, Desarrolladora y
Administrador.

Este modulo utiliza las funciones de "inputs.py" para pedir y
validar datos, y las funciones de "prints.py" para mostrar
resultados por pantalla.
"""

import inputs
import prints


# ---------------------------------------------------------------
# DATOS PRECARGADOS (hardcodeados)
# ---------------------------------------------------------------

# Usuarios predefinidos del sistema, segun la consigna.
USUARIOS_PRECARGADOS = [
    {"usuario": "jugador1", "clave": "vegetta777", "tipo": "Jugador"},
    {"usuario": "rockstargames", "clave": "reddeadonline",
     "tipo": "Desarrolladora"},
    {"usuario": "adminsteam", "clave": "admin999",
     "tipo": "Administrador"},
]

# Datos hardcodeados del perfil de jugador (4 str y 3 int).
PERFIL_JUGADOR = {
    "nombre": "Juan Perez",
    "apodo": "progamer01",
    "pais": "Argentina",
    "plataforma": "PC",
    "horas_jugadas": 350,
    "juegos_comprados": 12,
    "nivel": 27,
}

# Datos hardcodeados del estudio desarrollador (3 str y 3 int).
DATOS_ESTUDIO = {
    "nombre_estudio": "Rockstar Games",
    "pais": "Estados Unidos",
    "sitio_web": "www.rockstargames.com",
    "juegos_publicados": 19,
    "empleados": 2000,
    "año_fundacion": 1998,
}

# Catalogo hardcodeado de juegos por empresa desarrolladora.
CATALOGO_JUEGOS = {
    "rockstargames": [
        ("Red Dead Redemption 2", 29.99),
        ("Grand Theft Auto V", 14.99),
        ("Bully", 9.99),
    ],
    "cdprojektred": [
        ("The Witcher 3", 19.99),
        ("Cyberpunk 2077", 39.99),
    ],
    "nintendo": [
        ("The Legend of Zelda", 49.99),
        ("Super Mario Odyssey", 44.99),
    ],
}


# ---------------------------------------------------------------
# LOGIN
# ---------------------------------------------------------------

def validar_login(lista_usuarios, usuario_ingresado, clave_ingresada):
    """
    Busca, recorriendo la lista de usuarios con un ciclo, si
    existe un usuario cuyo nombre y clave coincidan con los
    ingresados.

    Parametros:
        lista_usuarios (list): lista de diccionarios de usuarios.
        usuario_ingresado (str): nombre de usuario ingresado.
        clave_ingresada (str): contrasenia ingresada.

    Retorna:
        dict o None: el diccionario del usuario encontrado, o
        None si no existe una coincidencia.
    """
    for i in range(len(lista_usuarios)):
        usuario_actual = lista_usuarios[i]

        if (usuario_actual["usuario"] == usuario_ingresado and
                usuario_actual["clave"] == clave_ingresada):
            return usuario_actual

    return None


# ---------------------------------------------------------------
# OPCIONES DEL ROL JUGADOR
# ---------------------------------------------------------------

def ver_perfil_jugador():
    """Muestra el perfil hardcodeado del jugador."""
    prints.mostrar_perfil_jugador(PERFIL_JUGADOR)


def buscar_juegos_por_empresa(catalogo, empresa_buscada):
    """
    Busca dentro del catalogo la lista de juegos de una empresa,
    comparando de forma manual (sin usar metodos de string) y
    sin distinguir mayusculas de minusculas.

    Parametros:
        catalogo (dict): catalogo completo de juegos.
        empresa_buscada (str): nombre de empresa ingresado por
        el usuario.

    Retorna:
        list o None: lista de tuplas (titulo, precio) si se
        encuentra la empresa, o None si no existe en el catalogo.
    """
    empresa_buscada_minuscula = inputs.convertir_minusculas(
        empresa_buscada)

    for clave_empresa in catalogo:
        clave_minuscula = inputs.convertir_minusculas(clave_empresa)

        if clave_minuscula == empresa_buscada_minuscula:
            return catalogo[clave_empresa]

    return None


def explorar_catalogo():
    """
    Implementa la opcion "Explorar catalogo" del menu Jugador:
    pide el nombre de una empresa desarrolladora, muestra sus
    juegos, permite elegir uno, elegir un metodo de pago y
    simula la confirmacion (o cancelacion) de la compra.
    """
    empresa_ingresada = inputs.pedir_texto_minimo(
        "Ingrese el nombre de la empresa desarrolladora a "
        "buscar (minimo 4 caracteres): ", 4)

    juegos_encontrados = buscar_juegos_por_empresa(
        CATALOGO_JUEGOS, empresa_ingresada)

    if juegos_encontrados is None:
        prints.mostrar_mensaje(
            "No se encontraron juegos para esa empresa.")
        return

    prints.mostrar_catalogo(juegos_encontrados, empresa_ingresada)

    opcion_juego = inputs.pedir_opcion_menu(
        "Elija un juego (numero): ", 1, len(juegos_encontrados))

    juego_elegido = juegos_encontrados[opcion_juego - 1]
    titulo_elegido = juego_elegido[0]
    precio_elegido = juego_elegido[1]

    prints.mostrar_metodos_pago()
    opcion_pago = inputs.pedir_opcion_menu(
        "Elija un metodo de pago: ", 0, 2)

    if opcion_pago == 0:
        mensaje_cancelacion = (
            "Compra cancelada. No se realizo ningun cargo."
        )
        prints.mostrar_mensaje(mensaje_cancelacion)
        return

    if opcion_pago == 1:
        metodo_pago_texto = "Tarjeta de credito"
    else:
        metodo_pago_texto = "Tarjeta de debito"

    # Como solo se puede elegir un unico juego, el precio total
    # de la compra es directamente el precio del juego elegido.
    precio_total = precio_elegido

    prints.mostrar_mensaje("-" * 40)
    prints.mostrar_mensaje("Compra confirmada")
    prints.mostrar_mensaje(f"Juego: {titulo_elegido}")
    prints.mostrar_mensaje(f"Metodo de pago: {metodo_pago_texto}")
    prints.mostrar_mensaje(f"Precio total: $ {precio_total}")
    prints.mostrar_mensaje("-" * 40)


# ---------------------------------------------------------------
# OPCIONES DEL ROL DESARROLLADORA
# ---------------------------------------------------------------

def ver_datos_estudio():
    """Muestra los datos hardcodeados del estudio desarrollador."""
    prints.mostrar_datos_estudio(DATOS_ESTUDIO)


def publicar_juego():
    """
    Implementa la opcion "Publicar juego" del menu Desarrolladora:
    pide nombre y precio del juego (validando que el precio sea
    mayor a 0) y simula su publicacion.
    """
    nombre_juego = inputs.pedir_texto_minimo(
        "Ingrese el nombre del videojuego: ", 1)

    precio_juego = inputs.pedir_numero_decimal_positivo(
        "Ingrese el precio del videojuego: ")

    prints.mostrar_mensaje("-" * 40)
    mensaje_publicacion = (
        f"El juego '{nombre_juego}' fue publicado correctamente "
        f"en GameHub."
    )
    prints.mostrar_mensaje(mensaje_publicacion)
    prints.mostrar_mensaje(f"Precio de venta: $ {precio_juego}")
    prints.mostrar_mensaje("-" * 40)


def ver_ventas():
    """Simula la visualizacion de ventas del estudio."""
    prints.mostrar_mensaje("-" * 40)
    prints.mostrar_mensaje("Ventas del mes: 120 copias vendidas.")
    prints.mostrar_mensaje("-" * 40)


# ---------------------------------------------------------------
# OPCIONES DEL ROL ADMINISTRADOR
# ---------------------------------------------------------------

def crear_usuario(lista_usuarios):
    """
    Implementa la opcion "Crear usuario" del menu Administrador:
    pide y valida nombre, contrasenia y rol del nuevo usuario, y
    simula la carga de sus datos correspondientes.

    Parametros:
        lista_usuarios (list): lista actual de usuarios del
        sistema.

    Retorna:
        list: lista de usuarios actualizada, con el nuevo usuario
        agregado al final.
    """
    nuevo_usuario = inputs.pedir_texto_minimo(
        "Ingrese el nombre del nuevo usuario (minimo 3 "
        "caracteres): ", 3)

    nueva_clave = inputs.pedir_texto_minimo(
        "Ingrese la contrasenia (minimo 6 caracteres): ", 6)

    rol_valido = False
    rol_ingresado = ""

    while rol_valido is False:
        rol_ingresado = input(
            "Ingrese el rol (jugador / desarrolladora): ")
        rol_minuscula = inputs.convertir_minusculas(rol_ingresado)

        if rol_minuscula == "jugador" or rol_minuscula == "desarrolladora":
            rol_valido = True
        else:
            print("Error: el rol debe ser 'jugador' o "
                  "'desarrolladora'.")

    if rol_minuscula == "jugador":
        tipo_final = "Jugador"
        mensaje_datos = (
            "Se solicitaran los datos de perfil del jugador "
            "(los mismos que se muestran en 'Ver perfil')."
        )
        prints.mostrar_mensaje(mensaje_datos)
    else:
        tipo_final = "Desarrolladora"
        mensaje_datos = (
            "Se solicitaran los datos del estudio (los mismos "
            "que se muestran en 'Ver datos del estudio')."
        )
        prints.mostrar_mensaje(mensaje_datos)

    usuario_creado = {
        "usuario": nuevo_usuario,
        "clave": nueva_clave,
        "tipo": tipo_final,
    }

    # Se utiliza concatenacion de listas (en lugar de un metodo de
    # lista avanzado) para agregar el nuevo usuario a la lista.
    lista_usuarios_actualizada = lista_usuarios + [usuario_creado]

    prints.mostrar_mensaje("-" * 40)
    mensaje_creacion = (
        f"Usuario '{nuevo_usuario}' creado correctamente "
        f"como {tipo_final}."
    )
    prints.mostrar_mensaje(mensaje_creacion)
    prints.mostrar_mensaje("-" * 40)

    return lista_usuarios_actualizada


def borrar_usuario():
    """
    Implementa la opcion "Borrar usuario" del menu Administrador.
    No borra nada realmente: es una simulacion del proceso.
    """
    nombre_usuario = inputs.pedir_texto_minimo(
        "Ingrese el nombre de usuario a borrar (minimo 3 "
        "caracteres): ", 3)

    prints.mostrar_mensaje("-" * 40)
    mensaje_borrado = (
        f"El usuario '{nombre_usuario}' fue eliminado "
        f"correctamente (simulado)."
    )
    prints.mostrar_mensaje(mensaje_borrado)
    prints.mostrar_mensaje("-" * 40)


def ver_info_sistema():
    """Muestra la informacion general del sistema."""
    prints.mostrar_info_sistema()
