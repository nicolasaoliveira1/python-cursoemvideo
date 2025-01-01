from time import sleep
soma_idades = 0
idade_velho = 0
nome_velho = ""
sexos = "M","F"
mulheres = 0
for i in range(1,5):
    print(f"-----{i}ª PESSOA-----")
    nome = str(input("Nome: ")).strip().title()
    while True:
        idade = int(input("Idade: "))
        if idade < 0 or idade > 110:
            print("Idade inválida. Tente novamente!")
            continue
        break
    while True:
        sexo = input("Sexo [M/F]: ").upper().strip()
        if sexo not in sexos:
            print("Sexo inválido, digite M para masculino e F para feminino.")
            continue
        break
    if sexo == "M":
        if i == 1:
            idade_velho = idade
            nome_velho = nome
        else:
            if idade > idade_velho:
                idade_velho = idade
                nome_velho = nome
    elif sexo == "F":
        if idade < 20:
            mulheres += 1
    soma_idades += idade
    media = soma_idades/4
print("-="*20)
print("Analisando o grupo de pessoas...\n")
sleep(3)
print(f"A média de idade do grupo é de {media:.1f} anos")
if idade_velho != 0:
    print(f"O homem mais velho tem {idade_velho} anos e se chama {nome_velho}")
else:
    print("O grupo tem apenas mulheres!")
print(f"Ao todo são {mulheres} mulheres com menos de 20 anos.")
