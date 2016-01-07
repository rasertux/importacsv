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
            dados = Importa.get_dados()
            args = ()
            for item in dados:
                args += (item,)
            cursor.execute(self.helper.gera_query_insert(Importa), args)
            conexao.commit()
        except Exception as e:
            raise
        finally:
            cursor.close()
            self.factory.fecha_conexao(conexao)

    def deleta_dados(self, Importa):
        try:
            conexao = self.factory.get_conexao()
            cursor = conexao.cursor()
            dados = Importa.get_dados()
            args = (dados[0], )
            cursor.execute(self.helper.gera_query_delete(Importa), args)
            conexao.commit()
        except Exception as e:
            raise
        finally:
            cursor.close()
            self.factory.fecha_conexao(conexao)
