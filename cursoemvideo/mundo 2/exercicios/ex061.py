print("Gerador de PA\n")
n = int(input("Primeiro termo: "))
r = int(input("Razão da PA: "))
c = 0
i = n
while c < 10:
    print(i,end=" -> ")
    i += r
    c += 1
print("FIM")
