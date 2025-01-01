print("="*25)
print("10 TERMOS DE UMA PA")
print("="*25)
inicio = int(input("Primeiro termo: "))
razao = int(input("Razão: "))
for i in range(inicio, inicio + razao*10, razao):
    print(i,end=" → ")
print("ACABOU")