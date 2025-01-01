while True:
    tabuada = int(input("Digite o número para ver sua tabuada: "))
    if tabuada < 0 or tabuada > 15:
        print("Escolha um número de 1 a 15!")
        continue
    break
numeros = ["UM", "DOIS", "TRÊS", "QUATRO", "CINCO", "SEIS", "SETE", "OITO", "NOVE", "DEZ", "ONZE", "DOZE", "TREZE", "CATORZE", "QUINZE"]
print("-="*20)
print(f"TABUADA DO {numeros[tabuada-1]}")
print("-="*20)
for i in range(1, 11):
    print(f"{tabuada} x {i} = {tabuada * (i)}")
