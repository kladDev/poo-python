# Antonio Claudio Teixeira Alves

# Considere um sistema onde os dados são armazenados
# em dicionários. Nesse sistema existe um dicionario
# principal e o dicionário de backup. Cada vez que o
# dicionário principal atinge tamanho 5, ele imprime
# os dados na tela e apaga o seu conteúdo. Crie um
# programa que insira dados em um dicionário, realizando
# o backup a cada dado e excluindo os dados do dicionário
# principal quando ele atingir tamanho 5

lista = []
backup = []


def cadastrar():
    valor = 0
    valor += 1
    return {'valor': valor}

def mostrar(list):
    if len(list) == 0:
        print("Lista vazia")
    else:
        for i in list:
            print(i)

def interface():
    print("-"*15)
    print("SISTEMA DE BACKUP")
    print("-"*15)

    condicao = 0

    while condicao != 1:
        print("[1] - Cadastrar")
        print("[2] - Mostrar")
        print("[3] - Mostrar Backup")
        print("[4] - Sair")

        opcao = int(input("Sua opção: "))

        if opcao == 1:

            lista.append(cadastrar())
            print("Cadastrado com sucesso!")
            if len(lista) == 5:
                print("Lista atingiu seu limite")
                for i in range(5):
                    print(lista[i])
                    backup.append(lista[i])
                lista.clear()
        elif opcao == 2:
            mostrar(lista)
        elif opcao == 3:
            mostrar(backup)
        elif opcao == 4:
            condicao = 1
            print("Saindo ...")
        else:
            print("[ERRO] Opção inválida")

interface()