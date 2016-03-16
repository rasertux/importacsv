#importacsv - utilitario para importar, remover ou atualizar dados
#a partir de arquivos CSV para o banco de dados Mysql ou MariaDB.
#
# Copyright (c) 2015, 2016 Rafael Sergio da Costa <rasertux@gmail.com>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation.
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

from vendor.mysql.connector import connect
from vendor.mysql.connector import Error
import sys


class ConexaoFactory:
    def __init__(self):
        self.conexao = ''

    def get_conexao(self):
        try:
            self.conexao = connect(option_files='DB.cnf')
            return self.conexao
        except Error as e:
            print(e)
            sys.exit("Verifique os dados de conexão com o banco de dados!")

    def fecha_conexao(self, conexao):
        try:
            if (self.conexao.is_connected()):
                self.conexao.close()
        except Error as e:
            print(e)
