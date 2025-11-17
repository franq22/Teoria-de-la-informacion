import utils

def estimar_capacidad_binaria(matriz_canal: list[list[float]], paso: float) -> tuple[float, list[float]]:
    """
    Estima la capacidad de un canal binario (2 entradas) calculando
    I(A;B) para diferentes P(A) y encontrando el máximo.

    Parámetros:
    - matriz_canal: La matriz de probabilidad condicional P(B|A).
    - paso: El incremento para probar las probabilidades (ej: 0.1, 0.01).

    Retorna:
    - tupla (capacidad_estimada, probabilidad_optima)
    """
    
        
    maxima_informacion = -1.0  # Usamos -1 para asegurar que el primer cálculo sea mayor
    probabilidad_optima = [0.0, 1.0]
    
    p = 0.0
    
    # 2. Iterar sobre todas las posibles distribuciones de entrada P(A)
    # P(A) = [p, 1-p]
    # Iteramos p desde 0.0 hasta 1.0
    while p <= 1.00001: # Usamos una tolerancia para incluir el 1.0 exacto
        
        prob_a_priori = [p, 1.0 - p]
        
        # 3. Calcular la información mutua para esta P(A)
        info_actual = utils.calcular_informacion_mutua( prob_a_priori, matriz_canal )
        
        # 4. Actualizar el máximo si es necesario
        if info_actual > maxima_informacion:
            maxima_informacion = info_actual
            probabilidad_optima = prob_a_priori
            
        p += paso
        
    return maxima_informacion, probabilidad_optima

"""Para cada uno de los siguientes canales binarios, determinar su capacidad y la distribución
de probabilidades a priori que maximiza la información mutua:
0.60 0.40
0.20 0.80

0.25 0.75
0.90 0.10

0.51 0.49
0.72 0.28

0.77 0.23
0.20 0.80
"""

canales_binarios = [
    [[0.60, 0.40],
        [0.20, 0.80]],
        [[0.25, 0.75],
        [0.90, 0.10]],
        [[0.51, 0.49],
        [0.72, 0.28]],
        [[0.77, 0.23],
        [0.20, 0.80]]
]

for i, canal in enumerate(canales_binarios):
    capacidad, prob_optima = estimar_capacidad_binaria(canal, paso=0.0001)
    print(f"Canal Binario {i+1}:")
    print(f"  Capacidad Estimada: {capacidad:.4f} bits")
    print(f"  Distribución P(A) Óptima: {prob_optima}")
