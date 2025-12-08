"""función en Python que reciba como parámetros las matrices de dos
canales y genere la matriz del canal compuesto por los canales en serie"""

import utils

def canal_compuesto_serie(matriz_canal_1: list[list[float]], matriz_canal_2: list[list[float]]) -> list[list[float]]:
    if not matriz_canal_1 or not matriz_canal_2:
        return []
        
    num_filas_canal_1 = len(matriz_canal_1)
    num_columnas_canal_1 = len(matriz_canal_1[0])
    num_filas_canal_2 = len(matriz_canal_2)
    num_columnas_canal_2 = len(matriz_canal_2[0])
    
    if num_columnas_canal_1 != num_filas_canal_2:
        raise ValueError("El número de columnas del primer canal debe ser igual al número de filas del segundo canal.")
    
    matriz_compuesta = [[0.0 for _ in range(num_columnas_canal_2)] for _ in range(num_filas_canal_1)]
    
    for i in range(num_filas_canal_1):
        for j in range(num_columnas_canal_2):
            suma = 0.0
            for k in range(num_columnas_canal_1):
                suma += matriz_canal_1[i][k] * matriz_canal_2[k][j]
            matriz_compuesta[i][j] = suma
            
    return matriz_compuesta

"""Dados los siguientes canales en serie (el primero con entradas equiprobables):
0.7 0.0 0.3 0.0
0.2 0.6 0.0 0.2

0.9 0.0 0.1
0.0 1.0 0.0
0.1 0.1 0.8
0.0 0.5 0.5
a. Determinar la equivocación y la información mutua de cada canal
b. Obtener la matriz del canal compuesto
c. Calcular la equivocación y la información mutua del canal compuesto
d. Comparar los resultados obtenidos en cada caso"""

canal_1 = [[0.7, 0.0, 0.3, 0.0],
              [0.2, 0.6, 0.0, 0.2]]
canal_2 = [[0.9, 0.0, 0.1],
              [0.0, 1.0, 0.0],
              [0.1, 0.1, 0.8],
              [0.0, 0.5, 0.5]]

probs_entrada_canal_1 = [0.5, 0.5]
equivocacion_canal_1 = utils.calcular_equivocacion_ruido(probs_entrada_canal_1, canal_1)
info_mutua_canal_1 = utils.calcular_informacion_mutua(probs_entrada_canal_1, canal_1)
print(f"Canal 1 - Equivocación: {equivocacion_canal_1}, Información Mutua: {info_mutua_canal_1}")
probs_entrada_canal_2 = utils.calcular_prob_salida(probs_entrada_canal_1, canal_1)
equivocacion_canal_2 = utils.calcular_equivocacion_ruido(probs_entrada_canal_2, canal_2)
info_mutua_canal_2 = utils.calcular_informacion_mutua(probs_entrada_canal_2, canal_2)
print(f"Canal 2 - Equivocación: {equivocacion_canal_2}, Información Mutua: {info_mutua_canal_2}")
canal_compuesto = canal_compuesto_serie(canal_1, canal_2)
probs_entrada_compuesto = [0.5, 0.5]
equivocacion_compuesto = utils.calcular_equivocacion_ruido(probs_entrada_compuesto, canal_compuesto)
info_mutua_compuesto = utils.calcular_informacion_mutua(probs_entrada_compuesto, canal_compuesto)
print(f"Canal Compuesto - Matriz: {canal_compuesto}")
print(f"Canal Compuesto - Equivocación: {equivocacion_compuesto}, Información Mutua: {info_mutua_compuesto}")

