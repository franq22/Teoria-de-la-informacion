"""En el mercado hay 3 operadores de telefonía móvil. Se sabe que los clientes están distribuidos de manera uniforme, pero
que ante un reclamo severo de un cliente existe la posibilidad de que migren a alguno de los otros 2 operadores.
 Ante una queja severa de un cliente del Operador A, se sabe que el cliente tiene un 90% de probabilidades de
mantenerse con su operador, un 5% de pasar al operador B y un 5% de pasar al operador C.
 Ante una queja severa de un cliente del Operador B, se sabe que el cliente tiene un 95% de probabilidades de
mantenerse con su operador y un 5% de pasar al operador A.
 Ante una queja severa de un cliente del Operador C, se sabe que el cliente tiene un 80% de probabilidades de
mantenerse con su operador, un 15% de pasar al operador B y un 5% de pasar al operador A.
a) Modelar el proceso que describe la permanencia o migración de un cliente entre las 3 operadoras.
b) Calcular el vector estacionario."""

import utils

# Matriz de transición
M = [
    [0.90, 0.05, 0.05],  # Desde A
    [0.05, 0.95, 0.15],  # Desde B
    [0.05, 0.00, 0.80]   # Desde C
]

v_est = utils.stationary_vector(M)
print('Vector estacionario:', v_est)

