from model.contacorrente import ContaCorrente 
from model.conexao import connection    

class Cliente:
    def __init__(self, nome: str):
        self.nome = nome
        self.conta = None
        self.__adicionar__(nome)

    def criar_conta(self, numero_conta: int, agencia: str):
        self.conta = ContaCorrente(numero_conta, agencia)

    def __adicionar__(self, nome):
        with connection.cursor() as c:
            sql = "INSERT INTO cliente (nome) VALUES (%s)"
            c.execute(sql, (nome))
            connection.commit()