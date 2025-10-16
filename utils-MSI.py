import math
import random

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

# Funcion que devuelve alfabeto con sus probabilidades
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

    # Normalizar columnas
    matriz_col = []
    for j in range(n):
        col = [conteos[i][j] for i in range(n)]
        total = sum(col)
        if total == 0:
            matriz_col.append([0]*n)
        else:
            matriz_col.append([c/total for c in col])

    # Transponer para devolver en formato de listas de filas (cada fila es un vector-columna)
    matriz_col = [[matriz_col[j][i] for j in range(n)] for i in range(n)]

    return alfabeto, matriz_col


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


def simular_fuente(alfabeto, M, longitud, simbolo_inicial=None):
    n = len(alfabeto)
    if simbolo_inicial is None:
        estado = random.randrange(n)
    else:
        estado = alfabeto.index(simbolo_inicial)

    mensaje = [alfabeto[estado]]

    for _ in range(longitud - 1):
        # Distribución desde el estado actual (columna estado)
        probs = [M[i][estado] for i in range(n)]
        r = random.random()
        acum = 0
        for j, p in enumerate(probs):
            acum += p
            if r <= acum:
                estado = j
                break
        mensaje.append(alfabeto[estado])

    return "".join(mensaje)


def es_memoria_nula(M, tol=0.01):
    for fila in M:
        if max(fila)-min(fila) > tol:
            return False
    return True

def es_singular(codigos: list) -> bool:
    codigos_vistos = set()
    for codigo in codigos:
        if codigo in codigos_vistos:
            return True
        codigos_vistos.add(codigo)
    return False

def es_instantaneo(codigo: set) -> bool:
    """
    Un código es instantáneo si ningún símbolo es prefijo de otro.
    """
    codigo_lista = list(codigo)
    for i in range(len(codigo_lista)):
        for j in range(len(codigo_lista)):
            if i != j and codigo_lista[j].startswith(codigo_lista[i]):
                return False
    return True


def es_univocamente_decodificable(codigo: set) -> bool:
    S = [set(codigo), set()]
    i = 0
    seguir = True
    while seguir:
        for x in S[0]:
            for y in S[i]:
                if x.startswith(y) and x != y:
                    S[i+1].add(x[len(y):])
                else:
                    if y.startswith(x) and x != y:
                        S[i+1].add(y[len(x):])
        if codigo.intersection(S[i+1]) != set(): # Si la intersección no es vacía, no es unívocamente decodificable
            respuesta = False
            seguir = False
        else:
            if S[i+1] == set() or S[i+1] in S[0:i+1]:
                respuesta = True
                seguir = False
            else:
                S.append(set())
                i += 1
    return respuesta

def clasificar_codigo(codigo: list) -> str:
    if es_singular(codigo):
        return "bloque"
    elif es_instantaneo(set(codigo)):
        return "instantáneo"
    elif es_univocamente_decodificable(set(codigo)):
        return "univocamente decodificable"
    else:   
        return "no singular"
    
def get_longitudes( codigo):
    return [len(c) for c in codigo]

def get_alfabeto_codigos(C):
    x = ""
    for codigo in C:
        for caracter in codigo:
            if caracter not in x:
                x += caracter
    return x

def sumatoria_kraft(lista):
    r = len(get_alfabeto_codigos(lista))
    l = get_longitudes(lista)
    suma = sum([1/(r**i) for i in l])
    return suma 

def entropia_en_base_len_codigo(probabilidades, codigos):
    return entropia(probabilidades, len(get_alfabeto_codigos(codigos)))

def longitud_media(probabilidades, codigos):
    longitud_media = 0
    longitudes = get_longitudes(codigos)
    for p, l in zip(probabilidades, longitudes):
        longitud_media += p * l
    return longitud_media

def es_codigo_compacto(alfabeto_fuente: list, probabilidades: list, codigos: list, alfabeto_codigo: list = None) -> bool:
    """
    Condiciones:
    1. Li ≤ ⌈log_r(1/Pi)⌉ para cada símbolo i
    2. H ≤ L (la entropía debe ser menor o igual a la longitud media)
    
    """
    if not es_instantaneo(codigos):
        return False
    if alfabeto_codigo is None:
        alfabeto_codigo = ['0', '1']
    
    r = len(alfabeto_codigo)
    n = len(alfabeto_fuente)
    
    # Verificar condición 1
    for i in range(n):
        p = probabilidades[i]
        if p <= 0:
            continue
        
        longitud_real = len(codigos[i])
        longitud_maxima = math.ceil(math.log(1/p, r))
        
        if longitud_real > longitud_maxima:
            return False
    
    # Verificar condición 2: 
    H = entropia(probabilidades, r)
    L = longitud_media(probabilidades, codigos)
    
    if H > L:
        return False
    
    return True

def gen_codigo_compacto(alfabeto_fuente: list, probabilidades: list, alfabeto_codigo: list = None) -> list:
    """
    Genera un código compacto donde la longitud de cada palabra código
    es proporcional a su cantidad de información: l_i = ⌈log_r(1/p_i)⌉
    """
    if alfabeto_codigo is None:
        alfabeto_codigo = ['0', '1']
    
    r = len(alfabeto_codigo)  
    n = len(alfabeto_fuente)
    
    longitudes = []
    for p in probabilidades:
        if p > 0:
            l = math.ceil(math.log(1/p, r))
        else:
            l = 1  # Por defecto si p=0
        longitudes.append(l)
    
    # Ordenar símbolos por probabilidad (descendente) para asignar códigos
    indices_ordenados = sorted(range(n), key=lambda i: probabilidades[i], reverse=True)
    
    # Generar códigos asegurando que sean instantáneos (sin prefijos)
    codigos = [''] * n
    codigos_usados = []  # Mantener como lista para preservar orden
    prefijos_bloqueados = set()  # Prefijos que no pueden usarse
    
    for idx in indices_ordenados:
        longitud = longitudes[idx]
        codigo_encontrado = False
        
        # Generar todas las palabras de longitud 'longitud' hasta encontrar una válida
        palabras_candidatas = list(generar_palabras(alfabeto_codigo, longitud))
        
        for codigo_candidato in palabras_candidatas:
            # Verificar que no sea prefijo de ningún código usado
            # y que ningún código usado sea prefijo de este
            es_valido = True
            
            # Verificar que no comience con un prefijo bloqueado
            for prefijo in prefijos_bloqueados:
                if codigo_candidato.startswith(prefijo):
                    es_valido = False
                    break
            
            if not es_valido:
                continue
            
            # Verificar contra códigos ya usados
            for codigo_usado in codigos_usados:
                if codigo_candidato.startswith(codigo_usado) or codigo_usado.startswith(codigo_candidato):
                    es_valido = False
                    break
            
            if es_valido:
                codigos[idx] = codigo_candidato
                codigos_usados.append(codigo_candidato)
                # Bloquear este código como prefijo para futuros códigos
                prefijos_bloqueados.add(codigo_candidato)
                codigo_encontrado = True
                break
        
        if not codigo_encontrado:
            # Si no se encontró código válido, incrementar longitud
            longitud += 1
            longitudes[idx] = longitud
            palabras_candidatas = list(generar_palabras(alfabeto_codigo, longitud))
            
            for codigo_candidato in palabras_candidatas:
                es_valido = True
                
                for prefijo in prefijos_bloqueados:
                    if codigo_candidato.startswith(prefijo):
                        es_valido = False
                        break
                
                if not es_valido:
                    continue
                
                for codigo_usado in codigos_usados:
                    if codigo_candidato.startswith(codigo_usado) or codigo_usado.startswith(codigo_candidato):
                        es_valido = False
                        break
                
                if es_valido:
                    codigos[idx] = codigo_candidato
                    codigos_usados.append(codigo_candidato)
                    prefijos_bloqueados.add(codigo_candidato)
                    break
    
    return codigos


def generar_palabras(alfabeto: list, longitud: int):
    """
    Genera todas las palabras posibles de una longitud dada sobre un alfabeto,
    en orden lexicográfico.
    
    Parámetros:
        - alfabeto (list): Alfabeto a usar
        - longitud (int): Longitud de las palabras
    
    Retorna:
        - generator: Generador de palabras
    """
    if longitud == 0:
        yield ''
        return
    
    if longitud == 1:
        for simbolo in alfabeto:
            yield simbolo
    else:
        for simbolo in alfabeto:
            for palabra in generar_palabras(alfabeto, longitud - 1):
                yield simbolo + palabra
