import sys
from importamodel import Importa
from importadao import ImportaDao
from importacontroller import ImportaController

class Main:
    if(len(sys.argv) != 3):
        print("Sintaxe: python importacsv/main.py path tabela")
        print("Onde path é o caminho para o arquivo")
        print("tabela é o nome da tabela no banco de dados.")
    else:
        control = ImportaController()
        path = sys.argv[1]
        tabela = sys.argv[2]
        action = input("ImportaCSV - Digite 1 para INSERT, 2 para DELETE ou 0 para SAIR: ")
        if(action == '0'):
            sys.exit()
        elif(action == '1'):
            print("Importando, aguarde...")
            control.importa_csv(path, tabela)
            print("Arquivo importado com sucesso!")
        elif(action == '2'):
            caution = input("Os dados serão removidos do BD, tem certeza que quer continuar? 's' para Sim, 'n' para Não: ")
            if(caution == 's'):
                print("Removendo, aguarde...")
                control.remove_csv(path, tabela)
                print("Dados removidos com sucesso!")
            else:
                sys.exit()
        else:
            sys.exit("Opção inválida!")