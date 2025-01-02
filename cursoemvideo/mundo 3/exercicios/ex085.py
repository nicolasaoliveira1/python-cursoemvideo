lista = [[],[]]
for i in range(7):
    n = int(input(f"Digite o {i+1}o. valor: "))
    if n % 2 == 0:
        lista[0].append(n)
    else:
        lista[1].append(n)
print("Os valores pares digitados foram:",sorted(lista[0]))
print("Os valores impares digitados foram:", sorted(lista[1]))
