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

        for contato in self.contatos:
            print(contato)

    def incluirContato(self):

        while (x=='s'):

            c1 = Contato(criacao=input('DIGITE A DATA DE HOJE:\n'), nome=input('NOME DO CONTATO:\n'), email=input('EMAIL:\n'), numero=input('NUMERO DE TELEFONE:\n'), ddd=input('DDD:\n'), codigoPais=input('CODIGO DO PAIS:\n'))
            dicc = {'DATA DE CRIACAO DO CONTATO': c1.criacao, 'NOME': c1.nome, 'EMAIL': c1.email, 'NUMERO': c1.numero,'DDD': c1.ddd, 'CODIGO DO PAIS': c1.codigoPais }
            arquivo = open("contatos.json", 'wb')
            pickle.dump(dicc, arquivo)
            arquivo.close()
            arquivo = open("contatos.json", "rb")
            dicc = pickle.load(arquivo)
            arquivo.close()
            x = input("DESEJA ADICIONAR MAIS UM CONTATO:\n")


    def buscarConato(self,nome):

        for contato in self.contatos:
            if contato == nome:
                return contato
            else:
                return ("Infelizmente, nome do contato  digitado inválido")

    def excluirContato(self,nome):
        self.contatos.remove(self.buscarContato(nome))
