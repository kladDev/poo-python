import os
'''
     Criar um sistema que exiba para o usuário
     um menu com as seguintes opções:
            1 - Cadastrar Nova Conta
            2 - Encontrar uma conta
                1 - Remover Conta
                2 - Realizar transferência
                3 - Exibir saldo
                4 - Deposita Valor
'''

lista_contas = []

def limpar():
    os.system('clear')

def interface():
        sair = 0

        while sair != 3:

            print("[1] - Cadastrar nova conta")
            print("[2] - Encontrar uma conta")
            print("[3] - Sair")
            opcao = int(input("Opcao: "))

            limpar()

            if opcao == 1:

                numero = int(input("Número da conta: "))
                titular = input("Nome do titular: ")
                saldo = float(input("Saldo: "))

                limpar()
                lista_contas.append(criar_conta(numero, titular, saldo))

            elif opcao == 2:

                numero = int(input("Digite o numero da conta: "))
                conta_atual = busca_conta(numero)

                if conta_atual:
                    sub_interface(conta_atual)
                else:
                    print("[ERRO] Conta inexistente!")

            elif opcao == 3:

                sair = 3

            else:

                print("[ERRO] Opcao inválida")

def sub_interface(conta_atual):
    sair = 0

    while sair != 5:
        print("[1] - Remover conta")
        print("[2] - Realizar transferência")
        print("[3] - Exibir saldo")
        print("[4] - Depositar valor")
        print("[5] - Voltar")
        opcao = int(input("Opcao: "))
        limpar()

        if opcao == 1:

            remover_conta(conta_atual)
            interface()
            sair = 5

        elif opcao == 2:

            conta_desejada = int(input("Você deseja transferir para qualquer número de conta: "))
            conta_recebedora = busca_conta(conta_desejada)

            if conta_recebedora:

                print("Destinatário encontrado !")
                valor = float(input("Deseja transferir quantos R$ "))

                if conta_recebedora == conta_atual:
                    print("[ERRO] Você está tentando fazer uma transição pra si mesmo")
                else:
                    transferir_saldo(conta_atual, conta_recebedora, valor)

            else:
                print("[ERRO] Conta inválida")

        elif opcao == 3:

            mostrar_saldo(conta_atual)

        elif opcao == 4:

            valor = float(input("Deseja depositar quantos R$ "))
            if (valor > 0):
                depositar_dinheiro(conta_atual, valor)
            else:
                print("[ERRO] Impossível depositar valores negativos")

        elif opcao == 5:

            sair = 5
            limpar()
            interface()

        else:
            print("[ERRO] Opção inválida")


'''
    Para a opção nova conta deverá ser criado um
    função que receberá como argumentos: numero,
    titular, saldo e retornar um dicionário com
    essas informações. Cada conta criada deverá
    ser adicionada em uma lista de contas
'''

def criar_conta(numero, titular, saldo=0):
     nova_conta = {
        "numero": numero,
        "titular": titular,
        "saldo": saldo
    }
     print("Conta criado com sucesso!")
     return nova_conta

'''
    Criar uma função que encontra uma conta na 
    lista de contas a partir do numero da conta
    e mostre um novo menu
'''

def busca_conta(numero):
    for i in lista_contas:
        if i["numero"] == numero:
            print("Conta encontrada com sucesso!")
            return i
    return None

'''
    Deve ser criado uma função para remover uma
    conta da lista de contas
'''

def remover_conta(conta):
    lista_contas.remove(conta)
    print("Conta excluida com sucesso!")

'''
    Deve criar uma função para transferir valores
    de uma conta para outra respeitando os limites
'''

def transferir_saldo(conta_atual, conta_recebedora, valor):
    if valor <= conta_atual["saldo"] and valor > 0:
        for i in lista_contas:
            if i == conta_atual:
                conta_atual["saldo"] -= valor
            if i == conta_recebedora:
                conta_recebedora["saldo"] += valor
        print("Transferência feita com sucesso!")
    else:
        print(f"[ERRO] Você não possui esse valor {valor}")

'''
    Criar uma função para exibir o saldo de 
    uma conta especifica
'''

def mostrar_saldo(conta_atual):
    print(f'Você possui R${conta_atual["saldo"]}')

'''
    Criar uma função para depositar uma quantia
    na conta escolhida
'''

def depositar_dinheiro(conta_atual, valor):
    conta_atual["saldo"] += valor
    print("Valor depositado com sucesso!")

interface()
