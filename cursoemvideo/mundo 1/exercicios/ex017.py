import math
cateto_oposto = float(input("Comprimento do cateto oposto: "))
cateto_adjacente = float(input("Comprimento do cateto adjacente: "))
hipotenusa = math.hypot(cateto_adjacente, cateto_oposto)
print(f"A hipotenusa irá medir: {hipotenusa:.2f}")