""" Codificar una función booleana en Python que reciba como parámetros: una lista con la
distribución de probabilidades de una fuente, otra lista con palabras código para la
extensión de orden N y el valor de N, y verifique si el código cumple con el Primer Teorema
de Shannon.
"""

import utils

"""def teorema_shannon(probabilidades, codigo, N):
    # Obtener el alfabeto del código (base r)
    alfabeto_codigo = utils.get_alfabeto_codigos(codigo)
    r = len(alfabeto_codigo)
    
    # Calcular entropía de la fuente original en base r
    H = utils.entropia(probabilidades, r)
    
    cod_extension, prob_extension = utils.generarConExtension(codigo, probabilidades, N)
    
    print(cod_extension, prob_extension)

    # Obtener longitudes de las palabras código
    longitudes = utils.get_longitudes(codigo)
    
    # Calcular longitud media
    L = utils.longitud_media(prob_extension, cod_extension)
    
    print(f"Entropía H: {H:.4f} (base {r})")
    print(f"Longitud media L: {L:.4f}")
    print(f"L/N: {L/N:.4f}")
    print(f"H ≤ L/N < H + 1/N: {H:.4f} ≤ {L/N:.4f} < {H + 1/N:.4f}")
    
    # Verificar el teorema: H ≤ L/N < H + 1/N
    cumple_inferior = H <= L/N + 1e-10  # tolerancia numérica
    cumple_superior = L/N < H + 1/N + 1e-10
    
    return cumple_inferior and cumple_superior
"""

def teorema_shannon(probabilidades, codigo, N):
    s_n, probabilidades_n = utils.generarConExtension(codigo, probabilidades, N)
    L_n = utils.longitud_media(probabilidades_n, s_n)
    entropia = utils.entropia(probabilidades, r=len(utils.get_alfabeto_codigos(codigo)))
    print(f"Entropía H: {entropia:.4f} (base {len(utils.get_alfabeto_codigos(codigo))})")
    print(f"Longitud media L: {L_n:.4f}")
    print(f"L/N: {L_n/N:.4f}")
    print(f"H ≤ L/N < H + 1/N: {entropia:.4f} ≤ {L_n/N:.4f} < {entropia + 1/N:.4f}")
    return entropia <= L_n/N < entropia + 1/N

# Pruebas
print("="*50)
print("Ejemplo 1 con N=1:")
probs = [0.3, 0.1, 0.4, 0.2]
codigo_n1 = ['BA', 'CAB', 'A', 'CBA']  
N = 1
print(f"Cumple teorema: {teorema_shannon(probs, codigo_n1, N)}\n")
print("rendimiento y redundancia:")
rendimiento, redundancia = utils.rendimiento_redundancia(probs, codigo_n1)
print(f"Rendimiento: {rendimiento:.4f}, Redundancia: {redundancia:.4f}\n")

print("="*50)
print("Ejemplo 1 con N=2:")
N = 2
print(f"Cumple teorema: {teorema_shannon(probs, codigo_n1, N)}\n")
print("rendimiento y redundancia:")
rendimiento, redundancia = utils.rendimiento_redundancia(
    [p1*p2 for p1 in probs for p2 in probs],
    [c1 + c2 for c1 in codigo_n1 for c2 in codigo_n1]
)
print(f"Rendimiento: {rendimiento:.4f}, Redundancia: {redundancia:.4f}\n")
print("="*50)
print("Ejemplo 2 - Código 1 con N=1:")
probs2 = [0.5, 0.2, 0.3]
codigo1 = ['11', '010', '00']  # 3 códigos
print(f"Cumple teorema: {teorema_shannon(probs2, codigo1, 1)}\n")
print("rendimiento y redundancia:")
rendimiento, redundancia = utils.rendimiento_redundancia(probs2, codigo1)
print(f"Rendimiento: {rendimiento:.4f}, Redundancia: {redundancia:.4f}\n")
print("="*50)
print("Ejemplo 2 - Código 1 con N=2:")
probs2 = [0.5, 0.2, 0.3]
codigo1 = ['11', '010', '00']  # 3 códigos
print(f"Cumple teorema: {teorema_shannon(probs2, codigo1, 2)}\n")
print("rendimiento y redundancia:")
rendimiento, redundancia = utils.rendimiento_redundancia(
    [p1*p2 for p1 in probs2 for p2 in probs2],
    [c1 + c2 for c1 in codigo1 for c2 in codigo1]
)
print(f"Rendimiento: {rendimiento:.4f}, Redundancia: {redundancia:.4f}\n")
C2 = ["10", "001", "110", "010", "0000", "0001", "111", "0110", "0111"]
P_2 = [probs2[i]*probs2[j] for i in range(len(probs2)) for j in range(len(probs2))]
print("="*50)
print("Ejemplo 2 - Código 2 con N=2:")
print(f"Cumple teorema: {teorema_shannon(P_2, C2, 1)}\n")
