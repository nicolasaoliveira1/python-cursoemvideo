import datetime
ano = int(input("Ano de nascimento: "))
ano_atual = datetime.date.today().year
idade = ano_atual - ano
print(f"Quem nasceu em {ano} tem {idade} anos em {ano_atual}.")
if idade == 18:
    print("Esse é o ano do seu alistamento militar! Se aliste imediatamente!")
elif idade < 18:
    tempo = 18 - idade
    alistamento = ano_atual + tempo
    print(f"Ainda faltam {tempo} anos para o seu alistamento.")
    print(f"Seu alistamento será em {alistamento}.")
else:
    tempo = idade - 18
    alistamento = ano_atual - tempo
    print(f"Você já deveria ter se alistado há {tempo} anos.")
    print(f"Seu alistamento foi em {alistamento}.")
