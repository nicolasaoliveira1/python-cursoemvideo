from random import randint

def sorteia(lista):
    print("Sorteando 5 valores:",end=" ")
    for i in range(5):
        lista.append(randint(1,10))
    for n in nums:
        print(n,end=" ")

def somaPar(lista):
    s = 0
    for n in lista:
        if n % 2 == 0:
            s += n
    print(f"\nSomando os valores pares de {nums}, temos {s}")


nums = []
sorteia(nums)
somaPar(nums)
