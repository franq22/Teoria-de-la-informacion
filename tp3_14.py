import utils
import math
def es_compacto(codigo: list, probabilidades: list[float]) -> bool:
    """
    Determina si un código es compacto.
    
    Parámetros:
        - codigo: lista de cadenas que representan los códigos de los símbolos
        - probabilidades: lista de probabilidades de los símbolos
    
    Retorna: True si el código es compacto, False en caso contrario.
    
    Contrato:
        - codigo es distinto de None y no es una lista vacía
        - todos los elementos de codigo son cadenas no vacías
        - probabilidades es distinto de None y no es una lista vacía
        - todos los elementos de probabilidades son mayores que 0 y menores o iguales que 1
        - la suma de los elementos de probabilidades es igual a 1
        - la longitud de codigo es igual a la longitud de probabilidades
    """
    if utils.es_instantaneo(codigo):
        R = len(utils.get_alfabeto_codigos(codigo))
        LONGITUDES = utils.get_longitudes(codigo)
        i = 0
        respuesta = True
        while i < len(codigo) and respuesta:
            limite_superior = math.ceil(-math.log(probabilidades[i], R))
            if LONGITUDES[i] > limite_superior:
                respuesta = False
            i += 1
        return respuesta
    else:
        return False
    

probs = [0.10, 0.50, 0.10, 0.20, 0.05, 0.05]

codigo1 = ["==", "<", "<=", ">", ">=", "<>"]
codigo2 = [")", "[]", "]]", "([", "[()]", "([)]"]
codigo3 = ["/", "*", "-", "*", "++", "+-"]
codigo4 = [".,", ";", ",,", ":", "...", ",:;"]

print(es_compacto(codigo1, probs))  # True
print(es_compacto(codigo2, probs))  # False
print(es_compacto(codigo3, probs))  # False
print(es_compacto(codigo4, probs))  # True