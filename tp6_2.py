"""Realizar funciones booleanas en Python que reciban como parámetro la matriz de un canal
y verifiquen si se trata de:
a. Un canal sin ruido
b. Un canal determinante
"""
import utils

def es_canal_sin_ruido(matriz_canal: list[list[float]]) -> bool:
    if not matriz_canal:
        return False
        
    num_filas = len(matriz_canal)
    num_columnas = len(matriz_canal[0])

    for j_idx in range(num_columnas):
        contador_no_cero = 0
        
        for i_idx in range(num_filas):
            if matriz_canal[i_idx][j_idx] != 0.0:
                contador_no_cero += 1
                
        if contador_no_cero != 1:
            return False
            
    return True

def es_canal_determinante(matriz_canal: list[list[float]]) -> bool:
    if not matriz_canal:
        return False

    for fila_actual in matriz_canal:
        contador_no_cero = 0
        
        for probabilidad in fila_actual:
            if probabilidad != 0.0:
                contador_no_cero += 1
        
        if contador_no_cero != 1:
            return False
            
    return True

"""Dados los siguientes canales con entradas equiprobables:
0.0 1.0 0.0
0.0 0.0 1.0
0.0 1.0 0.0
1.0 0.0 0.0

1.0 0.0 0.0 0.0
0.0 0.2 0.0 0.8
0.0 0.0 1.0 0.0

0.3 0.5 0.2
0.2 0.3 0.5
0.5 0.2 0.3

0.0 0.0 1.0 0.0
1.0 0.0 0.0 0.0
0.0 1.0 0.0 0.0
0.0 0.0 0.0 1.0
a. Realizar una representación gráfica del canal
b. Informar si es un canal sin ruido y/o determinante
c. Calcular el ruido, la pérdida y la información"""

canales = [
    [[0.0, 1.0, 0.0],
        [0.0, 0.0, 1.0],
        [0.0, 1.0, 0.0],
        [1.0, 0.0, 0.0]],   
    [[1.0, 0.0, 0.0, 0.0],
        [0.0, 0.2, 0.0, 0.8],
        [0.0, 0.0, 1.0, 0.0]],
    [[0.3, 0.5, 0.2],
        [0.2, 0.3, 0.5],
        [0.5, 0.2, 0.3]],
    [[0.0, 0.0, 1.0, 0.0],
        [1.0, 0.0, 0.0, 0.0],
        [0.0, 1.0, 0.0, 0.0],
        [0.0, 0.0, 0.0, 1.0]]
]

for i, canal in enumerate(canales):
    probabilidades_entrada = [1/len(canal) for _ in range(len(canal))]
    print(f"Canal {i+1}:")
    
    sin_ruido = es_canal_sin_ruido(canal)
    determinante = es_canal_determinante(canal)
    
    print(f"  Es canal sin ruido: {sin_ruido}")
    print(f"  Es canal determinante: {determinante}")
    
    ruido = utils.calcular_equivocacion(probabilidades_entrada, canal)
    perdida = utils.calcular_perdida(probabilidades_entrada, canal)
    informacion = utils.calcular_informacion_mutua(probabilidades_entrada, canal)
    
    print(f"  Ruido: {ruido}")
    print(f"  Pérdida: {perdida}")
    print(f"  Información: {informacion}\n")