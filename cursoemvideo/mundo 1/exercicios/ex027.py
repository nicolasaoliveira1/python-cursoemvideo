#método com find (meu)
nome = str(input("Digite seu nome completo: ")).strip()
espaco = nome.find(" ")
ultimo_espaco = nome.rfind(" ")+1
primeiro_nome = nome[:espaco].title()
ultimo_nome = nome[ultimo_espaco:].title()
print(f"Prazer em te conhecer, {primeiro_nome}!")
print(f"Seu último nome é {ultimo_nome}")

# método com split (resolucao do guanabara)
""" n = str(input("Digite o nome completo: ")).strip()
nome = n.split()
primeiro_nome = nome[0].title()
ultimo_nome = nome[len(nome)-1].title()
print(f"Prazer em te conhecer, {primeiro_nome}!")
print(f"Seu último nome é {ultimo_nome}")
"""