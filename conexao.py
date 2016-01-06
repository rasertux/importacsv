import mysql.connector
from mysql.connector import Error

class ConexaoFactory:
    def __init__(self):
        self.conexao = ''

    def get_conexao(self):
        try:
            self.conexao = mysql.connector.connect(host='localhost', database='teste', user='root', password='')
            if self.conexao.is_connected():
                return self.conexao
            else:
                return None
        except Error as e:
            print(e)

    def fecha_conexao(self, conexao):
        try:
            if (self.conexao.is_connected):
                self.conexao.close()
                return True
            else:
                return False
        except Exception as e:
            raise
