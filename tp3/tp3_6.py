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
# ...existing code...

def es_univocamente_decodificable(codigo: set) -> bool:
    """
    Verifica si un código es unívocamente decodificable.

    Parámetros:
        - codigo (set): Lista de cadenas que representan el código.
    Retorna:
        - bool: True si el código es unívocamente decodificable, False en caso contrario.
    Precondiciones:
        - codigo no está vacío.
        - codigo es distinto de None
        - el codigo es no singular
    """
    S = [codigo, set()]
    i = 0
    seguir = True
    while seguir:
        for x in S[0]:
            for y in S[i]:
                if x.startswith(y) and x != y:
                    S[i+1].add(x[len(y):])
                else:
                    if y.startswith(x) and x != y:
                        S[i+1].add(y[len(x):])
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

CODIGO_1 = {"010", "101", "000", "111"}
CODIGO_2 = {"110", "001", "11", "00"}

print("Código 1 es instantáneo:", es_instantaneo(CODIGO_1))
print("Código 1 es unívocamente decodificable:", es_univocamente_decodificable(CODIGO_1))
print("Código 2 es instantáneo:", es_instantaneo(CODIGO_2))
print("Código 2 es unívocamente decodificable:", es_univocamente_decodificable(CODIGO_2))



