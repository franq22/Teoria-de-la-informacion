"""
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
0.34 0.26 0.20 0.20
a. Determinar la entropía a priori y la de la salida
b. Obtener la equivocación o ruido y la pérdida
c. Calcular la entropía afín a través de sus relaciones
d. Calcular la información mutua a través de sus relaciones
"""

import utils

canales = {
    "C1": { "probs_entrada": [0.14, 0.52, 0.34], "matriz_canal": [[0.50, 0.30, 0.20], [0.00, 0.40, 0.60], [0.20, 0.80, 0.00]] },
    "C2": { "probs_entrada": [0.25, 0.25, 0.50], "matriz_canal": [[0.25, 0.25, 0.25, 0.25], [0.25, 0.25, 0.00, 0.50], [0.50, 0.00, 0.50, 0.00]] },
    "C3": { "probs_entrada": [0.12, 0.24, 0.14, 0.50], "matriz_canal": [[0.25, 0.15, 0.30, 0.30], [0.23, 0.27, 0.25, 0.25], [0.10, 0.40, 0.25, 0.25], [0.34, 0.26, 0.20, 0.20]] }
}

for nombre_canal, datos in canales.items():
    probs_entrada = datos["probs_entrada"]
    matriz_canal = datos["matriz_canal"]

    entropia_entrada = utils.entropia(probs_entrada)
    probs_salida = utils.calcular_prob_salida(probs_entrada, matriz_canal)
    entropia_salida = utils.entropia(probs_salida)
    equivocacion = utils.calcular_equivocacion(probs_entrada, matriz_canal)
    perdida = utils.calcular_perdida(probs_entrada, matriz_canal)
    entropia_afin = utils.calcular_entropia_afin(probs_entrada, matriz_canal)
    informacion_mutua = utils.calcular_informacion_mutua(probs_entrada, matriz_canal)

    print(f"Canal {nombre_canal}:")
    print(f"  Entropía a priori: {entropia_entrada:.4f}")
    print(f"  Entropía de la salida: {entropia_salida:.4f}")
    print(f"  Equivocación o ruido: {equivocacion:.4f}")
    print(f"  Pérdida: {perdida:.4f}")
    print(f"  Entropía afín: {entropia_afin:.4f}")
    print(f"  Información mutua: {informacion_mutua:.4f}\n")