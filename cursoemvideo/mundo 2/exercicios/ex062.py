print("Gerador de PA\n")
n = int(input("Primeiro termo: "))
r = int(input("Razão da PA: "))
c = 0
i = n
t = 0
mais = 10
while mais != 0:
    while c < mais:
        print(i,end=" -> ")
        i += r
        c += 1
        t += 1
    print("PAUSA")
    c = 0
    mais = int(input("Quantos termos você quer mostrar a mais? "))
print(f"Progressão finalizada com {t} termos mostrados.")
