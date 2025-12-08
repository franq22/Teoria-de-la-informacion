"""Realizar una función en Python que reciba como parámetros: dos listas paralelas con la
distribución de probabilidades de una fuente y su codificación, y calcule el rendimiento y la
redundancia del código.
"""

import utils

def rendimiento_redundancia(probabilidades, codigos):  
    H = utils.entropia(probabilidades)
    L = utils.longitud_media(probabilidades, codigos)
    
    rendimiento = H / L if L != 0 else 0
    redundancia = 1 - rendimiento
    
    return rendimiento, redundancia