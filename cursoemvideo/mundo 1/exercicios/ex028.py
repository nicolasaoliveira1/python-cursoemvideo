import random
from time import sleep
num = random.randint(0,5)
print("Vou pensar em um número entre 0 e 5. Tente advinhar...\n")
chute = int(input("Em que número pensei? "))
print("\nPROCESSANDO...\n")
sleep(3)
if chute == num:
    print(f"PARABÉNS! Eu realmente pensei no número {num}. Você leu minha mente!")
else:
    print(f"GANHEI MUAHAHAHA! Eu pensei no número {num} e não no {chute}!")
