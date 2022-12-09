from model.imanter import *
from model.pessoa_fisica import *
from model.curso import *

lista_de_alunos = []
lista_de_curso = []
lista_de_disciplina = []

def separador():
        print('-'*20)

def menu_inicial():
    opcao = 1
    while opcao != 0:
        separador()
        print('Bem vindo(a),QAcadêmico')
        separador()
        print('[1] - Manter aluno')
        print('[2] - Manter curso')
        print('[3] - Manter disciplina')
        print('[4] - Matricular aluno')
        print('[5] - Listar todos os alunos de uma turma')
        print('[6] - Sair')
        separador()
        opcao = int(input('O que deseja fazer?\nOpção: '))

        if opcao == 1:
            menu_secundario(Aluno, lista_de_alunos)
        elif opcao == 2:
            menu_secundario(Curso, lista_de_curso)
        elif opcao == 3:
            menu_secundario(Disciplina, lista_de_disciplina)
        elif opcao == 4:
            menu_secundario()
        elif opcao == 5:
            menu_secundario()
        elif opcao == 6:
            print('Saindo...')
            opcao = 0
        else:
            print('[ERRO] Opção inválida')



def menu_secundario(classe, lista):
    opcao = 1
    while opcao != 0:
        separador()
        print('[1] - Cadastrar')
        print('[2] - Editar')
        print('[3] - Deletar')
        print('[4] - Pesquisar')
        print('[5] - Listar')
        print('[6] - Voltar')
        separador()
        opcao = int(input('O que deseja fazer?\nOpção: '))

        if opcao == 1:
            separador()
            add = classe.adicionar()
            lista.append(add)

        elif opcao == 2:

            source = classe.pesquisar(lista)

            if source:
                classe.editar(source)
            else:
                separador()
                print('[ERRO] Não encontrado,\nimpossível editar seu dados')

        elif opcao == 3:

            source = classe.pesquisar(lista)

            if source:
                lista.remove(source)
            else:
                separador()
                print('[ERRO] Não foi possível excluir')

        elif opcao == 4:

            source = classe.pesquisar(lista)

            if source:
                print(source.nome, source.cpf)
                separador()
                print('ENCONTRADO COM SUCESSO')
            else:
                separador()
                print('[ERRO] Não encontrado')

        elif opcao == 5:
            for i in lista:
                print(i.nome)
            

        elif opcao == 6: 
            opcao = 0
            separador()
            print('Voltando..')

        else:
            separador()
            print('[ERRO] Opção inválida')

menu_inicial()