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
