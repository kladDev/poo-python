from model.imanter import IManter

class Curso(IManter):
    def __init__(self, nome: str, descricao: str):
        self.nome = nome
        self.descricao = descricao
        self.disciplina = []
    
    def adicionar():
        nome = input('Digite o nome da disciplina: ')
        descricao = input('Digite a descrição da disciplina: ')

        return Curso(nome, descricao)

    def editar(curso):
        opcao = 1
        while opcao != 0:
            print('-'*20)
            print(f'Editar curso de {curso.nome}')
            print('-'*20)
            print('[1] - Nome')
            print('[2] - Descrição')
            print('[3] - Concluir')
            opcao = int(input('O que deseja editar?\nSua opção: '))

            if opcao == 1:
                curso.nome = input('Novo nome do curso: ')
            elif opcao == 2:
                curso.descricao = input('Nova descrição do curso: ')
            elif opcao == 3:
                print('Alterações do curso feita com sucesso')
                opcao = 0
            else:
                print('[ERRO] Opção inválida')

    def pesquisar(lista):
        print('-'*20)
        nome = input('Digite o nome da disciplina: ')
        for i in lista:
            if i.nome == nome:
                return i

class Disciplina(IManter):
    def __init__(self, nome: str, descricao: str, carga_horaria: int, ano: int, semestre: int):
        self.nome = nome
        self.descricao = descricao
        self.carga_horaria = carga_horaria
        self.ano = ano
        self.semestre = semestre
    
    def adicionar():
        nome = input('Digite o nome da disciplina: ')
        descricao = input('Digite a descrição da disciplina: ')
        carga_horaria= int(input('Digite a carga horária: '))
        ano = int(input('Digite o ano da disciplina: '))
        semestre = int(input('Digite o semestre: '))

        return Disciplina(nome, descricao, carga_horaria, ano, semestre)

    def pesquisar(lista):
        print('-'*20)
        nome_disciplina = input('Qual o nome da disciplina?\nSua Opção: ')
        for i in lista:
            if i.nome == nome_disciplina:
                return i

    def editar(disciplina):
        opcao = 1
        while opcao != 0:
            print('-'*20)
            print(f'Editar disciplina de {disciplina.nome}')
            print('-'*20)
            print('[1] - Nome')
            print('[2] - Descrição')
            print('[3] - Carga Horária')
            print('[4] - Ano')
            print('[5] - semestre')
            print('[6] - Concluir')
            opcao = int(input('O que deseja editar?\nSua opção: '))

            if opcao == 1:
                disciplina.nome = input('Novo nome da disciplina: ')
            elif opcao == 2:
                disciplina.descricao = input('Nova descrição: ')
            elif opcao == 3:
                disciplina.carga_horaria = int(input('Nova carga horária: '))
            elif opcao == 4:
                disciplina.ano = int(input('Novo ano: '))
            elif opcao == 5:
                disciplina.semestre = int(input('Novo semestre: '))
            elif opcao == 6:
                print('Alteraçõs feitas com sucesso em disciplina')
                opcao = 0
            else:
                print('[ERRO] Opção inválida')