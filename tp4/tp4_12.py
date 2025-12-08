"""Para una fuente de información con distribución de probabilidades:
P = { 0.385, 0.154, 0.128, 0.154, 0.179 }
a. Calcular la entropía de la fuente
b. Generar una codificación de Huffman
c. Obtener una codificación de Shannon-Fano
d. Graficar los árboles binarios que surgen de cada codificación
e. Comparar la longitud media, el rendimiento y la redundancia de cada código"""

import utils

probs = [0.385, 0.154, 0.128, 0.154, 0.179]
print("a. Entropía de la fuente:")
entropy = utils.entropia(probs)
print(f"   H = {entropy:.4f} bits/símbolo\n")
print("b. Codificación de Huffman:")
huffman = utils.huffman(probs)
print(f"   Código de Huffman: {huffman}")
shannon_fano = utils.shannon_fano(probs)
print("\nc. Codificación de Shannon-Fano:")
print(f"   Código de Shannon-Fano: {shannon_fano}\n")
print("e. Comparación de códigos: \n")
print("   Código de Huffman:")
L = utils.longitud_media(probs, huffman)
R, p = utils.rendimiento_redundancia(probs, huffman)
print(" longitud media, rendimiento y redundancia del código de Huffman calculados.\n" )
print(L, R, p)
print("   Código de Shannon-Fano:")
L_sf = utils.longitud_media(probs, shannon_fano)
R_sf, p_sf = utils.rendimiento_redundancia(probs, shannon_fano)
print(" longitud media, rendimiento y redundancia del código de Shannon-Fano calculados.\n" )
print(L_sf, R_sf, p_sf)