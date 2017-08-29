from model.Pessoa import Pessoa
from model.Agenda import Agenda
from model.Contato import Contato
from model.Telefone import Telefone
from datetime import datetime
import json

def main():
    e1 = Agenda("paulo"," "," "," ",00,00,00)
    menu(e1)

def menu(e1):
    while True :
        try:
            print("Menu : \n 1 - Incluir contato\n 2 - Listar contatos\n 3 - Remover contato\n 4 - Buscar contato\n 5 - Quantidade de contatos \n 6 - Sair")
            resp = int(input("Escolha uma das opções do menu :\n"))

            if (resp == 1):
                nome = str(input("Informe o seu nome:"))
                nascimento = str(input("Informe a sua data de nascimento:"))
                email = str(input("Informe o seu email:"))
                numero = int(input("Informe o seu numero:"))
                ddd = int(input("Informe o seu ddd:"))
                codigoPais = int(input("Informe o código do seu País:"))
                criacao = datetime
                pessoa = Pessoa(nome, nascimento, email)
                telefone = Telefone(numero, ddd, codigoPais)
                contato = Contato(pessoa, criacao, telefone)

            elif (resp == 2):
                e1.listarContatos()
            elif (resp == 3):
                e1.excluirContato()
            elif (resp == 4):
                e1.buscarContato()
            elif (resp == 5):
                e1.contarContatos()
            break
        except:
            print("Ouve algum erro... Please, tente novamente!")

if __name__ == "__main__":
    main()