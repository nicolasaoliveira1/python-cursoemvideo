frase = str(input("Digite uma frase: ")).strip().lower()
conta = frase.count("a")
print(f"A letra A apareceu {conta} vezes na frase")
primeira = frase.find("a")+1
print(f"A primeira letra A apareceu na posição {primeira}")
ultima = frase.rfind("a")+1
print(f"A última letra A apareceu na posição {ultima}")
