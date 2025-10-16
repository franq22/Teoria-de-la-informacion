import utils

cadena = "ABDAACAABACADAABDAADABDAAABDCDCDCDC"

alfabeto, probabilidades = utils.getAlfaProbabilidades(cadena)
print(f'Alfabeto: {alfabeto}')
print(f'Probabilidades: {probabilidades}')