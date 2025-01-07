from lib.interface import *

def arquivoExiste(nome):
    try:
        a = open(nome, "rt")
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close
    except:
        print("Houve um erro na criação do arquivo.")
    else:
        print(f"Arquivo {nome} criado com sucesso!")

def lerArquivo(nome):
    try:
        a = open(nome,"rt")
    except:
        print("Erro ao ler o arquivo.")
    else:
        cabeçalho("PESSOAS CADASTRADAS")
        for i, linha in enumerate(a):
            dado = linha.split(";")
            dado[1] = dado[1].replace("\n", "")
            print(f"{i} - {dado[0]:<30}{dado[1]:>3} anos")
    finally:
        a.close()

def cadastrar(arq, nome="Desconhecido", idade = 0):
    try:
        a = open(arq, "at")
    except:
        print("Houve um ERRO na abertura do arquivo.")
    else:
        try:
            a.write(f"{nome};{idade}\n")
        except:
            print("Houve um erro na hora de escrever os dados.")
        else:
            print(f"Novo registro de {nome} adicionado!")
        finally:
            a.close()

def remover(arq, idx): #função nova para remover pessoas cadastradas
    try:
        a = open(arq, "rt")
        nomes = []
        dado = []
    except:
        print("Houve um ERRO ao ler o arquivo.")
    else:
        try:
            for linha in a:
                nomes.append(linha)
                dado.append(linha.split(";"))
            nome_removido = dado[idx][0]
            del(nomes[idx])
            a = open(arq, "wt")
            for n in nomes:
                a.write(n)
        except IndexError:
            print("Índice inválido, tente novamente.")
        except:
            print("Houve um erro")
        else:
            print(f"{nome_removido} foi removido(a) da lista.")
