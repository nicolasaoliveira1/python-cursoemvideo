from random import randint
from time import sleep
print("JOGO PEDRA PAPEL TESOURA")
print("-=" *17)
print("Suas opções:")
print("[ 0 ] PEDRA")
print("[ 1 ] PAPEL")
print("[ 2 ] TESOURA")
itens = ("Pedra", "Papel", "Tesoura")
while True:
    jogador = int(input("Qual é a sua jogada? "))
    if jogador > 2 or jogador < 0:
        print("Jogada inválida. Escolha de 0 a 2")
        continue
    break
sleep(1)
print("JO")
sleep(0.8)
print("KEN")
sleep(0.8)
print("PÔ!!")
sleep(0.4)
computador = randint(0,2)
print("-=" *17)
print(f"Você jogou {itens[jogador]}")
print(f"O computador jogou {itens[computador]}")
print("-=" *17)
if computador == jogador:
    print("\033[33mEMPATE\n\033[m")
elif computador == 1:
    if jogador == 0:
        print("\033[31mVOCÊ PERDEU\n\033[m")
    else:
        print("\033[32mVOCÊ VENCEU\n\033[m")
elif computador == 2:
    if jogador == 1:
        print("\033[31mVOCÊ PERDEU\n\033[m")
    else:
        print("\033[32mVOCÊ VENCEU\n\033[m")
elif computador == 0:
    if jogador == 2:
        print("\033[31mVOCÊ PERDEU\n\033[m")
    else:
        print("\033[32mVOCÊ VENCEU\n\033[m")
