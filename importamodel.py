class Importa:
    def __init__(self):
        self.dados = []
        self.campos = []
        self.tabela = ""
        self.where = {}

    def get_dados(self):
        return self.dados

    def set_dados(self, dados = []):
        self.dados = dados

    def get_campos(self):
        return self.campos

    def set_campos(self, campos = []):
        self.campos = campos

    def get_tabela(self):
        return self.tabela

    def set_tabela(self, tabela):
        self.tabela = tabela

    def get_where(self):
        return self.where

    def set_where(self, where = {}):
        self.where = where
