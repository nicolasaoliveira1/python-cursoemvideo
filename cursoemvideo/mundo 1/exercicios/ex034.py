salario = float(input("Qual o salário do funcionário? R$"))
if salario < 1250:
    aumento = 0.15
else: 
    aumento = 0.1
salario_aumentado = salario + (salario * aumento)
print(f"Quem ganhava R${salario:.2f} passa a ganhar R${salario_aumentado:.2f} agora.")
