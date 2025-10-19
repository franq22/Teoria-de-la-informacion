import math
import random
import heapq

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
    nuevas_letras = [''.join(combinacion) for combinacion in combinaciones]

    return nuevas_letras, nuevas_probabilidades

# Función para calcular la cantidad de información
# p: probabilidad del evento
# r: base del logaritmo (default 2)
# retorna la cantidad de información en bits (si r=2)
def cantidadInformacion(p: float, r=2) -> float:
    if p <= 0 or p > 1:
        resultado = 0
    else:
        resultado = math.log(1/p, r)
    return resultado

# Funcion para calcular entropia
# probabilidades: lista de probabilidades de los eventos
# r: base del logaritmo (default 2)
# retorna la entropia en bits (si r=2)
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

def mensaje_a_matriz(mensaje):
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
    """
    Calcula el vector estacionario con convención por columnas:
    v_{k+1} = M * v_k
    """
    n = len(M)
    v = [1.0/n] * n  # inicial uniforme

    for _ in range(max_iter):
        new_v = [0.0] * n
        # multiplicación M * v
        for i in range(n):          # fila i
            for j in range(n):      # columna j
                new_v[i] += M[i][j] * v[j]

        # diferencia máxima
        diff = max(abs(new_v[k] - v[k]) for k in range(n))
        v = new_v
        if diff < tol:
            break
    return v


def markov_source_entropy(M):
    """
    Entropía promedio de la fuente (bits/símbolo),
    con convención por columnas.
    """
    v = stationary_vector(M)
    H = 0.0
    n = len(M)

    for j in range(n):  # estado actual
        # Distribución de transición desde j = columna j
        probs = [M[i][j] for i in range(n)]
        H_j = 0.0
        for p in probs:
            if p > 0:
                H_j -= p * math.log(p, 2)
        H += v[j] * H_j
    return H


def simular_fuente(alfabeto, M, longitud, simbolo_inicial=None):
    """
    Genera un mensaje usando la matriz por columnas.
    """
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


def es_memoria_nula(M, tol=1e-9):
    """
    Fuente de memoria nula si todas las columnas son iguales (dentro de tol).
    """
    n = len(M)
    # Tomamos la primera columna como referencia
    ref_col = [M[i][0] for i in range(n)]
    for j in range(1, n):
        for i in range(n):
            if abs(M[i][j] - ref_col[i]) > tol:
                return False
    return True

def es_singular(codigos: list) -> bool:
    """
    Determina si un codigo de encriptación es singular; es decir, si existen dos letras que se encripten de la misma manera.

    Parametros:
        - codigos (list): Lista de códigos.
    Retorna:
        - bool: True si el código es singular, False en caso contrario.
    Precondiciones:
        - codigos no está vacía.
        - codigos es distinto de None.
    """
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
    """
    Verifica si un código es unívocamente decodificable.

    Parámetros:
        - codigo (set): Lista de cadenas que representan el código.
    Retorna:
        - bool: True si el código es unívocamente decodificable, False en caso contrario.
    Precondiciones:
        - codigo no está vacío.
        - codigo es distinto de None
        - el codigo es no singular
    """
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
    """
    Clasifica un código como instantáneo, sin prefijo, o no sin prefijo.
    """
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

def longitud_media(probabilidades, codigo):
    long = get_longitudes(codigo)
    L = sum([p * l for p, l in zip(probabilidades, long)])
    return L

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

def teorema_shannon(probabilidades, codigo, N):
    H = entropia(probabilidades, r=len(get_alfabeto_codigos(codigo)))/N
    L = longitud_media(probabilidades, codigo)
    print(f"Entropía H: {H:.4f} (base {len(get_alfabeto_codigos(codigo))})")
    print(f"Longitud media L: {L:.4f}")
    print(f"L/N: {L/N:.4f}")
    return H <= L/N < H + 1/N


def huffman(probabilidades):
    n = len(probabilidades)
    
    items = [[probabilidades[i], [i]] for i in range(n)]
    heapq.heapify(items)
    
    while len(items) > 1:
        item1 = heapq.heappop(items)  # menor
        item2 = heapq.heappop(items)  # segundo menor
        
        prob_combinada = item1[0] + item2[0]
        indices_combinados = item1[1] + item2[1]
        
        heapq.heappush(items, [prob_combinada, indices_combinados])
    

    codigos = [''] * n
    
    # Reiniciar la lista de items para asignar códigos
    items = [[probabilidades[i], [i]] for i in range(n)]
    heapq.heapify(items)
    
    # Diccionario para almacenar códigos parciales
    codigo_dict = {i: '' for i in range(n)}
    
    while len(items) > 1:
        item1 = heapq.heappop(items)
        item2 = heapq.heappop(items)
        
        # Asignar '1' al primero (menor) y '0' al segundo
        for idx in item1[1]:
            codigo_dict[idx] = '0' + codigo_dict[idx]
        for idx in item2[1]:
            codigo_dict[idx] = '1' + codigo_dict[idx]
        
        prob_combinada = item1[0] + item2[0]
        indices_combinados = item1[1] + item2[1]
        heapq.heappush(items, [prob_combinada, indices_combinados])
    
    return [codigo_dict[i] for i in range(n)]
    

def shannon_fano(probabilidades):
    n = len(probabilidades)
    
    # Crear lista de items: [probabilidad, índice]
    items = [[probabilidades[i], i] for i in range(n)]
    
    # Ordenar por probabilidad descendente
    items.sort(reverse=True, key=lambda x: x[0])
    
    # Diccionario para almacenar códigos
    codigo_dict = {i: '' for i in range(n)}
    
    # Función recursiva para dividir y asignar códigos
    def dividir(items_grupo):
        if len(items_grupo) <= 1:
            return
        
        # Calcular el punto de división que hace las sumas más equilibradas
        total = sum(item[0] for item in items_grupo)
        suma_acumulada = 0
        mejor_pos = 1
        mejor_diferencia = float('inf')
        
        for pos in range(1, len(items_grupo)):
            suma_izq = sum(item[0] for item in items_grupo[:pos])
            suma_der = sum(item[0] for item in items_grupo[pos:])
            diferencia = abs(suma_izq - suma_der)
            
            if diferencia < mejor_diferencia:
                mejor_diferencia = diferencia
                mejor_pos = pos
        
        # Dividir en dos grupos
        grupo_superior = items_grupo[:mejor_pos]
        grupo_inferior = items_grupo[mejor_pos:]
        
        # Asignar '1' al grupo superior y '0' al inferior
        for item in grupo_superior:
            codigo_dict[item[1]] = codigo_dict[item[1]] + '1'
        
        for item in grupo_inferior:
            codigo_dict[item[1]] = codigo_dict[item[1]] + '0'
        
        # Recursión en cada grupo
        dividir(grupo_superior)
        dividir(grupo_inferior)
    
    # Iniciar la división
    dividir(items)
    
    # Convertir diccionario a lista en orden original
    return [codigo_dict[i] for i in range(n)]

def rendimiento_redundancia(probabilidades, codigos):  

    H = entropia(probabilidades, r=len(get_alfabeto_codigos(codigos)))
    L = longitud_media(probabilidades, codigos)
    
    rendimiento = H / L if L != 0 else 0
    redundancia = 1 - rendimiento
    
    return rendimiento, redundancia