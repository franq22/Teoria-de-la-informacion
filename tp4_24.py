"""Desarrollar funciones en Python que resuelvan lo siguiente:
a. Dado un carácter, devolver un byte que represente su código ASCII (7 bits) y utilice
el bit menos significativo para almacenar la paridad del código.
b. Dado un byte que se obtuvo como resultado de la función anterior, verificar si es
correcto o tiene errores.
"""

import utils

def char_to_ascii_with_parity(char):
    ascii_value = ord(char)
    binary_code = format(ascii_value, '07b')  # Obtener el código ASCII en 7 bits
    parity_bit = str(binary_code.count('1') % 2)  # Calcular el bit de paridad (paridad par)
    byte_with_parity = binary_code + parity_bit  # Añadir el bit de paridad al final
    return byte_with_parity

def verify_ascii_with_parity(byte):
    data_bits = byte[:-1]  # Los primeros 7 bits son los datos
    parity_bit = byte[-1]  # El último bit es el bit de paridad
    calculated_parity = str(data_bits.count('1') % 2)  # Calcular la paridad de los datos
    return calculated_parity == parity_bit  # Verificar si la paridad coincide

"""Dadas las siguientes matrices que contienen mensajes representados con código ASCII y
sus bits de paridad vertical, longitudinal y cruzada, detectar los errores y, en caso de ser
posible, recuperar el mensaje original:
a. 00100001 b. 00101101 c. 00101010 d. 00010100
10000111 10011001 10000010 10010000
10000010 10001010 10011010 10011110
10100110 10011100 10011111 10011001
10000010 10000010 10100101 10000010
e. 00110101 f. 00001001 g. 00011101 h. 00111110
10011010 10101001 10010011 10000111
10101011 10100101 10011101 10010000
10100100 10001011 10001100 10000010
10000010 10100110 10011111 10101010"""

matrices = {
    'a': ["00100001", "10000111", "10000010", "10100110", "10000010"],
    'b': ["00101101", "10011001", "10001010", "10011100", "10000010"],
    'c': ["00101010", "10000010", "10011010", "10011111", "10100101"],
    'd': ["00010100", "10010000", "10011110", "10011001", "10000010"],
    'e': ["00110101", "10011010", "10101011", "10100100", "10000010"],
    'f': ["00001001", "10101001", "10100101", "10001011", "10100110"],
    'g': ["00011101", "10010011", "10011101", "10001100", "10011111"],
    'h': ["00111110", "10000111", "10010000", "10000010", "10101010"],
}


def detectar_y_corregir_errores(matriz_str):
    matriz = [list(fila) for fila in matriz_str]
    filas = len(matriz)
    columnas = len(matriz[0])

    filas_con_error = []
    columnas_con_error = []

    # VERIFICAR PARIDAD DE FILAS (VRC)
    for i in range(1, filas):
        data_bits = matriz[i][:-1]  # Datos
        given_parity_bit = matriz[i][-1] # Paridad VRC
        calculated_parity = '1' if "".join(data_bits).count('1') % 2 != 0 else '0'
        if calculated_parity != given_parity_bit:
            filas_con_error.append(i)

    # VERIFICAR PARIDAD DE COLUMNAS (LRC)
    for j in range(columnas - 1):
        data_bits = [matriz[i][j] for i in range(1, filas)] # Datos
        given_parity_bit = matriz[0][j] # Paridad LRC
        calculated_parity = '1' if "".join(data_bits).count('1') % 2 != 0 else '0'
        if calculated_parity != given_parity_bit:
            columnas_con_error.append(j)

    # ANALIZAR Y CORREGIR
    
    if len(filas_con_error) == 1 and len(columnas_con_error) == 1:
        # Caso 1: Error único en un bit de DATOS. Corregible. 
        fila = filas_con_error[0]
        columna = columnas_con_error[0]
        bit_actual = matriz[fila][columna]
        matriz[fila][columna] = '1' if bit_actual == '0' else '0'

    elif (len(filas_con_error) == 1 and len(columnas_con_error) == 0) or \
         (len(filas_con_error) == 0 and len(columnas_con_error) == 1):
        # Caso 2: Error en bit de PARIDAD. Corregible.
        corner_bit = matriz[0][-1]
        
        # Calcular paridad de la fila LRC (matriz[0][:-1])
        lrc_bits = matriz[0][:-1]
        calc_lrc_parity = '1' if "".join(lrc_bits).count('1') % 2 != 0 else '0'
        
        # Calcular paridad de la columna VRC (matriz[1...][-1])
        vrc_bits = [matriz[i][-1] for i in range(1, filas)]
        calc_vrc_parity = '1' if "".join(vrc_bits).count('1') % 2 != 0 else '0'

        # Ambas deben coincidir con el bit de la esquina
        if calc_lrc_parity == calc_vrc_parity:
            return "—" # No se puede corregir
        else:
            pass 

    elif len(filas_con_error) == 0 and len(columnas_con_error) == 0:
        # Caso 3: Sin errores. Verificar paridad cruzada
        corner_bit = matriz[0][-1]
        
        # Calcular paridad de la fila LRC (matriz[0][:-1])
        lrc_bits = matriz[0][:-1]
        calc_lrc_parity = '1' if "".join(lrc_bits).count('1') % 2 != 0 else '0'
        
        # Calcular paridad de la columna VRC (matriz[1...][-1])
        vrc_bits = [matriz[i][-1] for i in range(1, filas)]
        calc_vrc_parity = '1' if "".join(vrc_bits).count('1') % 2 != 0 else '0'

        # Ambas deben coincidir con el bit de la esquina
        if calc_lrc_parity != corner_bit or calc_vrc_parity != corner_bit:
            return "—" # No se puede corregir
    
    else:
        # Caso 4: Múltiples errores. Incorregible. 
        return "—"

    # DECODIFICAR EL MENSAJE 
    mensaje_decodificado = ''
    try:
        for i in range(1, filas): 
            bits_ascii = "".join(matriz[i][:-1]) # Toma los 7 bits de datos
            valor_ascii = int(bits_ascii, 2)
            mensaje_decodificado += chr(valor_ascii)
    except (ValueError, TypeError):
        return "—" 

    return mensaje_decodificado

for key, matriz in matrices.items():
    print(f"\n--- Procesando matriz '{key}' ---")
    mensaje = utils.detectar_y_corregir_errores(matriz)
    print(f"Mensaje original: '{mensaje}'")