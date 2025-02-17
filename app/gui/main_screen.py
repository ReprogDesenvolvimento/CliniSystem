import tkinter as tk
from tkinter import ttk
import sqlite3
from tkinter import messagebox

from app.gui.medico import MedicoWindow
from app.gui.paciente import PacienteWindow
from app.gui.consultas import ConsultaWindow

class Backend:
    """Classe para gerenciar a lógica do sistema."""

    def __init__(self):
        self.dados_pacientes = []

    def obter_consultas(self):
        conn = sqlite3.connect("app/database/clinica.db")
        cursor = conn.cursor()

        try:
            cursor.execute("SELECT consultas.id_consulta, pacientes.nome, medicos.nome, consultas.data, consultas.horario FROM consultas JOIN pacientes ON consultas.id_paciente = pacientes.id_paciente JOIN medicos ON consultas.id_medico = medicos.id_medico")
            registros = cursor.fetchall()
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao acessar o banco de dados: {e}")

        conn.close()

        return registros

class Interface:
    """Classe para gerenciar a interface gráfica."""

    def __init__(self):
        self.raiz = tk.Tk()
        self.backend = Backend()
        self.raiz.title("Sistema de Gestão Hospitalar | CliniSystem")
        self.raiz.geometry("1200x700")

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

    def abrir_medico(self):
        """Abre a janela de médicos."""
        MedicoWindow()

    def abrir_paciente(self):
        """Abre a janela de pacientes."""
        PacienteWindow()

    def abrir_consultas(self):
        """Abre a janela de consultas."""
        ConsultaWindow()

    def criar_menu_lateral(self):
        menu_frame = tk.Frame(self.raiz, bg="lightgray", width=180)
        menu_frame.pack(side=tk.LEFT, fill=tk.Y)

        botoes = [
            ("Médico", self.abrir_medico),
            ("Paciente", self.abrir_paciente),
            ("Consulta", self.abrir_consultas)
        ]

        for texto, comando in botoes:
            btn = tk.Button(menu_frame, text=texto, font=("Arial", 12), bg="white", relief=tk.GROOVE, height=2, command=comando)
            btn.pack(fill=tk.X, pady=5, padx=10)

    def criar_dashboard(self):
        dashboard_frame = tk.Frame(self.raiz, bg="white")
        dashboard_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=10, pady=10)

        paineis = [
            ["Médicos", "blue"],
            ["Pacientes", "red"],
            ["Consultas", "green"]
        ]

        panel_frame = tk.Frame(dashboard_frame, bg="white")
        panel_frame.pack(pady=10)

        for texto_painel, cor in paineis:
            conn = sqlite3.connect("app/database/clinica.db")
            cursor = conn.cursor()
            
            query = {
                "Médicos": "SELECT * FROM MEDICOS",
                "Pacientes": "SELECT * FROM PACIENTES",
                "Consultas": "SELECT * FROM CONSULTAS"
            }
            
            try:
                count = 0

                cursor.execute(query[texto_painel])
                registros = cursor.fetchall()
                for registro in registros:
                    count += 1
            except Exception as e:
                messagebox.showerror("Erro", f"Erro ao acessar o banco de dados: {e}")

            conn.close()
            painel = tk.Label(panel_frame, text=f"{texto_painel}\n{count}", bg=cor, fg="white", font=("Arial", 14, "bold"), width=25, height=3, relief=tk.RIDGE)
            painel.pack(side=tk.LEFT, padx=5, pady=5)

        self.criar_tabela_consultas(dashboard_frame)
    
    def criar_tabela_consultas(self, frame_pai):
        appointment_frame = tk.Frame(frame_pai, bg="white")
        appointment_frame.pack(fill=tk.BOTH, expand=True, pady=10)

        table_label = tk.Label(appointment_frame, text="Consultas", font=("Arial", 12, "bold"), bg="white")
        table_label.pack(anchor=tk.W)

        colunas = ["ID consulta", "Nome Paciente", "Nome Médico", "Data", "Horário"]
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
