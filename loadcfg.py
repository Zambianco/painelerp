import sqlite3

class dbprmt():    
    def __init__(self):
        with open ("P:\Rodrigo\pcp.conf", 'r') as configs:
            for linha in configs.readlines():
                if "logindb" in linha:
                    self.dbpath = str(linha.replace('\n',"").split("=")[1])

    
                    
