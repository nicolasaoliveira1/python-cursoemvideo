frase = input("Digite uma frase: ").split()
frase = "".join(frase).upper()
inverso = ''
for letra in range(len(frase)-1, -1 ,-1):
    inverso += frase[letra]
print(f"O inverso de {frase} é {inverso}")
if frase == inverso:
    print("A frase digitada é um palíndromo!")
else:
    print("A frase digitada não é um palíndromo.")
