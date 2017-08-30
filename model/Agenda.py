from model.Pessoa import Pessoa
import pickle
from model.Contato import Contato
class Agenda(Pessoa):

    def __init__(self,proprietario,nascimento,email):
        self.proprietario = proprietario
        self.nascimento = nascimento
        self.email = email

    def contarContatos(self):
        pass
    
    def listarContatos(self):
        pass

    def incluirContato(self):

        while (x=='s'):

            c1 = Contato(criacao=input('Digite a data de hoje:\n'), nome=input('Nome do contato:\n'), email=input('Email:\n'), numero=input('Numero de telefone:\n'), ddd=input('DDD:\n'), codigoPais=input('Codigo do Pais:\n'))
            dicc = {'Data de criação do contato': c1.criacao, 'Nome': c1.nome, 'Email': c1.email, 'Numero': c1.numero,'ddd': c1.ddd, 'Codigo do Pais': c1.codigoPais }
            arquivo = open("contatos.json", 'wb')
            pickle.dump(dicc, arquivo)
            arquivo.close()
            arquivo = open("contatos.json", "rb")
            dicc = pickle.load(arquivo)
            arquivo.close()
            x = input("Deseja adicionar mais de um conatato:\n")

    def buscarConato(self):
          pass

    def excluirContato(self,nome):
        pass
