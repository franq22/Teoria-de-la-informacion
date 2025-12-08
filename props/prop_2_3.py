import utils

cad = 'ABDAACAABACADAABDAADABDAAABDCDCDCDC'
alfa, probs = utils.getAlfaProbabilidades(cad)

print('Alfabeto:', alfa)
print('Probabilidades:', probs)
print('Entropía:', utils.entropia(probs))