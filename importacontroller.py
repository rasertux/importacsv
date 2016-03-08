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
