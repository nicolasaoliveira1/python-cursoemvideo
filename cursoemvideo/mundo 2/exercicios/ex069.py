maior = homens = mulheres = 0
while True:
    print("-"*40)
    print("CADASTRE UMA PESSOA")
    print("-"*40)
    idade = 0
    while True:
        idade = input("Idade: ")
        if idade.isdigit():
            if int(idade) > 0:
                break
        continue
    if int(idade) > 18:
       maior += 1
    sexo = " "
    while sexo not in "MF":
        sexo = str(input("Sexo: [M/F] ")).upper().strip()[0]
    if sexo == "M":
        homens += 1
    if sexo == "F" and int(idade) < 20:
        mulheres += 1
    continuar = " "
    while continuar not in "SN":
        continuar = input("Quer continuar? [S/N] ").upper().strip()[0]
    if continuar == "N":
        break
print(f"Total de pessoas com mais de 18 anos: {maior}")
if homens == 1:
    print(f"Ao todo temos {homens} homem cadastrado.")
elif homens > 1:
    print(f"Ao todo temos {homens} homens cadastrados.")
else:
    print("Não temos homens cadastrados.")
if mulheres == 1:
    print(f"E temos {mulheres} mulher com menos de 20 anos.")
elif mulheres > 1:
    print(f"E temos {mulheres} mulheres com menos de 20 anos.")
