def area():
    print("Cálcular área do terreno")
    print("-"*25)
    l = float(input("LARGURA (m): "))
    c = float(input("COMPRIMENTO (m): "))
    a = l*c
    print(f"A área de um terreno {l}x{c} é de {a:.1f} metros quadrados.")

area()