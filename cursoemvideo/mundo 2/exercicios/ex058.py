from random import randint
numero = randint(1,10)
print("Sou seu computador... Acabei de pensar em um número entre 1 e 10.")
print("Será que você consegue adivinhar qual foi?")
tentativas = 0
palpite = 0
while palpite != numero:
    palpite = int(input("Qual é o seu palpite? "))
    while palpite not in range(1,11):
        palpite = int(input("\033[31mNúmero inválido.\033[m Qual é o seu palpite (de 1 a 10)? "))
    if palpite < numero:
        print("Mais... Tente mais uma vez.")
    elif palpite > numero:
        print("Menos... Tente mais uma vez.")
    tentativas += 1
print(f"Acertou com {tentativas} tentativas. Parabéns!")
