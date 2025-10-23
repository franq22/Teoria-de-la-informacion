"""Realizar funciones en Python que reciban como parámetros: una lista con las
probabilidades a priori y la matriz de probabilidades condicionales del canal, y devuelvan:
a. Una lista con las probabilidades de los símbolos de salida
b. Una matriz con las probabilidades a posteriori del canal
c. Una matriz con las probabilidades de los eventos simultáneos"""

import utils

def calcular_prob_simultaneas(prob_a_priori: list[float], 
                               matriz_canal: list[list[float]]) -> list[list[float]]:
    """
    Calcula la matriz de probabilidades simultáneas P(ai, bj).
    P(ai, bj) = P(bj | ai) * P(ai)
    """
    num_a = len(prob_a_priori)
    if num_a == 0:
        return []
    
    num_b = len(matriz_canal[0])
    
    # Crear una matriz vacía para los resultados
    matriz_simultanea = [[0.0 for _ in range(num_b)] for _ in range(num_a)]
    
    for i in range(num_a):  # 'i' itera sobre las entradas (filas)
        for j in range(num_b):  # 'j' itera sobre las salidas (columnas)
            prob_ai = prob_a_priori[i]
            prob_bj_dado_ai = matriz_canal[i][j]
            
            matriz_simultanea[i][j] = prob_bj_dado_ai * prob_ai
            
    return matriz_simultanea

def calcular_prob_salida(prob_a_priori: list[float], 
                          matriz_canal: list[list[float]]) -> list[float]:
    """
    Calcula la lista de probabilidades de los símbolos de salida P(bj).
    P(bj) = Σ [P(ai, bj)] para todo i
    """
    # Primero, obtener la matriz de probabilidades conjuntas
    matriz_simultanea = calcular_prob_simultaneas(prob_a_priori, matriz_canal)
    
    if not matriz_simultanea:
        return []
        
    num_a = len(matriz_simultanea)
    num_b = len(matriz_simultanea[0])
    
    prob_salida_bj = [0.0 for _ in range(num_b)]
    
    for j in range(num_b):  # Iterar sobre cada columna (salida bj)
        suma_columna = 0.0
        for i in range(num_a):  # Sumar todas las filas (entradas ai)
            suma_columna += matriz_simultanea[i][j]
        prob_salida_bj[j] = suma_columna
        
    return prob_salida_bj

def calcular_prob_a_posteriori(prob_a_priori: list[float], 
                                matriz_canal: list[list[float]]) -> list[list[float]]:
    """
    Calcula la matriz de probabilidades a posteriori P(ai | bj).
    P(ai | bj) = P(ai, bj) / P(bj)
    """
    # 1. Calcular el numerador: P(ai, bj)
    matriz_simultanea = calcular_prob_simultaneas(prob_a_priori, matriz_canal)
    
    # 2. Calcular el denominador: P(bj)
    prob_salida_bj = calcular_prob_salida(prob_a_priori, matriz_canal)
    
    if not matriz_simultanea:
        return []

    num_a = len(matriz_simultanea)
    num_b = len(matriz_simultanea[0])
    
    # Crear la matriz para los resultados
    matriz_a_posteriori = [[0.0 for _ in range(num_b)] for _ in range(num_a)]
    
    for i in range(num_a):
        for j in range(num_b):
            numerador = matriz_simultanea[i][j]
            denominador = prob_salida_bj[j]
            
            if denominador == 0:
                # Si P(bj) es 0, este evento de salida es imposible
                matriz_a_posteriori[i][j] = 0.0 
            else:
                matriz_a_posteriori[i][j] = numerador / denominador
                
    return matriz_a_posteriori

"""Considerar un canal que recibe mensajes de un alfabeto A = { a, b, c }, con probabilidades
P = { 0.3, 0.3, 0.4 }, y entrega mensajes con un alfabeto B = { 1, 2, 3 }, caracterizado por la
siguiente matriz de probabilidades condicionales:
    1   2   3
a 0.4 0.4 0.2
b 0.3 0.2 0.5
c 0.3 0.4 0.3
a. Calcular las probabilidades de los símbolos de salida
b. Obtener las probabilidades a posteriori del canal
c. Determinar las probabilidades de los eventos simultáneos"""

prob_a_priori = [0.3, 0.3, 0.4]  # P(a), P(b), P(c)
matriz_canal = [
    [0.4, 0.4, 0.2],  # P(1|a), P(2|a), P(3|a)
    [0.3, 0.2, 0.5],  # P(1|b), P(2|b), P(3|b)
    [0.3, 0.4, 0.3]   # P(1|c), P(2|c), P(3|c)
]

# a. Calcular las probabilidades de los símbolos de salida
prob_salida = calcular_prob_salida(prob_a_priori, matriz_canal)
print("Probabilidades de los símbolos de salida P(bj):", prob_salida)

# b. Obtener las probabilidades a posteriori del canal
matriz_a_posteriori = calcular_prob_a_posteriori(prob_a_priori, matriz_canal)
print("Matriz de probabilidades a posteriori P(ai | bj):")
for fila in matriz_a_posteriori:
    print(fila)

# c. Determinar las probabilidades de los eventos simultáneos
matriz_simultanea = calcular_prob_simultaneas(prob_a_priori, matriz_canal)
print("Matriz de probabilidades simultáneas P(ai, bj):")
for fila in matriz_simultanea:
    print(fila)