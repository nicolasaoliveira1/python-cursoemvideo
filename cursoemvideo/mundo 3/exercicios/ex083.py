expr = input("Digite uma expressão matemática: ").strip()
pilha = []
for simb in expr:
    if simb == "(":
        pilha.append(simb)
    elif simb == ")":
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(")")
            break
if len(pilha) == 0:
    print("Expressão válida")
else:
    print("Expressão inválida")
