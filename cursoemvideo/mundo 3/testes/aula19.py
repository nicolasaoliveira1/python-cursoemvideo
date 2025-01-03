#dicionarios
pessoas = {"Nome": "Gustavo", "Sexo":"Masculino", "Idade": "22"}
pessoas["Peso"] = "90"
print(f"{pessoas["Nome"]} tem {pessoas["Idade"]} anos!")
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())
for k, v in pessoas.items():
    print(f"{k} = {v}")

brasil = []
estado1 = {"uf": "Rio de Janeiro", "sigla": "RJ"}
estado2 = {"uf": "São Paulo", "sigla": "SP"}
brasil.append(estado1)
brasil.append(estado2)
print(brasil[0]["uf"])

