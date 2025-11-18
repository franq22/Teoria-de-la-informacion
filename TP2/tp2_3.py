import utils

list1 = [1/6, 1/6, 1/6, 1/6, 1/6, 1/6]
print(f'Entropia dado una lista de probabilidades uniforme: {utils.entropia(list1)}')
list2=[1/9, 1/6, 1/9, 1/9, 1/6, 1/3]
print(f'Entropia dado una lista de probabilidades no uniforme: {utils.entropia(list2)}')