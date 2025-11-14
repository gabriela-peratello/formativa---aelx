import  ttkbootstrap as ttk
import sqlite3
import random
from tkinter import messagebox

 #LISTA DAS FRUTAS
frutas = ["🍒", "🍎", "🍓", "🍅"]

#CRIANDO A JANELA BASE
class Sorteio_frutas:
    def __init__(self):
        self.janela = ttk.Window(themename="cosmo")
        self.janela.geometry("700x600")
        self.janela.resizable(False, False)

        ttk.Label(self.janela, text="SORTEIO DE FRUTAS", font=("sylfaen", 20)).pack()

        #TEXTO TÍTULO
        self.janela_titulo = ttk.Label(self.janela, text="Seja bem-vindo(a)! Vamos testar sua sorte?", font="sylfaen").pack(pady=10)

#------------------------------------------------------------------------------------------------------------------------------------
        #FAZER AS FRUTAS APARECEREM NA TELA
        frame_frutas = ttk.Frame(self.janela)
        frame_frutas.pack(pady=20)

        self.fruta01 = ttk.Label(frame_frutas, text="🍒", font=("sylfaen", 70), bootstyle="", padding=10, relief="solid")
        self.fruta01.pack(side='left', padx=10)
        self.fruta02 = ttk.Label(frame_frutas, text="🍒", font=("sylfaen", 70), bootstyle="", padding=10, relief="solid")
        self.fruta02.pack(side='left', padx=10)
        self.fruta03 = ttk.Label(frame_frutas, text="🍒", font=("sylfaen", 70), bootstyle="", padding=10, relief="solid")
        self.fruta03.pack(side='left', padx=10)

# -----------------------------------------------------------------------------------------------------------------------------------
        frame_botoes = ttk.Frame(self.janela)
        frame_botoes.pack(pady=20)

        
        self.janela_botao = ttk.Button(frame_botoes, style="outline button", text="Sortear", width=20, command=sortear)
        self.janela_botao.pack(side="left", padx=10)

# ------------------------------------------------------------------------------------------------------------------------------------
        #TITULO
        self.janela_resultados = ttk.Label(self.janela, text="Se liga nos seus resultados!", font=("sylfaen", 15)).pack(pady=5)
        #TREEVIEW
        self.tw = ttk.Treeview(self.janela)
        self.tw.pack(padx=15)
        #NÃO EH O NOME QUE APARECE NA TELA
        self.tw["columns"] = ("resultado")
        #CABEÇALHO
        self.tw.heading("resultado", text="resultado")
        self.tw["show"] = "headings"

#--------------------------------------------------------------------------------------------------------------------------------------        
        def sortear():
                f01 = random.choice(frutas)
                f02 = random.choice(frutas)
                f03 = random.choice(frutas)

                # 2. Atualizar Frontend (Labels)
                self.fruta01.config(text=f01)
                self.fruta02.config(text=f02)
                self.fruta03.config(text=f03)

                if f01 == f02 and f02 == f03 :
                        messagebox.showinfo("Parabéns, você ganhou!", 
                                        f"\n\nVocê conseguiu {f01}-{f02}-{f03}!")

               
                # jogada = f"{f01} - {f02} - {f03}"















            

















app = Sorteio_frutas()      
app.janela.mainloop()