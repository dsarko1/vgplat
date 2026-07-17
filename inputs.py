"""
Modulo: inputs.py

Contiene todas las funciones encargadas de pedir datos al usuario
por teclado y validarlos.
"""

def es_todo_digitos(cadena):
    """
    Verifica, caracter por caracter, si una cadena esta formada
    unicamente por digitos numericos (0 al 9).

    No se utiliza isdigit(). El algoritmo compara cada caracter
    de la cadena contra una lista de digitos validos.

    Parametros:
        cadena (str): cadena a analizar.

    Retorna:
        bool: True si todos los caracteres son digitos y la
        cadena no esta vacia. False en caso contrario.
    """
    digitos_validos = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

    if len(cadena) == 0:
        return False

    for i in range(len(cadena)):
        caracter_actual = cadena[i]
        es_digito = False

        for j in range(len(digitos_validos)):
            if caracter_actual == digitos_validos[j]:
                es_digito = True

        if es_digito is False:
            return False

    return True


def es_numero_decimal_positivo(cadena):
    """
    Verifica, caracter por caracter, si una cadena representa un
    numero decimal (por ejemplo "19.99" o "20"), permitiendo un
    unico punto decimal.

    Parametros:
        cadena (str): cadena a analizar.

    Retorna:
        bool: True si la cadena tiene un formato numerico valido.
        False en caso contrario.
    """
    digitos_validos = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    cantidad_de_puntos = 0

    if len(cadena) == 0:
        return False

    for i in range(len(cadena)):
        caracter_actual = cadena[i]

        if caracter_actual == ".":
            cantidad_de_puntos = cantidad_de_puntos + 1
        else:
            es_digito = False
            for j in range(len(digitos_validos)):
                if caracter_actual == digitos_validos[j]:
                    es_digito = True
            if es_digito is False:
                return False

    if cantidad_de_puntos > 1:
        return False

    return True


def convertir_minusculas(cadena):
    """
    Convierte manualmente una cadena a minusculas utilizando los
    codigos ASCII de cada caracter (ord y chr), sin usar el
    metodo lower() de las cadenas.

    Parametros:
        cadena (str): cadena original.

    Retorna:
        str: nueva cadena en minusculas.
    """
    resultado = ""

    for i in range(len(cadena)):
        caracter_actual = cadena[i]
        codigo_ascii = ord(caracter_actual)

        # Las letras mayusculas A-Z van del codigo 65 al 90.
        if codigo_ascii >= 65 and codigo_ascii <= 90:
            codigo_convertido = codigo_ascii + 32
            resultado = resultado + chr(codigo_convertido)
        else:
            resultado = resultado + caracter_actual

    return resultado


def pedir_texto_minimo(mensaje, minimo_caracteres):
    """
    Solicita un texto por teclado y vuelve a pedirlo mientras no
    cumpla con la cantidad minima de caracteres exigida.

    Parametros:
        mensaje (str): texto que se muestra al pedir el dato.
        minimo_caracteres (int): cantidad minima de caracteres.

    Retorna:
        str: texto valido ingresado por el usuario.
    """
    while True:
        texto_ingresado = input(mensaje)

        if len(texto_ingresado) >= minimo_caracteres:
            return texto_ingresado
        else:
            print(f"Error: debe ingresar al menos {minimo_caracteres} "
                  f"caracteres.")


def pedir_numero_entero(mensaje):
    """
    Solicita un numero entero por teclado. Vuelve a pedirlo
    mientras el usuario no ingrese solamente digitos.

    Parametros:
        mensaje (str): texto que se muestra al pedir el dato.

    Retorna:
        int: numero entero valido ingresado por el usuario.
    """
    while True:
        entrada = input(mensaje)

        if es_todo_digitos(entrada) is True:
            numero_convertido = int(entrada)
            return numero_convertido
        else:
            print("Error: debe ingresar unicamente numeros enteros.")


def pedir_opcion_menu(mensaje, opcion_minima, opcion_maxima):
    """
    Solicita al usuario que elija una opcion de menu dentro de un
    rango valido (por ejemplo, entre 1 y 4).

    Parametros:
        mensaje (str): texto que se muestra al pedir el dato.
        opcion_minima (int): valor minimo permitido.
        opcion_maxima (int): valor maximo permitido.

    Retorna:
        int: opcion elegida, dentro del rango permitido.
    """
    while True:
        numero_elegido = pedir_numero_entero(mensaje)

        if numero_elegido >= opcion_minima and numero_elegido <= opcion_maxima:
            return numero_elegido
        else:
            print(f"Error: ingrese una opcion entre {opcion_minima} "
                  f"y {opcion_maxima}.")


def pedir_numero_decimal_positivo(mensaje):
    """
    Solicita un numero decimal mayor a 0 (por ejemplo, un precio).
    Vuelve a pedirlo mientras el formato no sea valido o el valor
    no sea mayor a cero.

    Parametros:
        mensaje (str): texto que se muestra al pedir el dato.

    Retorna:
        float: numero decimal positivo ingresado por el usuario.
    """
    while True:
        entrada = input(mensaje)

        if es_numero_decimal_positivo(entrada) is True:
            numero_convertido = float(entrada)
            if numero_convertido > 0:
                return numero_convertido
            else:
                print("Error: el numero debe ser mayor a 0.")
        else:
            print("Error: ingrese un numero valido. Ejemplo: 19.99")
