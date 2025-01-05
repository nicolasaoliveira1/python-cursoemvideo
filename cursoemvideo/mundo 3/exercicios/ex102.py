def fatorial(n, show=False):
    '''
    -> Calcula o Fatorial de um Número.
    :param n: O número a ser calculado.
    :param show: Se o cálculo será mostrado ou não. (Opcional)
    :return: Retorna o fatorial do número.
    '''
    f = 1
    for c in range(n,0,-1):
        if show:
            print(f"{c} ="if c == 1 else f"{c} x",end=" ")
        f *= c
    return f

print(fatorial(5,show=True))
help(fatorial)