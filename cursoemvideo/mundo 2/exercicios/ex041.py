from datetime import date
nasc = int(input("Ano de nascimento do atleta: "))
ano = date.today().year
idade = ano - nasc
print(f"O atleta tem {idade} anos.")
if idade <= 9:
    classificacao = "MIRIM"
elif idade <= 14:
    classificacao = "INFANTIL"
elif idade <= 19:
    classificacao = "JÚNIOR"
elif idade <= 25:
    classificacao = "SÊNIOR"
else:
    classificacao = "MASTER"
print(f"Classificação: {classificacao}")