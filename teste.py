import ttkbootstrap as ttk
import sqlite3
import random
from tkinter import messagebox

# --- Constantes ---
FRUTAS_LISTA = ['🍎', '🍌', '🍇', '🍊', '🍍', '🍓']


class SorteioApp:
    
    def __init__(self):
        self.janela = ttk.Window(themename="darkly")
        self.janela.title("Sorteio de Frutas v3 (1 Campo) - SENAI")
        self.janela.geometry("600x600") # Pode ser um pouco menor

        # --- Widgets da Interface (Idêntico ao anterior) ---
        
        ttk.Label(self.janela, text="Sorteio de Frutas 🎰", font=("Helvetica", 24, "bold"), bootstyle="primary").pack(pady=20)

        frame_frutas = ttk.Frame(self.janela)
        frame_frutas.pack(pady=20)

        self.lbl_fruta1 = ttk.Label(frame_frutas, text="🍓", font=("Arial", 64), bootstyle="info", padding=10, relief="solid")
        self.lbl_fruta1.pack(side='left', padx=10)
        
        self.lbl_fruta2 = ttk.Label(frame_frutas, text="🍓", font=("Arial", 64), bootstyle="info", padding=10, relief="solid")
        self.lbl_fruta2.pack(side='left', padx=10)
        
        self.lbl_fruta3 = ttk.Label(frame_frutas, text="🍓", font=("Arial", 64), bootstyle="info", padding=10, relief="solid")
        self.lbl_fruta3.pack(side='left', padx=10)

        self.btn_sortear = ttk.Button(self.janela, text="Sortear!", 
                                      bootstyle="success-outline", 
                                      command=self.realizar_sorteio)
        self.btn_sortear.pack(pady=20, ipadx=20, ipady=10)

        # --- Área do Histórico (Treeview - Atualizado) ---
        ttk.Label(self.janela, text="Histórico de Jogadas", font=("Helvetica", 16)).pack(pady=(10, 5))

        tree_frame = ttk.Frame(self.janela)
        tree_frame.pack(fill="both", expand=True, padx=20, pady=10)

        scrollbar = ttk.Scrollbar(tree_frame, orient="vertical")
        scrollbar.pack(side="right", fill="y")

        # Definição das colunas (ATUALIZADO)
        cols = ('resultado') # Colunas super simplificadas
        self.tree = ttk.Treeview(tree_frame, 
                                 columns=cols, 
                                 show='headings', 
                                 bootstyle="INFO",
                                 yscrollcommand=scrollbar.set)
        
        scrollbar.config(command=self.tree.yview)

        # Configurando os Cabeçalhos (ATUALIZADO)

        self.tree.heading('resultado', text='Resultado da Jogada')

        # Configurando a largura das colunas (ATUALIZADO)
        self.tree.column('resultado', width=450, anchor="center") # Campo principal

        self.tree.pack(fill="both", expand=True)

        # Criando o banco de dados
        self.criar_database()

        # --- Carregamento Inicial ---
        self.atualizar_treeview()

    def realizar_sorteio(self):
        """
        Função principal: Sorteia, formata a string e salva no banco (v3).
        """
        # 1. Lógica (Sorteio)
        f1 = random.choice(FRUTAS_LISTA)
        f2 = random.choice(FRUTAS_LISTA)
        f3 = random.choice(FRUTAS_LISTA)

        # 2. Atualizar Frontend (Labels)
        self.lbl_fruta1.config(text=f1)
        self.lbl_fruta2.config(text=f2)
        self.lbl_fruta3.config(text=f3)

        # Formata a string de resultado com base na vitória
        if f1 == f2 and f2 == f3 :
            messagebox.showinfo("🎉 VENCEDOR! 🎉", 
                                f"PARABÉNS!!\n\nVocê conseguiu {f1}-{f2}-{f3}!\n\nVocê é um mestre das frutas! 🏆")

        # 4. Salvar no Backend (INSERT - Atualizado)
        jogada = f"{f1} - {f2} - {f3}"

        self.salvar_jogada(jogada)

        # 5. Atualizar Histórico (SELECT)
        self.atualizar_treeview()    

    def criar_database(self):
        """
        Cria o banco e a tabela 'jogadas' (VERSÃO 3).
        A tabela terá APENAS 1 campo de dados (resultado).
        """
        conn = sqlite3.connect("sorteio.db")
        cursor = conn.cursor()
        
        # ATUALIZADO: Tabela com apenas id e resultado
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS jogadas (
                resultado TEXT NOT NULL
            )
        """)
        conn.commit()
        conn.close()

    def atualizar_treeview(self):
        """
        Busca (SELECT) todas as jogadas (VERSÃO 3).
        """
        conn = sqlite3.connect("sorteio.db")
        cursor = conn.cursor()
        
        # ATUALIZADO: SQL buscando apenas id e resultado
        sql = "SELECT resultado FROM jogadas"
        cursor.execute(sql)
        resultados = cursor.fetchall()
        conn.close()

        # Limpar o Treeview (para não duplicar)
        for i in self.tree.get_children():
            self.tree.delete(i)

        # Popular o Treeview
        for jogada in resultados:
            # A tupla 'jogada' já vem no formato (resultado),
            # exatamente o que o Treeview espera.
            self.tree.insert("", "end", values=jogada)

    def salvar_jogada(self,resultado_final_str):
        """
        Salva (INSERT) a string de resultado final no banco (VERSÃO 3).
        """
        conn = sqlite3.connect("sorteio.db")
        cursor = conn.cursor()
        
        # ATUALIZADO: SQL com apenas um valor
        sql = "INSERT INTO jogadas (resultado) VALUES (?)"
        cursor.execute(sql, (resultado_final_str,)) # Note a vírgula (,) para tupla
        conn.commit()
        conn.close()

    def run(self):
        self.janela.mainloop()


# --- 3. Execução do Programa ---

if __name__ == "__main__":
  
    # Instanciar a classe da aplicação
    app = SorteioApp()
    
    # Rodar o loop principal
    app.run()