import utils 

def mensaje_a_matriz(mensaje):
    alfabeto = sorted(list(set(mensaje)))
    n = len(alfabeto)
    indices = {simbolo: i for i, simbolo in enumerate(alfabeto)}

    # inicializamos matriz de conteos (igual que antes)
    conteos = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(len(mensaje) - 1):
        a, b = mensaje[i], mensaje[i+1]
        conteos[indices[a]][indices[b]] += 1

    # normalizamos filas
    matriz = []
    for fila in conteos:
        total = sum(fila)
        if total == 0:
            matriz.append([0]*n)
        else:
            matriz.append([c/total for c in fila])

    # transponer la matriz para tenerla en columnas
    matriz_col = [[matriz[i][j] for i in range(n)] for j in range(n)]

    return alfabeto, matriz_col


import random

def simular_fuente(alfabeto, matriz, longitud, simbolo_inicial=None):
    """
    Genera una cadena de longitud 'longitud' según la matriz de transición.
    """
    n = len(alfabeto)
    indices = {i: simbolo for i, simbolo in enumerate(alfabeto)}

    if simbolo_inicial is None:
        estado = random.randrange(n)
    else:
        estado = alfabeto.index(simbolo_inicial)

    mensaje = [alfabeto[estado]]

    for _ in range(longitud - 1):
        probs = matriz[estado]
        r = random.random()
        acum = 0
        for j, p in enumerate(probs):
            acum += p
            if r <= acum:
                estado = j
                break
        mensaje.append(indices[estado])

    return "".join(mensaje)


mensaje = "CAAACCAABAACBBCABACCAAABCBBACC"
alfabeto, matriz = mensaje_a_matriz(mensaje)

print("Alfabeto:", alfabeto)
print("Matriz de transición:")
for fila in matriz:
    print(fila)

simulado = simular_fuente(alfabeto, matriz, 20, simbolo_inicial="A")
print("Mensaje simulado:", simulado)

print("¿Fuente de memoria nula?:", utils.es_memoria_nula(matriz, tol= 0.1))
print("Entropia de la fuente; ", utils.markov_source_entropy(matriz), " bits/símbolo")
