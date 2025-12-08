def calcular_probabilidad_error(prob_a_priori: list[float], 
                                matriz_canal: list[list[float]]) -> float:
    regla_decision = []
    for j in range(len(matriz_canal[0])):
        max_prob = -1.0
        mejor_i = 0
        for i in range(len(matriz_canal)):
            prob_actual = matriz_canal[i][j]
            if prob_actual > max_prob:
                max_prob = prob_actual
                mejor_i = i
        regla_decision.append(mejor_i)

    prob_error = 0.0
    for i in range(len(matriz_canal)):
        for j in range(len(matriz_canal[0])):
            if regla_decision[j] != i:
                prob_error += prob_a_priori[i] * matriz_canal[i][j]
    return prob_error

"""Calcular la probabilidad de error del siguiente canal, utilizando la regla de decisión de
máxima posibilidad. Considerar una distribución uniforme de probabilidades a priori.
0.6 0.4
0.2 0.8
"""

canal1 = [[0.6, 0.4],
         [0.2, 0.8]]

prob_a_priori_uniforme = [0.5, 0.5]

prob_error_canal1 = calcular_probabilidad_error(prob_a_priori_uniforme, canal1)
print(f"Probabilidad de error del canal 1: {prob_error_canal1:.4f}")
"""Determinar la probabilidad de error del canal para las siguientes distribuciones de
probabilidad a priori, utilizando la regla de decisión de máxima posibilidad:
0.6 0.3 0.1
0.1 0.8 0.1
0.3 0.3 0.4
a. { 1/3, 1/3, 1/3 }
b. { 1/8, 3/8, 4/8 }
c. { 4/15, 3/15, 8/15 }"""

canal2 = [[0.6, 0.3, 0.1],
          [0.1, 0.8, 0.1],
            [0.3, 0.3, 0.4]]

distribuciones_a_priori = {
    "Uniforme": [1/3, 1/3, 1/3],
    "Distribucion B": [1/8, 3/8, 4/8],
    "Distribucion C": [4/15, 3/15, 8/15]
}

for nombre_dist, prob_a_priori in distribuciones_a_priori.items():
    prob_error = calcular_probabilidad_error(prob_a_priori, canal2)
    print(f"Probabilidad de error de canal 2 con {nombre_dist}: {prob_error:.4f}")

canal3 =[[0.5, 0.2, 0.3],
         [0.2, 0.3, 0.5],
         [0.3, 0.3, 0.4] ]
prob_a_priori_canal3 = [1/3, 1/3, 1/3]

prob_error_canal3 = calcular_probabilidad_error(prob_a_priori_canal3, canal3)
print(f"Probabilidad de error del canal 3: {prob_error_canal3:.4f}")