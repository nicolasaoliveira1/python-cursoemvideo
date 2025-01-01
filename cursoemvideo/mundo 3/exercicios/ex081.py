lista = []
while True:
    num = int(input("Digite um valor: "))
    lista.append(num)
    continuar = " "
    while continuar not in "SN":
        continuar = input("Quer continuar? [S/N] ").strip().upper()
    if continuar in "N":
        break
print("=-"*30)
print(f"Você digitou {len(lista)} elementos")
print("Em ordem decrescente:",sorted(lista,reverse=True))
if 5 in lista:
    print("O valor 5 está na lista!")
else:
    print("O valor 5 não foi encontrado na lista!")
