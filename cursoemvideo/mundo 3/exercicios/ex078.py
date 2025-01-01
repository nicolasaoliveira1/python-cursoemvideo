lista = []
indmaior = []
indmenor = []
maior = menor = 0
for i in range(5):
    lista.append(int(input(f"Digite o valor na posição {i}: ")))
    if i == 0:
        maior = lista[i]
        menor = lista[i]
    else:
        maior = max(maior, lista[i])
        menor = min(menor, lista[i])
for c,n in enumerate(lista):
    if n == maior:
        indmaior.append(c)
    if n == menor:
        indmenor.append(c)
print("=-"*30)
print(f"Você digitou os valores {lista}")
print(f"O maior valor digitado foi {maior} nas posições",end=" ")
for i in indmaior:
    print(i,end="... ")
print(f"\nO menor valor digitado foi {menor} nas posições",end=" ")
for i in indmenor:
    print(i,end="... ")
