ficha = []
pessoa = {}
media = 0
while True:
    pessoa["nome"] = str(input("Nome: ")).strip().capitalize()
    while True:
        pessoa["sexo"] = str(input("Sexo: [M/F] ")).strip().upper()
        if pessoa["sexo"] not in "MF" or pessoa["sexo"] in " ":
            print("ERRO! Por favor digite apenas M ou F.")
            continue
        break
    while True:
        pessoa["idade"] = int(input("Idade: "))
        if pessoa["idade"] <= 0 or pessoa["idade"] > 100:
            print("Idade inválida, tente novamente!")
            continue
        break
    while True:
        opc = str(input("Quer continuar? [S/N] ")).upper().strip()
        if opc not in "SN" or opc in " ":
            print("ERRO! Responda apenas S ou N.")
            continue
        break
    ficha.append(pessoa.copy())
    media += pessoa["idade"]
    if opc in "N":
        break
media /= len(ficha)
print("=-"*30)
print(f"A) Ao todo temos {len(ficha)} pessoas cadastradas.")
print(f"B) A média de idade é de {media:.1f}")
print("C) As mulheres cadastradas foram",end=" ")
for v in ficha:
    if v["sexo"] in "F": 
        print(v["nome"],end=" ")
print("\nD) Lista das pessoas que estão acima da média de idade:")
for v in ficha:
    if v["idade"] >= media:
        print(f"   - Nome = {v['nome']}; Sexo = {v['sexo']}; Idade = {v['idade']};")
print("<< ENCERRADO >>")
