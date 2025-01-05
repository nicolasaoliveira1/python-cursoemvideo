def contador(i,f,p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    print(f"Contagem de {i} até {f} de {p} em {p}")
    if i < f:
        for j in range(i,f+1,p):
            print(j,end=" ")
        print("FIM!",end=" ")
        print()
    else:
        for j in range(i,f-1,-p):
            print(j,end=" ")
        print("FIM!")

contador(1,10,1)
contador(10,0,2)
print("Agora é sua vez de personalizar a contagem!")
i = int(input("Início: "))
f = int(input("Fim: "))
p = int(input("Passo: "))
contador(i,f,p)
