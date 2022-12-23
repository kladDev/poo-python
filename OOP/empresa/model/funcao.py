from config.conexao import conectar 

class Funcao():
    def __init__(self, cod: str, nome: str) -> None:
        self.cod = cod
        self.nome = nome

    @staticmethod
    def pesquisar_funcao():
        cod = input('Digite o código da função: ')
        print('-'*20)

        conexao = conectar()
        with conexao.cursor() as c:
            sql = "SELECT funcao.cod, funcao.nome FROM funcao WHERE cod = %s"
            c.execute(sql, (cod))
            res_one = c.fetchone()
            conexao.close()
            return res_one
        
    @staticmethod
    def __editar_funcao__():
        dado = Funcao.pesquisar_funcao()

        if dado:
            condicao = 1

            print('O que deseja editar?')
            while condicao != 0:
                print('[1] - Codigo')
                print('[2] - Nome')
                print('[0] - Voltar')
                print('-'*20)
                
                try:
                    opcao = int(input('Sua opção: '))
                    if opcao == 1:
                        while condicao != -1:
                            cod = str(input('Novo código: '))

                            if len(cod) <= 5:
                                print('-'*20)
                                print('Código atualizado com sucesso')
                                print('-'*20)
                                condicao = -1
                            else:
                                print('[ERROR] Código só pode tem no máximo 5 caracteres') 
                        conexao = conectar()
                        with conexao.cursor() as cursor:
                            sql = "UPDATE funcao SET cod=%s WHERE cod=%s"
                            cursor.execute(sql, (cod, dado['cod']))
                        conexao.commit()
                        conexao.close()
                    
                    elif opcao == 2:
                        nome = str(input('Novo nome: '))

                        conexao = conectar()
                        with conexao.cursor() as cursor:
                            sql = "UPDATE funcao SET nome=%s WHERE cod=%s"
                            cursor.execute(sql, (nome, dado['cod']))
                        conexao.commit()
                        conexao.close()
                        print('-'*20)
                        print('Nome da função atualizado com sucesso !')
                        print('-'*20)

                    elif opcao == 0:
                        condicao = 0 
                    else:
                        print('[ERROR] Opção inválida')
    
   
                except ValueError:
                    print('[ERROR] Aceita somente numero')
        else:
            print('[ERROR] Código não encontrado')

    @staticmethod
    def __delete_funcao__():
        dado = Funcao.pesquisar_funcao()

        if dado:
            try:
                conexao = conectar()
                with conexao.cursor() as cursor:
                    sql = "DELETE FROM funcao WHERE cod=%s"
                    cursor.execute(sql, (dado['cod']))
                conexao.commit()
                conexao.close()

                print('Excluindo com sucesso !')
                print('-'*20)
            except:
                print('[ERROR] Existe funcionário vinculado com esse código')
                print('        Sendo assim, não é possível deletar')
                print('-'*20)
        else:
            print('[ERROR] Código não encontrado')

    @staticmethod
    def __verificar_funcao__():
        conexao = conectar()
        with conexao.cursor() as c:
            sql = "SELECT * FROM funcao"
            c.execute(sql)
            res_one = c.fetchone()
            conexao.close()
            return res_one