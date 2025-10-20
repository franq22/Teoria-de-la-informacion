"""Implementar funciones en Python que reciban como parámetros: una cadena de
caracteres que contenga un alfabeto fuente y una lista de cadenas de caracteres que
almacena una codificación en el alfabeto binario, y resuelvan lo siguiente:
a. Dada una cadena de caracteres con un mensaje escrito en el alfabeto fuente,
devolver una secuencia de bytes (bytearray) que contenga el mensaje codificado.
b. Dada una secuencia de bytes, decodificar y retornar el mensaje original.
Sugerencia: manipular el mensaje codificado como una cadena de caracteres de unos y
ceros, tanto para codificar como para decodificar, y realizar las conversiones entre binarios
y enteros con las funciones de casteo correspondientes.
"""

import utils

def codificar(mensaje, alfabeto, codificacion) -> bytearray:
    # Crear un diccionario de codificación
    cod_dict = {simbolo: codigo for simbolo, codigo in zip(alfabeto, codificacion)}
    
    # Codificar el mensaje
    mensaje_codificado = ''.join(cod_dict[simbolo] for simbolo in mensaje)
    
    # Convertir la cadena de bits a bytearray
    byte_array = bytearray()
    for i in range(0, len(mensaje_codificado), 8):
        byte = mensaje_codificado[i:i+8]
        byte_array.append(int(byte.ljust(8, '0'), 2))  # Rellenar con ceros si es necesario
    
    return byte_array

def decodificar(byte_array: bytearray, alfabeto, codificacion) -> str:
    # Crear un diccionario de decodificación
    decod_dict = {codigo: simbolo for simbolo, codigo in zip(alfabeto, codificacion)}
    
    # Convertir bytearray a cadena de bits
    mensaje_codificado = ''.join(f'{byte:08b}' for byte in byte_array)
    
    # Decodificar el mensaje
    mensaje_decodificado = ''
    codigo_actual = ''
    for bit in mensaje_codificado:
        codigo_actual += bit
        if codigo_actual in decod_dict:
            mensaje_decodificado += decod_dict[codigo_actual]
            codigo_actual = ''
    return mensaje_decodificado


SIMBOLOS = [
    " ", ",", ".", ":", ";",
    "A", "B", "C", "D", "E",
    "F", "G", "H", "I", "J",
    "K", "L", "M", "N", "Ñ",
    "O", "P", "Q", "R", "S",
    "T", "U", "V", "W", "X",
    "Y", "Z"
]
PROBABILIDADES = [
    0.175990, 0.014093, 0.015034, 0.000542, 0.002109,
    0.111066, 0.015368, 0.030176, 0.038747, 0.101604,
    0.004873, 0.008762, 0.007953, 0.049740, 0.003706,
    0.000034, 0.048149, 0.021041, 0.050490, 0.002018,
    0.073793, 0.019583, 0.010246, 0.051446, 0.058406,
    0.031093, 0.033240, 0.008930, 0.000012, 0.000706,
    0.007851, 0.003199
]

huffman_cod = utils.huffman(PROBABILIDADES)
mensaje_original = "HOLA, COMO ESTAS"
mensaje_codificado = codificar(mensaje_original, SIMBOLOS, huffman_cod)
print("Mensaje codificado (bytearray):", mensaje_codificado)
# Persistir en archivo binario
nombre_archivo = "mensaje_codificado.dat"
with open(nombre_archivo, 'wb') as archivo:
    archivo.write(mensaje_codificado)


mensaje_decodificado = decodificar(mensaje_codificado, SIMBOLOS, huffman_cod)
print("Mensaje decodificado:", mensaje_decodificado)

print("Tase de compresión:", utils.tasa_de_compresion(mensaje_original, mensaje_codificado))