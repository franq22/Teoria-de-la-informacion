"""Desarrollar una función en Python que reciba como parámetros: una lista con las
probabilidades a priori y la matriz de probabilidades condicionales del canal, y retorne una
lista con las entropías a posteriori.
"""

import utils

def calcular_entropias_a_posteriori(probs_entrada: list[float], matriz_canal: list[list[float]]) -> list[float]:
    alfabeto_B = sorted(list(range(len(matriz_canal[0]))))  
    probs_salida = utils.calcular_prob_salida(probs_entrada, matriz_canal)
    entropias_a_posteriori = []

    for j, b in enumerate(alfabeto_B):
        entropia = 0.0
        for i, a in enumerate(range(len(matriz_canal))):
            prob_a_posteriori = 0.0
            if probs_salida[j] > 0:
                prob_a_posteriori = (probs_entrada[i] * matriz_canal[i][j]) / probs_salida[j]
            if prob_a_posteriori > 0:
                entropia += utils.cantidadInformacion(prob_a_posteriori) * prob_a_posteriori
        entropias_a_posteriori.append(entropia)

    return entropias_a_posteriori


""" Calcular las entropías a priori y a posteriori de los siguientes canales:
Canal Probabilidades a priori Matriz del canal
C1 { 0.14, 0.52, 0.34 }
0.50 0.30 0.20
0.00 0.40 0.60
0.20 0.80 0.00
C2 { 0.25, 0.25, 0.50 }
0.25 0.25 0.25 0.25
0.25 0.25 0.00 0.50
0.50 0.00 0.50 0.00
C3 { 0.12, 0.24, 0.14, 0.50 }
0.25 0.15 0.30 0.30
0.23 0.27 0.25 0.25
0.10 0.40 0.25 0.25
0.34 0.26 0.20 0.20"""

canal_1_probs_entrada = [0.14, 0.52, 0.34]
canal_1_matriz = [
    [0.50, 0.30, 0.20],
    [0.00, 0.40, 0.60],
    [0.20, 0.80, 0.00]
]
canal_2_probs_entrada = [0.25, 0.25, 0.50]
canal_2_matriz = [
    [0.25, 0.25, 0.25, 0.25],
    [0.25, 0.25, 0.00, 0.50],
    [0.50, 0.00, 0.50, 0.00]
]
canal_3_probs_entrada = [0.12, 0.24, 0.14, 0.50]
canal_3_matriz = [
    [0.25, 0.15, 0.30, 0.30],
    [0.23, 0.27, 0.25, 0.25],
    [0.10, 0.40, 0.25, 0.25],
    [0.34, 0.26, 0.20, 0.20]
]

entropias_a_posteriori_canal_1 = calcular_entropias_a_posteriori(canal_1_probs_entrada, canal_1_matriz)
print("Canal 1 - Entropías a posteriori:", entropias_a_posteriori_canal_1)
entropia_a_priori_canal_1 = utils.entropia(canal_1_probs_entrada)
print("Canal 1 - Entropía a priori:", entropia_a_priori_canal_1)
entropias_a_posteriori_canal_2 = calcular_entropias_a_posteriori(canal_2_probs_entrada, canal_2_matriz)
print("Canal 2 - Entropías a posteriori:", entropias_a_posteriori_canal_2)
entropia_a_priori_canal_2 = utils.entropia(canal_2_probs_entrada)
print("Canal 2 - Entropía a priori:", entropia_a_priori_canal_2)
entropias_a_posteriori_canal_3 = calcular_entropias_a_posteriori(canal_3_probs_entrada, canal_3_matriz)
print("Canal 3 - Entropías a posteriori:", entropias_a_posteriori_canal_3)
entropia_a_priori_canal_3 = utils.entropia(canal_3_probs_entrada)
print("Canal 3 - Entropía a priori:", entropia_a_priori_canal_3)
