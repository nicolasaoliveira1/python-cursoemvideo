sexo = input("Informe o seu sexo: [M/F] ").upper().strip()
while sexo not in ("M", "F"):
    sexo = input("Dados inválidos. Por favor, informe seu sexo: ").upper().strip()
if sexo == "F":
    print("Sexo FEMININO registrado com sucesso!")
else:
    print("Sexo MASCULINO registrado com sucesso!")
