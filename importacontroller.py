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
    def __init__(self, logger):
        self.logger = logger
        self.conexao = ConexaoFactory().get_conexao()
        self.dao = ImportaDao(self.conexao, logger)
        self.helper = ImportaHelper(logger)
        self.imp = Importa()

    def importa_csv(self, path, tabela):
        bar = Bar('Importando:', max=len(list(open(path, 'r')))-1)
        with open(path, 'r') as arquivocsv:
            for l, dict in enumerate(DictReader(arquivocsv)):
                self.imp.set_tabela(tabela)
                self.imp.set_campos(list(dict.keys()))
                self.imp.set_dados(list(dict.values()))
                query = self.helper.gera_query_insert(self.imp, l)
                if(not self.dao.run_query(self.imp, query)):
                    break
                if query:
                    bar.next()
        bar.finish()
        return not self.logger.get_errors() if True else False

    def remove_csv(self, path, tabela):
        bar = Bar('Removendo:', max=len(list(open(path, 'r')))-1)
        with open(path, 'r') as arquivocsv:
            for l, dict in enumerate(DictReader(arquivocsv)):
                self.imp.set_tabela(tabela)
                self.imp.set_campos(list(dict.keys()))
                self.imp.set_dados(list(dict.values()))
                query = self.helper.gera_query_delete(self.imp, l)
                if(not self.dao.run_query(self.imp, query)):
                    break
                if query:
                    bar.next()
        bar.finish()
        return not self.logger.get_errors() if True else False

    def atualiza_csv(self, path, tabela, where = None):
        bar = Bar('Atualizando:', max=len(list(open(path, 'r')))-1)
        with open(path, 'r') as arquivocsv:
            for l, dict in enumerate(DictReader(arquivocsv)):
                self.imp.set_tabela(tabela)
                self.imp.set_where({where: dict.pop(where)})
                self.imp.set_campos(list(dict.keys()))
                self.imp.set_dados(list(dict.values()))
                query = self.helper.gera_query_update(self.imp, l)
                if(not self.dao.run_query(self.imp, query)):
                    break
                if query:
                    bar.next()
        bar.finish()
        return not self.logger.get_errors() if True else False

    def __del__(self):
        self.conexao.close()
