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

# Painel principal
main_frame = tk.Frame(raiz, bg="white")
main_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=10, pady=10)

# Seção de pesquisa
tk.Label(main_frame, text="Buscar Consulta", font=("Arial", 12, "bold"), bg="white").grid(row=0, column=0, columnspan=4, sticky="w", pady=5)

tk.Label(main_frame, text="Nome do Paciente:", bg="white", font=("Arial", 10)).grid(row=1, column=0, sticky="w")
entry_nome = tk.Entry(main_frame, width=30)
entry_nome.grid(row=1, column=1, padx=5, pady=5, sticky="ew")

btn_search = tk.Button(main_frame, text="Buscar", bg="blue", fg="white", font=("Arial", 10, "bold"))
btn_search.grid(row=1, column=2, padx=5, pady=5)
btn_clear = tk.Button(main_frame, text="Limpar", bg="gray", fg="white", font=("Arial", 10, "bold"))
btn_clear.grid(row=1, column=3, padx=5, pady=5)

# Seção de botões de ações
tk.Label(main_frame, text="Menu de Consultas", font=("Arial", 12, "bold"), bg="white").grid(row=2, column=0, columnspan=4, sticky="w", pady=5)

btn_today = tk.Button(main_frame, text="Mostrar Consultas de Hoje", bg="blue", fg="white", font=("Arial", 10, "bold"))
btn_today.grid(row=3, column=0, padx=5, pady=5)
btn_all = tk.Button(main_frame, text="Mostrar Todas as Consultas", bg="green", fg="white", font=("Arial", 10, "bold"))
btn_all.grid(row=3, column=1, padx=5, pady=5)
btn_delete_all = tk.Button(main_frame, text="Excluir Todas", bg="red", fg="white", font=("Arial", 10, "bold"))
btn_delete_all.grid(row=3, column=2, padx=5, pady=5)
btn_delete_today = tk.Button(main_frame, text="Excluir Histórico de Hoje", bg="gray", fg="white", font=("Arial", 10, "bold"))
btn_delete_today.grid(row=3, column=3, padx=5, pady=5)

# Seção da Tabela
tabela_frame = tk.Frame(main_frame)
tabela_frame.grid(row=4, column=0, columnspan=4, pady=10, sticky="nsew")

colunas = ["ID", "Nome", "Contato", "Sintomas", "Especialização", "Médico", "Data Consulta", "Hora"]
tabela_pacientes = ttk.Treeview(tabela_frame, columns=colunas, show="headings")

for col in colunas:
    tabela_pacientes.heading(col, text=col)
    tabela_pacientes.column(col, width=140, anchor="center")

tabela_pacientes.pack(fill=tk.BOTH, expand=True)

raiz.mainloop()