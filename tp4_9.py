"""Dadas las siguientes fuentes, generar códigos de Huffman y de Shannon-Fano:
Símbolos S1 S2 S3 S4
Fuente A 0.2 0.2 0.3 0.3
Fuente B 0.4 0.25 0.25 0.1"""

import utils   

fuente_A_probs = [0.2, 0.2, 0.3, 0.3]
fuente_B_probs = [0.4, 0.25, 0.25, 0.1]

print("Fuente A:")
print("Código de Huffman:")
huffman_A = utils.huffman(fuente_A_probs)
print(huffman_A)
print("Código de Shannon-Fano:")
shannon_fano_A = utils.shannon_fano(fuente_A_probs)
print(shannon_fano_A)
print("\nFuente B:")
print("Código de Huffman:")
huffman_B = utils.huffman(fuente_B_probs)
print(huffman_B)
print("Código de Shannon-Fano:")
shannon_fano_B = utils.shannon_fano(fuente_B_probs)
print(shannon_fano_B)