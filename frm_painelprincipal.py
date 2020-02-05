#from frm_cadstveic import admfrota
import frm_acesso
from tkinter import messagebox
from tkinter import Tk, Menu, Label


class frm_principal():
    def autabertprod(self):
        from frm_ticketabertura import autabert
        autabert(self.user)
        return None


    def pecaseservs(self):
        from frm_dadosos import frm_geros
        frm_geros(self.user)
        return None


    def frota(self):
        from frm_cadstveic import admfrota
        admfrota(self.user)
        return None    
    

    def __init__(self, user):
        self.user = user # Nome de usuario logado

        #============== Janela principal ==============
        self.principal = Tk()
        self.principal.minsize(800, 500)
        self.principal.title("RSC - Painel principal")
    

        #======= Menu superior =======
        menubar = Menu(self.principal)
        pesssoasmenu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="CRM", menu = pesssoasmenu)
        pesssoasmenu.add_command(label="Cadastrar", command=None)
        pesssoasmenu.add_command(label="Relatório", command=None)
        pesssoasmenu.add_separator()     

        #---- Menu de veículos ----
        mn_veiculos = Menu(menubar, tearoff=0) #Cria o menu de Veículos
        menubar.add_cascade(label="Veículos", menu=mn_veiculos)

        #-- Submenu de cadastro --
        sub_cad = Menu(self.principal, tearoff=0) #Cria submenu de cadastro
        mn_veiculos.add_cascade(label="Cadastro", menu=sub_cad)
        sub_cad.add_command(label="Motoristas", command=None)
        sub_cad.add_command(label="Veículos", command=lambda: frm_principal.frota(self))
        
        #-- Submenu de utilização --
        sub_utilz = Menu(self.principal, tearoff=0)
        mn_veiculos.add_cascade(label="Utilização", menu=sub_utilz)
        sub_utilz.add_command(label="Relatório", command=None)
        sub_utilz.add_command(label="Rodagens", command=None)

        #---- Menu de serviços ----
        servicosmenu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Serviços", menu = servicosmenu)
        servicosmenu.add_command(label="Peças e serviços", command=lambda: frm_principal.pecaseservs(self))
        servicosmenu.add_command(label="Relatório", command=None)
        servicosmenu.add_command(label="Injeção", command=None)
        servicosmenu.add_command(label="Autorizar abertura de produção", command=lambda: frm_principal.autabertprod(self))   

        self.principal.config(menu = menubar)
        self.principal.update()

        

        
        #============== Widgets Principais ==============        
        self.lbl_logeduser = Label(self.principal, text="Usuário: " + self.user.title())
        self.lbl_logeduser.place(rely=1.0, relx=0.0, x=0, y=0, anchor="sw")
        
        self.principal.mainloop()


    
