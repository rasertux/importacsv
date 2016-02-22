from importamodel import Importa

class ImportaHelper:
    def gera_query_insert(self, Importa):
        dados = len(Importa.get_dados())
        campos = Importa.get_campos()
        tabela = Importa.get_tabela()
        query = "INSERT INTO %s(" % tabela
        query += ','.join(campos)
        query += ") VALUES(" + "%s," * (dados -1) + "%s);"
        return query

    def gera_query_delete(self, Importa):
        campos = Importa.get_campos()
        tabela = Importa.get_tabela()
        query = "DELETE FROM %s WHERE " % tabela
        query += campos[0] + "=%s"
        return query

    def gera_query_update(self, Importa):
        campos = Importa.get_campos()
        tabela = Importa.get_tabela()
        wherecampo = list(Importa.get_where().keys())[0]
        wherevalue = list(Importa.get_where().values())[0]
        query = "UPDATE %s SET " % tabela
        query += '=%s,'.join(campos) + '=%s'
        query += " WHERE " + wherecampo + '=' + wherevalue
        return query
