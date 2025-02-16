# Correções implementadas:
# - Funcionalidades completas para adicionar, limpar e marcar consultas.
# - Persistência simples de dados usando arquivos JSON.
# - Ações implementadas para os botões sem comandos.

import tkinter as tk
from tkinter import ttk, messagebox
import json
import os
from app.gui.controller import CliniSystemController

# Função auxiliar para carregar/salvar dados
def carregar_dados(arquivo):
    if os.path.exists(arquivo):
        with open(arquivo, 'r') as f:
            return json.load(f)
    return []

def salvar_dados(arquivo, dados):
    with open(arquivo, 'w') as f:
        json.dump(dados, f, indent=4)

class MedicoWindow:
    def __init__(self, controller):
        self.controller = controller
        self.janela = None
        self.abrir_janela()

    def abrir_janela(self):
        if self.janela is None or not self.janela.winfo_exists():
            self.janela = tk.Toplevel()
            self.janela.title("Gerenciar Médicos e Especializações")
            self.janela.geometry("1200x700")
            self.criar_interface()
        else:
            self.janela.lift()

    def adicionar_medico(self):
        nome = self.nome_entry.get()
        especializacao = self.especializacao_entry.get()
        taxa = self.consulta_entry.get()
        contato = self.contato_entry.get()
        email = self.email_entry.get()

        if nome and especializacao and taxa and contato and email:
            medico = self.controller.adicionar_medico(nome, especializacao, taxa, contato, email)
            self.tabela_medicos.insert('', tk.END, values=(medico['nome'], medico['especializacao'], medico['taxa'], medico['contato'], medico['email']))
            self.limpar_campos_medico()
            salvar_dados('medicos.json', self.controller.obter_medicos())
            messagebox.showinfo('Sucesso', f"Médico {nome} adicionado com sucesso!")
        else:
            messagebox.showwarning('Atenção', 'Preencha todos os campos!')

    def limpar_campos_medico(self):
        self.nome_entry.delete(0, tk.END)
        self.especializacao_entry.delete(0, tk.END)
        self.consulta_entry.delete(0, tk.END)
        self.contato_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)

    def criar_interface(self):
        frame = tk.Frame(self.janela, bg="white")
        frame.pack(fill=tk.BOTH, expand=True)

        tk.Label(frame, text="Nome:", bg="white").grid(row=0, column=0, padx=5, pady=5)
        self.nome_entry = tk.Entry(frame)
        self.nome_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(frame, text="Especialização:", bg="white").grid(row=1, column=0, padx=5, pady=5)
        self.especializacao_entry = tk.Entry(frame)
        self.especializacao_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(frame, text="Taxa:", bg="white").grid(row=2, column=0, padx=5, pady=5)
        self.consulta_entry = tk.Entry(frame)
        self.consulta_entry.grid(row=2, column=1, padx=5, pady=5)

        tk.Label(frame, text="Contato:", bg="white").grid(row=3, column=0, padx=5, pady=5)
        self.contato_entry = tk.Entry(frame)
        self.contato_entry.grid(row=3, column=1, padx=5, pady=5)

        tk.Label(frame, text="Email:", bg="white").grid(row=4, column=0, padx=5, pady=5)
        self.email_entry = tk.Entry(frame)
        self.email_entry.grid(row=4, column=1, padx=5, pady=5)

        btn_add = tk.Button(frame, text="Adicionar", bg="blue", fg="white", command=self.adicionar_medico)
        btn_add.grid(row=5, column=0, pady=5)

        btn_clear = tk.Button(frame, text="Limpar", bg="red", fg="white", command=self.limpar_campos_medico)
        btn_clear.grid(row=5, column=1, pady=5)

        colunas = ("Nome", "Especialização", "Taxa", "Contato", "E-mail")
        self.tabela_medicos = ttk.Treeview(frame, columns=colunas, show="headings")

        for col in colunas:
            self.tabela_medicos.heading(col, text=col)
            self.tabela_medicos.column(col, width=140)

        self.tabela_medicos.grid(row=6, column=0, columnspan=2, pady=5)

        # Carregar médicos existentes
        medicos_existentes = carregar_dados('medicos.json')
        for med in medicos_existentes:
            self.controller.adicionar_medico(**med)
            self.tabela_medicos.insert('', tk.END, values=(med['nome'], med['especializacao'], med['taxa'], med['contato'], med['email']))


