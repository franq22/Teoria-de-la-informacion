"""
Implementar una función en Python que reciba como parámetros: un número entero N y
dos listas paralelas que contengan las palabras código de una codificación y sus
respectivas probabilidades, y genere aleatoriamente un posible mensaje de N símbolos
codificados emitido por dicha fuente
"""

import utils
import random

def generar_mensaje_aleatorio(N: int, codigo: list, probabilidades: list[float]) -> str:
    mensaje = random.choices(codigo, weights=probabilidades, k=N)
    return ''.join(mensaje)

probs = [0.10, 0.50, 0.10, 0.20, 0.05, 0.05]
codigo1 = ["==", "<", "<=", ">", ">=", "<>"]
codigo2 = [")", "[]", "]]", "([", "[()]", "([)]"]
codigo3 = ["/", "*", "-", "*", "++", "+-"]

print(generar_mensaje_aleatorio(10, codigo1, probs))
print(generar_mensaje_aleatorio(10, codigo2, probs))