tupla = ("APRENDER", "PROGRAMAR", "LINGUAGEM", "PYTHON", "CURSO", "GRATIS", "ESTUDAR", "PROGRAMADOR")
for i in tupla:
    print(f"\nNa palavra {i} temos",end=" ")
    for l in i:
        if l in "AEIOU":
            print(l,end=" ")
