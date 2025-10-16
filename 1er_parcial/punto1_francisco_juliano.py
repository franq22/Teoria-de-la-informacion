import math
import random



def get_mat_transicion_and_alfabeto(mensaje):
    """
    Construye la matriz de transición por columnas.
    Cada columna j corresponde al estado actual j,
    y contiene las probabilidades de transición hacia otros estados.
    """
    alfabeto = sorted(list(set(mensaje)))
    n = len(alfabeto)
    indices = {simbolo: i for i, simbolo in enumerate(alfabeto)}

    # Conteos por columnas
    conteos = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(len(mensaje) - 1):
        a, b = mensaje[i], mensaje[i+1]
        conteos[indices[b]][indices[a]] += 1

    matriz_col = []
    for j in range(n):
        col = [conteos[i][j] for i in range(n)]
        total = sum(col)
        if total == 0:
            matriz_col.append([0]*n)
        else:
            matriz_col.append([c/total for c in col])

    matriz_col = [[matriz_col[j][i] for j in range(n)] for i in range(n)]

    return alfabeto, matriz_col

def getAlfaProbabilidades(texto: str):
    alfabeto = []
    probabilidades = []
    longitud = len(texto)
    for simbolo in texto:
        if simbolo in alfabeto:
            index = alfabeto.index(simbolo)
            probabilidades[index] += 1
        else:
            alfabeto.append(simbolo)
            probabilidades.append(1)
    for i in range(len(probabilidades)):
        probabilidades[i] /= longitud
    return alfabeto, probabilidades

def es_memoria_nula(M, tol=0.01):
    for fila in M:
        if max(fila)-min(fila) > tol:
            return False
    return True

def cantidadInformacion(p: float, r=2) -> float:
    if p <= 0 or p > 1:
        resultado = 0
    else:
        resultado = math.log(1/p, r)
    return resultado

def entropia(probabilidades: list, r=2) -> float:
    H = 0
    for p in probabilidades:
        H += p * cantidadInformacion(p, r)
    return H

# Función recursiva para generar las combinaciones
def generar_combinaciones(alfabeto: list, N: int) -> list:
    if N == 1:
        return [[letra] for letra in alfabeto]
    else:
        combinaciones_previas = generar_combinaciones(alfabeto, N - 1)
        nuevas_combinaciones = []
        for combinacion in combinaciones_previas:
            for letra in alfabeto:
                nuevas_combinaciones.append(combinacion + [letra])
        return nuevas_combinaciones

# Esta función recibe una lista con el alfabeto de una fuente, otra
# con su distribución de probabilidades y un entero N, y genera dos nuevas
# listas con la extensión de orden N y su distribución de probabilidades
def generarConExtension(alfabeto: list, probabilidades: list[float], N: int):
    if N <= 0:
        return [], []

    # Generar las combinaciones de longitud N
    combinaciones = generar_combinaciones(alfabeto, N)

    # Calcular las probabilidades de cada combinación
    nuevas_probabilidades = []
    for combinacion in combinaciones:
        probabilidad = 1.0
        for letra in combinacion:
            indice = alfabeto.index(letra)
            probabilidad *= probabilidades[indice]
        nuevas_probabilidades.append(probabilidad)

    # Convertir las combinaciones de listas de letras a cadenas
    nuevas_letras = [''.join(str(combinacion)) for combinacion in combinaciones]

    return nuevas_letras, nuevas_probabilidades

def stationary_vector(M, max_iter=10000, tol=1e-12):
    n = len(M)
    v = [1.0/n] * n  

    for _ in range(max_iter):
        new_v = [0.0] * n
        for i in range(n):          
            for j in range(n):      
                new_v[i] += M[i][j] * v[j]

        diff = max(abs(new_v[k] - v[k]) for k in range(n))
        v = new_v
        if diff < tol:
            break
    return v

def markov_source_entropy(M):
    v = stationary_vector(M)
    H = 0.0
    n = len(M)

    for j in range(n):  
        probs = [M[i][j] for i in range(n)]
        H_j = 0.0
        for p in probs:
            if p > 0:
                H_j -= p * math.log(p, 2)
        H += v[j] * H_j
    return H

def resolver(mensaje):
    alfabeto, probs = getAlfaProbabilidades(mensaje)

    for i in range(len(alfabeto)):
        print(' P de', alfabeto[i],' ', probs[i])
    alfa, matriz = get_mat_transicion_and_alfabeto(mensaje)
    print(alfa)
    print('matriz ',matriz)

    if es_memoria_nula(matriz):
        print('Entropia: ',entropia(probs))
        print('es nula')
        alfa_ext, probs_ext = generarConExtension(alfabeto,probs,2)
        for i in range(len(alfa_ext)):
            print('P de ',alfa_ext[i],' ',probs_ext[i])
        print('Entropia de orden 2',entropia(probs_ext))
    else:
        print('Entropia de Markov: ',markov_source_entropy(matriz))
        print('no es nula')
        print('vector estacionario: ',stationary_vector(matriz))


mensaje1 = ';;,;,;:,,,.;,,.,,,::,;;;,:;.,,;:,,,:..;,;;.,;,,.:;'
resolver(mensaje1)
mensaje2 = ']]]([[]))([(])]([]([([([)([([([[([))][([([[([)([(]'
resolver(mensaje2)