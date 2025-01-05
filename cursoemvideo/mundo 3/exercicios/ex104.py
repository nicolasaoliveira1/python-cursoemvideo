def leiaInt(texto):
    while True:
        n = input(texto)
        if n.isnumeric():
            return int(n)
        print("ERRO! Digite um número inteiro.")


n = leiaInt("Digite um número: ")
print(f"Você acabou de digitar o número {n}")
