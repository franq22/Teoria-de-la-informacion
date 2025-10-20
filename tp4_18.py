""" Comprimir los siguientes mensajes utilizando el algoritmo RLC:
a. XXXYZZZZ
b. AAAABBBCCDAA
c. UUOOOOAAAIEUUUU
"""

import utils

"""Realizar una función en Python que reciba como parámetro una cadena de caracteres con
un mensaje y devuelva una secuencia de bytes (bytearray) que contenga el mensaje
comprimido con RLC, utilizando un byte para almacenar la representación en código ASCII
del carácter y otro byte para el número.
"""

def rlc_comprimir(mensaje: str) -> bytearray:
    byte_array = bytearray()
    n = len(mensaje)
    i = 0
    while i < n:
        count = 1
        while i + 1 < n and mensaje[i] == mensaje[i + 1]:
            count += 1
            i += 1
        byte_array.append(ord(mensaje[i]))  # Carácter en ASCII
        byte_array.append(count)             # Número de repeticiones
        i += 1
    return byte_array

def bytearray_a_bits(b: bytearray) -> str:
    """Devuelve una cadena de '0'/'1' con todos los bytes (8 bits cada uno)."""
    return ''.join(f'{byte:08b}' for byte in b)

def bits_a_bytearray(bits: str) -> bytearray:
    """Convierte una cadena de bits a bytearray.
     Si la longitud de bits no es múltiplo de 8, se rellena con ceros a la derecha."""
    relleno = (-len(bits)) % 8
    bits_padded = bits + '0'*relleno
    ba = bytearray(int(bits_padded[i:i+8], 2) for i in range(0, len(bits_padded), 8))
    return ba

cadena1 = "XXXYZZZZ"
cadena2 = "AAAABBBCCDAA"
cadena3 = "UUOOOOAAAIEUUUU"

print("Cadena 1 comprimida:", rlc_comprimir(cadena1))
print("Cadena 2 comprimida:", rlc_comprimir(cadena2))
print("Cadena 3 comprimida:", rlc_comprimir(cadena3))

bit = bytearray_a_bits(rlc_comprimir(cadena1))
print("Cadena 2 comprimida en bits:", bit)
print("Cadena 2 comprimida en bytearray:", bits_a_bytearray(bit))

print("Tasa de compresión cadena 1:", utils.tasa_de_compresion(cadena1, rlc_comprimir(cadena1)))
print("Tasa de compresión cadena 2:", utils.tasa_de_compresion(cadena2, rlc_comprimir(cadena2)))
print("Tasa de compresión cadena 3:", utils.tasa_de_compresion(cadena3, rlc_comprimir(cadena3)))
