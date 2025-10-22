"""Codificar funciones en Python que resuelvan lo siguiente:
a. Dada una cadena de caracteres, generar una secuencia de bytes (bytearray) que
contenga su representación con código ASCII y sus bits de paridad vertical,
longitudinal y cruzada.
b. Dada una secuencia de bytes que se obtuvo como resultado de la función anterior,
devolver el mensaje original o una cadena de caracteres vacía si no se pueden
corregir los errores.
Sugerencia: generar una matriz de bits para realizar las operaciones, transformando la
secuencia de bytes en una lista de cadenas de caracteres binarias y, luego, cada cadena
de caracteres en una lista de números enteros que representen los bits."""

import utils

def mensaje_a_bytes_con_paridad(mensaje):
    matriz = []
    
    # Convertir cada carácter a su representación ASCII con paridad
    for char in mensaje:
        byte_with_parity = utils.char_to_ascii_with_parity(char)
        matriz.append(list(byte_with_parity))
    
    filas = len(matriz)
    columnas = len(matriz[0])
    
    # Calcular bits de paridad LRC 
    lrc_bits = []
    for j in range(columnas): 
        column_bits = [matriz[i][j] for i in range(filas)]
        parity_bit = '1' if column_bits.count('1') % 2 != 0 else '0'
        lrc_bits.append(parity_bit)
    
    matriz.insert(0, lrc_bits) # Añadir fila de paridad LRC al principio 
    
    # Convertir la matriz a bytearray
    byte_array = bytearray()
    for fila in matriz:
        byte_str = ''.join(fila)
        byte_value = int(byte_str, 2)
        byte_array.append(byte_value)
    
    return byte_array

def bytes_con_paridad_a_mensaje(byte_array: bytearray) -> str:
    if not byte_array:
        return ""
    matriz_str = [f'{byte:08b}' for byte in byte_array]
    mensaje = utils.detectar_y_corregir_errores(matriz_str)
    return "" if mensaje == "—" else mensaje


# --- PRUEBA DEL CICLO COMPLETO ---

mensaje_original = "CASA"

print(f"Mensaje original: '{mensaje_original}'")

# 1. CODIFICAR
bytes_codificados = mensaje_a_bytes_con_paridad(mensaje_original)
print(f"Bytes codificados: {utils.bytearray_a_bits(bytes_codificados)}")

# 2. DECODIFICAR
mensaje_decodificado = bytes_con_paridad_a_mensaje(bytes_codificados)
print(f"Mensaje decodificado: '{mensaje_decodificado}'")

print("-" * 20)

# 3. PRUEBA CON ERRORES
print("Simulando un error corregible...")
# Corrompemos un bit de datos (el primer bit de 'H')
bytes_corregibles = bytearray(bytes_codificados)
bytes_corregibles[1] = bytes_corregibles[1] ^ 0b10000000 # Invertimos el primer bit de 'H'

print(f"Bytes corruptos: {bytes_corregibles}")
mensaje_corregido = bytes_con_paridad_a_mensaje(bytes_corregibles)
print(f"Mensaje corregido: '{mensaje_corregido}'")

print("-" * 20)

# 4. PRUEBA CON MÚLTIPLES ERRORES
print("Simulando errores incorregibles...")
bytes_incorregibles = bytearray(bytes_codificados)
bytes_incorregibles[1] = bytes_incorregibles[1] ^ 0b10000000 # Error 1
bytes_incorregibles[2] = bytes_incorregibles[2] ^ 0b01000000 # Error 2

print(f"Bytes muy corruptos: {bytes_incorregibles}")
mensaje_fallido = bytes_con_paridad_a_mensaje(bytes_incorregibles)
print(f"Mensaje fallido: '{mensaje_fallido}'") # Debería estar vacío
