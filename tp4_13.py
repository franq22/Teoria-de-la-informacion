"""Dada una fuente de información que emite el siguiente mensaje representativo:
58784784525368669895745123656253698989656452121702300223659
a. Calcular la entropía de la fuente
b. Construir una codificación de Huffman
c. Generar una codificación de Shannon-Fano
d. Comparar la longitud media, el rendimiento y la redundancia de cada código"""

import utils

mensaje = "58784784525368669895745123656253698989656452121702300223659"
alfa, probs = utils.getAlfaProbabilidades(mensaje)
H = utils.entropia(probs) 
print(f"Entropía de la fuente: {H:.4f} bits/símbolo")
print("\nAlfabeto y probabilidades:")
for simbolo, prob in zip(alfa, probs):
    print(f"Símbolo: {simbolo}, Probabilidad: {prob:.4f}")
huffman_cod = utils.huffman(probs)
shannon_fano_cod = utils.shannon_fano(probs)
print("\nCodificación de Huffman:")
print(huffman_cod)
print("\nCodificación de Shannon-Fano:")
print(shannon_fano_cod)
L_huffman = utils.longitud_media(probs, huffman_cod)
L_shannon_fano = utils.longitud_media(probs, shannon_fano_cod)
n_huffman, R_huffman = utils.rendimiento_redundancia(probs, huffman_cod)
n_shannon_fano, R_shannon_fano = utils.rendimiento_redundancia(probs, shannon_fano_cod)
print(f"\nLongitud media de Huffman: {L_huffman:.4f} bits/símbolo")
print(f"Rendimiento de Huffman: {n_huffman:.4f}")
print(f"Redundancia de Huffman: {R_huffman:.4f} bits/símbolo")
print(f"\nLongitud media de Shannon-Fano: {L_shannon_fano:.4f} bits/símbolo")
print(f"Rendimiento de Shannon-Fano: {n_shannon_fano:.4f}")
print(f"Redundancia de Shannon-Fano: {R_shannon_fano:.4f} bits/símbolo") 