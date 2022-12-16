from model.conexao import connection    

class ContaCorrente:
    def __init__(self, numero_conta: str, agencia: str, valor = 0):
        self.conta = numero_conta
        self.agencia = agencia
        self.valor = valor
        self.__adicionar__(numero_conta, agencia, valor)

    def __adicionar__(self, numero_conta, agencia, valor):
        with connection.cursor() as c:
            sql = "INSERT INTO conta_corrente (numero_conta, agencia, saldo) VALUES (%s, %s, %f)"
            c.execute(sql, (numero_conta, agencia, valor))
            connection.commit()



    