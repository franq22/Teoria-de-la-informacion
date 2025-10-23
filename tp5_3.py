"""Dadas las siguientes secuencias de entrada y sus respectivas salidas, las cuales describen
el comportamiento de los canales, calcular las probabilidades a priori y la matriz del canal.
Canal 1 Canal 2
Entrada 1101011001101010010101010100011111 110101100110101100110101100111110011
Salida 1001111111100011101101010111110110 110021102110022010220121122100112011"""

import utils

canal_1_entrada = "1101011001101010010101010100011111"
canal_1_salida = "1001111111100011101101010111110110"
canal_2_entrada = "110101100110101100110101100111110011"
canal_2_salida = "110021102110022010220121122100112011"

alfa1, probs1 = utils.getAlfaProbabilidades(canal_1_entrada)
print("Canal 1 - Alfabeto y probabilidades de entrada:", alfa1, probs1)
matriz_canal_1 = utils.calcular_matriz_canal(canal_1_entrada, canal_1_salida)
print("Canal 1 - Matriz del canal:")
for fila in matriz_canal_1:
    print(fila)

alfa2, probs2 = utils.getAlfaProbabilidades(canal_2_entrada)
print("Canal 2 - Alfabeto y probabilidades de entrada:", alfa2, probs2)
matriz_canal_2 = utils.calcular_matriz_canal(canal_2_entrada, canal_2_salida)
print("Canal 2 - Matriz del canal:")
for fila in matriz_canal_2:
    print(fila)
