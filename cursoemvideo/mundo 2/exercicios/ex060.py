'''
             #GAMBIARRA
num = int(input("Digite um número para calcular seu fatorial: "))
cont = (num - 1)
total_atual = num * cont
total_final = 0
print(f"Calculando {num}! = {num} x {num-1} x ",end="")
while cont != 2:
    cont -= 1
    total_final = total_atual * cont
    total_atual = total_final
    print(cont,end=" x ")
print("1 =",(total_final))
'''

            #GUANABARA
num = int(input("Digite um número para calcular seu fatorial: "))
cont = num
f = 1
print(f"Calculando {num}! = ",end="")
while cont >= 1: 
    print(cont,end="")
    print(" x " if cont > 1 else " = ",end="")
    f *= cont
    cont -= 1
print(f)
