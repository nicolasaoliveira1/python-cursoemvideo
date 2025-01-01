from datetime import date
ano_atual = date.today().year
maiores = 0
menores = 0
for i in range(7):
    while True:
        ano = int(input(f"Em que ano a {i+1}ª pessoa nasceu? "))
        if ano > ano_atual or ano < 1800:
            print("Ano inválido. Tente novamente!")
        break
    idade = ano_atual - ano
    if idade >= 18:
        maiores += 1
    else:
        menores += 1
print(f"Ao todo tivemos {maiores} pessoas maiores de idade")
print(f"E também tivemos {menores} pessoas menores de idade")
