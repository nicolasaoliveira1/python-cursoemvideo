soma = 0
pares = 0
for i in range(6):
    numero = int(input(f"Digite o {i+1} número: "))
    if numero % 2 == 0:
        pares += 1
        soma += numero
print(f"Você informou {pares} números pares e a soma foi {soma}")