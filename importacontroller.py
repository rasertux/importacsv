"""This module does imports, removes and updates from CSV to DB"""

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

from csv import DictReader
from importamodel import Importa
from conexao import ConexaoFactory
from importadao import ImportaDao
from importahelper import ImportaHelper
from vendor.progress.bar import Bar


class ImportaController:
    """This class contain methods to import, remove and update"""
    def __init__(self, logger):
        self.logger = logger
        self.conexao = ConexaoFactory().get_conexao()
        self.dao = ImportaDao(self.conexao, logger)
        self.helper = ImportaHelper(logger)
        self.imp = Importa()

    def importa_csv(self, path, tabela):
        """This method import data from CSV to DB"""
        loadbar = Bar('Importando:', max=len(list(open(path, 'r')))-1)
        with open(path, 'r') as arquivocsv:
            for linha, item in enumerate(DictReader(arquivocsv)):
                self.imp.set_tabela(tabela)
                self.imp.set_campos(list(item.keys()))
                self.imp.set_dados(list(item.values()))
                query = self.helper.gera_query_insert(self.imp, linha+2)
                if not self.dao.run_query(self.imp, query):
                    break
                if query:
                    loadbar.next()
        loadbar.finish()
        return True if not self.logger.get_errors() else False

    def remove_csv(self, path, tabela):
        """This method remove data from DB using CSV column in where"""
        loadbar = Bar('Removendo:', max=len(list(open(path, 'r')))-1)
        with open(path, 'r') as arquivocsv:
            for linha, item in enumerate(DictReader(arquivocsv)):
                self.imp.set_tabela(tabela)
                self.imp.set_campos(list(item.keys()))
                self.imp.set_dados(list(item.values()))
                query = self.helper.gera_query_delete(self.imp, linha+2)
                if not self.dao.run_query(self.imp, query):
                    break
                if query:
                    loadbar.next()
        loadbar.finish()
        return True if not self.logger.get_errors() else False

    def atualiza_csv(self, path, tabela, where):
        """This method update data from CSV to DB"""
        loadbar = Bar('Atualizando:', max=len(list(open(path, 'r')))-1)
        with open(path, 'r') as arquivocsv:
            for linha, item in enumerate(DictReader(arquivocsv)):
                self.imp.set_tabela(tabela)
                if not where or where not in item:
                    self.logger.set_errors(
                        "Cláusula \"Where\" não informada ou inválida!")
                    break
                self.imp.set_where({where: item.pop(where)})
                self.imp.set_campos(list(item.keys()))
                self.imp.set_dados(list(item.values()))
                query = self.helper.gera_query_update(self.imp, linha+2)
                if not self.dao.run_query(self.imp, query):
                    break
                if query:
                    loadbar.next()
        loadbar.finish()
        return True if not self.logger.get_errors() else False
