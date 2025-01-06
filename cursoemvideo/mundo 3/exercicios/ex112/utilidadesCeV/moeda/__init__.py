def formata(preço=0):
    formatado = f"R${preço:.2f}".replace(".",",")
    return formatado

def aumentar(preço=0, taxa=0, mostra=True):
    v = preço + (preço * taxa / 100)
    if mostra:
        return formata(v)
    return v

def diminuir(preço=0, taxa=0, mostra=True):
    v = preço - (preço * taxa / 100)
    if mostra:
        return formata(v)
    return v

def dobro(preço=0, mostra=True):
    if mostra:
        return formata(preço*2)
    return preço*2

def metade(preço=0, mostra=True):
    if mostra:
        return formata(preço/2)
    return preço/2

def resumo(n, aum, red):
    print("-"*35)
    print("RESUMO DO VALOR".center(35))
    print("-"*35)
    print(f"Preço analisado: \t{formata(n)}")
    print(f"Dobro do preço: \t{dobro(n)}")
    print(f"Metade do preço: \t{metade(n)}")
    print(f"{aum}% de aumento: \t{aumentar(n,aum)}")
    print(f"{red}% de redução: \t{diminuir(n,red)}")
    print("-"*35)