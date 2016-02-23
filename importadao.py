from conexao import ConexaoFactory

class ImportaDao:
    def __init__(self):
        self.factory = ConexaoFactory()

    def run_query(self, Importa, query):
        try:
            conexao = self.factory.get_conexao()
            cursor = conexao.cursor()
            dados = tuple(Importa.get_dados()) + tuple(Importa.get_where().values())
            cursor.execute(query, dados)
            conexao.commit()
            return True
        except Exception as e:
            print(e)
            return False
        finally:
            cursor.close()
            self.factory.fecha_conexao(conexao)
