opcao = "S"
cont = s = maior = menor = 0
while opcao in "S":
    n = int(input("Digite um número: "))
    maior = max(maior,n)
    if menor == 0:
        menor = maior
    menor = min(menor,n)
    s += n
    cont += 1
    while True:
        opcao = str(input("Quer continuar? [S/N] ")).upper().strip()[0]
        if opcao not in "SN":
            print("\nOpção inválida, tente novamente!")
            continue
        break
media = s / cont
print(f"\nVocê digitou {cont} números e a média foi {media}")
print(f"O maior valor foi {maior} e o menor foi {menor}")
