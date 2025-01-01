print("ANALISADOR DE TRIÂNGULOS!")
a = float(input("Primeiro segmento: "))
b = float(input("Segundo segmento: "))
c = float(input("Terceiro segmento: "))
if a < b + c and b < a + c and c < b + a:
    print("Os segmentos podem formar um triângulo!!")
else:
    print("Os segmentos não formam um triângulo.")
