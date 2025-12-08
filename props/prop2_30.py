import utils

"""30) Un agente comercial realiza su trabajo en tres ciudades A, B y C. Para evitar desplazamientos innecesarios está todo el
día en la misma ciudad y allí pernocta, desplazándose a otra ciudad al día siguiente, si no tiene suficiente trabajo. Después
de estar trabajando un día en C, la probabilidad de tener que seguir trabajando en ella al día siguiente es 0.4, la de tener que
viajar a B es 0.4 y la de tener que ir a A es 0.2. Si el viajante duerme un día en B, con probabilidad de un 20% tendrá que seguir
trabajando en la misma ciudad al día siguiente, en el 60% de los casos viajará a C, mientras que irá a A con probabilidad
0.2. Por último si el agente comercial trabaja todo un día en A, permanecerá en esa misma ciudad, al día siguiente, con una
probabilidad 0.1, irá a B con una probabilidad de 0.3 y a C con una probabilidad de 0.6.
a) Modelar el proceso que describe el movimiento.
b) Calcular la probabilidad de cada uno de los símbolos.
c) Determinar la entropía y el vector estacionario."""

# Matriz de transición desde columnas
M = [
    [0.1, 0.2, 0.2],  # Desde A
    [0.3, 0.2, 0.4],  # Desde B
    [0.6, 0.6, 0.4]   # Desde C
]


v_est = utils.stationary_vector(M)
print('Vector estacionario:', v_est)
print('Entropía de la fuente:', utils.markov_source_entropy(M))