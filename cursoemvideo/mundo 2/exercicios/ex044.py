print("============LOJAS GUANABARA============")
preco = float(input("Preço das compras: R$"))
desconto_vista = preco - (preco * 0.1)
desconto_vista_cartao = preco - (preco * 0.05)
juros = 0.2
print("FORMAS DE PAGAMENTO")
print("[ 1 ] à vista dinheiro/cheque")
print("[ 2 ] à vista cartão")
print("[ 3 ] em 2x no cartão")
print("[ 4 ] 3x ou mais no cartão")
pagamento = int(input("Qual é a opção? "))
if pagamento == 1:
    print(f"Sua compra de R${preco:.2f} vai custar R${desconto_vista:.2f} no final.")
elif pagamento == 2:
    print(f"Sua compra de R${preco:.2f} vai custar R$ {desconto_vista_cartao} no final.")
elif pagamento == 3:
    print(f"Sua compra será parcelada em 2x de R${(preco/2):.2f} SEM JUROS")
    print(f"Sua compra custará R${preco:.2f} no final.")
elif pagamento == 4:
    while True:
        quant_parcelas = int(input("Quantas parcelas? "))
        if quant_parcelas < 3:
            print("Quantidade de parcelas menor que 3x. Tente novamente!")
            continue
        if quant_parcelas > 12:
            print("Quantidade de parcelas maior que 12x. Tente novamente!")
            continue
        break
    parcela = preco / quant_parcelas
    parcela_com_juros = parcela + (parcela*juros)
    preco_parcelado = parcela_com_juros * quant_parcelas
    print(f"Sua compra será parcelada em {quant_parcelas}x de R${parcela_com_juros:.2f} COM JUROS")
    print(f"Sua compra será de R${preco:.2f} vai custar R${preco_parcelado} no final.")
else:
    print("Forma de pagamento inválida. Tente novamente!")
