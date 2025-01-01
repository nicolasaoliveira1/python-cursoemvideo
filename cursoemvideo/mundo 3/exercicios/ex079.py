lista = []
while True:
    continuar = ' '
    n = int(input("Digite um valor: "))
    if n not in lista:
        lista.append(n)
        print("Valor adicionado com sucesso..")
    else:
        print("Valor duplicado. Não será adicionado..")
    while continuar not in "SN":
        continuar = input("Quer continuar? [S/N] ").upper().strip()
    if continuar in "N":
        break
print(f"Você digitou os valores {sorted(lista)}")
