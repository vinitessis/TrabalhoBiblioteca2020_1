import mysql.connector

class Conexao:
    def __init__(self):
        self.__conn =  mysql.connector.connect(host = 'localhost', database = 'trab_finalap2', user ='', password = '')
        self.__cursor = self.abrir()
    
    def abrir(self): 
        cursor =  self.__conn.cursor()
        return(cursor)
    
    def executar(self, query):
        self.__cursor.execute(query)
        self.__conn.commit()
    
    def mostrar (self, query):
        self.__cursor.execute(query)
        result = self.__cursor.fetchall()
        return result
        
    def fechar(self):
        self.__cursor.close()
        self.__conn.close()