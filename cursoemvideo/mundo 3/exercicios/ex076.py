tupla = ("Lápis", 1.75,
         "Borracha", 2.00,
         "Caderno", 15.90,
         "Estojo", 25.00, 
         "Transferidor", 4.20, 
         "Compasso", 9.99, 
         "Mochila", 120.32, 
         "Canetas", 22.30, 
         "Livro", 4.90)
print("-"*45)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print("-"*45)
for i in range(0,len(tupla)):
    if i % 2 == 0:
        print(f"{tupla[i]:.<35}",end="R$ ")
    else:
        print(f"{tupla[i]:>7.2f}")
print("-"*45)
'''
tupla = ("Lápis", 1.75,
         "Borracha", 2.00,
         "Caderno", 15.90,
         "Estojo", 25.00, 
         "Transferidor", 4.20, 
         "Compasso", 9.99, 
         "Mochila", 120.32, 
         "Canetas", 22.30, 
         "Livro", 4.90)
print("-"*45)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print("-"*45)
for i in range(0,len(tupla),2):
    print(f"{tupla[i]:.<35}",end="")
    print(f"R$ {tupla[i+1]:>7.2f}")
print("-"*45)
'''