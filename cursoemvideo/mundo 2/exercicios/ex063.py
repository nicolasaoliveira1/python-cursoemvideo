print("Sequência de Fibonacci")
print("-="*25)
t = int(input("Quantos termos você quer mostrar? "))
c = 0
f = 1
while t != 0:
    print(f"{c} -> ",end="")
    c += f
    f = c - f
    t -= 1
print("Fim")
