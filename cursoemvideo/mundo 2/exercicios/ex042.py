a = int(input("Primeiro segmento: "))
b = int(input("Segundo segmento: "))
c = int(input("Terceiro segmento: "))
if a < b + c and b < a + c and c < b + a:
    if a == b == c:
        print("Os segmentos PODEM formar um triângulo EQUILÁTERO")
    elif a != b != c != a:
        print("Os segmentos PODEM formar um triângulo ESCALENO")
    else:
        print("Os segmentos PODEM formar um triângulo ISÓSCELES")
else:
    print("Os segmentos NÃO formam um triângulo.")
