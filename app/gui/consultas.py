import tkinter as tk
from tkinter import ttk
from app.gui.controller import CliniSystemController


class ConsultaWindow:
    def __init__(self, controller):
        self.controller = controller
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

    def sair(self):
        self.janela.destroy()  # Agora estamos destruindo 'self.janela' ao invés de 'self.raiz'

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
        entry_nome = tk.Entry(aba_principal, width=30)
        entry_nome.grid(row=1, column=1, padx=5, pady=5, sticky="ew")

        btn_search = tk.Button(aba_principal, text="Buscar", bg="blue", fg="white", font=("Arial", 10, "bold"), command=self.buscar_consulta)
        btn_search.grid(row=1, column=2, padx=5, pady=5)
        btn_clear = tk.Button(aba_principal, text="Limpar", bg="gray", fg="white", font=("Arial", 10, "bold"), command=self.limpar_busca)
        btn_clear.grid(row=1, column=3, padx=5, pady=5)

        tk.Label(aba_principal, text="Menu de Consultas", font=("Arial", 12, "bold"), bg="white").grid(row=2, column=0, columnspan=4, sticky="w", pady=5)

        btn_today = tk.Button(aba_principal, text="Mostrar Consultas de Hoje", bg="blue", fg="white", font=("Arial", 10, "bold"), command=self.mostrar_consultas_hoje)
        btn_today.grid(row=3, column=0, padx=5, pady=5)
        btn_all = tk.Button(aba_principal, text="Mostrar Todas as Consultas", bg="green", fg="white", font=("Arial", 10, "bold"), command=self.mostrar_todas_as_consultas)
        btn_all.grid(row=3, column=1, padx=5, pady=5)
        btn_delete_all = tk.Button(aba_principal, text="Excluir Todas", bg="red", fg="white", font=("Arial", 10, "bold"), command=self.excluir_todas_as_consultas)
        btn_delete_all.grid(row=3, column=2, padx=5, pady=5)
        btn_delete_today = tk.Button(aba_principal, text="Excluir Histórico de Hoje", bg="gray", fg="white", font=("Arial", 10, "bold"), command=self.excluir_historico_hoje)
        btn_delete_today.grid(row=3, column=3, padx=5, pady=5)

        tabela_frame = tk.Frame(aba_principal)
        tabela_frame.grid(row=4, column=0, columnspan=4, pady=10, sticky="nsew")

        colunas = ["ID", "Nome", "Contato", "Sintomas", "Especialização", "Médico", "Data Consulta", "Hora"]
        tabela_pacientes = ttk.Treeview(tabela_frame, columns=colunas, show="headings")

        for col in colunas:
            tabela_pacientes.heading(col, text=col)
            tabela_pacientes.column(col, width=140, anchor="center")

        tabela_pacientes.pack(fill=tk.BOTH, expand=True)

        # ==== Aba de Gerenciar Consultas ====
        aba_consultas = tk.Frame(abas, bg="white")
        abas.add(aba_consultas, text="Gerenciar Consultas")

        # ---- Conteúdo da Aba de Gerenciar Consultas ----
        tk.Label(aba_consultas, text="Paciente:", bg="white").grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
        paciente_cb = ttk.Combobox(aba_consultas)
        paciente_cb.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(aba_consultas, text="Sintomas:", bg="white").grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
        sintomas_entry = tk.Entry(aba_consultas)
        sintomas_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(aba_consultas, text="Especialização:", bg="white").grid(row=2, column=0, padx=5, pady=5, sticky=tk.W)
        especializacao_cb = ttk.Combobox(aba_consultas)
        especializacao_cb.grid(row=2, column=1, padx=5, pady=5)

        tk.Label(aba_consultas, text="Data da Consulta (DD/MM/AAAA):", bg="white").grid(row=3, column=0, padx=5, pady=5, sticky=tk.W)
        data_consulta_entry = tk.Entry(aba_consultas)
        data_consulta_entry.grid(row=3, column=1, padx=5, pady=5)

        tk.Label(aba_consultas, text="Horário (HH:MM:SS):", bg="white").grid(row=4, column=0, padx=5, pady=5, sticky=tk.W)
        horario_entry = tk.Entry(aba_consultas)
        horario_entry.grid(row=4, column=1, padx=5, pady=5)

        botao_marcar = tk.Button(aba_consultas, text="Marcar Consulta", bg="green", fg="white", command=self.marcar_consulta)
        botao_marcar.grid(row=5, column=0, padx=5, pady=5)
        botao_limpar_consulta = tk.Button(aba_consultas, text="Limpar", bg="red", fg="white", command=self.limpar_campos_consulta)
        botao_limpar_consulta.grid(row=5, column=1, padx=5, pady=5)

        # Tabela para exibir consultas
        tabela_consultas = ttk.Treeview(aba_consultas, columns=("Paciente", "Sintomas", "Especialização", "Data", "Hora"), show="headings")
        tabela_consultas.heading("Paciente", text="Paciente")
        tabela_consultas.heading("Sintomas", text="Sintomas")
        tabela_consultas.heading("Especialização", text="Especialização")
        tabela_consultas.heading("Data", text="Data")
        tabela_consultas.heading("Hora", text="Hora")
        tabela_consultas.grid(row=6, column=0, columnspan=2, padx=5, pady=5)

    # Funções de ação dos botões
    def buscar_consulta(self):
        print("Buscar consulta")
        
    def limpar_busca(self):
        print("Limpar busca")

    def mostrar_consultas_hoje(self):
        print("Mostrar consultas de hoje")

    def mostrar_todas_as_consultas(self):
        print("Mostrar todas as consultas")

    def excluir_todas_as_consultas(self):
        print("Excluir todas as consultas")

    def excluir_historico_hoje(self):
        print("Excluir histórico de hoje")
        
    def marcar_consulta(self):
        print("Marcar consulta")

    def limpar_campos_consulta(self):
        print("Limpar campos de consulta")
