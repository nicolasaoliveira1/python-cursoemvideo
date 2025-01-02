matriz = [[0,0,0],[0,0,0],[0,0,0]]
somaPares = somaTerceira = maior = 0
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f"Valor para [{l},{c}]: "))
        if matriz[l][c] % 2 == 0:
            somaPares += matriz[l][c]
        if c == 2:
            somaTerceira += matriz[l][c]
        if l == 1:
            if c == 0:
                maior = matriz[l][c]
            else:
                if matriz[l][c] > maior:
                    maior = matriz[l][c]
print("=-"*30)
for l in range(0,3):
    for c in range(0,3):
        print(f"[{matriz[l][c]:^5}]", end='')
    print()
print("=-"*30)
print(f"Soma dos valores pares: {somaPares}")
print(f"Soma terceira coluna: {somaTerceira}")
print(f"Maior valor segunda linha: {maior}")
