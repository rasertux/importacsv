from importamodel import Importa

class ImportaHelper:
    def gera_query_insert(self, Importa):
        dados = Importa.get_dados()
        campos = Importa.get_campos()
        tabela = Importa.get_tabela()
        query = "INSERT INTO %s(" % tabela
        for item in campos:
            if(item == campos[len(campos) -1]):
                query += item
            else:
                query += item + ", "
        query += ") VALUES("
        for item in dados:
            if(item == dados[len(dados) -1]):
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
