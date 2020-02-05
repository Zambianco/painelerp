from os import listdir
import sqlite3
import hashlib # biblioteca que calcula o hash
import getpass 

# <<<<<<<<<<<<<< localização do banco de dados <<<<<<<<<<<<<<
with open ("P:\Rodrigo\pcp.conf", 'r') as configs:
    for linha in configs.readlines():
        if "logindb" in linha:
            dbpath = str(linha.replace('\n',"").split("=")[1])
# >>>>>>>>>>>>>> localização do banco de dados >>>>>>>>>>>>>>
          
conn = sqlite3.connect(dbpath)
cursor = conn.cursor()

class geraHash:
    def __init__(self, login, senha):
        self.login = login
        self.senha = senha

    def getHash(self):
        hash1 = hashlib.md5()
        hash2 = hashlib.md5()
        hash3 = hashlib.md5()

        hash1.update(self.login.encode('utf-8'))
        hash2.update(self.senha.encode('utf-8'))
        hash3.update(hash1.hexdigest()[:-6:-1].encode('utf-8'))

        return hash2.hexdigest() + hash3.hexdigest()

def cadastrar():
    login = input("Login: ").strip().lower()
    senha = getpass.getpass(prompt='Senha: ')
    senha = geraHash(login, senha).getHash()

    cursor.execute("""
    INSERT INTO loginsenha (login, senhahash)
    VALUES (?, ?)
""", (login,  senha))

    conn.commit()

