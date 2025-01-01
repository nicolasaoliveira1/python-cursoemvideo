print("TESTE DE NÚMEROS PRIMOS")
print("-="*20)
num = int(input("Digite um número: "))
divisoes = 0
for i in range(1,num+1):
    if num % i == 0:
        divisoes += 1
        print(f"\033[33m{i}\033[m",end=" ")
    else:
        print(f"\033[31m{i}\033[m",end=" ")  
print(f"\nO número {num} foi divisível {divisoes} vezes")
if divisoes == 2:
    print("Por isso ele É PRIMO!")
else:
    print("Por isso ele NÃO é PRIMO!")
