from random import randint
from operator import itemgetter
jogadores = {}
for c in range(1,5):
    jogadores[f"jogador {c}"]=randint(1,6)
rank = {}
print("Valores sorteados:")
for k, v in jogadores.items():
    print(f"{k} tirou {v} no dado.")
print("=-"*25)
print("   == RANKING DOS JOGADORES ==")
rank = sorted(jogadores.items(), key=itemgetter(1), reverse=True) # sortear os valores ordem decrescente!
for i, v in enumerate(rank):
    print(f"{i+1}° Lugar: {v[0]} com {v[1]}")
