import utils

alfabeto = ["S1", "S2", "S3", "S4", "S5"]
probs = [0.13, 0.34, 0.37, 0.12, 0.04]
alfa_cod = ['a', 'b', 'c']

cod = utils.gen_codigo_compacto(alfabeto, probs, alfa_cod)

print('Código:', cod)
print('Entropía:', utils.entropia(probs, 3))
print('Longitud promedio:', utils.longitud_media(probs, cod))
print('Es compacto? ', utils.es_codigo_compacto(alfabeto, probs, cod, alfabeto_codigo = alfa_cod))