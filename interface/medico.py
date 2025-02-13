import tkinter as tk
from tkinter import ttk

# Função para sair do aplicativo
def sair():
    raiz.destroy()

# Criar a janela principal
raiz = tk.Tk()
raiz.title("Sistema de Gestão Hospitalar | CliniSystem")
raiz.geometry("1024x768")
raiz.resizable(True, True)

# Título superior
cabecalho = tk.Label(raiz, text="Sistema de Gestão Hospitalar | CliniSystem", bg="navy", fg="white", font=("Arial", 14, "bold"))
cabecalho.pack(fill=tk.X)

# Menu lateral
menu_lateral = tk.Frame(raiz, bg="lightgray", width=200)
menu_lateral.pack(side=tk.LEFT, fill=tk.Y)

botoes_menu = ["Início", "Médico", "Paciente", "Consulta", "Sair"]
for texto in botoes_menu:
    comando = sair if texto == "Sair" else None
    botao = tk.Button(menu_lateral, text=texto, font=("Arial", 12), bg="white", relief=tk.RIDGE, command=comando)
    botao.pack(fill=tk.X, pady=5, padx=10)

# Área principal para Gerenciar Médicos e Especializações
tela_principal = tk.Frame(raiz, bg="white")
tela_principal.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=10, pady=10)

# Aba de gerenciamento
abas = ttk.Notebook(tela_principal)
abas.pack(fill=tk.BOTH, expand=True)

# ==== GERENCIAR MÉDICOS ====
aba_medicos = tk.Frame(abas, bg="white")
abas.add(aba_medicos, text="Gerenciar Médicos")

tk.Label(aba_medicos, text="Especialização:", bg="white").grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
especializacao_cb = ttk.Combobox(aba_medicos)
especializacao_cb.grid(row=0, column=1, padx=5, pady=5)

tk.Label(aba_medicos, text="Nome:", bg="white").grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
nome_entry = tk.Entry(aba_medicos)
nome_entry.grid(row=1, column=1, padx=5, pady=5)

tk.Label(aba_medicos, text="Taxa de Consulta:", bg="white").grid(row=2, column=0, padx=5, pady=5, sticky=tk.W)
consulta_entry = tk.Entry(aba_medicos)
consulta_entry.grid(row=2, column=1, padx=5, pady=5)

tk.Label(aba_medicos, text="Contato:", bg="white").grid(row=3, column=0, padx=5, pady=5, sticky=tk.W)
contato_entry = tk.Entry(aba_medicos)
contato_entry.grid(row=3, column=1, padx=5, pady=5)

tk.Label(aba_medicos, text="E-mail:", bg="white").grid(row=4, column=0, padx=5, pady=5, sticky=tk.W)
email_entry = tk.Entry(aba_medicos)
email_entry.grid(row=4, column=1, padx=5, pady=5)

botao_adicionar = tk.Button(aba_medicos, text="Adicionar", bg="blue", fg="white")
botao_adicionar.grid(row=5, column=0, padx=5, pady=5)
botao_limpar = tk.Button(aba_medicos, text="Limpar", bg="red", fg="white")
botao_limpar.grid(row=5, column=1, padx=5, pady=5)

# Tabela para exibir médicos
tabela_medicos = ttk.Treeview(aba_medicos, columns=("Nome", "Especialização", "Taxa", "Contato", "E-mail"), show="headings")
tabela_medicos.heading("Nome", text="Nome")
tabela_medicos.heading("Especialização", text="Especialização")
tabela_medicos.heading("Taxa", text="Taxa de Consulta")
tabela_medicos.heading("Contato", text="Contato")
tabela_medicos.heading("E-mail", text="E-mail")
tabela_medicos.grid(row=6, column=0, columnspan=2, padx=5, pady=5)

# ==== GERENCIAR ESPECIALIZAÇÕES ====
aba_especializacoes = tk.Frame(abas, bg="white")
abas.add(aba_especializacoes, text="Gerenciar Especializações")

tk.Label(aba_especializacoes, text="Gerenciar Especializações", bg="white", font=("Arial", 12, "bold")).grid(row=0, column=0, columnspan=2, padx=5, pady=5)
tk.Label(aba_especializacoes, text="Digite a Especialização", bg="white").grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
especializacao_entry = tk.Entry(aba_especializacoes, width=40)
especializacao_entry.grid(row=1, column=1, padx=5, pady=5)

botao_adicionar_esp = tk.Button(aba_especializacoes, text="Adicionar", bg="blue", fg="white", width=15)
botao_adicionar_esp.grid(row=2, column=0, padx=5, pady=5)
botao_limpar_esp = tk.Button(aba_especializacoes, text="Limpar", bg="red", fg="white", width=15)
botao_limpar_esp.grid(row=2, column=1, padx=5, pady=5)

# Área de pesquisa
tk.Label(aba_especializacoes, text="Pesquisar", bg="white").grid(row=3, column=0, padx=5, pady=5, sticky=tk.W)
entrada_pesquisa = tk.Entry(aba_especializacoes)
entrada_pesquisa.grid(row=3, column=1, padx=5, pady=5)
botao_pesquisar = tk.Button(aba_especializacoes, text="Pesquisar", bg="blue", fg="white")
botao_pesquisar.grid(row=3, column=2, padx=5, pady=5)

# Tabela para exibir especializações
tabela_especializacoes = ttk.Treeview(aba_especializacoes, columns=("ID", "Especialização", "Data de Criação", "Data de Atualização"), show="headings")
tabela_especializacoes.heading("ID", text="ID")
tabela_especializacoes.heading("Especialização", text="Especialização")
tabela_especializacoes.heading("Data de Criação", text="Data de Criação")
tabela_especializacoes.heading("Data de Atualização", text="Data de Atualização")
tabela_especializacoes.grid(row=4, column=0, columnspan=3, padx=5, pady=5)

raiz.mainloop()
