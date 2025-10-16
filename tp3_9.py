

def get_longitudes( codigo):
    return [len(c) for c in codigo]

def get_alfabeto_codigos(C):
    x = ""
    for codigo in C:
        for caracter in codigo:
            if caracter not in x:
                x += caracter
    return x

def sumatoria_kraft(lista):
    r = len(get_alfabeto_codigos(lista))
    l = get_longitudes(lista)
    suma = sum([1/(r**i) for i in l])
    return suma 

