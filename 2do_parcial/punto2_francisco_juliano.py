import math

def getAlfaProbabilidades(texto: str):
    alfabeto = []
    probabilidades = []
    longitud = len(texto)
    for simbolo in texto:
        if simbolo in alfabeto:
            index = alfabeto.index(simbolo)
            probabilidades[index] += 1
        else:
            alfabeto.append(simbolo)
            probabilidades.append(1)
    for i in range(len(probabilidades)):
        probabilidades[i] /= longitud
    return alfabeto, probabilidades

def getAlfaProbabilidades_binario(texto: str):
    alfabeto = ['0', '1']
    longitud = len(texto)
    
    if longitud == 0:
        return alfabeto, [0.0, 0.0]
        
    count_0 = texto.count('0')
    count_1 = texto.count('1')
    
    prob_0 = count_0 / longitud
    prob_1 = count_1 / longitud
    
    probabilidades = [prob_0, prob_1]
    
    return alfabeto, probabilidades

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

def cantidadInformacion(p: float, r=2) -> float:
    if p <= 0 or p > 1:
        resultado = 0
    else:
        resultado = math.log(1/p, r)
    return resultado


def calcular_equivocacion_ruido(probs_entrada: list[float], matriz_canal: list[list[float]], probs_salida) -> float:
    equivocacion = 0.0

    for j in range(len(matriz_canal[0])):
        entropia_a_posteriori = 0.0
        for i in range(len(matriz_canal)):
            prob_a_posteriori = 0.0
            if probs_salida[j] > 0:
                prob_a_posteriori = (probs_entrada[i] * matriz_canal[i][j]) / probs_salida[j]
            if prob_a_posteriori > 0:
                entropia_a_posteriori += cantidadInformacion(prob_a_posteriori) * prob_a_posteriori
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
                entropia_a_priori += cantidadInformacion(prob_a_priori) * prob_a_priori
        perdida += probs_entrada[i] * entropia_a_priori

    return perdida

def calcular_matriz_simultanea(prob_a_priori: list[float], 
                               matriz_canal: list[list[float]]) -> list[list[float]]:
    num_a = len(prob_a_priori)
    if num_a == 0:
        return []
    
    num_b = len(matriz_canal[0])
    
    matriz_simultanea = [[0.0 for _ in range(num_b)] for _ in range(num_a)]
    
    for i in range(num_a):  
        for j in range(num_b):  
            prob_ai = prob_a_priori[i]
            prob_bj_dado_ai = matriz_canal[i][j]
            
            matriz_simultanea[i][j] = prob_bj_dado_ai * prob_ai
            
    return matriz_simultanea

def calcular_prob_salida(prob_a_priori: list[float], 
                          matriz_canal: list[list[float]]) -> list[float]:
    """
    Calcula la lista de probabilidades de los símbolos de P(bj).
    P(bj) = Σ [P(ai, bj)] para todo i
    """

    matriz_simultanea = calcular_matriz_simultanea(prob_a_priori, matriz_canal)
    
    if not matriz_simultanea:
        return []
        
    num_a = len(matriz_simultanea)
    num_b = len(matriz_simultanea[0])
    
    prob_salida_bj = [0.0 for _ in range(num_b)]
    
    for j in range(num_b):  
        suma_columna = 0.0
        for i in range(num_a):  
            suma_columna += matriz_simultanea[i][j]
        prob_salida_bj[j] = suma_columna
        
    return prob_salida_bj

def calcular_informacion_mutua(probs_entrada: list[float], matriz_canal: list[list[float]]) -> float:
    matriz_simultanea = calcular_matriz_simultanea(probs_entrada, matriz_canal)
    probs_salida = calcular_prob_salida(probs_entrada, matriz_canal)
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

def se_pueden_combinar_columnas(matriz_canal: list[list[float]], col1: int, col2: int) -> bool:
    if not matriz_canal:
        return False
        
    num_filas = len(matriz_canal)
    constante_proporcionalidad = None

    for i in range(num_filas):
        prob1 = matriz_canal[i][col1]
        prob2 = matriz_canal[i][col2]

        if not math.isclose(prob2, 0.0):
            constante_proporcionalidad = prob1 / prob2
            break
        elif not math.isclose(prob1, 0.0):
            constante_proporcionalidad = float('inf') 
            break
    
    if constante_proporcionalidad is None:
        return True

    for i in range(num_filas):
        prob1 = matriz_canal[i][col1]
        prob2 = matriz_canal[i][col2]
        
        if constante_proporcionalidad == float('inf'):
            if not math.isclose(prob2, 0.0):
                return False 
        else:
            if not math.isclose(prob1, constante_proporcionalidad * prob2):
                return False
                
    return True

def generar_matriz_canal_determinante(matriz_canal: list[list[float]], col1: int, col2: int) -> list[list[float]]:
    if not matriz_canal:
        return []
        
    num_filas = len(matriz_canal)
    num_columnas = len(matriz_canal[0])
    
    nueva_matriz = []
    
    for i in range(num_filas):
        nueva_fila = []
        for j in range(num_columnas):
            if j == col1:
                nueva_fila.append(matriz_canal[i][col1] + matriz_canal[i][col2])
            elif j == col2:
                continue
            else:
                nueva_fila.append(matriz_canal[i][j])
        nueva_matriz.append(nueva_fila)
        
    return nueva_matriz

def generar_matriz_reducida(matriz_original: list[list[float]]) -> list[list[float]]:
    matriz_reducida = [fila[:] for fila in matriz_original]
    
    hubo_reduccion = True
    while hubo_reduccion:
        hubo_reduccion = False
        num_columnas_actual = len(matriz_reducida[0])
        
        for col1 in range(num_columnas_actual):
            for col2 in range(col1 + 1, num_columnas_actual):
                
                if se_pueden_combinar_columnas(matriz_reducida, col1, col2):
                    
                    matriz_reducida = generar_matriz_canal_determinante(matriz_reducida, col1, col2)
                    hubo_reduccion = True
                    break
            if hubo_reduccion:
                break
                
    return matriz_reducida

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

def entropia(probabilidades: list, r=2) -> float:
    H = 0
    for p in probabilidades:
        H += p * cantidadInformacion(p, r)
    return H

def calcular_capacidad_binaria(matriz_canal: list[list[float]], paso: float) -> tuple[float, list[float]]: 
        
    maxima_informacion = -1.0  
    probabilidad_optima = [0.0, 1.0]
    
    p = 0.0
    
    while p <= 1.000001: # Tolerancia para incluir el 1.0 exacto
        
        prob_a_priori = [p, 1.0 - p]
        
        info_actual = calcular_informacion_mutua( prob_a_priori, matriz_canal )
        
        if info_actual > maxima_informacion:
            maxima_informacion = info_actual
            probabilidad_optima = prob_a_priori
            
        p += paso
        
    return maxima_informacion, probabilidad_optima

def calcular_probabilidad_error(prob_a_priori: list[float], 
                                matriz_canal: list[list[float]]) -> float:
    regla_decision = []
    for j in range(len(matriz_canal[0])):
        max_prob = -1.0
        mejor_i = 0
        for i in range(len(matriz_canal)):
            prob_actual = prob_a_priori[i] * matriz_canal[i][j]
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

def detectar_y_corregir_errores(matriz_str):
    matriz = [list(fila) for fila in matriz_str]
    filas = len(matriz)
    columnas = len(matriz[0])

    filas_con_error = []
    columnas_con_error = []

    # Verificar paridad cruzada
    corner_bit = matriz[0][-1]
        
    # Calcular paridad de la fila LRC 
    lrc_bits = matriz[0][:-1]
    calc_lrc_parity = '1' if "".join(lrc_bits).count('1') % 2 != 0 else '0'
    
    # Calcular paridad de la columna VRC 
    vrc_bits = [matriz[i][-1] for i in range(1, filas)]
    calc_vrc_parity = '1' if "".join(vrc_bits).count('1') % 2 != 0 else '0'

    if calc_lrc_parity != corner_bit or calc_vrc_parity != corner_bit:
        return "—"     

    # Verificar paridad de filas (VRC)
    for i in range(1, filas):
        data_bits = matriz[i][:-1]  
        given_parity_bit = matriz[i][-1] 
        calculated_parity = '1' if "".join(data_bits).count('1') % 2 != 0 else '0'
        if calculated_parity != given_parity_bit:
            filas_con_error.append(i)

    # Verificar paridad de columnas (LRC)
    for j in range(columnas - 1):
        data_bits = [matriz[i][j] for i in range(1, filas)] 
        given_parity_bit = matriz[0][j]
        calculated_parity = '1' if "".join(data_bits).count('1') % 2 != 0 else '0'
        if calculated_parity != given_parity_bit:
            columnas_con_error.append(j)

    # Analizar y corregir errores
    
    if len(filas_con_error) == 1 and len(columnas_con_error) == 1: 
        fila = filas_con_error[0]
        columna = columnas_con_error[0]
        bit_actual = matriz[fila][columna]
        matriz[fila][columna] = '1' if bit_actual == '0' else '0'
    elif (len(filas_con_error) != 0 or len(columnas_con_error) != 0):
        return "—"

    # Decodificar el mensaje
    mensaje_decodificado = ''
    try:
        for i in range(1, filas): 
            bits_ascii = "".join(matriz[i][:-1]) # Toma los 7 bits de datos
            valor_ascii = int(bits_ascii, 2)
            mensaje_decodificado += chr(valor_ascii)
    except (ValueError, TypeError):
        return "—" 

    return mensaje_decodificado

entrada = "10011111101000101000101110110100"
salida = "LKKMKMLLKKMJJKJKKKKJKKJMJKKKJLJK"

alfa_apriori, probs_apriori = getAlfaProbabilidades(entrada)
alfa_probs = sorted(zip(alfa_apriori, probs_apriori))
alfa_apriori, probs_apriori = zip(*alfa_probs)
print("Alfabeto apriori:", alfa_apriori)
print("Probabilidades apriori:", probs_apriori)
alfa_salida, probs_salida = getAlfaProbabilidades(salida)
alfa_probs = sorted(zip(alfa_salida, probs_salida))
alfa_salida, probs_salida = zip(*alfa_probs)
print("Alfabeto salida:", alfa_salida)
print("Probabilidades salida:", probs_salida)

matriz = calcular_matriz_canal(entrada, salida)
for fila in matriz:
    print(fila)
print("Es canal sin ruido?", es_canal_sin_ruido(matriz))
print("Es canal determinante?", es_canal_determinante(matriz))
equivocacion = calcular_equivocacion_ruido(probs_apriori, matriz, probs_salida)
peridida = calcular_perdida(probs_apriori, matriz)
print(f"H(A/B) = {equivocacion:.4f}")
print(f"H(B/A) = {peridida:.4f}")
print(f"I(A;B) = {calcular_informacion_mutua(probs_apriori, matriz):.4f}")

canal_reducido = generar_matriz_reducida(matriz)
for fila in canal_reducido:
    print(fila)
capacidad, prob_optima = calcular_capacidad_binaria(canal_reducido, 0.01)
print(f"Capacidad del canal: {capacidad:.4f}")
print(f"Probabilidades óptimas de entrada: {prob_optima}")

prob_error = calcular_probabilidad_error(probs_apriori, matriz)
print(f"Probabilidad de error: {prob_error:.4f}")
matriz_str = [entrada[i:i+8] for i in range(0, len(entrada), 8)]
mensaje_decodificado = detectar_y_corregir_errores(matriz_str)
print(mensaje_decodificado)

