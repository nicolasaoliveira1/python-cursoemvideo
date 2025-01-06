#Nesse arquivo ex107 foram feitos os exercícios 107, 108 e 109, 
# já que os exercícios apenas modificavam e melhoravam o mesmo código

import moeda

n = float(input("Digite o preço: R$"))
print(f"A metade de {moeda.formata(n)} é {moeda.metade(n,False)}")
print(f"O dobro de {moeda.formata(n)} é {moeda.dobro(n,)}")
print(f"Aumentando o valor em 10%, temos {moeda.aumentar(n,10,False)}")
print(f"Reduzindo o valor em 13%, temos {moeda.diminuir(n,13)}")
