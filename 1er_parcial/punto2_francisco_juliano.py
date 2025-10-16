import math
import random

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

def get_longitudes( codigo):
    return [len(c) for c in codigo]

def get_alfabeto_codigos(C):
    x = ""
    for codigo in C:
        for caracter in codigo:
            if caracter not in x:
                x += caracter
    return x

def es_instantaneo(codigo: set) -> bool:
    """
    Un código es instantáneo si ningún símbolo es prefijo de otro.
    """
    codigo_lista = list(codigo)
    for i in range(len(codigo_lista)):
        for j in range(len(codigo_lista)):
            if i != j and codigo_lista[j].startswith(codigo_lista[i]):
                return False
    return True

def sumatoria_kraft(lista):
    r = len(get_alfabeto_codigos(lista))
    l = get_longitudes(lista)
    suma = sum([1/(r**i) for i in l])
    return suma 

def entropia_en_base_len_codigo(probabilidades, codigos):
    return entropia(probabilidades, len(get_alfabeto_codigos(codigos)))

def longitud_media(probabilidades, codigos):
    longitud_media = 0
    longitudes = get_longitudes(codigos)
    for p, l in zip(probabilidades, longitudes):
        longitud_media += p * l
    return longitud_media

def es_singular(codigos: list) -> bool:
    codigos_vistos = set()
    for codigo in codigos:
        if codigo in codigos_vistos:
            return True
        codigos_vistos.add(codigo)
    return False

def es_codigo_compacto(alfabeto_fuente: list, probabilidades: list, codigos: list, alfabeto_codigo: list = None) -> bool:
    """
    Condiciones:
    1. Li ≤ ⌈log_r(1/Pi)⌉ para cada símbolo i
    2. H ≤ L (la entropía debe ser menor o igual a la longitud media)
    
    """
    if not es_instantaneo(codigos):
        return False
    if alfabeto_codigo is None:
        alfabeto_codigo = ['0', '1']
    
    r = len(alfabeto_codigo)
    n = len(alfabeto_fuente)
    
    # Verificar condición 1
    for i in range(n):
        p = probabilidades[i]
        if p <= 0:
            continue
        
        longitud_real = len(codigos[i])
        longitud_maxima = math.ceil(math.log(1/p, r))
        
        if longitud_real > longitud_maxima:
            return False
    
    # Verificar condición 2: 
    H = entropia(probabilidades, r)
    L = longitud_media(probabilidades, codigos)
    
    if H > L:
        return False
    
    return True

def es_univocamente_decodificable(codigo: set) -> bool:
    S = [codigo]
    S.append(set())
    i = 0
    seguir = True
    print('S ',i,' ',S[i])
    while seguir:
        for x in S[0]:
            for y in S[i]:
                if x.startswith(y) and x != y:
                    S[i+1].add(x[len(y):])
                else:
                    if y.startswith(x) and x != y:
                        S[i+1].add(y[len(x):])
        print('S ',i+1,' ',S[i+1])
        if codigo.intersection(S[i+1]) != set(): # Si la intersección no es vacía, no es unívocamente decodificable
            respuesta = False
            seguir = False
        else:
            if S[i+1] == set() or S[i+1] in S[0:i+1]:
                respuesta = True
                seguir = False
            else:
                S.append(set())
                i += 1
    return respuesta

def clasificar_codigo(codigo: list) -> str:
    if es_singular(codigo):
        return "bloque"
    elif es_instantaneo(set(codigo)):
        return "instantáneo"
    elif es_univocamente_decodificable(set(codigo)):
        return "univocamente decodificable"
    else:   
        return "no singular"

def resolver(codigo, probs, alfa_fuente):
    print('Entropia: ', entropia_en_base_len_codigo(probs, codigo))
    print('Longitud media:', longitud_media(probs, codigo))
    print('Kraft: ', sumatoria_kraft(codigo))
    print('Clasificacion: ',clasificar_codigo(codigo))
    print('Es compacto? ',es_codigo_compacto(alfa_fuente,probs,codigo,get_alfabeto_codigos(codigo)))

print('Primer codigo:')
alfa_fuente=['S1','S2','S3','S4','S5']
codigo1 = ['])','(',')[','[','(]']
probs1 = [0.15, 0.25, 0.05, 0.45, 0.10]
resolver(codigo1, probs1,alfa_fuente)
print('Segundo codigo:')
codigo2 = ['(]',']','[)',')','([']
resolver(codigo2,probs1, alfa_fuente)