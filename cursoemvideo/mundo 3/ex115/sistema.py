from lib.interface import *
from lib.arquivo import *
from time import sleep

arq = "cursoemvideo.txt"

if not arquivoExiste(arq):
    criarArquivo(arq)
    
while True:
    resposta = menu(["Ver pessoas cadastradas","Cadastrar nova pessoa", "Remover uma pessoa", "Sair do sistema"])
    if resposta == 1:
        # opção de listar o conteúdo de um arquivo
        lerArquivo(arq)
    elif resposta == 2:
        cabeçalho("NOVO CADASTRO")
        nome = leiaNome("Nome: ") #função nova implementada
        idade = leiaInt("Idade: ")
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        cabeçalho("REMOVER PESSOA")
        lerArquivo(arq)
        idx = leiaInt("Cód. da pessoa a ser removida: ")
        remover(arq,idx) #função nova implementada
    elif resposta == 4:
        cabeçalho("Saindo do sistema.. Até logo!")
        break
    else:
        print("ERRO! Digite uma opção válida")
    sleep(1)
