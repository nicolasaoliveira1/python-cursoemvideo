from time import sleep
n1 = int(input("Primeiro valor: "))
n2 = int(input("Segundo valor: "))
opcao = 0
while opcao != 5:
    print(" [ 1 ] Somar")
    print(" [ 2 ] Multiplicar")
    print(" [ 3 ] Maior")
    print(" [ 4 ] Novos números")
    print(" [ 5 ] Sair")
    opcao = int(input(">>>>> Qual é a sua opção? "))
    if opcao == 1:
        print(f"A soma de {n1} + {n2} é {n1+n2}")
    elif opcao == 2:
        print(f"O produto de {n1} * {n2} é {n1*n2}")
    elif opcao == 3:
        print(f"O maior número entre {n1} e {n2} é {max(n1,n2)}")
    elif opcao == 4:
        print("Informe os números novamente!")
        n1 = int(input("Primeiro valor: "))
        n2 = int(input("Segundo valor: "))
    elif opcao == 5:
        print("Finalizando...")
    else:
        print("Opcão inválida, tente novamente.")
    print("=-"*20)
    sleep(1)
print("Fim do programa, volte sempre!")
