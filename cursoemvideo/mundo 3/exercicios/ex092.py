
carteira = {}
carteira["nome"] = str(input("Nome: ")).strip().capitalize()
ano = int(input("Ano de nascimento: "))
carteira["idade"] = 2025 - ano
carteira["ctps"] = int(input("Carteira de trabalho (0 não tem): "))
if carteira["ctps"] > 0:
    carteira["contratação"] = int(input("Ano de Contratação: "))
    carteira["salário"] = float(input("Salário: R$"))
    idade = carteira["contratação"] - ano
    carteira["aposentadoria"] = idade + 35
for k, v in carteira.items():
    print(f"  - {k} tem o valor {v}")
