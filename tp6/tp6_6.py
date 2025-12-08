"""Desarrollar funciones en Python que reciban como parámetros: la matriz de un canal y los
índices de dos columnas, y realicen lo siguiente:
a. Verificar si las columnas se pueden combinar en una reducción suficiente
b. Generar la matriz del canal determinante necesario para combinar las columnas
"""

import utils
import math

def se_pueden_combinar_columnas(matriz_canal: list[list[float]], col1: int, col2: int) -> bool:
    """
    Verifica si dos columnas son combinables para una reducción suficiente.
    
    Esto es cierto si y solo si los vectores de las columnas son proporcionales,
    es decir, P(b_col1 | a_i) = C * P(b_col2 | a_i) para todas las entradas 'i'.
    """
    if not matriz_canal:
        return False
        
    num_filas = len(matriz_canal)
    constante_proporcionalidad = None

    # 1. Encontrar la constante de proporcionalidad (C)
    for i in range(num_filas):
        prob1 = matriz_canal[i][col1]
        prob2 = matriz_canal[i][col2]

        # Usamos math.isclose para manejar la precisión de los floats
        if not math.isclose(prob2, 0.0):
            # Encontramos una fila donde col2 no es cero,
            # esto define la constante
            constante_proporcionalidad = prob1 / prob2
            break
        elif not math.isclose(prob1, 0.0):
            # Si col2 es 0 pero col1 no es 0, la única forma de que
            # sean proporcionales es que col2 sea *siempre* 0.
            # Verificaremos esto en el paso 2.
            constante_proporcionalidad = float('inf') # Usamos inf como bandera
            break
    
    # Si ambas columnas son completamente cero, son proporcionales (C=cualquier cosa)
    if constante_proporcionalidad is None:
        return True

    # 2. Verificar que todas las filas respeten la constante
    for i in range(num_filas):
        prob1 = matriz_canal[i][col1]
        prob2 = matriz_canal[i][col2]
        
        if constante_proporcionalidad == float('inf'):
            # Si p1 > 0, p2 debe ser 0.
            if not math.isclose(prob2, 0.0):
                return False # p2 no fue 0
        else:
            # Comprobar P(b1|ai) = C * P(b2|ai)
            if not math.isclose(prob1, constante_proporcionalidad * prob2):
                return False
                
    return True

def generar_matriz_canal_determinante(matriz_canal: list[list[float]], col1: int, col2: int) -> list[list[float]]:
    if not matriz_canal:
        return []
        
    num_filas = len(matriz_canal)
    num_columnas = len(matriz_canal[0])
    
    nueva_matriz = []
    
    for i in range(num_filas):
        nueva_fila = []
        for j in range(num_columnas):
            if j == col1:
                nueva_fila.append(matriz_canal[i][col1] + matriz_canal[i][col2])
            elif j == col2:
                continue
            else:
                nueva_fila.append(matriz_canal[i][j])
        nueva_matriz.append(nueva_fila)
        
    return nueva_matriz

def generar_matriz_reducida(matriz_original: list[list[float]]) -> list[list[float]]:
    matriz_reducida = [fila[:] for fila in matriz_original]
    
    hubo_reduccion = True
    while hubo_reduccion:
        hubo_reduccion = False
        num_columnas_actual = len(matriz_reducida[0])
        
        for col1 in range(num_columnas_actual):
            for col2 in range(col1 + 1, num_columnas_actual):
                
                if se_pueden_combinar_columnas(matriz_reducida, col1, col2):
                    
                    matriz_reducida = generar_matriz_canal_determinante(matriz_reducida, col1, col2)
                    hubo_reduccion = True
                    break
            if hubo_reduccion:
                break
                
    return matriz_reducida

"""Dados los siguientes canales con entradas equiprobales:
0.4 0.6 0.0 0.0
0.0 0.0 0.5 0.5
0.0 0.0 0.7 0.3

0.2 0.3 0.5
0.0 0.0 1.0
0.0 0.0 1.0

0.4 0.0 0.2 0.4
0.4 0.3 0.2 0.1
0.0 0.3 0.0 0.7

0.0 0.5 0.0 0.5
0.8 0.0 0.2 0.0
0.0 0.5 0.0 0.5
0.8 0.0 0.2 0.0

a. Efectuar todas las reducciones suficientes posibles
b. Calcular la información mutua en cada paso
c. Verificar si se obtiene un canal reducido determinante"""

canales = [
    [[0.4, 0.6, 0.0, 0.0],
     [0.0, 0.0, 0.5, 0.5],
     [0.0, 0.0, 0.7, 0.3]],
     
    [[0.2, 0.3, 0.5],
     [0.0, 0.0, 1.0],
     [0.0, 0.0, 1.0]],
     
    [[0.4, 0.0, 0.2, 0.4],
     [0.4, 0.3, 0.2, 0.1],
     [0.0, 0.3, 0.0, 0.7]],
     
    [[0.0, 0.5, 0.0, 0.5],
     [0.8, 0.0, 0.2, 0.0],
     [0.0, 0.5, 0.0, 0.5],
     [0.8, 0.0, 0.2, 0.0]]
]

for idx, canal in enumerate(canales):
    print(f"Canal {idx + 1}:")
    matriz_actual = canal
    probs_entrada = [1 / len(matriz_actual) for _ in range(len(matriz_actual))]
    
    reducciones_realizadas = True
    while reducciones_realizadas:
        reducciones_realizadas = False
        num_columnas = len(matriz_actual[0])
        
        for col1 in range(num_columnas):
            for col2 in range(col1 + 1, num_columnas):
                if se_pueden_combinar_columnas(matriz_actual, col1, col2):
                    print(f"  Combinando columnas {col1} y {col2}")
                    matriz_actual = generar_matriz_canal_determinante(matriz_actual, col1, col2)
                    info_mutua = utils.calcular_informacion_mutua(probs_entrada, matriz_actual)
                    print(f"    Nueva matriz: {matriz_actual}")
                    print(f"    Información Mutua: {info_mutua}")
                    reducciones_realizadas = True
                    break
            if reducciones_realizadas:
                break
    
    es_determinante = utils.es_canal_determinante(matriz_actual)
    print(f"  Canal reducido determinante: {es_determinante}\n")