import utils 

# Probabilidades
probs = [0.10, 0.50, 0.10, 0.20, 0.05, 0.05]

codigo1 = ["==", "<", "<=", ">", ">=", "<>"]
codigo2 = [")", "[]", "]]", "([", "[()]", "([)]"]
codigo3 = ["/", "*", "-", "*", "++", "+-"]
codigo4 = [".,", ";", ",,", ":", "...", ",:;"]

print("Código 1:",utils.clasificar_codigo(codigo1))
print("Código 2:",utils.clasificar_codigo(codigo2))
print("Código 3:",utils.clasificar_codigo(codigo3))
print("Código 4:",utils.clasificar_codigo(codigo4))