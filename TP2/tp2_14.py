import math

def stationary_vector(M, max_iter=10000, tol=1e-12):
    """
    Calcula el vector estacionario de una cadena de Markov
    usando el método iterativo de potencias.
    P: matriz de transición (lista de listas).
    """
    n = len(M)
    # distribución inicial uniforme
    v = [1.0/n] * n

    for _ in range(max_iter):
        new_v = [0.0] * n
        # multiplicación vector * matriz
        for j in range(n):
            for i in range(n):
                new_v[j] += v[i] * M[i][j]

        # calcular la diferencia máxima
        diff = max(abs(new_v[k] - v[k]) for k in range(n))
        v = new_v
        if diff < tol:
            break
    return v

def markov_source_entropy(M):
    """
    Calcula la entropía promedio de la fuente de Markov,
    en bits por símbolo.
    """
    v = stationary_vector(M)
    H = 0.0
    n = len(M)

    for i in range(n):
        H_i = 0.0
        for m in M[i]:
            if m > 0:
                H_i -= m * math.log(m, 2)
        H += v[i] * H_i
    return H

# Ejemplo con la matriz del ejercicio 13
M = [
    [0.5, 0.5, 0.0],
    [1/3, 1/3, 1/3],
    [0.0, 1.0, 0.0]
]

v = stationary_vector(M)
H = markov_source_entropy(M)

print("Vector estacionario:", v)
print("Entropía de la fuente:", H, "bits/símbolo")
