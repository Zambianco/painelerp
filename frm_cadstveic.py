from tkinter import Toplevel, Frame, Entry, Button, LabelFrame, OptionMenu, StringVar, Label, Place, Grid, BooleanVar
from tkinter.ttk import LabelFrame, Entry, Button, OptionMenu, Checkbutton
import sqlite3
from maskedentry import MaskedWidget
import frm_painelprincipal
from tkinter import messagebox

#>>>>>>>>>> Conexão ao banco de dados >>>>>>>>>>
from loadcfg import dbprmt # nas configurações carrega os parametros do db
cfg = dbprmt() # Carrega a configuração da localização do banco de dados

conn = sqlite3.connect(cfg.dbpath)
cursor = conn.cursor()
#<<<<<<<<<< Conexão ao banco de dados <<<<<<<<<<

class admfrota():
    #Janela de cadastro e edição de dados dos veículos integrantes da frota
    def busca(self):
        #Busca de informações no banco de dados            
        pass

    def buscarenavam(renavam=None):
        print(renavam)
        
        dados = cursor.fetchall()
        print(dados)

    def salva(self):
        self.placa = self.entry_placa.get().replace("-", "").replace("_", "").lower()
        self.montadora = self.entry_mont.get().lower()
        self.modelo = self.entry_modl.get().lower()
        self.anofabr = self.entry_anof.get()
        self.anomod = self.entry_anom.get()
        self.vin = self.entry_vin.get().lower()
        self.renavam = self.entry_renav.get()
        self.comb = self.combs.get().lower()
        self.hab = self.habil.get().lower()
        self.lubrtipo = self.entry_oleo.get().lower()
        self.lubrdata = self.entry_troleodt.get().replace("/", "").replace("_", "")
        self.lubrkm = self.entry_troleokm.get().replace("km", "").replace("_", "")
        self.pneutipo = self.entry_tipopneu.get().lower()
        self.pneukm = self.entry_manutpneukm.get().replace("km", "").replace("_", "")
        self.pneudata = self.entry_manutpneudt.get().replace("/", "").replace("_", "")
        self.ativo = True
        """..."""

        if self.placa is "" or self.comb is "?":
            messagebox.showerror("Erro", "É necessário preencher a placa")
            raise Exception("Campo de preenchimento obrigatório")


        
            
        
        dados = (self.placa,
              self.montadora,
              self.modelo,
              self.anofabr,
              self.anomod,
              self.vin,
              self.renavam,
              self.comb,
              self.hab,
              self.lubrtipo,
              self.lubrdata,
              self.lubrkm,
              self.pneutipo,
              self.pneukm,
              self.pneudata,
              self.ativo)

        

        try:
            cursor.execute("""
            INSERT OR IGNORE INTO frota_veic (placa,
                                    montadora,
                                    modelo,
                                    anofabr,
                                    anomodel,
                                    vin,
                                    renavam,
                                    combustivel,
                                    habnec,
                                    lubrtipo,
                                    lubrdata,
                                    lubrkm,
                                    pneutipo,
                                    pneukmtroca,
                                    pneudatatroca,
                                    ativo)

            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,dados)

            conn.commit()

            print("dados inseridos com sucesso")
        except teste:
            print("Erro")
        

    def __init__(self, user):
        self.user = user
        self.cadveic = Toplevel()
        self.cadveic.title("Cadastro de veículos")
        self.cadveic.resizable(0, 0)
        self.cadveic.attributes('-topmost', 'true')
        #-----------------------
        #----- Frame busca -----
        frame_busca = Frame(self.cadveic)
        frame_busca.grid(row = 0, column = 0, columnspan=2)

        #----- Campo busca -----
        self.buscaplaca = Label(frame_busca, text="Busca (placa):")
        self.buscaplaca.grid(row = 0, column = 0, pady = 2)

        self.entry_buscaplaca = Entry(frame_busca)
        self.entry_buscaplaca.grid(row = 0, column = 1, pady = 2)

        self.bt_buscaplaca = Button(frame_busca, command=None) # Botão busca
        self.bt_buscaplaca.grid(row = 0, column = 2, pady = 2)
   

        #----------------------------------------
        #----- Frame dados de identificação -----
        lblframe_dados = LabelFrame(self.cadveic, text = "Dados do veículo")
        lblframe_dados.grid(row = 1, column = 0, padx = 10)
        
        #----- Campo placa -----
        self.lbl_placa = Label(lblframe_dados, text="Placa:")
        self.lbl_placa.grid(row = 0, column = 0, pady = 2, sticky="E")

        self.entry_placa = MaskedWidget(lblframe_dados, 'fixed', mask='xxx-xxx9')
        self.entry_placa.grid(row = 0, column = 1, pady = 2)

        #----- Campo montadora -----
        self.lbl_mont = Label(lblframe_dados, text="Montadora:")
        self.lbl_mont.grid(row = 1, column = 0, pady = 2, sticky="E")

        self.entry_mont = Entry(lblframe_dados)
        self.entry_mont.grid(row = 1, column = 1, pady = 2)

        #----- Campo modelo -----
        self.lbl_modl = Label(lblframe_dados, text="Modelo:")
        self.lbl_modl.grid(row = 2, column = 0, pady = 2, sticky="E")

        self.entry_modl = Entry(lblframe_dados)
        self.entry_modl.grid(row = 2, column = 1, pady = 2)

        #----- Campo ano fabr. -----
        self.lbl_anof = Label(lblframe_dados, text="Ano fabr.:")
        self.lbl_anof.grid(row = 3, column = 0, pady = 2, sticky="E")

        self.entry_anof = Entry(lblframe_dados)
        self.entry_anof.grid(row = 3, column = 1, pady = 2)

        #----- Campo ano model. -----
        self.lbl_anom = Label(lblframe_dados, text="Ano model.:")
        self.lbl_anom.grid(row = 4, column = 0, pady = 2, sticky="E")

        self.entry_anom = Entry(lblframe_dados)
        self.entry_anom.grid(row = 4, column = 1, pady = 2)

        #----- Campo VIN -----
        self.lbl_vin = Label(lblframe_dados, text="VIN:")
        self.lbl_vin.grid(row = 5, column = 0, pady = 2, sticky="E")

        self.entry_vin = Entry(lblframe_dados)
        self.entry_vin.grid(row = 5, column = 1, pady = 2)

        #----- Campo renavan -----
        self.lbl_renav = Label(lblframe_dados, text="Renavam:")
        self.lbl_renav.grid(row = 6, column = 0, pady = 2, sticky="E")

        self.entry_renav = Entry(lblframe_dados)
        self.entry_renav.grid(row = 6, column = 1, pady = 2)

        #----- Campo combustível -----
        self.lbl_combs = Label(lblframe_dados, text="Combustível:")
        self.lbl_combs.grid(row = 7, column = 0, pady = 2, sticky="E")

        self.combs = StringVar(self.cadveic)
        opcoescombs = ["?", "Álcool", "Álcool/Gasolina", "Gasolina", "Diesel"]
        self.combs.set(opcoescombs[0])
        self.opm_combs = OptionMenu(lblframe_dados, self.combs, *opcoescombs)
        self.opm_combs.grid(row = 7, column = 1, pady = 2)

        #----- Campo Hab. Nec. -----
        self.lbl_habil = Label(lblframe_dados, text="Hab. Nec.:")
        self.lbl_habil.grid(row = 8, column = 0, pady = 2, sticky="E")

        self.habil = StringVar(self.cadveic)
        opcoeshabil = ["?", "A", "B", "C", "D", "E"]
        self.habil.set(opcoescombs[0])
        self.opm_habil = OptionMenu(lblframe_dados, self.habil, *opcoeshabil)
        self.opm_habil.grid(row = 8, column = 1, pady = 2)


        #-------------------------------------
        #----- Frame 1 -----
        frame_1 = LabelFrame(self.cadveic)
        frame_1.grid(row = 1, column = 1, padx = 10, sticky="N")

        
        #-------------------------------------
        #----- Frame dados de manutenção -----
        lblframe_manut = LabelFrame(frame_1, text = "Dados de manutenção")
        lblframe_manut.grid(row = 0, column = 0, padx = 10, sticky="N")

        #----- Campo tipo óleo -----
        self.lbl_oleo = Label(lblframe_manut, text="Tipo de óleo lubrificante:")
        self.lbl_oleo.grid(row = 0, column = 0, pady = 2, sticky="E")

        self.entry_oleo = Entry(lblframe_manut)
        self.entry_oleo.grid(row = 0, column = 1, pady = 2)

        #----- Campo último km troca de lubrificante -----
        self.lbl_troleokm = Label(lblframe_manut, text="Última troca lub.:")
        self.lbl_troleokm.grid(row = 1, column = 0, pady = 2, sticky="E")

        self.entry_troleokm = MaskedWidget(lblframe_manut, 'fixed', mask='9999999 km')
        self.entry_troleokm.grid(row = 1, column = 1, pady = 2)
     
        self.entry_troleodt = MaskedWidget(lblframe_manut, 'fixed', mask='99/99/9999')
        self.entry_troleodt.grid(row = 1, column = 2, pady = 2)

        #----- Campo tipo de pneu -----
        self.lbl_tipopneu = Label(lblframe_manut, text="Tipo de pneu:")
        self.lbl_tipopneu.grid(row = 2, column = 0, pady = 2, sticky="E")

        self.entry_tipopneu = Entry(lblframe_manut)
        self.entry_tipopneu.grid(row = 2, column = 1, pady = 2)

        #----- Campo último km manutenção pneu -----
        self.lbl_manutpneukm = Label(lblframe_manut, text="Último bal./ali./rod.:")
        self.lbl_manutpneukm.grid(row = 3, column = 0, pady = 2, sticky="E")

        self.entry_manutpneukm = MaskedWidget(lblframe_manut, 'fixed', mask='9999999 km')
        self.entry_manutpneukm.grid(row = 3, column = 1, pady = 2)
        
        self.entry_manutpneudt = MaskedWidget(lblframe_manut, 'fixed', mask='99/99/9999')
        self.entry_manutpneudt.grid(row = 3, column = 2, pady = 2)

        #----- Checkbox veículo ativo -----
        self.veicativo = BooleanVar() 
        self.cb_veicativo = Checkbutton(lblframe_manut, text="Veículo ativo", \
                                        variable=self.veicativo)
        self.cb_veicativo.grid(row = 5, column = 5, pady = 2)
        self.veicativo.set = 1

        #-------------------------------------
        #----- Frame botões -----
        lblframe_botao = LabelFrame(frame_1, text = "Opções")
        lblframe_botao.grid(row = 1, column = 0, padx = 10, sticky="S")

        
        #----- Botão salvar -----
        self.bt_gerar = Button(lblframe_botao, text="Salvar", \
                               command=self.salva) # Botão salvar
        self.bt_gerar.grid(row = 0, column = 0, padx = 10, sticky="N")

        #----- Botão excluir -----
        self.bt_gerar = Button(lblframe_botao, text="Excluir", \
                               command=None) # Botão salvar
        self.bt_gerar.grid(row = 0, column = 1, padx = 10, sticky="N")
        
        
        #----- Assinatura do usuário logado -----
        self.lbl_logeduser = Label(self.cadveic, text="Usuário: " + self.user.title())
        self.lbl_logeduser.grid(row = 4, column = 0, sticky="sW")

