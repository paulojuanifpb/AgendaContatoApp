from model.Pessoa import Pessoa
from model.Agenda import Agenda
from model.Contato import Contato
from model.Telefone import Telefone
from datetime import datetime
import json
import pickle


def main():

    #cadastro do proprietário
    print("INFORME OS DADOS QUE SERÃO PEDIDOS PARA SER CADASTRADO COMO PROPRIETARIO:\n ")
    e1 = Agenda(proprietario = input('DIGITE O SEU NOME:\n'),nascimento = input("DIDITE A SUA DADTA DE NASCIMENTO:\n"),email= input("DIGITE O SEU EMAIL:\n"))
    dicp = {'Nome': e1.proprietario , 'Data de Nascimento': e1.nascimento, 'Email': e1.email}
    arquivo = open("proprietario.json",'wb')
    pickle.dump(dicp,arquivo)
    arquivo.close()
    arquivo = open("proprietario.json","rb")
    dicp = pickle.load(arquivo)
    arquivo.close()
    menu(e1)


def menu(e1):
    while True :

            print("Menu : \n 1 - Incluir contato\n 2 - Listar contatos\n 3 - Remover contato\n 4 - Buscar contato\n 5 - Quantidade de contatos \n 6 - Sair")
            resp = int(input("Escolha uma das opções do menu :\n"))

            if (resp == 1):
               e1.incluirContato()


            elif (resp == 2):
                e1.listarContatos()
            elif (resp == 3):
                e1.excluirContato()
            elif (resp == 4):
                e1.buscarContato()
            elif (resp == 5):
                e1.contarContatos()
            break


if __name__ == "__main__":
    main()