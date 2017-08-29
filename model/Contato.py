from model.Pessoa import Pessoa
import datetime
import json

class Contato():
    def __init__(self,telefone,pessoa):
        self.telefone = telefone
        self.pessoa = pessoa
        self.criacao = datetime.datetime.now()

    def litarTelefones(self):
        pass