from model.Telefone import Telefone
from model.Contato import Contato
import json

class Agenda():

    def __init__(self,proprietario,nome,nascimento,email,numero,ddd,codigoPais):
        self.proprietario = proprietario
        self.contatos = []
        self.nome = nome
        self.nascimento = nascimento
        self.email = email
        self.numero = numero
        self.ddd = ddd
        self.codigoPais = codigoPais

    def contarContatos(self):
        return len(self.contatos)
    def listarContatos(self):

        for contato in self.contatos:
            print(contato)

    def incluirContato(self, contato):
        self.contatos.append(contato)
    def buscarConato(self,nome):

        for contato in self.contatos:
            if contato == nome:
                return contato
            else:
                return ("Infelizmente, nome do contato  digitado inválido")

    def excluirContato(self,nome):
        self.contatos.remove(self.buscarContato(nome))

    def salvarJson(self):
        arquivo = open('contatos.json', 'w')
        arquivo.write(json.dumps(self.contatos))
        arquivo.close()