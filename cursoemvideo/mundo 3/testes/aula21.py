# funcoes part 2
def somar(a=0,b=0,c=0):
    s = a+b+c
    return s


r1 = somar(1,2,3)
r2 = somar(4,3,0)
r3 = somar(1,8)
print(f"As somas foram: {r1}, {r2} e {r3}")

def fatorial(num=1):
    f = 1
    for c in range(num,0,-1):
        f *= c
    return f
f1 = fatorial(4)
f2 = fatorial(5)
f3 = fatorial()
print(f"Os resultados foram: {f1}, {f2} e {f3}")

def par(n=0):
    if n%2 == 0:
        return True
    else:
        return False
num = int(input("Digite um número: "))
if par(num):
    print("É par")
else:
    print("Não é par")
