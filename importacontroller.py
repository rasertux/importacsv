#importacsv - utilitario para importar, remover ou atualizar dados
#a partir de arquivos CSV para o banco de dados Mysql ou MariaDB.

# Copyright (c) 2015, 2016 Rafael Sergio da Costa <rasertux@gmail.com>

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
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston,

from csv import DictReader
from importamodel import Importa
from importadao import ImportaDao
from importahelper import ImportaHelper
from vendor.progress.bar import Bar

class ImportaController:
    def __init__(self):
        self.status = True
        self.dao = ImportaDao()
        self.helper = ImportaHelper()
        self.imp = Importa()

    def importa_csv(self, path, tabela):
        bar = Bar('Importando:', max=len(list(open(path, 'r')))-1)
        arquivocsv = DictReader(open(path, 'r'))
        for dict in arquivocsv:
            self.imp.set_tabela(tabela)
            self.imp.set_campos(list(dict.keys()))
            self.imp.set_dados(list(dict.values()))
            query = self.helper.gera_query_insert(self.imp)
            self.status = self.dao.run_query(self.imp, query)
            bar.next()
            if (not self.status): break
        bar.finish()
        return self.status

    def remove_csv(self, path, tabela):
        bar = Bar('Removendo:', max=len(list(open(path, 'r')))-1)
        arquivocsv = DictReader(open(path, 'r'))
        for dict in arquivocsv:
            self.imp.set_tabela(tabela)
            self.imp.set_campos(list(dict.keys()))
            self.imp.set_dados(list(dict.values()))
            query = self.helper.gera_query_delete(self.imp)
            self.status = self.dao.run_query(self.imp, query)
            bar.next()
            if (not self.status): break
        bar.finish()
        return self.status

    def atualiza_csv(self, path, tabela, where):
        bar = Bar('Atualizando:', max=len(list(open(path, 'r')))-1)
        arquivocsv = DictReader(open(path, 'r'))
        for dict in arquivocsv:
            self.imp.set_tabela(tabela)
            self.imp.set_where({where : dict.pop(where)})
            self.imp.set_campos(list(dict.keys()))
            self.imp.set_dados(list(dict.values()))
            query = self.helper.gera_query_update(self.imp)
            self.status = self.dao.run_query(self.imp, query)
            bar.next()
            if (not self.status): break
        bar.finish()
        return self.status
