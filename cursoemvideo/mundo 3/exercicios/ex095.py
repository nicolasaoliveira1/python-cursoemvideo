time = []
gols = []
jogador = {}
while True:
    gols.clear()
    jogador["nome"] = str(input("Nome do jogador: ")).strip().capitalize()
    partidas = int(input(f"Quantas partidas {jogador['nome']} jogou? "))
    for i in range(partidas):
        gols.append(int(input(f"Quantos gols na partida {i+1}? ")))
        jogador["gols"] = gols[:]
    jogador["total"] = sum(gols)
    while True:
        opc = str(input("Quer continuar? [S/N] ")).upper().strip()
        if opc not in "SN" or opc in " ":
            print("ERRO. Digite apenas S ou N!")
            continue
        break
    time.append(jogador.copy())
    if opc in "N":
        break
print("=-"*30)
print(f"{"cod":<4}{"nome":<10}{"gols":>15}{"total":>15}")
print("-"*45)
for i,v in enumerate(time):
    print(f"{i:>3} ", end="")       #formatacao inconscistente, voltar no futuro
    for d in v.values():
        print(f"{str(d):<20}",end="")
    print()
print("-"*45) 
while True:
    idx = int(input("Mostrar dados de qual jogador? (999 para parar) "))
    if idx == 999:
        break
    if idx <= len(time)-1:
        print(f"-- LEVANTAMENTO DO JOGADOR {time[idx]["nome"]}:")
        for i, v in enumerate(time[idx]["gols"]):
            print(f"  - No jogo {i+1} fez {v} gols.")
    else:
        print(f"ERRO, não existe jogador com código {idx}")
    print("-"*45)
print("Programa finalizado")
