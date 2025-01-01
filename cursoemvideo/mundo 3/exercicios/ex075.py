nums = (int(input("Digite um número: ")), int(input("Digite outro número: ")), int(input("Digite mais um número: ")), int(input("Digite o último número: ")))
print("Você digitou os valores", nums)
if 9 in nums:
    print(f"O número 9 apareceu {nums.count(9)} vezes")
else:
    print("O número 9 não aparece na tupla!")
if 3 in nums:
    ind = nums.index(3) + 1
    print(f"O número 3 apareceu na {ind} posição")
else:
    print("O número 3 não aparece na tupla!")
print("Os valores pares digitados foram ",end="")
for n in nums:
    if n % 2 == 0:
        print(n,end=" ")