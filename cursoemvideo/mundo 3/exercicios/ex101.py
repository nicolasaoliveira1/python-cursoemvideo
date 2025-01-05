def voto(nasc):
    from datetime import date
    ano = date.today().year
    idade = ano - nasc
    if idade < 16:
        return f"Com {idade} anos: VOTO NEGADO"
    elif idade > 65 or (idade >= 16 and idade < 18):
        return f"Com {idade} anos: VOTO OPCIONAL"
    else:
        return f"Com {idade} anos: VOTO OBRIGATÓRIO"


nasc = int(input("Em que ano você nasceu? "))
print(voto(nasc))
