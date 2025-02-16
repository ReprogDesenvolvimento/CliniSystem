import tkinter as tk
from tkinter import ttk
from app.gui.controller import CliniSystemController
from app.gui.medico import MedicoWindow
from app.gui.paciente import PacienteWindow
from app.gui.consultas import ConsultaWindow

class Backend:
    """Classe para gerenciar a lógica do sistema."""
    
    def __init__(self):
        self.dados_pacientes = []

    def obter_consultas(self):
        """Retorna uma lista de consultas de hoje."""
        return [
            (1, "João Silva", "(11) 99999-9999", "Febre", "Clínico Geral", "Dr. Pedro"),
            (2, "Maria Oliveira", "(21) 98888-8888", "Dor de cabeça", "Neurologista", "Dra. Ana")
        ]

    def alterar_senha(self, usuario, senha_atual, nova_senha):
        """Simula a alteração de senha."""
        print(f"Alterando senha para o usuário: {usuario}")
        return True

class Interface:
    """Classe para gerenciar a interface gráfica."""

    def __init__(self):
        self.raiz = tk.Tk()
        self.backend = Backend()
        self.raiz.title("Sistema de Gestão Hospitalar | CliniSystem")
        self.raiz.geometry("1200x700")
        self.raiz.state("zoomed")

        self.criar_cabecalho()
        self.criar_menu_lateral()
        self.criar_dashboard()

        self.raiz.mainloop()

    def sair(self):
        """Fecha a aplicação."""
        self.raiz.destroy()

    def criar_cabecalho(self):
        cabecalho = tk.Frame(self.raiz, bg="navy", height=50)
        cabecalho.pack(fill=tk.X)

        titulo = tk.Label(cabecalho, text="Sistema de Gestão Hospitalar | CliniSystem", bg="navy", fg="white", font=("Arial", 16, "bold"))
        titulo.pack(side=tk.LEFT, padx=20, pady=10)

        logout_btn = tk.Button(cabecalho, text="Sair", bg="orange", fg="white", font=("Arial", 10, "bold"), command=self.sair)
        logout_btn.pack(side=tk.RIGHT, padx=20, pady=10)
    
        self.controller = CliniSystemController()

    def abrir_medico(self):
        """Abre a janela de médicos."""
        MedicoWindow(self.controller)

    def abrir_paciente(self):
        """Abre a janela de pacientes."""
        PacienteWindow(self.controller)

    def abrir_consultas(self):
        """Abre a janela de consultas."""
        ConsultaWindow(self.controller)

    def criar_menu_lateral(self):
        menu_frame = tk.Frame(self.raiz, bg="lightgray", width=180)
        menu_frame.pack(side=tk.LEFT, fill=tk.Y)

        botoes = [
            ("Médico", self.abrir_medico),
            ("Paciente", self.abrir_paciente),
            ("Consulta", self.abrir_consultas),
            ("Sair", self.sair)
        ]

        for texto, comando in botoes:
            btn = tk.Button(menu_frame, text=texto, font=("Arial", 12), bg="white", relief=tk.GROOVE, height=2, command=comando)
            btn.pack(fill=tk.X, pady=5, padx=10)

    def criar_dashboard(self):
        dashboard_frame = tk.Frame(self.raiz, bg="white")
        dashboard_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=10, pady=10)

        paineis = [
            ("Especializações", "orange"),
            ("Médicos", "blue"),
            ("Pacientes", "yellow"),
            ("Consultas de Hoje", "green")
        ]

        panel_frame = tk.Frame(dashboard_frame, bg="white")
        panel_frame.pack(pady=10)

        for texto_painel, cor in paineis:
            painel = tk.Label(panel_frame, text=f"{texto_painel}\n(0)", bg=cor, fg="white", font=("Arial", 14, "bold"), width=20, height=3, relief=tk.RIDGE)
            painel.pack(side=tk.LEFT, padx=5, pady=5)

        self.criar_tabela_consultas(dashboard_frame)
        self.criar_alterar_senha(dashboard_frame)

    def criar_tabela_consultas(self, frame_pai):
        appointment_frame = tk.Frame(frame_pai, bg="white")
        appointment_frame.pack(fill=tk.BOTH, expand=True, pady=10)

        table_label = tk.Label(appointment_frame, text="Consultas de Hoje", font=("Arial", 12, "bold"), bg="white")
        table_label.pack(anchor=tk.W)

        colunas = ["ID Paciente", "Nome Paciente", "Contato", "Sintomas", "Especialidade", "Médico"]
        table = ttk.Treeview(appointment_frame, columns=colunas, show="headings", height=5)

        for col in colunas:
            table.heading(col, text=col)
            table.column(col, anchor=tk.CENTER, width=120)

        for consulta in self.backend.obter_consultas():
            table.insert("", "end", values=consulta)

        table.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        scrollbar = ttk.Scrollbar(appointment_frame, orient=tk.VERTICAL, command=table.yview)
        table.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    def criar_alterar_senha(self, frame_pai):
        password_frame = tk.Frame(frame_pai, bg="white")
        password_frame.pack(fill=tk.X, pady=10)

        password_label = tk.Label(password_frame, text="Alterar Senha", font=("Arial", 12, "bold"), bg="white")
        password_label.pack(anchor=tk.W)

        self.entradas = {}
        campos = ["Usuário", "Senha Atual", "Nova Senha"]
        for campo in campos:
            label = tk.Label(password_frame, text=campo, bg="white", font=("Arial", 10))
            label.pack(anchor=tk.W)
            entrada = tk.Entry(password_frame, show="*" if "Senha" in campo else None, font=("Arial", 10))
            entrada.pack(fill=tk.X, pady=2)
            self.entradas[campo] = entrada

        alterar_senha_btn = tk.Button(password_frame, text="Alterar Senha", bg="blue", fg="white", font=("Arial", 10), command=self.alterar_senha)
        alterar_senha_btn.pack(pady=5)

    def alterar_senha(self):
        usuario = self.entradas["Usuário"].get()
        senha_atual = self.entradas["Senha Atual"].get()
        nova_senha = self.entradas["Nova Senha"].get()

        if self.backend.alterar_senha(usuario, senha_atual, nova_senha):
            print("Senha alterada com sucesso!")
