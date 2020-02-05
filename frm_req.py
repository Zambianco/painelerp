import sqlite3
from tkinter import *
from datetime import datetime # calcula de horas e datas
import tkinter.ttk as ttk


conn = sqlite3.connect("requisicao.db")
cursor = conn.cursor()

class Requisicao():
    #Janela de requisição interna
    def loadtiporeq():
        cursor.execute("""
                          SELECT * FROM tiporeq;
                          """)
        tipos = cursor.fetchall()
        return tipos

    def loadtipounid():
        cursor.execute("""
                          SELECT * FROM tipounidade;
                          """)
        tipos = cursor.fetchall()
        return tipos
    
    def __init__(self, user):
        self.user = user
        #============== Janela principal ==============
        self.req = Tk()
        self.req.resizable(0, 0)
        self.req.title("Requisição")
        #============== Janela principal ==============

        #============== Menu superior ==============
        menubar = Menu(self.req)
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="Pesquisa", command = None)
        filemenu.add_separator()
        menubar.add_cascade(label="Requisicao", menu=filemenu)
        self.req.config(menu=menubar)
        self.req.update()

        
        #-----------------------
        #----- Frame dados -----
        frame_dados = Frame(self.req)
        frame_dados.pack(fill=X)

        #----- Campo tipo de requisição -----
        self.tiporeq = StringVar(self.req)
        opcoestiporeq = ["{} - {}".format(item[0], item[1]) for item in Requisicao.loadtiporeq()]
        self.tiporeq.set(None)
        self.opm_tiporeq = OptionMenu(frame_dados, self.tiporeq, *opcoestiporeq)
        self.opm_tiporeq.grid(row = 0, column = 0, columnspan = 2, sticky="W")

        #----- Campo prestador -----
        self.lbl_prestador = Label(frame_dados, text="Prestador:")
        self.lbl_prestador.grid(row = 1, column = 0, pady = 2, sticky="E")

        self.prestador = Entry(frame_dados, width = 30)
        self.prestador.grid(row = 1, column = 1, pady = 2, sticky="W")

        #----- Campo funcionário prestador -----
        self.lbl_funcprest = Label(frame_dados, text="Func. Prest.:")
        self.lbl_funcprest.grid(row = 1, column = 2, pady = 2, sticky="E")

        self.funcprest = Entry(frame_dados, width = 30)
        self.funcprest.grid(row = 1, column = 3, pady = 2, sticky="W")

        #----- Campo funcionário retífica -----
        self.lbl_funcprest = Label(frame_dados, text="Func. Retif.:")
        self.lbl_funcprest.grid(row = 2, column = 0, pady = 2, sticky="E")

        self.funcprest = Entry(frame_dados, width = 30)
        self.funcprest.grid(row = 2, column = 1, pady = 2, sticky="W")
        
        #----- Campo texto da requisição -----
        self.lbl_texto = Label(frame_dados, text="Finalidade:")
        self.lbl_texto.grid(row = 3, column = 0, pady = 2, sticky="NE")
        
        self.funcprest = Text(frame_dados, height = 3, width = 55)
        self.funcprest.grid(row = 3, column = 1, pady = 2, columnspan = 4, rowspan = 4,sticky="NW")

        #-----------------------
        #----- Frame itens -----
        frame_item = Frame(self.req)
        frame_item.pack(fill=X)

        #----- Campo lista de itens -----
        self.itens = ttk.Treeview(frame_item)
        self.itens["columns"]=("one","two","three","four","five")
        self.itens.column("#0", width=50, minwidth=50, stretch=NO)
        self.itens.column("one", width=50, minwidth=50, stretch=NO)
        self.itens.column("two", width=100, minwidth=100, stretch=NO)
        self.itens.column("three", width=150, minwidth=150, stretch=NO)
        self.itens.column("four", width=200, minwidth=200, stretch=NO)
        self.itens.column("five", width=200, minwidth=200, stretch=NO)

        self.itens.heading("#0",text="Item",anchor=W)
        self.itens.heading("one", text="Qtd.",anchor=W)
        self.itens.heading("two", text="Unidade",anchor=W)
        self.itens.heading("three", text="Código",anchor=W)
        self.itens.heading("four", text="Descrição",anchor=W)
        self.itens.heading("five", text="Observação",anchor=W)

        self.itens.grid(row = 0, column = 0, columnspan=6, sticky="ew")

        #-----------------------
        #----- Frame CRUD1 -----
        frame_crud = Frame(self.req)
        frame_crud.pack()

        #----- Campo quantidade -----
        self.lbl_qtd = Label(frame_crud, text="Quantidade:")
        self.lbl_qtd.pack(side=LEFT)

        self.qtd = Spinbox(frame_crud, from_=0, to=999, width=5)
        self.qtd.pack(side=LEFT)

        #----- Campo Unidade -----
        self.unid = StringVar(self.req)
        opcoestipounid = [item[0] for item in Requisicao.loadtipounid()]
        self.unid.set("Unidade")
        self.opm_unid = OptionMenu(frame_crud, self.unid, *opcoestipounid)
        self.opm_unid.config(width=20)
        self.opm_unid.pack(side=LEFT)
        
        #----- Campo Código -----
        self.lbl_qtd = Label(frame_crud, text="Código:")
        self.lbl_qtd.pack(padx = 5, side=LEFT)

        self.qtd = Entry(frame_crud, width = 15)
        self.qtd.pack(side=LEFT)

        #----- Campo Descrição -----
        self.lbl_qtd = Label(frame_crud, text="Descrição:")
        self.lbl_qtd.pack(padx = 5, side=LEFT)

        self.qtd = Entry(frame_crud, width = 40)
        self.qtd.pack(side=LEFT)

        #-----------------------
        #----- Frame CRUD2 -----
        frame_crud2 = Frame(self.req)
        frame_crud2.pack()
        
        #----- Campo Observação -----
        self.lbl_obs = Label(frame_crud2, text="Observação:")
        self.lbl_obs.pack(side=LEFT)

        self.obs = Entry(frame_crud2, width = 112)
        self.obs.pack(side=LEFT)

        #-----------------------
        #----- Frame botões CRUD -----
        frame_btcrud = Frame(self.req)
        frame_btcrud.pack(side=LEFT)

        self.bt_gerar = Button(self.req, text="Gerar", \
                               command=self.req) # Botão gerar ticket
        self.bt_gerar.place(x = 250, y = 110, width=100, height=25)


        #============== Nome de usuario no rodapé ==============        
        self.lbl_logeduser = Label(self.req, text="Usuário: " + self.user.title())
        self.lbl_logeduser.pack(side=LEFT)#place(rely=1.0, relx=0.0, x=0, y=0, anchor="sw")
        
        

        
        mainloop()

Requisicao("Rodrigo")






        
