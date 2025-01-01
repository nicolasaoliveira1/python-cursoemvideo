dias = int(input("Por quantos dias foi alugado? "))
km = float(input("Quantos km foram percorridos? "))
preco = dias * 60 + 0.15 * km
print(f"O total a pagar é de R${preco:.2f}")
