import math
ang = int(input("Digite o ângulo desejado: "))
rad = math.radians(ang)
sen = math.sin(rad)
cos = math.cos(rad)
tan = math.tan(rad)
print(f"O ângulo de {ang} tem o SENO de {sen:.2f}")
print(f"O ângulo de {ang} tem o COSSENO de {cos:.2f}")
print(f"O ângulo de {ang} tem a TANGENTE de {tan:.2f}")
