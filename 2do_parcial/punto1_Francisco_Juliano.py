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

def cantidadInformacion(p: float, r=2) -> float:
    if p <= 0 or p > 1:
        resultado = 0
    else:
        resultado = math.log(1/p, r)
    return resultado

def entropia(probabilidades: list, r=2) -> float:
    H = 0
    for p in probabilidades:
        H += p * cantidadInformacion(p, r)
    return H

def shannon_fano(probabilidades):
    n = len(probabilidades)
    
    items = [[probabilidades[i], i] for i in range(n)]
    
    items.sort(reverse=True, key=lambda x: x[0])
    
    codigo_dict = {i: '' for i in range(n)}
    
    def dividir(items_grupo):
        if len(items_grupo) <= 1:
            return
        
        total = sum(item[0] for item in items_grupo)
        suma_acumulada = 0
        mejor_pos = 1
        mejor_diferencia = float('inf')
        
        for pos in range(1, len(items_grupo)):
            suma_izq = sum(item[0] for item in items_grupo[:pos])
            suma_der = sum(item[0] for item in items_grupo[pos:])
            diferencia = abs(suma_izq - suma_der)
            
            if diferencia < mejor_diferencia:
                mejor_diferencia = diferencia
                mejor_pos = pos
        
        grupo_superior = items_grupo[:mejor_pos]
        grupo_inferior = items_grupo[mejor_pos:]
        
        for item in grupo_superior:
            codigo_dict[item[1]] = codigo_dict[item[1]] + '1'
        
        for item in grupo_inferior:
            codigo_dict[item[1]] = codigo_dict[item[1]] + '0'
        
        dividir(grupo_superior)
        dividir(grupo_inferior)
    
    dividir(items)
    
    return [codigo_dict[i] for i in range(n)]

def tasa_de_compresion(mensaje_original: str, mensaje_codificado: bytearray) -> float:
    tam_original = len(mensaje_original) * 8  
    tam_codificado = len(mensaje_codificado) * 8  

    if tam_codificado == 0:
        return float('inf')  

    tasa_compresion = tam_original / tam_codificado
    return tasa_compresion

def codificar(mensaje, alfabeto, codificacion) -> bytearray:
    cod_dict = {simbolo: codigo for simbolo, codigo in zip(alfabeto, codificacion)}
    
    mensaje_codificado = ''.join(cod_dict[simbolo] for simbolo in mensaje)
    
    byte_array = bytearray()
    for i in range(0, len(mensaje_codificado), 8):
        byte = mensaje_codificado[i:i+8]
        byte_array.append(int(byte.ljust(8, '0'), 2))  
    
    return byte_array

def generar_combinaciones(alfabeto: list, N: int) -> list:
    if N == 1:
        return [[letra] for letra in alfabeto]
    else:
        combinaciones_previas = generar_combinaciones(alfabeto, N - 1)
        nuevas_combinaciones = []
        for combinacion in combinaciones_previas:
            for letra in alfabeto:
                nuevas_combinaciones.append(combinacion + [letra])
        return nuevas_combinaciones

def generarConExtension(alfabeto: list, probabilidades: list[float], N: int):
    if N <= 0:
        return [], []

    # Generar las combinaciones de longitud N
    combinaciones = generar_combinaciones(alfabeto, N)

    # Calcular las probabilidades de cada combinación
    nuevas_probabilidades = []
    for combinacion in combinaciones:
        probabilidad = 1.0
        for letra in combinacion:
            indice = alfabeto.index(letra)
            probabilidad *= probabilidades[indice]
        nuevas_probabilidades.append(probabilidad)

    # Convertir las combinaciones de listas de letras a cadenas
    nuevas_letras = [''.join(combinacion) for combinacion in combinaciones]

    return nuevas_letras, nuevas_probabilidades

def get_longitudes( codigo):
    return [len(c) for c in codigo]

def longitud_media(probabilidades, codigo):
    long = get_longitudes(codigo)
    L = sum([p * l for p, l in zip(probabilidades, long)])
    return L

def teorema_shannon(probabilidades, codigo, N):
    H = entropia(probabilidades)/N
    L = longitud_media(probabilidades, codigo)
    print(f"Entropía H: {H:.4f}")
    print(f"Longitud media L: {L:.4f}")
    print(f"L/N: {L/N:.4f}")
    return H <= L/N < H + 1/N
mensaje = "WTTWTUTWTVWVWVWTVVVT"
alfa, probs = getAlfaProbabilidades(mensaje)

alfa_probs = sorted(zip(alfa, probs))
alfa, probs = zip(*alfa_probs)

H = entropia(probs)
print(alfa)
print(probs)
print(f"Entropia fuente: {H:.4f}")
codigo = shannon_fano(probs)
print(codigo)

mensaje_codificado = codificar(mensaje, alfa, codigo)
tasa_comp = tasa_de_compresion(mensaje, mensaje_codificado)
print("tase de compresion: ", tasa_comp)
alfa_ext, probs_ext = generarConExtension(alfa,probs, 3)
codigo_ext = shannon_fano(probs_ext)

L_1 = longitud_media(probs, codigo)
ren1 = H/L_1
red1 = 1 - ren1
print(f"L1: {L_1:.4f}, rendimiento: {ren1:.4f}, redundancia: {red1:.4f}")

L_3 = longitud_media(probs_ext, codigo_ext)
ren3 = entropia(probs_ext)/L_3
red3 = 1 - ren3
print(f"L3: {L_3:.4f}, rendimiento: {ren3:.4f}, redundancia: {red3:.4f}")

print("Cumple shannon el primer codigo?", teorema_shannon(probs, codigo, 1))
print("Cumple shannon el codigo de la tercera extension?", teorema_shannon(probs_ext, codigo_ext, 3))
