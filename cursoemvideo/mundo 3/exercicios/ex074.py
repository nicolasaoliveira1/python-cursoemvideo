from random import randint
v = (randint(1,10), randint(1,10), randint(1,10), randint(1,10), randint(1,10), )
print("Os números sorteados foram: ",end="")
for n in v:
    print(n,end=" ")
print("\nO maior valor foi",max(v))
print("O menor valor foi",min(v))
