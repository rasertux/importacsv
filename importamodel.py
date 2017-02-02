"""This module is the model for importacsv"""

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

class Importa:
    """This class contain methods to get and set data"""
    def __init__(self):
        self._dados = []
        self._campos = []
        self._tabela = ""
        self._where = {}

    def get_dados(self):
        """This method get data"""
        return self._dados

    def set_dados(self, dados):
        """This method set data"""
        self._dados = dados

    def get_campos(self):
        """This method get fields"""
        return self._campos

    def set_campos(self, campos):
        """This method set fields"""
        self._campos = campos

    def get_tabela(self):
        """This method get tables"""
        return self._tabela

    def set_tabela(self, tabela):
        """This method set tables"""
        self._tabela = tabela

    def get_where(self):
        """This method get where"""
        return self._where

    def set_where(self, where):
        """This method set where"""
        self._where = where
