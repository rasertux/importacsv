import sys
from importamodel import Importa
from importadao import ImportaDao
from importacontroller import ImportaController

class Main:
    if(len(sys.argv) != 3):

        print("Sintaxe:")
        print("    python importacsv/main.py path tabela")
        print("    Onde path é o caminho para o arquivo")
        print("    tabela é o nome da tabela no banco de dados.")
        print("OBS:")
        print("    A primeira linha da coluna do arquivo CSV")
        print("    deve possuir o nome do campo da tabela.")
    else:
        control = ImportaController()
        path = sys.argv[1]
        tabela = sys.argv[2]
        action = input("Digite 1 para INSERT, 2 para DELETE ou 0 para SAIR: ")
        if(action == '0'):
            sys.exit()
        elif(action == '1'):
            print("Importando, aguarde...")
            if (control.importa_csv(path, tabela)):
                print("Arquivo importado com sucesso!")
            else:
                print("Erro ao importar, verifique o arquivo.")
        elif(action == '2'):
            caution = input("Os dados serão removidos do BD, continuar? 'S' para Sim, 'N' para Não: ")
            if(caution == 's' or caution == 'S'):
                print("Removendo, aguarde...")
                if (control.remove_csv(path, tabela)):
                    print("Dados removidos com sucesso!")
                else:
                    print("Erro ao remover, verique o arquivo.")
            else:
                sys.exit()
        else:
            sys.exit("Opção inválida!")
