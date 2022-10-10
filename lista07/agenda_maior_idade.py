# Antonio Claudio Teixeira Alves

# Crie um programa que cadastre informações de várias
# pessoas (nome, idade e cpf) e depois coloque em um
# dicionário. Depois remova todas as pessoas menores de
# 18 anos do dicionário e coloque em outro dicionário

lista_maioridade = []
lista_menoridade= []

def interface():
    print("-"*15)
    print("Cadastramento de clientes")
    print("-"*15)

    condicao = 0

    while condicao != 1:
        print("[1] - Cadastrar usuários")
        print("[2] - Mostrar todos os usuários")
        print("[3] - Remover os usuários menores de 18 anos")
        print("[4] - Mostrar usuários removidos")
        print("[5] - Sair")

        opcao = int(input("Sua opção: "))

        if opcao == 1:
            lista_maioridade.append(cadastrar_usuario())
            print("Usuário cadastro com sucesso!")
        elif opcao == 2:
            mostrar_usuarios(lista_maioridade)
        elif opcao == 3:
            remover_usuarios_menor()
            print("Usuários com menores de idade removido com sucesso!")
        elif opcao == 4:
            mostrar_usuarios(lista_menoridade)
        elif opcao == 5:
            condicao = 1
            print("Saindo...")
        else:
            print("[ERRO] Opção inválida")

def cadastrar_usuario():
    nome = input("Nome: ")
    idade = int(input("Idade: "))
    cpf = int(input("CPF (somente números): "))

    return {'nome': nome, 'idade': idade, 'cpf': cpf}

def mostrar_usuarios(lista):
    if len(lista) == 0:
        print("Lista vazia!")
    else:
        for i in lista:
            print(i)

def remover_usuarios_menor():
    for i in lista_maioridade:
        if i['idade'] < 18:
            lista_menoridade.append(i)

interface()
