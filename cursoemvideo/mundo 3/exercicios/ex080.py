lista = []
for i in range(5):
    while True:
        num = int(input("Digite um valor: "))
        if num in lista:
            print("Valor já adicionado, tente novamente")
            continue
        break
    if i == 0 or num > lista[-1]:
        lista.append(num)
        print("Adicionado ao final da lista...")
    else:
        for valor in lista:
            if num < valor:
                lista.insert(lista.index(valor),num)
                print(f"Adicionado na posição {lista.index(valor)-1} da lista...")
                break
print("=-"*30)
print("Os valores digitados em ordem foram:",lista)
