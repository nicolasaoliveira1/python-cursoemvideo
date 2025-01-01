nome = str(input("Qual o seu nome completo? ")).strip().lower()
silva = nome.find("silva")
print("Seu nome tem Silva?", nome[silva:silva+5] == "silva")

""" nome = str(input("Qual o seu nome completo? ")).strip()
print(f"Analisando seu nome: {nome.title()}")
nome = nome.lower()
nome = nome.split()
if "silva" in nome:
    print("Seu nome possui Silva!")
else:
    print("Seu nome não possui Silva.") """