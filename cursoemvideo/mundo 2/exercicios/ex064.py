s = t = n = 0
while n != 999:
    n = int(input("Digite um número [999 para parar ]: ")) 
    s += n
    t += 1
print(f"Você digitou {t-1} números e a soma entre eles foi {s-999}.")
