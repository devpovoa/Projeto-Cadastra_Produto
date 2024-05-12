import psycopg2 as connectar


class AppDB:
    def __init__(self) -> None:
        print('Método Construtor')

    # Método para abri conexão no banco de dados.
    def abrirConexao(self):
        try:
            self.connection = connectar.connect(
                database="seu_bancoDeDados_BD", host="seu_host_de_preferencia", user="seu_usuário", password="sua_senha", port="sua_porta_configurada")
        except (Exception, connectar.Error) as error:
            if (self.connection):
                print("Falha ao se conectar ao Banco de Dados", error)

    # Método para selecionar dados.
    def selecionarDados(self):
        try:
            self.abrirConexao()
            cursor = self.connection.cursor()

            print("Selecionando todos os produtos")
            sql_select_query = """SELECT * FROM public."PRODUTO";"""

            cursor.execute(sql_select_query)
            registros = cursor.fetchall()
            print(registros)
        except (Exception, connectar.Error) as error:
            print("Error in select operation", error)
        finally:
            if (self.connection):
                cursor.close()
                self.connection.close()
                print("A conexão com o PostgreSQL foi fechada.")
        return registros

    # Método para inserir dados.
    def inserirDados(self, codigo, nome, preco):
        try:
            self.abrirConexao()
            cursor = self.connection.cursor()
            postgres_insert_query = """INSERT INTO public."PRODUTO"("codigo", "nome", "preco") VALUES (%s, %s, %s);"""
            record_to_insert = (codigo, nome, preco)
            cursor.execute(postgres_insert_query, record_to_insert)
            self.connection.commit()
            count = cursor.rowcount
            print(count, "Registro inserido com sucesso na tabela PRODUTO")
        except (Exception, connectar.Error) as error:
            if (self.connection):
                print("Falha ao inserir registro na tabela PRODUTO", error)
        finally:
            if (self.connection):
                cursor.close()
                self.connection.close()
                print("A conexão com o PostgreSQL foi fechada.")

    # Método para Atualizar dados.
    def atualizarDados(self, codigo, nome, preco):
        try:
            self.abrirConexao()
            cursor = self.connection.cursor()

            print("Registro antes da Atualização ")
            sql_select_query = """SELECT * FROM public."PRODUTO" WHERE "codigo"=%s;"""
            cursor.execute(sql_select_query, (codigo,))
            record = cursor.fetchone()
            print(record)

            sql_update_query = """UPDATE public."PRODUTO" SET "nome"=%s, "preco"=%s WHERE "codigo"=%s; """
            cursor.execute(sql_update_query, (nome, preco, codigo))
            self.connection.commit()
            count = cursor.rowcount
            print(count, "Registro Atulizado com sucesso!")
            print("Registro após Atualização")
            sql_select_query = """SELECT * FROM public."PRODUTO" WHERE "codigo"=%s;"""
            cursor.execute(sql_select_query, (codigo,))
            record = cursor.fetchone()
            print(record)
        except (Exception, connectar.Error) as error:
            print("Erro na Atulização", error)
        finally:
            if (self.connection):
                cursor.close()
                self.connection.close()
                print("A conexão com o PostgreSQL foi fechada.")

    # Método que exclui dados.
    def excluirDados(self, codigo):
        try:
            self.abrirConexao()
            cursor = self.connection.cursor()

            sql_delete_query = """DELETE FROM public."PRODUTO" WHERE "codigo"=%s; """
            cursor.execute(sql_delete_query, (codigo,))
            self.connection.commit()
            count = cursor.rowcount
            print(count, "Registro excluído com sucesso!")
        except (Exception, connectar.Error) as error:
            print("Erro na Exclusão", error)
        finally:
            if (self.connection):
                cursor.close()
                self.connection.close()
                print("A conexão com o PostgreSQL foi fechada.")
