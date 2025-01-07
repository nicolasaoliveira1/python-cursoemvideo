def leiaInt(texto):
    while True:
        try:
            n = int(input(texto))
        except KeyboardInterrupt:
            print("\nERRO: por favor digite um número inteiro válido.")
        except (ValueError,TypeError):
            print("ERRO: por favor digite um número inteiro válido.")
        else:
            return n

def leiaNome(texto): #função nova para tratar os nomes
    while True:
        try:
            n = input(texto).strip().title()
            if not n.isalpha():
                print("ERRO: O nome deve conter apenas letras. Tente novamente.")
                continue
        except KeyboardInterrupt:
            print("\nERRO: Entrada interrompida pelo usuário.")
            continue
        else:
            return n

def linha(tam = 40):
    return "-" * tam

def cabeçalho(txt):
    print(linha())
    print(txt.center(40))
    print(linha())

def menu(lista):
    cabeçalho("MENU PRINCIPAL")
    for i, o in enumerate(lista,start=1):
        print(f"{i} - {o}")
    print(linha())
    opc = leiaInt("Sua opção: ")
    return opc

