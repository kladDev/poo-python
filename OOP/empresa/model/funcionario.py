from model.funcao import Funcao
from config.conexao import conectar


class Funcionario():
    def __init__(self, nome: str, cpf: str, funcao: Funcao, salario: float, telefone: str) -> None:
        self.nome = nome
        self.cpf = cpf
        self.funcao = funcao
        self.salario = salario
        self.telefone = telefone
        self.__inserir_funcionario__()

    def __inserir_funcionario__(self):
        conexao = conectar()

        with conexao.cursor() as c:
            sql = "INSERT INTO funcionario (cpf, nome, funcao, salario, telefone) VALUES (%s, %s, (SELECT funcao.id FROM funcao WHERE cod = %s), %s, %s)"
            c.execute(sql, (self.cpf, self.nome, self.funcao.cod, self.salario, self.telefone))
        conexao.commit()
        conexao.close()

    @staticmethod
    def pesquisar_funcionario():
        cpf = input('Informe o cpf desejado: ')
        print('-'*20)

        conexao = conectar()
        with conexao.cursor() as c:
            sql = "SELECT funcionario.cpf, funcionario.nome, funcionario.salario, funcionario.telefone, funcao.nome  FROM funcionario, funcao  WHERE funcao.id = funcionario.funcao AND funcionario.cpf = %s"
            c.execute(sql, (cpf))
            res_one = c.fetchone()
            conexao.close()
            return res_one

    @staticmethod
    def __editar_funcionario__():
        registro = Funcionario.pesquisar_funcionario()

        if registro:
            print('O que deseja editar?')
            condicao = 1

            while condicao != 0:
                print('[1] - Nome')
                print('[2] - CPF')
                print('[3] - Salário')
                print('[4] - Telefone')
                print('[5] - Função')
                print('[0] - Voltar')
                print('-'*20)
                try:
                    opcao = int(input('Sua opção: '))
                    if opcao == 1:
                        nome = str(input('Novo nome: '))
                        print('-'*20)

                        conexao = conectar()
                        with conexao.cursor() as cursor:
                            sql = "UPDATE funcionario SET nome=%s WHERE cpf=%s"
                            cursor.execute(sql, (nome, registro['cpf']))
                        conexao.commit()
                        conexao.close()

                        print('Nome atualizado com sucesso !')
                        print('-'*20)

                    elif opcao == 2:
                        while condicao != -1:
                            cpf = str(input('CPF: '))

                            if cpf.isnumeric() and len(cpf) == 11 and int(cpf) > 0:
                                condicao = -1 
                            else:
                                print('[ERRO] Somente letras e tamanho deve ser igual a 11')

                        conexao = conectar()
                        with conexao.cursor() as cursor:
                            sql = "UPDATE funcionario SET cpf=%s WHERE cpf=%s"
                            cursor.execute(sql, (cpf, registro['cpf']))
                        conexao.commit()
                        conexao.close()

                        registro['cpf'] = cpf
                        print('-'*20)
                        print('CPF atualizado !')
                        print('-'*20)

                    elif opcao == 3:

                        while condicao != -3:
                            try:
                                salario = float(input('Salário: '))

                                if salario > 0:
                                    print('-'*20)
                                    print('Salário atualizado com sucesso !')
                                    print('-'*20)

                                    conexao = conectar()
                                    with conexao.cursor() as cursor:
                                        sql = "UPDATE funcionario SET salario=%s WHERE cpf=%s"
                                        cursor.execute(sql, (salario, registro['cpf']))
                                    conexao.commit()
                                    conexao.close()
                                    
                                    condicao = -3

                                else:
                                    print('[ERROR] Salário não pode ser negativo')

                            except ValueError:

                                print('[ERROR] Somente números positivos')

                            
                    elif opcao == 4:
                        telefone = str(input('Novo telefone: '))

                        conexao = conectar()
                        with conexao.cursor() as cursor:
                            sql = "UPDATE funcionario SET telefone=%s WHERE cpf=%s"
                            cursor.execute(sql, (telefone, registro['cpf']))
                        conexao.commit()
                        conexao.close()

                        print('-'*20)
                        print('Telefone atualizado com sucesso !')
                        print('-'*20)

                    elif opcao == 5:
                        funcao = Funcao.pesquisar_funcao()

                        if funcao:
                            print(f'Função atualizada para {funcao["nome"]}')
                            print('-'*20)

                            conexao = conectar()
                            with conexao.cursor() as cursor:
                                sql = "UPDATE funcionario SET funcao=(SELECT funcao.id FROM funcao WHERE cod=%s) WHERE cpf= %s"
                                cursor.execute(sql, (funcao['cod'], registro['cpf']))
                            conexao.commit()
                            conexao.close()

                    elif opcao == 0:
                        condicao = 0
                    else:
                        print('[ERROR] Opção inválida')

                except ValueError:
                    print('[ERROR] Aceita somente numero')
    
    @staticmethod
    def __deletar_funcionario__():
        registro = Funcionario.pesquisar_funcionario()

        if registro:
            conexao = conectar()
            with conexao.cursor() as cursor:
                sql = "DELETE FROM funcionario WHERE cpf=%s"
                cursor.execute(sql, (registro['cpf']))
            conexao.commit()
            conexao.close()

            print('Excluindo com sucesso !')
            print('-'*20)  

        else:
            print('[ERROR] Funcionário não cadastrado')             