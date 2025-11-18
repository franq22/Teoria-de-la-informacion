import utils

lista = [0.5, 0.25, 0.125, 0.125, 1]


def generar_lista_con_info(lista):
    lista2 = []
    for i in lista:
        lista2.append(utils.cantidadInformacion(i))    
    return lista2

print(f'Entropia: {utils.entropia(lista)}')
print(f'Cantidad de informacion: {generar_lista_con_info(lista)}')

