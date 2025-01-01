pessoas = []
dado = []
pesos = []
while True:
    nome = str(input("Nome: ")).capitalize().strip()
    peso = float(input("Peso: "))
    dado.append(nome)
    dado.append(peso)
    pesos.append(peso)
    pessoas.append(dado[:])
    continuar = " "
    while continuar not in "SN":
        continuar = input("Quer continuar? [S/N] ").upper().strip()
    dado.clear()
    if continuar in "N":
        break
print("=-"*30)
print(f"Ao todo, você cadastrou {len(pessoas)} pessoas: ",end="")
for p in pessoas:
    print(p[0], end=", ")
print(f"\nO maior peso foi de {max(pesos)}Kg. Peso de",end=" ")
for p in pessoas:
    if p[1] == max(pesos):
        print(p[0],end=" ")
print(f"\nO menor peso foi de {min(pesos)}Kg. Peso de",end=" ")
for p in pessoas:
    if p[1] == min(pesos):
        print(p[0],end=" ")
