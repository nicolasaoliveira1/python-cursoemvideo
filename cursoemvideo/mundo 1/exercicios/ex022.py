nome = input("Digite seu nome completo: ").strip()
print("Analisando seu nome...")
print(f"Seu nome em maiúsculas é {nome.upper()}")
print(f"Seu nome em minúsculas é {nome.lower()}")
letras = nome.replace(" ", "")
print(f"Seu nome tem ao todo {len(letras)} letras")
palavras = nome.split()
print(f"Seu primeiro nome é {palavras[0]} e ele tem {len(palavras[0])} letras")