def printLinha(msg):
    tam = len(msg) + 4
    print("~"*tam)
    print(f" {msg}")
    print("~"*tam)


def manual():
    while True:
        printLinha("SISTEMA DE AJUDA PyHELP")
        cmd = str(input("Função ou Biblioteca > ")).strip().lower()
        if cmd == "fim":
            break
        printLinha(f"Acessando o manual de comando '{cmd}'")
        help(cmd)
    printLinha("Até logo!")


manual()