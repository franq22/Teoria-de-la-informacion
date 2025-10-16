import utils

m = [
    [0.5,1/3,0],
    [0.5,1/3,1],
    [0,1/3,0]
]

print('Vector estacionario:', utils.stationary_vector(m))
print('Entropía de la fuente:', utils.markov_source_entropy(m))
