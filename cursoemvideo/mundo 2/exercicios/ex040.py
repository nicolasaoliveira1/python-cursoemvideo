n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
media = (n1 + n2) / 2
print(f"Tirando {n1:.1f} e {n2:.1f}, a média do aluno é de {media:.1f}")
if media < 5:
    print("O aluno está REPROVADO")
elif media >= 5 and media < 7:
    print("O aluno está na RECUPERAÇÃO")
else:
    print("O aluno está APROVADO")

