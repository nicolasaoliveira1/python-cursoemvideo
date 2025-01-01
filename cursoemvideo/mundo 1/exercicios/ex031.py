d = float(input("Digite a distância da viagem em Km? "))
if d <= 200:
    preco = 0.5 * d
    print(f"O preço da sua passagem será de R${preco:.2f}")
else: 
    preco = 0.45 * d
    print(f"O preço da sua passagem será de R${preco:.2f}")
