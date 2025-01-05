#funcoes testes
def soma(*valores):
    s = 0
    for v in valores:
        s+= v
    print(f"Recebi os valores {valores} e a soma deu {s}")

def contador(*num):
    tam = len(num)
    print(f"Recebi os valores {num} e são ao todo {tam} números")

def dobraValor(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1

soma(7,1,9,1,3,2,4)

contador(2,1,7)
contador(8, 0)
contador(4,4,7,6,2)

valores = [8, 4, 3, 7, 1, 9]
dobraValor(valores)
print(valores)
