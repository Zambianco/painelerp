from os import listdir
import sqlite3
from tkinter import *
import frm_acesso
from tkinter import messagebox
from datetime import datetime # calcula de horas e datas
import tkinter.ttk as ttk
from loadcfg import dbprmt # nas configurações carrega os parametros do db
from tkinter.ttk import *

cfg = dbprmt() # Carrega a configuração da localização do banco de dados

conn = sqlite3.connect(cfg.dbpath)
cursor = conn.cursor()

"""
# Gera código de autenticação:    
while True:
	totp = pyotp.TOTP('qwertyuiop')
	totp.now()
"""
	
class frm_geros():
         
    def __init__(self, user):
        self.user = user # Nome de usuario logado

        #============== Janela principal ==============
        self.dadosos = Tk()
        self.dadosos.minsize(620, 160)
        self.dadosos.lift()
        self.dadosos.title("Gerenciamento de Ordem de serviço")
        #============== Janela principal ==============


        #============== Menu superior ==============
        menubar = Menu(self.dadosos)
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="E-mails para aviso", command = lambda : autabert.listaaviso(self))
        filemenu.add_separator()
        menubar.add_cascade(label="Cadastro", menu=filemenu)
        self.dadosos.config(menu=menubar)
        self.dadosos.update()    

        
        #============== Widgets Principais ==============        
        frame_dados = Frame(self.dadosos)
        frame_dados.pack(side = TOP, pady = 10)

        self.lbl_numos = Label(frame_dados, text="OS:")
        self.lbl_numos.pack(side=LEFT)

        self.entry_numos = Entry(frame_dados)
        self.entry_numos.pack(side=LEFT, padx = 10)

        self.lbl_motor = Label(frame_dados, text="Motor:")
        self.lbl_motor.pack(side=LEFT)

        self.entry_motor = Entry(frame_dados)
        self.entry_motor.pack(side=LEFT)





        self.abas = ttk.Notebook(self.dadosos)
        self.frame_aba1 = Frame(self.abas)
        self.frame_aba2 = Frame(self.abas)
        self.frame_aba3 = Frame(self.abas)
        self.frame_aba4 = Frame(self.abas)
        self.frame_aba5 = Frame(self.abas)

        self.abas.add(self.frame_aba1,text='Dados\n')
        self.abas.add(self.frame_aba2,text='Checklist\n')
        self.abas.add(self.frame_aba3,text='Peças e serviços\n')
        self.abas.add(self.frame_aba4,text='Serviços de terceiro\n')
        self.abas.add(self.frame_aba5,text='Peças e serviços sobre\nresponsabilidade do cliente')


        self.label1 = Label(self.frame_aba1,text='Esta é a aba 1')
        self.label1.pack(padx=0, pady=40)

        self.label2= Label(self.frame_aba2,text='Esta é a aba 2')
        self.label2.pack(padx=0, pady=40)
        
        self.label3 = Label(self.frame_aba3,text='Esta é a aba 3')
        self.label3.pack(padx=0, pady=40)
        
        
        self.abas.pack(fill=X)


        
        self.lbl_logeduser = Label(self.dadosos, text="Usuário: " + self.user.title())
        self.lbl_logeduser.place(rely=1.0, relx=0.0, x=0, y=0, anchor=SW)
        
        self.dadosos.mainloop()
