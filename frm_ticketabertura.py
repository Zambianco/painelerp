from os import listdir
import sqlite3
from tkinter import *
import frm_acesso
from tkinter import messagebox
from datetime import datetime # calcula de horas e datas
import tkinter.ttk as ttk


# <<<<<<<<<<<<<< conexão ao banco de dados <<<<<<<<<<<<<<
from loadcfg import dbprmt # nas configurações carrega os parametros do db
cfg = dbprmt() # Carrega a configuração da localização do banco de dados
conn = sqlite3.connect(cfg.dbpath)
cursor = conn.cursor()
# >>>>>>>>>>>>>> conexão ao banco de dados >>>>>>>>>>>>>>

"""
# Gera código de autenticação:    
while True:
	totp = pyotp.TOTP('qwertyuiop')
	totp.now()
"""
	
# <<<<<<<<<<<<<< reportlab imports <<<<<<<<<<<<<<
from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib.units import mm
from reportlab.pdfgen import canvas

from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

from datetime import datetime

pdfmetrics.registerFont(TTFont('Calibri', 'calibri.ttf'))
pdfmetrics.registerFont(TTFont('Courier', 'cour.ttf'))
# >>>>>>>>>>>>>> reportlab imports >>>>>>>>>>>>>>

def gerarticket():
    ticket = canvas.Canvas("{}.pdf".format(numos))
    ticket.setPageSize((59.4 * mm, 105 * mm))
    
    # ===== OS =====
    fontsize = 20
    posx = 5 * mm
    posy = 92.5 * mm
    ticket.setFont("Calibri", fontsize)
    ticket.drawString(posx, posy, "OS:")

    # ===== Cliente =====
    fontsize = 10
    posx = 5 * mm
    posy = 86.5 * mm
    ticket.setFont("Calibri", fontsize)
    ticket.drawString(posx, posy, "Cliente:")

    # ===== Motor =====
    fontsize = 10
    posx = 5 * mm
    posy = 76 * mm
    ticket.setFont("Calibri", fontsize)
    ticket.line(posx, posy + fontsize, 54.4 * mm, posy + fontsize) # Linha horizontal sobre o texto
    ticket.drawString(posx, posy, "Motor:")

    # ===== Operação =====
    fontsize = 10
    posx = 5 * mm
    posy = 65 * mm
    ticket.setFont("Calibri", fontsize)
    ticket.line(posx, posy + fontsize, 54.4 * mm, posy + fontsize) # Linha horizontal sobre o texto
    ticket.drawString(posx, posy, "Operação:")

    # ===== Data de liberação =====
    fontsize = 10
    posx = 5 * mm
    posy = 53 * mm
    ticket.setFont("Calibri", fontsize)
    ticket.line(posx, posy + fontsize, 54.4 * mm, posy + fontsize) # Linha horizontal sobre o texto
    ticket.drawString(posx, posy, "Data de liberação de produção:")
    ticket.line(posx + 15 * mm, posy - 7 * mm, posx + 17 * mm, posy - 2 * mm) # Barra da data
    ticket.line(posx + 28 * mm, posy - 7 * mm, posx + 30 * mm, posy - 2 * mm) # Barra da data

    # ===== Fornecedor de peças =====
    fontsize = 10
    posx = 5 * mm
    posy = 41 * mm
    ticket.setFont("Calibri", fontsize)
    ticket.line(posx, posy + fontsize, 54.4 * mm, posy + fontsize) # Linha horizontal sobre o texto
    ticket.drawString(posx + 20 * mm, posy, "Peças:")
    ticket.rect(posx, posy - 7 * mm, 6 * mm, 6 * mm, stroke=1, fill=0) # Quadrado de seleção de peças

    ticket.setFont("Calibri", fontsize + 4)
    ticket.rect(posx + 29 * mm, posy - 7 * mm, 6 * mm, 6 * mm, stroke=1, \
                fill=0) # Quadrado de seleção de peças
    ticket.drawString(posx + 7 * mm, posy - 6 * mm, "Retífica")
    ticket.rect(posx + 29 * mm, posy - 7 * mm, 6 * mm, 6 * mm, stroke=1, \
                fill=0) # Quadrado de seleção de peças
    ticket.drawString(posx + 36 * mm, posy - 6 * mm, "Cliente")

    # ===== Observação =====
    fontsize = 10
    posx = 5 * mm
    posy = 30 * mm
    ticket.setFont("Calibri", fontsize)
    ticket.drawString(posx, posy, "Observação:")
##    ticket.line(posx, posy - 8 * mm, 54.4 * mm, posy - 8 * mm) # Linha horizontal para obs.
##    ticket.line(posx, posy - 16 * mm, 54.4 * mm, posy - 16 * mm) # Linha horizontal para obs.
##    ticket.line(posx, posy - 24 * mm, 54.4 * mm, posy - 24 * mm) # Linha horizontal para obs.
    
    ticket.showPage()
    ticket.save()


class autabert():
    #Formulário para autorização de abertura da produção.
    
    def listaaviso(self):
        #Formulário com a listagem dos endereços de e-mails a serem avisados
        #quando uma OS tiver a produção liberada.
        self.listaemail = Toplevel(self.autabert)

        #----------------------------------------
        #----- Frame dados -----
        lblframe_dados = LabelFrame(self.listaemail, text = "Informações para envio do e-mail")
        lblframe_dados.grid(row = 1, column = 0, sticky="E")
        
        #----- Campo destinatario -----
        self.lbl_destin = Label(lblframe_dados, text="Destinatário:")
        self.lbl_destin.grid(row = 0, column = 0, padx = 2, sticky="E")

        self.entry_destin = Entry(lblframe_dados)
        self.entry_destin.grid(row = 0, column = 1, padx = 2)

        #----- Campo e-mail -----
        self.lbl_email = Label(lblframe_dados, text="e-mail:")
        self.lbl_email.grid(row = 0, column = 2, padx = 2, sticky="E")

        self.entry_email = Entry(lblframe_dados)
        self.entry_email.grid(row = 0, column = 3, padx = 2, ipadx=50)
        
        #----- Botão cadastrar -----
        self.bt_gerar = Button(lblframe_dados, text="Cadastrar", \
                               command=None) # Botão cadastrar
        self.bt_gerar.grid(row = 0, column = 6, padx = 2)

        #----- Botão excluir -----
        self.bt_gerar = Button(lblframe_dados, text="Excluir", \
                               command=None) # Botão excluir
        self.bt_gerar.grid(row = 0, column = 7, padx = 2)



        
        self.tree = ttk.Treeview(self.listaemail,
                                 columns=('Destinatário', 'email'))
        
        self.tree.heading('#0', text='Destinatário')
        self.tree.heading('#1', text='email')
        self.tree.column('#0')
        self.tree.column('#1')

        self.tree.grid(row=4, columnspan=4, sticky='nsew')
        self.treeview = self.tree

        
    def autorizaprod(self):
        #Método que grava no banco de dados a abertura da produção e dispara os
        #e-mails para os contatos previamente cadastrados.
        self.numos = self.entry_numos.get()
        self.urgente = self.osurgente.get()
        self.fornpecas = self.pecas.get()
        self.observacao = self.text_obs.get('1.0', END)
        print(self.user)   
        try:
            dataautorizacao = datetime.now().timestamp()
            #Tenta registrar os dados no db
            cursor.execute("""
            INSERT INTO autabertprod (numos,
                                      urgente,
                                      dataautorizacao,
                                      fornpecas,
                                      observacao)
            VALUES (?,?,?,?,?)
            """, (self.numos, self.urgente, dataautorizacao, self.fornpecas, \
                  self.observacao,))

            conn.commit()
            messagebox.showinfo("Produção liberada", "Abertura de produção liberada com sucesso")

        except sqlite3.IntegrityError:
            #Caso ocorra da OS já ter sido liberada é buscada a data de abertura no db
            cursor.execute("""
            SELECT dataautorizacao
            FROM autabertprod
            WHERE numos = {}
            """.format(self.numos))

            buscadata = cursor.fetchone()
            buscadata = datetime.fromtimestamp(buscadata[0]).strftime("%m/%d/%Y, %H:%M:%S")
            messagebox.showerror("Erro", "Abertura de ordem de serviço já" + 
                                        " autorizada em {}".format(buscadata))

        
    def __init__(self, user):
        self.user = user # Nome de usuario logado

        #============== Janela principal ==============
        self.autabert = Tk()
        self.autabert.minsize(620, 160)
        self.autabert.maxsize(620, 160)
        self.autabert.resizable(0,0)
        self.autabert.lift()
        #self.autabert.attributes('-topmost', 1)
        self.autabert.title("Autorização de abertura de produção")
        #============== Janela principal ==============


        #============== Menu superior ==============
        menubar = Menu(self.autabert)
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="E-mails para aviso", command = lambda : autabert.listaaviso(self))
        filemenu.add_separator()
        menubar.add_cascade(label="Cadastro", menu=filemenu)
        self.autabert.config(menu=menubar)
        self.autabert.update()    

        
        #============== Widgets Principais ==============        
        self.lbl_numos = Label(self.autabert, text="OS:")
        self.lbl_numos.place(x = 10, y = 30, width=50, height=25)

        self.entry_numos = Entry(self.autabert)
        self.entry_numos.place(x = 60, y = 30, width=80, height=25)

        self.osurgente = BooleanVar() 
        self.chbt_urgente = Checkbutton(self.autabert, text="Urgente", \
                                        variable=self.osurgente)
        self.chbt_urgente.place(x = 150, y = 30, width=80, height=25)

        self.lbl_fornpecas = Label(self.autabert, text="Peças:")
        self.lbl_fornpecas.place(x = 10, y = 65, width=50, height=25)

        self.pecas = StringVar(self.autabert)
        self.pecas.set("?")
        opcoesfornpc = ["?", "-", "C", "R", "C/R"]
        self.opm_fornpc = OptionMenu(self.autabert, self.pecas, *opcoesfornpc)
        self.opm_fornpc.place(x = 60, y = 65, width=80, height=25)

        self.lbl_obs = Label(self.autabert, text="Observação:")
        self.lbl_obs.place(x = 270, y = 30, width=70, height=25)

        self.text_obs = Text(self.autabert)
        self.text_obs.place(x = 350, y = 30, width=250, height=65)

        self.bt_gerar = Button(self.autabert, text="Autorizar", \
                               command=self.autorizaprod) # Botão gerar ticket
        self.bt_gerar.place(x = 250, y = 110, width=100, height=25)

        self.lbl_logeduser = Label(self.autabert, text="Usuário: " + self.user.title())
        self.lbl_logeduser.place(x = 10, y = 110, width=100, height=25)
        
        self.autabert.mainloop()
