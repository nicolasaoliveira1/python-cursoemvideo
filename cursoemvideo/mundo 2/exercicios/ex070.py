print("-"*40)
print("LOJA SUPER BARATÃO")
print("-"*40)
c = b = p = s = 0
nome_barato = ""
while True:
    nome = input("Nome do produto: ").strip().capitalize()
    preco = int(input("Preço: R$"))
    c += 1
    s += preco
    if preco > 1000:
        p += 1
    if c == 1:
        b = preco
        nome_barato = nome
    else:
        if preco < b:
            b = preco
            nome_barato = nome  
    continuar = " "
    while continuar not in "SN":
        continuar = input("Quer continuar? [S/N] ").strip().upper()
    if continuar == "N":
        break
print(f"O total da compra foi R${s:.2f}")
print(f"Temos {p} produtos custando mais de R$1000.00")
print(f"O produto mais barato foi {nome_barato} que custa R${b:.2f}")
