'''
#GAMBIARRA NICOLAS
print("="*40)
print("BANCO CEV")
print("="*40)
valor = int(input("Qual valor você quer sacar? R$"))
cinquenta = vinte = dez = um = 0
while valor > 0:
    if valor >= 50:
        valor -= 50
        cinquenta += 1
    elif valor >= 20:      
        valor -= 20
        vinte += 1
    elif valor >= 10:
        valor -= 10
        dez += 1
    elif valor >= 1:
        valor -= 1
        um += 1
if cinquenta > 0:
    print(f"Total de {cinquenta} cédulas de R$50")
if vinte > 0:
    print(f"Total de {vinte} cédulas de R$20")
if dez > 0:
    print(f"Total de {dez} cédulas de R$10")
if um > 0:
    print(f"Total de {um} cédulas de R$1")
print("="*40)
print("Volte sempre ao Banco CEV! Tenha um bom dia!")
'''
#RESOLUCAO GUANABARA
valor = int(input("Qual valor você quer sacar? R$"))
ced = 50
totced = 0
while True:
    if valor >= ced:
        valor -= ced
        totced += 1
    else:
        if totced > 0:
            print(f"Total de {totced} cédulas de R${ced}")
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if valor == 0:
            break
