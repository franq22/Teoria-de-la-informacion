""") Codificar una fuente de siete símbolos en un código instantáneo trinario de acuerdo a las siguientes pautas:
1. El alfabeto código original es X={a, b, c}.
2. s1s2 = aba y s2s3 = babb son algunas de las palabras código de la extensión de segundo orden de S.
3. Las cuatro últimas palabras correspondientes a los símbolos: s4, s5 ,s6 y s7 de la extensión de primer orden son iguales en
longitud.
a) Justificar las longitudes halladas.
b) Aplicar la fórmula de la inecuación de Kraft."""

import utils

alfa_cod = ['a', 'b', 'c']

alfa = ['s1', 's2', 's3', 's4', 's5', 's6', 's7']
longitudes = [1,2,2,3,3,3,3]
codigo = ['a','ba','bb','caa','cab','cbb','cbc']

kraft = utils.sumatoria_kraft(codigo)
if kraft < 1 and utils.es_instantaneo(codigo):
    print("El codigo cumple los requisitos")