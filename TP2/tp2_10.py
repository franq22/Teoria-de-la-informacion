import utils

# Función recursiva para generar las combinaciones
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

# Esta función recibe una lista con el alfabeto de una fuente, otra
# con su distribución de probabilidades y un entero N, y genera dos nuevas
# listas con la extensión de orden N y su distribución de probabilidades
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
    nuevas_letras = [''.join(str(combinacion)) for combinacion in combinaciones]

    return nuevas_letras, nuevas_probabilidades

simbolos = ['a', 'b', 'c', 'd']
prob = [0.1, 0.3, 0.4, 0.2]
n = 2
nuevos_simbolos, nuevas_prob = generarConExtension(simbolos, prob, n)
print(f'Simbolos con extension de orden {n}: {nuevos_simbolos}')
print(f'Probabilidades con extension de orden {n}: {nuevas_prob}')
print(f'Entropia con extension de orden {n}: {utils.entropia(nuevas_prob)}')
print( f'Entropia calculudad usando la ecuacion n*H(X): {n * utils.entropia(prob)}' )

n = 3
nuevos_simbolos, nuevas_prob = generarConExtension(simbolos, prob, n)
print(f'Simbolos con extension de orden {n}: {nuevos_simbolos}')
print(f'Probabilidades con extension de orden {n}: {nuevas_prob}')
print(f'Entropia con extension de orden {n}: {utils.entropia(nuevas_prob)}')
print( f'Entropia calculudad usando la ecuacion n*H(X): {n * utils.entropia(prob)}' )