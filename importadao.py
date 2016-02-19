from conexao import ConexaoFactory
from importahelper import ImportaHelper

class ImportaDao:
    def __init__(self):
        self.factory = ConexaoFactory()
        self.helper = ImportaHelper()

    def insere_dados(self, Importa):
        try:
            conexao = self.factory.get_conexao()
            cursor = conexao.cursor()
            dados = tuple(Importa.get_dados())
            cursor.execute(self.helper.gera_query_insert(Importa), dados)
            conexao.commit()
            return True
        except Exception as e:
            print(e)
            return False
        finally:
            cursor.close()
            self.factory.fecha_conexao(conexao)

    def deleta_dados(self, Importa):
        try:
            conexao = self.factory.get_conexao()
            cursor = conexao.cursor()
            dados = tuple(Importa.get_dados())
            cursor.execute(self.helper.gera_query_delete(Importa), dados)
            conexao.commit()
            return True
        except Exception as e:
            print(e)
            return False
        finally:
            cursor.close()
            self.factory.fecha_conexao(conexao)
