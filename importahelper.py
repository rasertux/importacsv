from importamodel import Importa

class ImportaHelper:
    def gera_query_insert(self, Importa):
        dados = Importa.get_dados()
        campos = Importa.get_campos()
        tabela = Importa.get_tabela()
        query = "INSERT INTO %s(" % tabela
        i = 0
        for item in campos:
            i += 1
            if(i >= len(campos)):
                query += item
            else:
                query += item + ", "
        query += ") VALUES("
        i = 0
        for item in dados:
            i += 1
            if(i >= len(dados)):
                query += "%s"
            else:
                query += "%s, "
        query += ");"
        return query

    def gera_query_delete(self, Importa):
        dados = Importa.get_dados()
        campos = Importa.get_campos()
        tabela = Importa.get_tabela()
        query = "DELETE FROM %s WHERE " % tabela
        query += campos[0] + "=%s"
        return query
