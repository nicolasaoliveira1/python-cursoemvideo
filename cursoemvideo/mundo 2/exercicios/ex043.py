peso = float(input("Qual é seu peso? (Kg) "))
altura = float(input("Qual é sua altura? (m) "))
imc = peso / (altura * altura)
print(f"O seu IMC é de {imc:.1f}")
if imc < 18.5:
    print("Cuidado! Você está ABAIXO DO PESO.")
elif imc >= 18.5 and imc <= 25:
    print("Parabéns! Você está no PESO IDEAL.")
elif imc > 25 and imc <= 30:
    print("Tome cuidado! Você está com SOBREPESO.")
elif imc > 30 and imc <= 40:
    print("Procure um médico! Você está com OBESIDADE")
else:
    print("Procure um médico IMEDIATAMENTE! Você está com OBESIDADE MÓRBIDA.")
