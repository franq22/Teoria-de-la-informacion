import utils

simbolos = ['a', 'b', 'c', 'd']
prob = [0.1, 0.3, 0.4, 0.2]

for s, p in zip(simbolos, prob):
    print(f'Cantidad de informacion del simbolo {s} con probabilidad {p}: {utils.cantidadInformacion(p)}')
print(f'Entropia dado una lista de simbolos y sus probabilidades: {utils.entropia(prob)}')