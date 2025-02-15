import tkinter as tk
from tkinter import ttk

# Função para sair do aplicativo
def sair():
    raiz.destroy()

# Criar a janela principal
raiz = tk.Tk()
raiz.title("Sistema de Gestão Hospitalar | CliniSystem")
raiz.geometry("1200x700")
raiz.state("zoomed")

# Cabeçalho superior
cabecalho = tk.Frame(raiz, bg="navy", height=50)
cabecalho.pack(fill=tk.X)
titulo = tk.Label(cabecalho, text="Sistema de Gestão Hospitalar | CliniSystem", bg="navy", fg="white", font=("Arial", 16, "bold"))
titulo.pack(side=tk.LEFT, padx=20, pady=10)
logout_btn = tk.Button(cabecalho, text="Sair", bg="orange", fg="white", font=("Arial", 10, "bold"), command=sair)
logout_btn.pack(side=tk.RIGHT, padx=20, pady=10)

# Menu lateral
menu_frame = tk.Frame(raiz, bg="lightgray", width=180)
menu_frame.pack(side=tk.LEFT, fill=tk.Y)
menu_botoes = ["Início", "Médico", "Paciente", "Consulta", "Sair"]
for texto_botao in menu_botoes:
    comando = sair if texto_botao == "Sair" else None
    btn = tk.Button(menu_frame, text=texto_botao, font=("Arial", 12), bg="white", relief=tk.GROOVE, height=2)
    btn.pack(fill=tk.X, pady=5, padx=10)

# Dashboard principal
dashboard_frame = tk.Frame(raiz, bg="white")
dashboard_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=10, pady=10)

# Painéis do Dashboard
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

# Tabela de "Consultas de Hoje"
appointment_frame = tk.Frame(dashboard_frame, bg="white")
appointment_frame.pack(fill=tk.BOTH, expand=True, pady=10)

table_label = tk.Label(appointment_frame, text="Consultas de Hoje", font=("Arial", 12, "bold"), bg="white")
table_label.pack(anchor=tk.W)

colunas = ["ID Paciente", "Nome Paciente", "Contato", "Sintomas", "Especialidade", "Médico"]
table = ttk.Treeview(appointment_frame, columns=colunas, show="headings", height=5)

for col in colunas:
    table.heading(col, text=col)
    table.column(col, anchor=tk.CENTER, width=120)

table.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Barra de rolagem para a tabela
scrollbar = ttk.Scrollbar(appointment_frame, orient=tk.VERTICAL, command=table.yview)
table.configure(yscrollcommand=scrollbar.set)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Alterar Senha
password_frame = tk.Frame(dashboard_frame, bg="white")
password_frame.pack(fill=tk.X, pady=10)

password_label = tk.Label(password_frame, text="Alterar Senha", font=("Arial", 12, "bold"), bg="white")
password_label.pack(anchor=tk.W)

campos = ["Usuário", "Senha Atual", "Nova Senha"]
for campo in campos:
    label = tk.Label(password_frame, text=campo, bg="white", font=("Arial", 10))
    label.pack(anchor=tk.W)
    entrada = tk.Entry(password_frame, show="*" if "Senha" in campo else None, font=("Arial", 10))
    entrada.pack(fill=tk.X, pady=2)

alterar_senha_btn = tk.Button(password_frame, text="Alterar Senha", bg="blue", fg="white", font=("Arial", 10))
alterar_senha_btn.pack(pady=5)

# Rodar a aplicação
raiz.mainloop()
