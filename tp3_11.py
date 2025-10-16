import utils

"""11. Dadas dos listas paralelas que contengan las palabras código de una codificación y sus
respectivas probabilidades, codificar funciones en Python que calculen:
a. la entropía de la fuente
b. la longitud media del código """

def entropia_codigo(probabilidades, codigos):
    return utils.entropia(probabilidades, len(utils.get_alfabeto_codigos(codigos)))

def longitud_media(probabilidades, codigos):
    longitud_media = 0
    longitudes = utils.get_longitudes(codigos)
    for p, l in zip(probabilidades, longitudes):
        longitud_media += p * l
    return longitud_media

probs = [0.10, 0.50, 0.10, 0.20, 0.05, 0.05]

codigo1 = ["==", "<", "<=", ">", ">=", "<>"]
codigo2 = [")", "[]", "]]", "([", "[()]", "([)]"]
codigo3 = ["/", "*", "-", "*", "++", "+-"]
codigo4 = [".,", ";", ",,", ":", "...", ",:;"]

print("Código 1: Entropía =", entropia(probs, codigo1), "Longitud media =", longitud_media(probs, codigo1))
print("Código 2: Entropía =", entropia(probs, codigo2), "Longitud media =", longitud_media(probs, codigo2))
print("Código 3: Entropía =", entropia(probs, codigo3), "Longitud media =", longitud_media(probs, codigo3))
print("Código 4: Entropía =", entropia(probs, codigo4), "Longitud media =", longitud_media(probs, codigo4))
