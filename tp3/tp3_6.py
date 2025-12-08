import utils

def clasificar_codigo(codigo: list) -> str:
    """
    Clasifica un código como instantáneo, sin prefijo, o no sin prefijo.
    """
    if utils.es_singular(codigo):
        return "bloque"
    elif utils.es_instantaneo(set(codigo)):
        return "instantáneo"
    elif utils.es_univocamente_decodificable(set(codigo)):
        return "univocamente decodificable"
    else:   
        return "no singular"
    
codigo1  = ["011", "000", "010", "101", "001", "100"]
codigo2  = ["110", "100", "101", "001", "110", "010"]
codigo3  = ["10", "1100", "0101", "1011", "0", "110"]
codigo4  = ["1101", "10", "1111", "1100", "1110", "0"]
codigo5  = ["011", "0111", "01", "0", "011111", "01111"]
codigo6  = ["1110", "0", "110", "1101", "1011", "10"]

print("Código 1:",clasificar_codigo(codigo1))
print("Código 2:",clasificar_codigo(codigo2))
print("Código 3:",clasificar_codigo(codigo3))
print("Código 4:",clasificar_codigo(codigo4))
print("Código 5:",clasificar_codigo(codigo5))
print("Código 6:",clasificar_codigo(codigo6))