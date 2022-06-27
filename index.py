from tkinter import *
from PIL import Image, ImageTk

# --------------------Função redimensionar img-------------------- #
def redimensionar(img, x, y):
        rimg = img.resize((x, y), Image.ANTIALIAS)
        new_img = ImageTk.PhotoImage(rimg)
        return new_img

# -----------------------Class Button----------------------- #

class botoes:
    def __init__(self, container):
        self.bt = Button(container)
        self.bt.configure(
            bg='#C4C4C4',
            width=14,
            height=2,
            font=('Verdana', 18, 'bold')
        )
            
class Janela_Index:
    def __init__(self,privilegio):
        self.index = Tk()
        self.privilegio = privilegio
        self.tela()
        self.inserir_elementos()
        self.index.mainloop()
    
    def tela(self):
        self.index.title("Love Pet")
        self.index.geometry("1024x600")
        self.index.configure(bg="#086788")
        self.index.resizable(False, False)
    # --------------------Função sair-------------------- #

    def sairProg(self):
        self.index.destroy()
        
    # -------------------Funções para abrir as páginas-------------------#
    def Open_cadPes(self):
        print('calma bb')


    def Open_adoc(self):
        print('calma bb')


    def Open_geren(self):
        print('calma bb')


    def Open_cadPet(self):
        print('calma bb')


    def Open_tabPet(self):
        print('calma bb')


    def Open_cadCli(self):
        print('calma bb')

    def inserir_elementos(self):
        img = (Image.open('sair.png'))
        self.img = redimensionar(img, 25, 25)
        
        # -----------------------Nome da empresa----------------------- #
        self.nome_empresa = Label(self.index)
        self.nome_empresa.configure(
            text="Love Pet",
            bg='#086788',
            fg='#FFFFFF',
            font=('Verdana', 40, 'bold')
        )
        self.nome_empresa.place(x=378, y=30)

        self.sair_botao = Button(self.index)
        self.sair_botao.configure(
            image=self.img,
            bg='#C4C4C4',
            width=30,
            height=40,
            relief=RAISED,
            command=self.sairProg
        )
        self.sair_botao.place(x=978, y=20)

        #-----------Menu---------#
        #   --lado esquerdo--    #
        self.cadPes_but = botoes(self.index)
        self.cadPes_but.bt.configure(text='Cadastro', command=self.Open_cadPes)
        self.cadPes_but.bt.place(x=238, y=160)

        self.adoc_but = botoes(self.index)
        self.adoc_but.bt.configure(text='Adoção', command=self.Open_adoc)
        self.adoc_but.bt.place(x=238, y=260)

        self.geren_but = botoes(self.index)
        self.geren_but.bt.configure(text='Gerenciamento', command=self.Open_geren)
      
        #   --lado Direito--    #

        self.cadPet_but = botoes(self.index)
        self.cadPet_but.bt.configure(text='Cadastra Pet', command=self.Open_cadPet)
        self.cadPet_but.bt.place(x=538, y=160)

        self.tabPet_but = botoes(self.index)
        self.tabPet_but.bt.configure(text='Tabela de Pets', command=self.Open_tabPet)
        self.tabPet_but.bt.place(x=538, y=260)

        self.cadCli_but = botoes(self.index)
        self.cadCli_but.bt.configure(text='Cadastrar Clínicas', command=self.Open_cadCli)
        
        if self.privilegio == 'Administrador':
            self.geren_but.bt.place(x=238, y=360)
            self.cadCli_but.bt.place(x=538, y=360)
        else:
            self.cadCli_but.bt.place(x=380, y=360)
    
