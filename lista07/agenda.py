# Antonio Claudio Teixeira Alves

# Crie um dicionário que é uma agenda e coloque nele
# os seguintes dados: chave (cpf), nome, idade, telefone.
# O programa deve ler um número indeterminado de dados,
# criar a agenda e imprimir todos os itens do dicionário
# no formato chave: nome-idade-fone

agenda = []

def adicionar():
    cpf = int(input("Digite seu CPF (somente números): "))
    nome = input("Digite seu nome: ")
    idade = int(input("Digite sua idade: "))
    telefone = int(input("Digite seu telefone (somente números): "))

    return {'cpf': cpf, 'nome': nome, 'idade': idade, 'telefone': telefone}

def mostrar():
    if len(agenda) == 0:
        print("Lista vazia!")
    else:
        for i in agenda:
            print(f"Nome: {i['nome']}")
            print(f"Idade: {i['idade']}")
            print(f'Telefone: {i["telefone"]}\n')

def interface():
    print("-"*16)
    print("AGENDA DE PESSOAS")
    print("-"*16)

    condicao = 0
    while condicao != 1:
        print("[1] - Cadastrar pessoas")
        print("[2] - Mostrar agenda")
        print("[3] - Sair")
        opcao = int(input("Sua opcao: "))

        if opcao == 1:
            agenda.append(adicionar())
            print("Cadastrada com sucesso!")
        elif opcao == 2:
            mostrar()
        elif opcao ==3:
            condicao = 1
            print("Saindo...")
        else:
            print("[ERRO] Opcao invalida")

interface()
