from model.imanter import IManter

class PessoaFisia:
    def __init__(self, nome: str, cpf: str) -> None:
        self.nome = nome
        self.cpf = cpf

class Aluno(PessoaFisia, IManter):
    def __init__(self, nome: str, cpf: str, matricula: int, ano_de_ingresso: int):
       super().__init__(nome, cpf)
       self.matricula = matricula
       self.ano_de_ingresso = ano_de_ingresso
       self.curso = None

    def adicionar():
        nome = input('Nome: ')
        cpf = input('CPF: ')
        matricula = int(input('Matricula: '))
        ano_de_ingresso = int(input('Ano de ingresso: '))

        return Aluno(nome, cpf, matricula, ano_de_ingresso)

    def pesquisar(lista):
        print('-'*20)
        matricula = int(input('Digite a matricula que deseja\nMatricula: '))
        for i in lista:
            if i.matricula == matricula:
                return i

    def editar(aluno):
        opcao = 1
        while opcao != 0:
            print('-'*20)
            print(f'Editar dados de {aluno.nome}')
            print('-'*20)
            print('[1] - Nome')
            print('[2] - CPF')
            print('[3] - Matricula')
            print('[4] - Ano de ingresso')
            print('[5] - Concluir')
            opcao = int(input('O que deseja editar?\nSua opção: '))

            if opcao == 1:
                aluno.nome = input('Novo nome: ')
            elif opcao == 2:
                aluno.cpf = input('Novo CPF: ')
            elif opcao == 3:
                aluno.matricula = int(input('Nova matrícula: '))
            elif opcao == 4:
                aluno.ano_de_ingresso = int(input('Novo ano de ingresso: '))
            elif opcao == 5:
                opcao = 0
                print('Alterações feitas com sucesso!')
            else:
                print('[ERRO] Opção inválida')



class Professor(PessoaFisia):
    def __init__(self, nome: str, cpf: str, salario: float, formacao: str):
        super().__init__(nome, cpf)
        self.salario = salario
        self.formacao = formacao

class Tecnico(PessoaFisia):
    def __init__(self, nome: str, cpf: str, area_de_atuacao: str):
        super().__init__(nome, cpf)
        self.area_de_atuacao = area_de_atuacao