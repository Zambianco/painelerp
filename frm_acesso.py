from os import listdir
import sqlite3
from tkinter import *
from tkinter import messagebox
from login import geraHash # para calcular o hash da senha
from loadcfg import dbprmt # nas configurações carrega os parametros do db

cfg = dbprmt() # Carrega a configuração da localização do banco de dados

conn = sqlite3.connect(cfg.dbpath)
cursor = conn.cursor()

permissao = []
class frm_login():
    # Formulário de acessos e chamada de funções para validar o acesso
    def validaacesso(self):
        cursor.execute("""
        SELECT senhahash
        FROM loginsenha
        WHERE login = ?
        """, (self.login,))
            
        busca = cursor.fetchone()
        senhainfor = geraHash(self.login, self.senha).getHash()
        self.senha = None
        
        if busca is None:
            messagebox.showerror("Erro de acesso", "Usuario não encontrado")
            return None
        elif busca[0] == senhainfor:
            return True
        else:
            messagebox.showerror("Erro de acesso", "Senha incorreta")
            return False


    def acessar(self):
        
            
        self.login = self.entry_login.get().strip().lower()
        self.senha = self.entry_senha.get()
        self.autoracess = (frm_login.validaacesso(self))

        if self.autoracess == True:
            self.fmlogin.destroy()
        return self.autoracess
        
            
    def __init__(self):     
        #>>>>>>>>>> Widgets >>>>>>>>>>
        self.fmlogin = Tk()
        self.fmlogin.minsize(150, 155)
        self.fmlogin.maxsize(150, 155)
        self.fmlogin.title("Autorização de abertura de produção")

        self.lbl_login = Label(self.fmlogin, text="Login:")
        self.lbl_login.place(x = 10, y = 30, width=50, height=25)

        self.entry_login = Entry(self.fmlogin)
        self.entry_login.place(x = 60, y = 30, width=80, height=25)

        self.lbl_senha = Label(self.fmlogin, text="Senha:")
        self.lbl_senha.place(x = 10, y = 65, width=50, height=25)

        self.entry_senha = Entry(self.fmlogin)
        self.entry_senha = Entry(self.fmlogin, show="*", width=10)
        self.entry_senha.place(x = 60, y = 65, width=80, height=25)

        self.bt_acessar = Button(self.fmlogin, text="Acessar", command=self.acessar, name = "bt_acessar") # Botão acessar
        self.bt_acessar.place(x = 25, y = 110, width=100, height=25)

        mainloop()


    
