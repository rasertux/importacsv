from csv import DictReader
from importamodel import Importa
from importadao import ImportaDao

class ImportaController:
    def importa_csv(self, path, tabela):
        dao = ImportaDao()
        arquivocsv = DictReader(open(path, 'r'))
        for dict in arquivocsv:
            imp = Importa()
            keys=[]
            values=[]
            for k,v in dict.items():
                keys.extend([k])
                values.extend([v])
            imp.set_tabela(tabela)
            imp.set_campos(keys)
            imp.set_dados(values)
            dao.insere_dados(imp)

    def remove_csv(self, path, tabela):
        dao = ImportaDao()
        arquivocsv = DictReader(open(path, 'r'))
        for dict in arquivocsv:
            imp = Importa()
            keys=[]
            values=[]
            for k,v in dict.items():
                keys.extend([k])
                values.extend([v])
            imp.set_tabela(tabela)
            imp.set_campos(keys)
            imp.set_dados(values)
            dao.deleta_dados(imp)
