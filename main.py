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

import sys
import os.path
from importacontroller import ImportaController

class Main:
    def __init__(self):
        self.control = ImportaController()

    def main(self):
        if(len(sys.argv) != 3):
            print("Sintaxe:")
            print("    python importacsv/main.py path tabela")
            print("    Onde path é o caminho para o arquivo")
            print("    tabela é o nome da tabela no banco de dados.")
            print("OBS:")
            print("    A primeira linha da coluna do arquivo CSV")
            print("    deve possuir os nomes dos campos da tabela.")
        elif(not os.path.isfile(sys.argv[1])):
            sys.exit("Arquivo não encontrado!")
        else:
            path = sys.argv[1]
            tabela = sys.argv[2]
            action = input("Digite 1 para INSERT, 2 para DELETE, 3 para UPDATE ou 0 para SAIR: ")
            if(action == '0'):
                sys.exit()
            elif(action == '1'):
                print("Processando, aguarde...")
                if (self.control.importa_csv(path, tabela)):
                    print("Arquivo importado com sucesso!")
                else:
                    print("Erro ao importar, verifique o arquivo.")
            elif(action == '2'):
                caution = input("Os dados serão removidos do BD, continuar? 'S' para Sim, 'N' para Não: ")
                if(caution == 's' or caution == 'S'):
                    print("Processando, aguarde...")
                    if (self.control.remove_csv(path, tabela)):
                        print("Dados removidos com sucesso!")
                    else:
                        print("Erro ao remover, verique o arquivo.")
                else:
                    sys.exit()
            elif(action == '3'):
                where = input("Informe o nome do campo que será utilizado na cláusula where: ")
                print("Processando, aguarde...")
                if (self.control.atualiza_csv(path, tabela, where)):
                    print("Dados atualizados com sucesso!")
                else:
                    print("Erro ao atualizar, verique o arquivo.")
            else:
                sys.exit("Opção inválida!")

if __name__ == "__main__":
    m = Main()
    m.main()
