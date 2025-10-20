"""Implementar una función en Python que reciba una lista de cadenas de caracteres que
representa una codificación binaria y devuelva: la distancia de Hamming, la cantidad de
errores que se pueden detectar y la cantidad de errores que se pueden corregir."""

def hamming_distance(codes):
    if len(codes) < 2:
        return 0, 0, 0 

    min_distance = float('inf')
    
    # Calcular la distancia de Hamming mínima entre todas las parejas de códigos
    for i in range(len(codes)):
        for j in range(i + 1, len(codes)):
            distance = sum(c1 != c2 for c1, c2 in zip(codes[i], codes[j]))
            if distance < min_distance:
                min_distance = distance

    # Calcular la cantidad de errores que se pueden detectar y corregir
    errors_detectable = min_distance - 1
    errors_correctable = (min_distance - 1) // 2

    return min_distance, errors_detectable, errors_correctable

""". Dados los siguientes códigos que representan colores:
Color Código 1 Código 2 Código 3
Rojo 00 000 0000
Amarillo 01 100 0011
Verde 10 101 1010
Azul 11 111 0101"""

codigo1 = ["00", "01", "10", "11"]
codigo2 = ["000", "100", "101", "111"]
codigo3 = ["0000", "0011", "1010", "0101"]

distancia1, detectable1, corregible1 = hamming_distance(codigo1)
distancia2, detectable2, corregible2 = hamming_distance(codigo2)
distancia3, detectable3, corregible3 = hamming_distance(codigo3)

print(f"Código 1: Distancia de Hamming = {distancia1}, Errores Detectables = {detectable1}, Errores Corregibles = {corregible1}")
print(f"Código 2: Distancia de Hamming = {distancia2}, Errores Detectables = {detectable2}, Errores Corregibles = {corregible2}")
print(f"Código 3: Distancia de Hamming = {distancia3}, Errores Detectables = {detectable3}, Errores Corregibles = {corregible3}")

"""Dados los siguientes códigos que representan colores:
Color Código 1 Código 2 Código 3
Rojo 0100100 0100100 0110000
Amarillo 0101000 0010010 0000011
Verde 0010010 0101000 0101101
Azul 0100000 0100001 0100110
"""

codigo4 = ["0100100", "0101000", "0010010", "0100000"]
codigo5 = ["0100100", "0010010", "0101000", "0100001"]
codigo6 = ["0110000", "0000011", "0101101", "0100110"]

distancia4, detectable4, corregible4 = hamming_distance(codigo4)
distancia5, detectable5, corregible5 = hamming_distance(codigo5)
distancia6, detectable6, corregible6 = hamming_distance(codigo6)

print(f"Código 4: Distancia de Hamming = {distancia4}, Errores Detectables = {detectable4}, Errores Corregibles = {corregible4}")
print(f"Código 5: Distancia de Hamming = {distancia5}, Errores Detectables = {detectable5}, Errores Corregibles = {corregible5}")
print(f"Código 6: Distancia de Hamming = {distancia6}, Errores Detectables = {detectable6}, Errores Corregibles = {corregible6}")