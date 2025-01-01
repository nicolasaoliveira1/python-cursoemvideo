pesos = []
for i in range(5):
    peso = float(input(f"Peso da {i+1}ª pessoa: "))
    pesos.append(peso)
maior = max(pesos)
menor = min(pesos)
print(f"O menor peso lido foi de {menor}Kg")
print(f"O maior peso lido foi de {maior}Kg")
