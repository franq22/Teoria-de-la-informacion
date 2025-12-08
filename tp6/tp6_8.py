import math
import utils

def es_canal_uniforme(matriz_canal: list[list[float]]) -> bool:
    """
    Verifica si un canal es uniforme (simétrico).
    
    Un canal es simétrico si todas sus filas son permutaciones
    entre sí
    """
    if not matriz_canal:
        return False
      
    num_filas = len(matriz_canal)
    firma_fila = sorted([round(p, 8) for p in matriz_canal[0]])
    
    for i in range(1, num_filas):
        fila_actual_ordenada = sorted([round(p, 8) for p in matriz_canal[i]])
        if fila_actual_ordenada != firma_fila:
            return False
            
    return True

def es_canal_determinante(matriz_canal: list[list[float]]) -> bool:
    """
    Verifica si el canal es Determinante (Sin Pérdida), H(B|A) = 0.
    Esto es cierto si cada FILA tiene exactamente un valor no nulo (usualmente 1.0).
    """
    if not matriz_canal:
        return False
    for fila in matriz_canal:
        contador_no_cero = 0
        for prob in fila:
            if not math.isclose(prob, 0.0):
                contador_no_cero += 1
        if contador_no_cero != 1:
            return False
    return True

def es_canal_sin_ruido(matriz_canal: list[list[float]]) -> bool:
    """
    Verifica si el canal es Sin Ruido (Sin Equivocación), H(A|B) = 0.
    Esto es cierto si cada COLUMNA tiene exactamente un valor no nulo (usualmente 1.0).
    """
    if not matriz_canal:
        return False
    num_filas = len(matriz_canal)
    num_columnas = len(matriz_canal[0])

    for j in range(num_columnas):
        contador_no_cero = 0
        for i in range(num_filas):
            if not math.isclose(matriz_canal[i][j], 0.0):
                contador_no_cero += 1
        if contador_no_cero != 1:
            return False
    return True

def calcular_capacidad(matriz_canal: list[list[float]]) -> float:

    num_entradas_r = len(matriz_canal)
    num_salidas_s = len(matriz_canal[0])

    if es_canal_determinante(matriz_canal):
        print(f"  (Detectado: Canal Determinante)")
        return math.log2(num_salidas_s)

    if es_canal_sin_ruido(matriz_canal):
        print(f"  (Detectado: Canal Sin Ruido)")
        return math.log2(num_entradas_r)
        
    if es_canal_uniforme(matriz_canal):
        print(f"  (Detectado: Canal Uniforme)")
        return math.log2(num_salidas_s) - utils.entropia(matriz_canal[0])

    raise ValueError("El canal no pertenece a un caso especial (Determinante, Sin Ruido o Uniforme).")

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
    capacidad = calcular_capacidad(canal)
    print(f"  Capacidad del canal: {capacidad:.4f} bits\n")