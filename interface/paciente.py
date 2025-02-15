import tkinter as tk
from tkinter import ttk

# Função para sair do aplicativo
def sair():
    raiz.destroy()

# Criar a janela principal
raiz = tk.Tk()
raiz.title("Sistema de Gestão Hospitalar | CliniSystem")
raiz.geometry("1200x700")
raiz.state("zoomed")  # Abre em tela cheia

# Título superior
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

# Painel principal
main_frame = tk.Frame(raiz, bg="white")
main_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=10, pady=10)

# Configurar grid
for i in range(5):
    main_frame.grid_columnconfigure(i, weight=1)
main_frame.grid_rowconfigure(8, weight=1)

# Seção de detalhes do paciente
tk.Label(main_frame, text="Detalhes do Paciente", font=("Arial", 12, "bold"), bg="white").grid(row=0, column=0, columnspan=2, sticky="w", pady=5)

campos = ["Nome do Paciente:", "Gênero:", "Data de Nascimento:", "Contato:", "E-mail:"]
entradas = []
for i, campo in enumerate(campos):
    tk.Label(main_frame, text=campo, bg="white").grid(row=i+1, column=0, sticky="w", pady=5)
    entry = tk.Entry(main_frame, width=30)
    entry.grid(row=i+1, column=1, padx=5, pady=5, sticky="ew")
    entradas.append(entry)

genero_cb = ttk.Combobox(main_frame, values=["Masculino", "Feminino", "Outro"])
genero_cb.grid(row=2, column=1, padx=5, pady=5, sticky="ew")

# Campo de endereço antes dos botões
tk.Label(main_frame, text="Endereço:", bg="white").grid(row=6, column=0, sticky="w", pady=5)
endereco_entry = tk.Entry(main_frame, width=50)
endereco_entry.grid(row=6, column=1, columnspan=2, padx=5, pady=5, sticky="ew")

# Seção de consulta médica
tk.Label(main_frame, text="Marcar Consulta", font=("Arial", 12, "bold"), bg="white").grid(row=0, column=2, columnspan=2, sticky="w", pady=5)

tk.Label(main_frame, text="Sintomas:", bg="white").grid(row=1, column=2, sticky="w")
tk.Entry(main_frame, width=30).grid(row=1, column=3, padx=5, pady=5, sticky="ew")

tk.Label(main_frame, text="Especialização:", bg="white").grid(row=2, column=2, sticky="w")
especializacao_cb = ttk.Combobox(main_frame, values=["Cardiologista", "Dermatologista", "Neurologista"])
especializacao_cb.grid(row=2, column=3, padx=5, pady=5, sticky="ew")

tk.Label(main_frame, text="Data da Consulta (DD/MM/AAAA):", bg="white").grid(row=3, column=2, sticky="w")
tk.Entry(main_frame).grid(row=3, column=3, padx=5, pady=5, sticky="ew")

tk.Label(main_frame, text="Horário (HH:MM:SS):", bg="white").grid(row=4, column=2, sticky="w")
tk.Entry(main_frame).grid(row=4, column=3, padx=5, pady=5, sticky="ew")

# Botões de ação
botoes_frame = tk.Frame(main_frame, bg="white")
botoes_frame.grid(row=7, column=0, columnspan=4, pady=10, sticky="ew")

for texto, cor in zip(["Adicionar", "Atualizar", "Excluir", "Limpar"], ["blue", "green", "red", "gray"]):
    btn = tk.Button(botoes_frame, text=texto, bg=cor, fg="white", font=("Arial", 10, "bold"))
    btn.pack(side=tk.LEFT, padx=10, pady=5, expand=True, fill=tk.X)

# Tabela de pacientes
tabela_frame = tk.Frame(main_frame)
tabela_frame.grid(row=8, column=0, columnspan=4, pady=10, sticky="nsew")
colunas = ["ID", "Nome", "Gênero", "Data Nasc.", "Contato", "E-mail", "Endereço", "Sintomas", "Especialização", "Médico", "Data Consulta", "Hora"]
tabela_pacientes = ttk.Treeview(tabela_frame, columns=colunas, show="headings")
for col in colunas:
    tabela_pacientes.heading(col, text=col)
    tabela_pacientes.column(col, width=100, anchor="center")
tabela_pacientes.pack(fill=tk.BOTH, expand=True)

raiz.mainloop()

