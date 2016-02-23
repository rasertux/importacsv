from csv import DictReader
from importamodel import Importa
from importadao import ImportaDao
from importahelper import ImportaHelper

class ImportaController:
    def __init__(self):
        self.status = True
        self.dao = ImportaDao()
        self.helper = ImportaHelper()

    def importa_csv(self, path, tabela):
        arquivocsv = DictReader(open(path, 'r'))
        for dict in arquivocsv:
            imp = Importa()
            imp.set_tabela(tabela)
            imp.set_campos(list(dict.keys()))
            imp.set_dados(list(dict.values()))
            query = self.helper.gera_query_insert(imp)
            self.status = self.dao.run_query(imp, query)
            if (not self.status): break
        return self.status

    def remove_csv(self, path, tabela):
        arquivocsv = DictReader(open(path, 'r'))
        for dict in arquivocsv:
            imp = Importa()
            imp.set_tabela(tabela)
            imp.set_campos(list(dict.keys()))
            imp.set_dados(list(dict.values()))
            query = self.helper.gera_query_delete(imp)
            self.status = self.dao.run_query(imp, query)
            if (not self.status): break
        return self.status

    def atualiza_csv(self, path, tabela, where):
        arquivocsv = DictReader(open(path, 'r'))
        for dict in arquivocsv:
            imp = Importa()
            imp.set_tabela(tabela)
            imp.set_where({where : dict.pop(where)})
            imp.set_campos(list(dict.keys()))
            imp.set_dados(list(dict.values()))
            query = self.helper.gera_query_update(imp)
            self.status = self.dao.run_query(imp, query)
            if (not self.status): break
        return self.status
