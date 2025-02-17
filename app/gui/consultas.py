import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import sqlite3
from app.utils import *
from app.classes.notafiscal import *
import random

class ConsultaWindow:
    def __init__(self):
        self.janela = None
        self.abrir_janela()

    def abrir_janela(self):
        """Abre a janela de consultas se ainda não estiver aberta."""
        if self.janela is None or not self.janela.winfo_exists():
            self.janela = tk.Toplevel()  # Abre uma nova janela Toplevel
            self.janela.title("Gestão de Consultas | CliniSystem")
            self.janela.geometry("1200x700")
            self.criar_interface()
        else:
            self.janela.lift()

    def criar_cabecalho(self):
        cabecalho = tk.Frame(self.janela, bg="navy", height=50)  # Usando self.janela, não self.raiz
        cabecalho.pack(fill=tk.X)
        titulo = tk.Label(cabecalho, text="Gestão de Consultas | CliniSystem", bg="navy", fg="white", font=("Arial", 16, "bold"))
        titulo.pack(side=tk.LEFT, padx=20, pady=10)
        logout_btn = tk.Button(cabecalho, text="Sair", bg="orange", fg="white", font=("Arial", 10, "bold"), command=self.sair)
        logout_btn.pack(side=tk.RIGHT, padx=20, pady=10)

    def criar_menu_lateral(self):
        menu_frame = tk.Frame(self.janela, bg="lightgray", width=180)  # Usando self.janela
        menu_frame.pack(side=tk.LEFT, fill=tk.Y)

        botoes = ["Início", "Médico", "Paciente", "Consulta", "Sair"]
        for texto in botoes:
            comando = self.sair if texto == "Sair" else None
            btn = tk.Button(menu_frame, text=texto, font=("Arial", 12), bg="white", relief=tk.GROOVE, height=2, command=comando)
            btn.pack(fill=tk.X, pady=5, padx=10)

    def criar_interface(self):
        """Cria a interface dentro da Toplevel."""
        main_frame = tk.Frame(self.janela, bg="white")
        main_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Notebook (abas)
        abas = ttk.Notebook(main_frame)
        abas.pack(fill=tk.BOTH, expand=True)

        # Aba principal (Gestão de Consultas)
        aba_principal = tk.Frame(abas, bg="white")
        abas.add(aba_principal, text="Gestão de Consultas")

        # ---- Conteúdo da Aba Principal ----
        tk.Label(aba_principal, text="Buscar Consulta", font=("Arial", 12, "bold"), bg="white").grid(row=0, column=0, columnspan=4, sticky="w", pady=5)

        tk.Label(aba_principal, text="Nome do Paciente:", bg="white", font=("Arial", 10)).grid(row=1, column=0, sticky="w")
        self.entry_nome = tk.Entry(aba_principal, width=30)
        self.entry_nome.grid(row=1, column=1, padx=5, pady=5, sticky="ew")

        btn_search = tk.Button(aba_principal, text="Buscar", bg="blue", fg="white", font=("Arial", 10, "bold"), command=self.buscar_consulta)
        btn_search.grid(row=1, column=2, padx=5, pady=5)

        tk.Label(aba_principal, text="Menu de Consultas", font=("Arial", 12, "bold"), bg="white").grid(row=2, column=0, columnspan=4, sticky="w", pady=5)

        btn_all = tk.Button(aba_principal, text="Mostrar Todas as Consultas", bg="green", fg="white", font=("Arial", 10, "bold"), command=self.mostrar_todas_as_consultas)
        btn_all.grid(row=3, column=1, padx=5, pady=5)
        btn_delete_all = tk.Button(aba_principal, text="Excluir Todas", bg="red", fg="white", font=("Arial", 10, "bold"), command=self.limpar_tabela)
        btn_delete_all.grid(row=3, column=2, padx=5, pady=5)

        tabela_frame = tk.Frame(aba_principal)
        tabela_frame.grid(row=4, column=0, columnspan=4, pady=10, sticky="nsew")

        colunas = ["ID consulta", "Nome Paciente", "Nome Médico", "Data", "Horário"]
        self.tabela_pacientes = ttk.Treeview(tabela_frame, columns=colunas, show="headings")

        for col in colunas:
            self.tabela_pacientes.heading(col, text=col)
            self.tabela_pacientes.column(col, width=140, anchor="center")

        self.tabela_pacientes.pack(fill=tk.BOTH, expand=True)

        # ==== Aba de Gerenciar Consultas ====
        aba_consultas = tk.Frame(abas, bg="white")
        abas.add(aba_consultas, text="Gerenciar Consultas")

        # ---- Conteúdo da Aba de Gerenciar Consultas ----
        tk.Label(aba_consultas, text="Id Paciente:", bg="white").grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
        self.paciente_cb = ttk.Entry(aba_consultas)
        self.paciente_cb.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(aba_consultas, text="Id Médico:", bg="white").grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
        self.medico_entry = tk.Entry(aba_consultas)
        self.medico_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(aba_consultas, text="Data da Consulta (DD-MM-AAAA):", bg="white").grid(row=2, column=0, padx=5, pady=5, sticky=tk.W)
        self.data_consulta_entry = tk.Entry(aba_consultas)
        self.data_consulta_entry.grid(row=2, column=1, padx=5, pady=5)

        tk.Label(aba_consultas, text="Horário (HH:MM:SS):", bg="white").grid(row=3, column=0, padx=5, pady=5, sticky=tk.W)
        self.horario_entry = tk.Entry(aba_consultas)
        self.horario_entry.grid(row=3, column=1, padx=5, pady=5)

        botao_marcar = tk.Button(aba_consultas, text="Marcar Consulta", bg="green", fg="white", command=self.marcar_consulta)
        botao_marcar.grid(row=4, column=0, padx=5, pady=5)

        # Tabela para exibir consultas
        self.tabela_consultas = ttk.Treeview(aba_consultas, columns=("Paciente", "Médico", "Data", "Hora"), show="headings")
        self.tabela_consultas.heading("Paciente", text="Paciente")
        self.tabela_consultas.heading("Médico", text="Médico")
        self.tabela_consultas.heading("Data", text="Data")
        self.tabela_consultas.heading("Hora", text="Hora")
        self.tabela_consultas.grid(row=6, column=0, columnspan=2, padx=5, pady=5)

    # Funções de ação dos botões
    def buscar_consulta(self):
        self.limpar_tabela()

        conn = sqlite3.connect("app/database/clinica.db")
        cursor = conn.cursor() 

        nome_paciente = self.entry_nome.get()
        cursor.execute("SELECT consultas.id_consulta, pacientes.nome, medicos.nome, consultas.data, consultas.horario FROM consultas JOIN pacientes ON consultas.id_paciente = pacientes.id_paciente JOIN medicos ON consultas.id_medico = medicos.id_medico WHERE pacientes.nome LIKE ?", (f"%{nome_paciente}%",))
        consultas = cursor.fetchall()

        self.atualizar_tabela(consultas)

        conn.close()

    def mostrar_todas_as_consultas(self):
        self.limpar_tabela()

        conn = sqlite3.connect("app/database/clinica.db")
        cursor = conn.cursor() 

        cursor.execute("SELECT consultas.id_consulta, pacientes.nome, medicos.nome, consultas.data, consultas.horario FROM consultas JOIN pacientes ON consultas.id_paciente = pacientes.id_paciente JOIN medicos ON consultas.id_medico = medicos.id_medico")
        consultas = cursor.fetchall()
        self.atualizar_tabela(consultas)

        conn.close()

    def marcar_consulta(self):
        id_paciente = self.paciente_cb.get()
        id_medico = self.medico_entry.get()
        data_consulta = self.data_consulta_entry.get()
        horario_consulta = self.horario_entry.get()

        consulta = [id_paciente, id_medico, data_consulta, horario_consulta]

        if id_paciente and id_medico and data_consulta and horario_consulta:
            insert_consulta(id_paciente, id_medico, data_consulta, horario_consulta)
            self.tabela_consultas.insert('', tk.END, values=(consulta[0], consulta[1], consulta[2], consulta[3]))
            self.limpar_campos_consulta()

            nfe = notafiscal(id_paciente, random.randint(200, 900), data_consulta, horario_consulta)
            nfe.emitir()
        else:
            messagebox.showwarning('Atenção', 'Preencha todos os campos!')

    def atualizar_tabela(self, consultas):
        for consulta in consultas:
            self.tabela_pacientes.insert("", "end", values=consulta)
    
    def limpar_tabela(self):
        for item in self.tabela_pacientes.get_children():
            self.tabela_pacientes.delete(item)
    
    def limpar_campos_consulta(self):
        self.paciente_cb.delete(0, tk.END)
        self.medico_entry.delete(0, tk.END)
        self.data_consulta_entry.delete(0, tk.END)
        self.horario_entry.delete(0, tk.END)