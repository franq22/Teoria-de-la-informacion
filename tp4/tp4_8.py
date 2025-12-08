"""Comparar los rendimientos y las redundancias de los siguientes códigos:
Fuente Probs Código 1 Código 2 Código 3 Código 4
A 0.2 01 00 0110 11
B 0.15 111 01 010 001
C 0.1 110 10 0111 000
D 0.3 101 110 1 10
E 0.25 100 111 00 01
"""

import utils

fuente_probs = [0.2, 0.15, 0.1, 0.3, 0.25]
C1 = ["01", "111", "110", "101", "100"]
C2 = ["00", "01", "10", "110", "111"]
C3 = ["0110", "010", "0111", "1", "00"]
C4 = ["11", "001", "000", "10", "01"]

print("Código 1:")
rendimiento, redundancia = utils.rendimiento_redundancia(fuente_probs, C1)
print(f"Rendimiento: {rendimiento:.4f}, Redundancia: {redundancia:.4f}\n")
print("Código 2:")
rendimiento, redundancia = utils.rendimiento_redundancia(fuente_probs, C2)
print(f"Rendimiento: {rendimiento:.4f}, Redundancia: {redundancia:.4f}\n")
print("Código 3:")
rendimiento, redundancia = utils.rendimiento_redundancia(fuente_probs, C3)
print(f"Rendimiento: {rendimiento:.4f}, Redundancia: {redundancia:.4f}\n")
print("Código 4:")
rendimiento, redundancia = utils.rendimiento_redundancia(fuente_probs, C4)
print(f"Rendimiento: {rendimiento:.4f}, Redundancia: {redundancia:.4f}\n")
