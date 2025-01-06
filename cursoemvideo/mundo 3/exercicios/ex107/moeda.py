def formata(preço=0):
    formatado = f"R${preço:.2f}".replace(".",",")
    return formatado

def aumentar(preço=0, taxa=0, mostra=True):
    v = preço * taxa / 100
    if mostra:
        return formata(preço + v)
    return(preço + v)

def diminuir(preço=0, taxa=0, mostra=True):
    v = preço * taxa / 100
    if mostra:
        return formata(preço - v)
    return(preço - v)

def dobro(preço=0, mostra=True):
    if mostra:
        return formata(preço*2)
    return preço*2

def metade(preço=0, mostra=True):
    if mostra:
        return formata(preço/2)
    return preço/2
