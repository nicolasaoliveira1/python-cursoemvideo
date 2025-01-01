from random import randint
print("=-"*25)
print("VAMOS JOGAR PAR OU ÍMPAR")
s = v = 0
while True:
    print("=-"*25)
    comp = randint(1,10)
    while True:
        n = int(input("Diga um valor: "))
        if n not in range(1,11):
            print("Escolha um número de 1 até 10. Tente denovo!")
            continue
        while True:
            opcao = input("Par ou ímpar? ").strip().upper()[0]
            if opcao not in "PIÍ" or opcao == " ":
                print("Digite: par ou ímpar")
                continue
            break
        break
    s = n + comp
    print("-"*45)
    print(f"Você jogou {n} e o computador {comp}. Total de {s}, ", end="")
    if s % 2 == 0:
        print("DEU PAR")
        print("-"*45)
        if opcao == "P":
            print("Você VENCEU!")
            print("Vamos jogar novamente...")
            v += 1
        else:
            print("Você PERDEU!")
            break
    else:
        print("DEU IMPAR")
        print("-"*45)
        if opcao == "I":
            print("Você VENCEU!")
            print("Vamos jogar novamente...")
            v += 1
        else:
            print("Você PERDEU!")
            break
if v < 1:
    print("Game Over! Você não venceu, mais sorte na próxima vez!")
elif v == 1:
    print(f"Game Over! Você venceu {v} vez.")
else:
    print(f"Game Over! Você venceu {v} vezes. Parabéns!!")
