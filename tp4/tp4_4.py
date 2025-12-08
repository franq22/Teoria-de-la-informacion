"""Para una fuente binaria con ω = 0.8, calcular la extensión de orden 3 y proponer una
codificación binaria que cumpla con el Primer Teorema de Shannon."""

import utils

probabilidades = [0.8, 0.2]  # Fuente binaria
codigo = ['0', '1']  # Código propuesto
N = 3  # Extensión de orden 3
print("="*50)
print("Fuente binaria con ω = 0.8 y N=3:")
print(f"Cumple teorema: {utils.teorema_shannon(probabilidades, codigo, N)}\n")