import utils

# Calcula la entropía de una fuente binaria de memoria nula
# Precondición: omega debe estar en el rango [0, 1]
def entropiaBinaria(omega: float) -> float:
    return utils.entropia([omega, 1 - omega])

print(f'Entropia fuente binaria omega=0.1: {entropiaBinaria(0.1)}')
print(f'Entropia fuente binaria omega=0.25: {entropiaBinaria(0.25)}')