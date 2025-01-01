n = int(input("Digite um número inteiro qualquer: "))
print("Escolha uma das bases para conversão:")
print("[ 1 ] converter para BINÁRIO")
print("[ 2 ] converter para OCTAL")
print("[ 3 ] converter para HEXADECIMAL")
base = int(input("Sua opção: "))
if base == 1:
    print(f"{n} convertido para BINÁRIO é igual a {bin(n)[2:]}")
elif base == 2:
    print(f"{n} convertido para OCTAL é igual a {oct(n)[2:]}")
elif base == 3:
    print(f"{n} convetido para HEXADECIMAL é igual a {hex(n)[2:]}")
else:
    print("Opção inválida. Tente novamente.")
