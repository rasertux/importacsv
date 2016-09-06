# importacsv - utilitario para importar, remover ou atualizar dados
# a partir de arquivos CSV para o banco de dados Mysql ou MariaDB.
#
# Copyright (c) 2015, 2016 Rafael Sergio da Costa <rasertux@gmail.com>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA 02110-1301 USA

from importamodel import Importa


class ImportaHelper:
    def __init__(self, logger):
        self.logger = logger
        self.error_message = "Erro na linha %s do arquivo CSV."

    def gera_query_insert(self, Importa, linha):
        dados = len(Importa.get_dados())
        campos = Importa.get_campos()
        tabela = Importa.get_tabela()
        try:
            query = "INSERT INTO %s(" % tabela
            query += ','.join(campos)
            query += ") VALUES(" + "%s," * (dados - 1) + "%s);"
            return query
        except Exception as e:
            self.logger.set_errors(self.error_message % linha)
            return None

    def gera_query_delete(self, Importa, linha):
        campos = Importa.get_campos()
        tabela = Importa.get_tabela()
        try:
            query = "DELETE FROM %s WHERE " % tabela
            query += campos[0] + "=%s"
            return query
        except Exception as e:
            self.logger.set_errors(self.error_message % linha)
            return None

    def gera_query_update(self, Importa, linha):
        campos = Importa.get_campos()
        tabela = Importa.get_tabela()
        try:
            wherecampo = list(Importa.get_where().keys())[0]
            query = "UPDATE %s SET " % tabela
            query += '=%s,'.join(campos) + '=%s'
            query += " WHERE " + wherecampo + '=%s'
            return query
        except Exception as e:
            self.logger.set_errors(self.error_message % linha)
            return None
