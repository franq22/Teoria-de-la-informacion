""" Para una fuente binaria con ω = 0.7:
a. Obtener una codificación mediante el algoritmo de Huffman
b. Codificar la extensión de orden 2 mediante el algoritmo de Shannon-Fano
c. Comprobar si las codificaciones cumplen con el Primer Teorema de Shannon
"""

import utils
import heapq

def huffman(probabilidades):
    n = len(probabilidades)
    
    items = [[probabilidades[i], [i]] for i in range(n)]
    heapq.heapify(items)
    
    while len(items) > 1:
        item1 = heapq.heappop(items)  # menor
        item2 = heapq.heappop(items)  # segundo menor
        
        prob_combinada = item1[0] + item2[0]
        indices_combinados = item1[1] + item2[1]
        
        heapq.heappush(items, [prob_combinada, indices_combinados])
    

    codigos = [''] * n
    
    # Reiniciar la lista de items para asignar códigos
    items = [[probabilidades[i], [i]] for i in range(n)]
    heapq.heapify(items)
    
    # Diccionario para almacenar códigos parciales
    codigo_dict = {i: '' for i in range(n)}
    
    while len(items) > 1:
        item1 = heapq.heappop(items)
        item2 = heapq.heappop(items)
        
        # Asignar '1' al primero (menor) y '0' al segundo
        for idx in item1[1]:
            codigo_dict[idx] = '0' + codigo_dict[idx]
        for idx in item2[1]:
            codigo_dict[idx] = '1' + codigo_dict[idx]
        
        prob_combinada = item1[0] + item2[0]
        indices_combinados = item1[1] + item2[1]
        heapq.heappush(items, [prob_combinada, indices_combinados])
    
    return [codigo_dict[i] for i in range(n)]
    

def shannon_fano(probabilidades):
    """
    Implementa el algoritmo de Shannon-Fano para generar un código.
    
    Parámetros:
        - probabilidades (list): Lista de probabilidades
    
    Retorna:
        - list: Lista de códigos en el mismo orden que las probabilidades
    
    Ejemplo:
        >>> shannon_fano([0.20, 0.27, 0.40, 0.13])
        ['001', '01', '1', '000']
    """
    n = len(probabilidades)
    
    # Crear lista de items: [probabilidad, índice]
    items = [[probabilidades[i], i] for i in range(n)]
    
    # Ordenar por probabilidad descendente
    items.sort(reverse=True, key=lambda x: x[0])
    
    # Diccionario para almacenar códigos
    codigo_dict = {i: '' for i in range(n)}
    
    # Función recursiva para dividir y asignar códigos
    def dividir(items_grupo):
        if len(items_grupo) <= 1:
            return
        
        # Calcular el punto de división que hace las sumas más equilibradas
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
        
        # Dividir en dos grupos
        grupo_superior = items_grupo[:mejor_pos]
        grupo_inferior = items_grupo[mejor_pos:]
        
        # Asignar '1' al grupo superior y '0' al inferior
        for item in grupo_superior:
            codigo_dict[item[1]] = codigo_dict[item[1]] + '1'
        
        for item in grupo_inferior:
            codigo_dict[item[1]] = codigo_dict[item[1]] + '0'
        
        # Recursión en cada grupo
        dividir(grupo_superior)
        dividir(grupo_inferior)
    
    # Iniciar la división
    dividir(items)
    
    # Convertir diccionario a lista en orden original
    return [codigo_dict[i] for i in range(n)]




probabilidades = [0.7, 0.3]  # Fuente binaria-
codigo_huffman = huffman(probabilidades)
print("="*50)
print("Fuente binaria con ω = 0.7 ")
print(f"Código de Huffman: {codigo_huffman}\n")


alfa,probs_2 = utils.generarConExtension(codigo_huffman,probabilidades,2)
print("Extensión de orden 2:")
print(f"Símbolos: {alfa}")
print(f"Probabilidades: {probs_2}\n")
codigos = shannon_fano(probs_2)

print("\nCódigo de Shannon-Fano generado:")
print("-"*40)
print(f"Códigos: {codigos}")

print("primer Teorema de Shannon:", utils.teorema_shannon(probabilidades, codigo_huffman, 1))
print("cumplen con el Primer Teorema de Shannon:   ", utils.teorema_shannon(probs_2, codigos, 1))

