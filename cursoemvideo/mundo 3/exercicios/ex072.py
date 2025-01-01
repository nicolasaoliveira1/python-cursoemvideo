nums = ("zero","um","dois","três","quatro","cinc","seis","sete","oito","nove","dez","onze","doze","treze","catorze","quinze","dezesseis", "dezessete", "dezoito","dezenove","vinte")
while True:
    sn = " "
    num = int(input("Digite um número entre 0 e 20: "))
    if num not in range(0,21):
        print("Tente novamente. ",end="")
    else:
        print(f"Você digitou o número {nums[num]}.")
        while sn not in "SN":
            sn = input("Quer continuar? [S/N] ").upper().strip()
        if sn == "N":
            break
print("\nObrigado por utilizar o programa!")
