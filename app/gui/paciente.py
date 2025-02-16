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

class PacienteWindow:
    def __init__(self, controller):
        self.controller = controller
        self.janela = None
        self.abrir_janela()

    def abrir_janela(self):
        if self.janela is None or not self.janela.winfo_exists():
            self.janela = tk.Toplevel()
            self.janela.title("Gerenciar Pacientes")
            self.janela.geometry("1200x700")
            self.criar_interface()
        else:
            self.janela.lift()

    def adicionar_paciente(self):
        nome = self.nome_entry.get()
        genero = self.genero_entry.get()
        nascimento = self.nascimento_entry.get()
        contato = self.contato_entry.get()
        email = self.email_entry.get()
        endereco = self.endereco_entry.get()

        if nome and genero and nascimento and contato and email and endereco:
            paciente = self.controller.adicionar_paciente(nome, genero, nascimento, contato, email, endereco)
            self.tabela_pacientes.insert('', tk.END, values=(paciente['nome'], paciente['genero'], paciente['nascimento'], paciente['contato'], paciente['email'], paciente['endereco']))
            self.limpar_campos_paciente()
            salvar_dados('pacientes.json', self.controller.obter_pacientes())
            messagebox.showinfo('Sucesso', f"Paciente {nome} adicionado com sucesso!")
        else:
            messagebox.showwarning('Atenção', 'Preencha todos os campos!')

    def limpar_campos_paciente(self):
        self.nome_entry.delete(0, tk.END)
        self.genero_entry.delete(0, tk.END)
        self.nascimento_entry.delete(0, tk.END)
        self.contato_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.endereco_entry.delete(0, tk.END)

    def criar_interface(self):
        frame = tk.Frame(self.janela, bg="white")
        frame.pack(fill=tk.BOTH, expand=True)

        tk.Label(frame, text="Nome do Paciente:", bg="white").grid(row=0, column=0, padx=5, pady=5)
        self.nome_entry = tk.Entry(frame)
        self.nome_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(frame, text="Gênero:", bg="white").grid(row=1, column=0, padx=5, pady=5)
        self.genero_entry = tk.Entry(frame)
        self.genero_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(frame, text="Data de Nascimento:", bg="white").grid(row=2, column=0, padx=5, pady=5)
        self.nascimento_entry = tk.Entry(frame)
        self.nascimento_entry.grid(row=2, column=1, padx=5, pady=5)

        tk.Label(frame, text="Contato:", bg="white").grid(row=3, column=0, padx=5, pady=5)
        self.contato_entry = tk.Entry(frame)
        self.contato_entry.grid(row=3, column=1, padx=5, pady=5)

        tk.Label(frame, text="E-mail:", bg="white").grid(row=4, column=0, padx=5, pady=5)
        self.email_entry = tk.Entry(frame)
        self.email_entry.grid(row=4, column=1, padx=5, pady=5)

        tk.Label(frame, text="Endereço:", bg="white").grid(row=5, column=0, padx=5, pady=5)
        self.endereco_entry = tk.Entry(frame, width=50)
        self.endereco_entry.grid(row=5, column=1, padx=5, pady=5)

        btn_add = tk.Button(frame, text="Adicionar", bg="blue", fg="white", command=self.adicionar_paciente)
        btn_add.grid(row=6, column=0, pady=5)

        btn_clear = tk.Button(frame, text="Limpar", bg="red", fg="white", command=self.limpar_campos_paciente)
        btn_clear.grid(row=6, column=1, pady=5)

        colunas = ("Nome", "Gênero", "Nascimento", "Contato", "E-mail", "Endereço")
        self.tabela_pacientes = ttk.Treeview(frame, columns=colunas, show="headings")

        for col in colunas:
            self.tabela_pacientes.heading(col, text=col)
            self.tabela_pacientes.column(col, width=140)

        self.tabela_pacientes.grid(row=7, column=0, columnspan=2, pady=5)

        # Carregar pacientes existentes
        pacientes_existentes = carregar_dados('pacientes.json')
        for pac in pacientes_existentes:
            self.controller.adicionar_paciente(**pac)
            self.tabela_pacientes.insert('', tk.END, values=(pac['nome'], pac['genero'], pac['nascimento'], pac['contato'], pac['email'], pac['endereco']))

