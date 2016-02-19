from csv import DictReader
from importamodel import Importa
from importadao import ImportaDao

class ImportaController:
    def __init__(self):
        self.status = True

    def importa_csv(self, path, tabela):
        dao = ImportaDao()
        arquivocsv = DictReader(open(path, 'r'))
        for dict in arquivocsv:
            imp = Importa()
            imp.set_tabela(tabela)
            imp.set_campos(list(dict.keys()))
            imp.set_dados(list(dict.values()))
            self.status = dao.insere_dados(imp)
            if (not self.status): break
        return self.status

    def remove_csv(self, path, tabela):
        dao = ImportaDao()
        arquivocsv = DictReader(open(path, 'r'))
        for dict in arquivocsv:
            imp = Importa()
            imp.set_tabela(tabela)
            imp.set_campos(list(dict.keys()))
            imp.set_dados(list(dict.values()))
            self.status = dao.deleta_dados(imp)
            if (not self.status): break
        return self.status
