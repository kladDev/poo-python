from model.funcao import Funcao
from model.funcionario import Funcionario
from config.conexao import conectar

def separador():
    print('-'*20)

def menu():
    condicao = None

    separador()
    print("BEM VINDO À NOSSA EMPRESA")
    print('O que deseja fazer?')
    
    while condicao != 0:
        separador()
        print('[1] - Manter Funções')
        print('[2] - Manter Funcionário')
        print('[0] - Sair')
        separador()

        try:
            opcao = int(input('Sua opção: '))

            if opcao == 1:
                menu_funcao()
            elif opcao == 2:
                existe_funcao = Funcao.__verificar_funcao__()

                if existe_funcao:
                    menu_funcionario()
                else:
                    print('[ERROR] Não existe nenhum função cadastrada')

            elif opcao == 0:
                condicao = 0
            else:
                print('[ERROR] Opção inválida')

        except ValueError:

            print("[ERROR] Você não digitou um número inteiro")
        
def dados_funcao():
    nome = str(input('Nome da função: '))

    condicao = 0

    while condicao != -1:
        cod = str(input('Codigo do função: '))
        if len(cod) <= 5:
            condicao = -1
        else:
            print('[ERROR] Código só pode tem no máximo 5 caracteres') 

    separador()

    conexao = conectar()

    f = Funcao(cod, nome)

    with conexao.cursor() as c:
        sql = "INSERT INTO funcao (cod, nome) VALUES (%s, %s)"
        c.execute(sql, (f.cod, f.nome))
    conexao.commit()
    conexao.close()

def menu_funcao():

    separador()
    print('O que deseja fazer')
    separador()

    condicao = 1

    while condicao != 0:

        condicao = 1

        existe_funcao = Funcao.__verificar_funcao__()

        print('[1] - Cadastrar Função')
        print('[2] - Pesquisar Função')
        print('[3] - Editar Função')
        print('[4] - Deletar Função')
        print('[0] - Voltar ao menu princial')
        separador()
        
        while condicao != -5:
            try:
                opcao = int(input('Sua opção: '))
                separador()
                condicao = -5
            except ValueError:
                print("[ERROR] Você não digitou um número inteiro")

        if existe_funcao:

                if opcao == 1:
                    dados_funcao()
                elif opcao == 2:

                    pesquisa = Funcao.pesquisar_funcao()

                    if pesquisa:
                        print('Dados encontrado com sucesso !')
                        print(f'O nome da função é {pesquisa["nome"]}')
                        print(f'E seu código é {pesquisa["cod"]}')
                        separador()
                    else:
                        print('Não foi possivel encontrar')
                        separador()

                elif opcao == 3:
                    Funcao.__editar_funcao__()
                elif opcao == 4:
                    Funcao.__delete_funcao__()
                elif opcao == 0:
                    condicao = 0
                else:
                    print('[ERROR] Opção inválida')
        else:
            if opcao == 1:
                dados_funcao()
            elif opcao == 0:
                condicao = 0
            else:
                print('[ERROR] Não é possível editar, pesquisar ou deletar.')
                print('[MOTIVO] Não tem função cadastrada')
                separador()

def menu_funcionario():

    separador()
    print('O que deseja fazer')
    separador()

    condicao = 1

    while condicao != 0:

        print('[1] - Cadastrar Funcionário')
        print('[2] - Pesquisar Funcionário')
        print('[3] - Editar Funcionário')
        print('[4] - Deletar Funcionário')
        print('[0] - Voltar ao menu princial')
        separador()
        
        try:
            opcao = int(input('Sua opção: '))
            separador()

            if opcao == 1:

                nome = str(input("Nome: "))

                while condicao != -1:
                    cpf = str(input('CPF: '))

                    if cpf.isnumeric() and len(cpf) == 11 and int(cpf) > 0:
                        condicao = -1 
                    else:
                        print('[ERRO] Somente letras e tamanho deve ser igual a 11')

                while condicao != -3:
                    try:
                        salario = float(input('Salário: '))

                        if salario > 0:
                            condicao = -3
                        else:
                            print('[ERROR] Salário não pode ser negativo')
                    except ValueError:

                        print('[ERROR] Somente números positivos')
                    
                telefone = input('Telefone: ')
                
                while condicao != -4:
                    dado = Funcao.pesquisar_funcao()

                    if dado:
                        f = Funcionario(nome, cpf, Funcao(dado['cod'], dado['nome']), salario, telefone)
                        condicao = -4
                    else:
                        print('[ERROR] Código inválido, tente novamente ...')

            elif opcao == 2:

                registro = Funcionario.pesquisar_funcionario()

                if registro:
                    print('Funcionário encontrado !\n')
                    print(f'Nome: {registro["nome"]}')
                    print(f'CPF: {registro["cpf"]}')
                    print(f'Salário: {registro["salario"]}')
                    print(f'Telefone: {registro["telefone"]}')
                    print(f'Função: {registro["funcao.nome"]}')
                    separador()
                else:
                    print('[ERROR] Funcionário não cadastrado')
                    separador()
                
            elif opcao == 3:
                Funcionario.__editar_funcionario__()
            elif opcao == 4:
                Funcionario.__deletar_funcionario__()
            elif opcao == 0:
                condicao = 0
            else:
                print('[ERROR] Opção inválida')

        except ValueError:

            print('[ERROR] Aceita somente números')       

menu()