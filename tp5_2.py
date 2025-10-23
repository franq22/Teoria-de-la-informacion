"""Codificar una función en Python que reciba como parámetros dos cadenas de caracteres
que contengan secuencias de entrada y de salida de un canal y retorne la matriz que
representa dicho canal.
"""

import utils

def calcular_matriz_canal(secuencia_entrada: str, secuencia_salida: str) -> list[list[float]]:
    if len(secuencia_entrada) != len(secuencia_salida):
        raise ValueError("Las secuencias de entrada y salida deben tener la misma longitud.")

    alfabeto_A = sorted(list(set(secuencia_entrada)))
    alfabeto_B = sorted(list(set(secuencia_salida)))

    conteo_conjunto = {a: {b: 0 for b in alfabeto_B} for a in alfabeto_A}
    conteo_entrada = {a: 0 for a in alfabeto_A}
    
    for a, b in zip(secuencia_entrada, secuencia_salida):
        conteo_conjunto[a][b] += 1
        conteo_entrada[a] += 1
            
    matriz_canal = []
    
    for a in alfabeto_A:
        fila_actual = []
        total_a = conteo_entrada[a]
        
        for b in alfabeto_B:
            if total_a > 0:
                probabilidad = conteo_conjunto[a][b] / total_a
            else:
                probabilidad = 0.0  
            
            fila_actual.append(probabilidad)
        
        matriz_canal.append(fila_actual)
                
    return matriz_canal


# Ejemplo de uso
entrada = "abcacaabbcacaabcacaaabcaca"
salida = "01010110011001000100010011"
alfabeto_A = sorted(list(set(entrada)))
alfabeto_B = sorted(list(set(salida)))
print("Alfabeto de entrada (A):", alfabeto_A)
print("Alfabeto de salida (B):", alfabeto_B)
matriz = calcular_matriz_canal(entrada, salida)
alfa, probs = utils.getAlfaProbabilidades(entrada)
print("Alfabeto y probabilidades de entrada:", alfa, probs)
