def leiaInt(texto):
    while True:
        try:
            n = int(input(texto))
        except KeyboardInterrupt:
            print("\nO usuário preferiu não digitar o número")
            return 0
        except:
            print("ERRO: por favor digite um número inteiro válido.")
        else:
            return n


def leiaFloat(texto):
    while True:
        try:
            n = float(input(texto))
        except KeyboardInterrupt:
            print("\nO usuário preferiu não digitar o número")
            return 0
        except:
            print("ERRO: por favor digite um número real válido.")
        else:
            return n


n = leiaInt("Digite um Inteiro: ")
n2 = leiaFloat("Digite um Real: ")
print(f"O valor inteiro digitado foi {n} e o real foi {n2}")
