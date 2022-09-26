# Aluno: Antonio Claudio Teixeira Alves
lista_funcionarios = []

def interface():
    condicao = 0
    while condicao != 1:
        print("[1] - Cadastrar Funcionários")
        print("[2] - Pesquisar funcionário")
        print("[0] - Sair")
        opcao = int(input("Sua opção: "))

        if opcao == 1:

            nome = input("Digite o nome: ")
            cpf = int(input("Digite o cpf (somente numeros): "))
            cargo = input("Digite o cargo: ")
            salario = float(input("Digite o salário: "))
            telefone = int(input("Digite o telefone (somente numeros): "))

            lista_funcionarios.append(cadastro_funcionario(nome, cpf, cargo, salario, telefone))
            print("Funcionario cadastro com sucesso!")

        elif opcao == 2:

            cpf = int(input("Digite o cpf do funcionario que deseja buscar: "))
            busca = pesquisar_funcionario(cpf)

            if busca != 0:
                sub_interface(busca)
            else:
                print("[ERRO] Usuário não encontrado")

        elif opcao == 0:

            print("Saindo...")
            condicao = 1

        else:

            print("[ERRO] Opção inválida")

def sub_interface(funcionario):
    condicao = 0
    while condicao != 1:

        print("[1] - Cadastro novo telefone")
        print("[2] - Editar dados do funcionário")
        print("[3] - Deletar Funcionário")
        print("[0] - Voltar")
        opcao = int(input("Sua opção: "))

        if opcao == 1:
            cadastra_telefone(funcionario)
            print("Telefone cadastrado com sucesso !")
        elif opcao == 2:
            editar_funcionario(funcionario)
        elif opcao == 3:
            demitir_funcionario(funcionario)
            condicao = 1
        elif opcao == 0:
            condicao = 1
        else:
            print("[ERRO] Opcao invalida!")

def cadastro_funcionario(nome, cpf, cargo, salario, telefones):

    if salario < 0:
        salario = 0

    dados = {
        "nome": nome,
        "cpf": cpf,
        "cargo": cargo,
        "salario": salario,
        "telefones": [],
    }
    dados["telefones"].append(telefones)

    return dados

def pesquisar_funcionario(cpf):
    for i in lista_funcionarios:
        if i["cpf"] == cpf:
            print(f"Nome: {i['nome']}")
            print(f"CPF: {i['cpf']}")
            print(f"Cargo: {i['cargo']}")
            print(f"Salário: {i['salario']}")

            print("Telefones: ", end="")
            for j in i["telefones"]:
                print(j, end=" ")
            print("")

            return i
    return 0

def cadastra_telefone(funcionario):
    telefone = int(input("Digite o novo telefone: "))
    funcionario["telefones"].append(telefone)


def editar_funcionario(funcionario):
    funcionario["nome"] = input("Edite o nome: ")
    funcionario["cpf"] = int(input("Edite o CPF (somente numeros): "))
    funcionario["cargo"] = input("Edite o cargo: ")
    funcionario["salario"] = float(input("Edite o salário: "))

    for i in funcionario["telefones"]:
        i = int(input("Edite os tefefone do contato: "))

def demitir_funcionario(funcionario):
    lista_funcionarios.remove(funcionario)
    print("Funcionário demitido !")

interface()