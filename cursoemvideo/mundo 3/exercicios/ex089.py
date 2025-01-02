alunos = []
while True:
    n1 = n2 = -1
    continuar = " "
    nome = input("Nome: ").strip().capitalize()
    while n1 not in range(0,11):
        n1 = float(input("Nota 1: "))
    while n2 not in range(0,10):
        n2 = float(input("Nota 2: "))
    media = (n1+n2)/2   
    alunos.append([nome, [n1, n2], media]) # adicionar elementos na lista criando outras listas
    while continuar not in "NS":
        continuar = input("Quer continuar? [S/N] ").upper().strip()
    if continuar in "N":
        break
print("=-"*30)
print(f"{"No.":<4}{"NOME":<10}{"MÉDIA":>8}")
print("-"*25)
for i, a in enumerate(alunos):
    print(f"{i:<4}{a[0]:<10}{a[2]:>8}")
while True:
    idx = int(input("\nMostrar notas de qual aluno (número)? (999 interrompe): "))
    if idx == 999:
        break
    if idx <= len(alunos) - 1:
        print(f"Notas de {alunos[idx][0]} são {alunos[idx][1]}")
print("FINALIZANDO...")
print("Volte sempre!")