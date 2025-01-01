preco = float(input("Qual o preço do produto? R$"))
desconto = 0.05
preco_final = preco -(preco * desconto)
print(f"O produto que custava R${preco:.2f}, na promoção com desconto de 5% vai custar R${preco_final:.2f}")
