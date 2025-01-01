lista = []
pares = []
impares = []
while True:
    num = int(input("Digite um valor: "))
    lista.append(num)
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)
    continuar = " "
    while continuar not in "SN":
        continuar = input("Quer continuar? [S/N] ").strip().upper()
    if continuar in "N":
        break
print(lista)
print(pares)
print(impares)
