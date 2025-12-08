"""Construir códigos de Huffman y de Shannon-Fano para fuentes de información que emiten
los siguientes mensajes representativos:
a. ABCDABCBDCBAAABBBCBCBABADBCBABCBDBCCCAAABB
b. AOEAOEOOOOEOAOEOOEOOEOAOAOEOEUUUIEOEOEO
"""

import utils
mensaje_a = "ABCDABCBDCBAAABBBCBCBABADBCBABCBDBCCCAAABB"
mensaje_b = "AOEAOEOOOOEOAOEOOEOOEOAOAOEOEUUUIEOEOEO"

alfa_a, probs_a = utils.getAlfaProbabilidades(mensaje_a)
alfa_b, probs_b = utils.getAlfaProbabilidades(mensaje_b)
print("Alfabeto y probabilidades mensaje a:")
print(list(zip(alfa_a, probs_a)))
print("\nAlfabeto y probabilidades mensaje b:")
print(list(zip(alfa_b, probs_b)))

print("Mensaje a:")
print("Código de Huffman:")
huffman_a = utils.huffman(probs_a)
print(huffman_a)
print("Código de Shannon-Fano:")
shannon_fano_a = utils.shannon_fano(probs_a)
print(shannon_fano_a)
print("\nMensaje b:")
print("Código de Huffman:")
huffman_b = utils.huffman(probs_b)
print(huffman_b)
print("Código de Shannon-Fano:")
shannon_fano_b = utils.shannon_fano(probs_b)
print(shannon_fano_b)
