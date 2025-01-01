numeros =  []
for i in range(0,5):
    num = int(input('Digite um numero: '))
    pos = 0
    while pos < len(numeros) and numeros[pos] < num:
        pos += 1
    numeros.insert(pos,num)
print(numeros)