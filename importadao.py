#importacsv - utilitario para importar, remover ou atualizar dados
#a partir de arquivos CSV para o banco de dados Mysql ou MariaDB.
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

class ImportaDao:
    def __init__(self, logger):
        self.logger = logger

    def run_query(self, conexao, cursor, Importa, query):
        try:
            dados = tuple(Importa.get_dados()) + tuple(Importa.get_where().values())
            cursor.execute(query, dados)
            conexao.commit()
            return True
        except Exception as e:
            conexao.rollback()
            self.logger.set_errors(e)
            return False
