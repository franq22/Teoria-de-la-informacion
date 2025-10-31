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

probs_salida = utils.calcular_prob_salida(probs, matriz)
print("Probabilidades de los símbolos de salida:", probs_salida)
probs_a_posteriori = utils.calcular_prob_a_posteriori(probs, matriz)
print("Probabilidades a posteriori P(A|B):")
for i, a in enumerate(alfabeto_A):
    fila_posteriori = {}
    for j, b in enumerate(alfabeto_B):
        fila_posteriori[b] = probs_a_posteriori[i][j]
    print(f"P(A={a}|B):", fila_posteriori)

simulteanos = utils.calcular_prob_simultaneas(probs, matriz)
print("Probabilidades simultáneas P(A,B):")
for i, a in enumerate(alfabeto_A):
    fila_simultaneos = {}
    for j, b in enumerate(alfabeto_B):
        fila_simultaneos[b] = simulteanos[i][j]
    print(f"P(A={a},B):", fila_simultaneos)

entropia_a_priori = utils.entropia(probs)
print("Entropía a priori H(A):", entropia_a_priori) 
entropia_a_posteriori = utils.calcular_entropias_a_posteriori(probs, matriz)
print("Entropías a posteriori H(A|B):", entropia_a_posteriori)