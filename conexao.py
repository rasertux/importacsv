import mysql.connector
from mysql.connector import Error

class ConexaoFactory:
    def __init__(self):
        self.conexao = ''

    def get_conexao(self):
        try:
            self.conexao = mysql.connector.connect(host='localhost', database='teste', user='root', password='')
            return self.conexao
        except Error as e:
            print(e)
            return None

    def fecha_conexao(self, conexao):
        try:
            if (self.conexao.is_connected()):
                self.conexao.close()
        except Exception as e:
            print(e)
