from random import randint
from time import sleep
print("JOGA NA MEGA SENA".center(50))
print("=-"*30)
jogo = []
jogos = int(input("Quantos jogos serão sorteados? "))
print(f"=-=-= SORTEANDO {jogos} JOGOS =-=-=")
for i in range(jogos):
    while len(jogo) < 6:
        num = randint(1,60)
        if num in jogo:
            continue
        jogo.append(num)
    print(f"Jogo {i+1}: {sorted(jogo)}")
    sleep(0.7)
    jogo.clear()
print("=-=-=- < BOA SORTE! > -=-=-=")
