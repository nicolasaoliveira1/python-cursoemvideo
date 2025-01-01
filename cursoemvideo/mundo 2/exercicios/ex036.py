valor = float(input("Valor da casa: R$"))
salario = float(input("Salário do comprador: R$"))
anos = float(input("Quantos anos de financiamento? "))
meses = anos * 12
prestacao = valor / meses
print(f"Para pagar uma casa de R${valor:.2f} em {anos} anos a prestação será de R${prestacao:.2f}")
trinta = salario * 0.3
if prestacao >= trinta:
    print("Empréstimo negado")
else:
    print("Empréstimo aprovado!")
