c = 1
while True:
    t = int(input("Quer ver a tabuada de qual valor? "))
    print("-="*25)
    if t < 0:
        break
    while c <= 10:
        print(f"{t} x {c} = {t*c}")
        c+=1
    print("-="*25)
    c = 1
print("PROGRAMA DE TABUADA ENCERRADO, VOLTE SEMPRE!")
