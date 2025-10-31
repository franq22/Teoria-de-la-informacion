"""Implementar funciones en Python que reciban como parámetros: una lista con las
probabilidades a priori y la matriz de probabilidades condicionales del canal, y calculen por
definición (es decir, a partir de las probabilidades, no de sus relaciones):
a. La equivocación o ruido
b. La pérdida
c. La entropía afín
d. La información mutua"""

import utils
import math

def calcular_equivocacion(probs_entrada: list[float], matriz_canal: list[list[float]]) -> float:
    probs_salida = utils.calcular_prob_salida(probs_entrada, matriz_canal)
    equivocacion = 0.0

    for j in range(len(matriz_canal[0])):
        entropia_a_posteriori = 0.0
        for i in range(len(matriz_canal)):
            prob_a_posteriori = 0.0
            if probs_salida[j] > 0:
                prob_a_posteriori = (probs_entrada[i] * matriz_canal[i][j]) / probs_salida[j]
            if prob_a_posteriori > 0:
                entropia_a_posteriori += utils.cantidadInformacion(prob_a_posteriori) * prob_a_posteriori
        equivocacion += probs_salida[j] * entropia_a_posteriori

    return equivocacion

def calcular_perdida(probs_entrada: list[float], matriz_canal: list[list[float]]) -> float:
    perdida = 0.0

    for i in range(len(matriz_canal)):
        entropia_a_priori = 0.0
        for j in range(len(matriz_canal[0])):
            prob_a_priori = 0.0
            if probs_entrada[i] > 0:
                prob_a_priori = (probs_entrada[i] * matriz_canal[i][j]) / probs_entrada[i]
            if prob_a_priori > 0:
                entropia_a_priori += utils.cantidadInformacion(prob_a_priori) * prob_a_priori
        perdida += probs_entrada[i] * entropia_a_priori

    return perdida

def calcular_entropia_afin(probs_entrada: list[float], matriz_canal: list[list[float]]) -> float:
    matriz_simultanea = utils.calcular_matriz_simultanea(probs_entrada, matriz_canal)
    entropia_afin = 0.0
    num_a = len(probs_entrada)
    if num_a == 0: return 0.0
    num_b = len(matriz_canal[0])

    for i in range(num_a):
        for j in range(num_b):
            prob_conjunta = matriz_simultanea[i][j]
            if prob_conjunta > 0:
                entropia_afin += prob_conjunta * utils.cantidadInformacion(prob_conjunta)
                
    return entropia_afin

def calcular_informacion_mutua(probs_entrada: list[float], matriz_canal: list[list[float]]) -> float:
    matriz_simultanea = utils.calcular_matriz_simultanea(probs_entrada, matriz_canal)
    probs_salida = utils.calcular_prob_salida(probs_entrada, matriz_canal)
    informacion_mutua = 0.0
    num_a = len(probs_entrada)
    if num_a == 0: return 0.0
    num_b = len(probs_salida)

    for i in range(num_a):
        prob_ai = probs_entrada[i]
        for j in range(num_b):
            prob_bj = probs_salida[j]
            prob_conjunta = matriz_simultanea[i][j]
            if prob_conjunta > 0:
                termino_log = prob_conjunta / (prob_ai * prob_bj)
                informacion_mutua += prob_conjunta * math.log2(termino_log)
                
    return informacion_mutua

def calcular_informacion_mutua2(probs_entrada: list[float], matriz_canal: list[list[float]]) -> float:

    entropia_entrada = utils.entropia(probs_entrada)

    equivocacion = calcular_equivocacion(probs_entrada, matriz_canal)

    informacion_mutua = entropia_entrada - equivocacion

    return informacion_mutua

"""Dados los siguientes canales:
Canal Probabilidades a priori Matriz del canal
C1 { 0.70, 0.30 }
0.7 0.3
0.4 0.6
C2 { 0.50, 0.50 }
0.3 0.3 0.4
0.3 0.3 0.4
C3 { 0.25, 0.50, 0.25 }
1.0 0.0 0.0 0.0
0.0 0.5 0.5 0.0
0.0 0.0 0.0 1.0
C4 { 0.25, 0.25, 0.25, 0.25 }
1.0 0.0 0.0
0.0 1.0 0.0
0.0 1.0 0.0
0.0 0.0 1.0
a. Determinar la entropía a priori y la de la salida
b. Obtener la equivocación o ruido y la pérdida
c. Calcular la entropía afín a través de sus relaciones
d. Calcular la información mutua a través de sus relaciones"""

canales = {
    "C1": { "probs_entrada": [0.70, 0.30], "matriz_canal": [[0.7, 0.3], [0.4, 0.6]] },
    "C2": { "probs_entrada": [0.50, 0.50], "matriz_canal": [[0.3, 0.3, 0.4], [0.3, 0.3, 0.4]] },
    "C3": { "probs_entrada": [0.25, 0.50, 0.25], "matriz_canal": [[1.0, 0.0, 0.0, 0.0], [0.0, 0.5, 0.5, 0.0], [0.0, 0.0, 0.0, 1.0]] },
    "C4": { "probs_entrada": [0.25, 0.25, 0.25, 0.25], "matriz_canal": [[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]] }
}

for nombre_canal, datos in canales.items():
    probs_entrada = datos["probs_entrada"]
    matriz_canal = datos["matriz_canal"]

    entropia_entrada = utils.entropia(probs_entrada)
    probs_salida = utils.calcular_prob_salida(probs_entrada, matriz_canal)
    entropia_salida = utils.entropia(probs_salida)
    equivocacion = calcular_equivocacion(probs_entrada, matriz_canal)
    perdida = calcular_perdida(probs_entrada, matriz_canal)
    entropia_afin = calcular_entropia_afin(probs_entrada, matriz_canal)
    informacion_mutua = calcular_informacion_mutua(probs_entrada, matriz_canal)

    print(f"Canal {nombre_canal}:")
    print(f"  Entropía a priori: {entropia_entrada:.4f}")
    print(f"  Entropía de la salida: {entropia_salida:.4f}")
    print(f"  Equivocación o ruido: {equivocacion:.4f}")
    print(f"  Pérdida: {perdida:.4f}")
    print(f"  Entropía afín: {entropia_afin:.4f}")
    print(f"  Información mutua: {informacion_mutua:.4f}\n")
