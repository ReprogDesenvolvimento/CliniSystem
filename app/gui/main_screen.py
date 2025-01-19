# Este arquivo contém as interfaces gráficas do sistema de gerenciamento da clínica.

import tkinter as tk  # Biblioteca para a criação de interfaces gráficas.
from tkinter import messagebox  # Módulo para exibição de caixas de mensagem.
import sqlite3  # Biblioteca para conexão com o banco de dados SQLite.

from app.utils import *  # Importa funções utilitárias, incluindo operações no banco de dados.
from app.classes.notafiscal import notafiscal  # Classe para manipulação de notas fiscais.

# Função para emitir nota fiscal de uma consulta
def emitir_nota_fiscal(id_paciente, valor, data_emissao):
    #Cria a nota fiscal e emite
    nota = notafiscal(id_nota=1, id_paciente=id_paciente, valor=valor, data_emissao=data_emissao)
    nota.emitir()  # Emitir a nota fiscal após cadastrar a consulta


# Função para cadastrar um paciente no sistema.
def cadastrar_paciente():
    def salvar():
        # Captura os dados inseridos pelo usuário na interface.
        nome = nome_var.get()
        data_nasc = data_nasc_var.get()
        cpf = cpf_var.get()
        telefone = telefone_var.get()
        endereco = endereco_var.get()

        try:
            # Insere os dados no banco de dados utilizando uma função utilitária.
            insert_paciente(nome, data_nasc, cpf, telefone, endereco)
            messagebox.showinfo("Sucesso", "Paciente cadastrado com sucesso!")
            janela.destroy()  # Fecha a janela após salvar os dados.
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao cadastrar paciente: {e}")

    # Cria a janela de cadastro de pacientes.
    janela = tk.Toplevel()
    janela.title("Cadastrar Paciente")

    tk.Label(janela, text="Nome").grid(row=0, column=0)
    nome_var = tk.StringVar()
    tk.Entry(janela, textvariable=nome_var).grid(row=0, column=1)

    tk.Label(janela, text="Data nascimento").grid(row=1, column=0)
    data_nasc_var = tk.StringVar()
    tk.Entry(janela, textvariable=data_nasc_var).grid(row=1, column=1)

    tk.Label(janela, text="CPF").grid(row=2, column=0)
    cpf_var = tk.StringVar()
    tk.Entry(janela, textvariable=cpf_var).grid(row=2, column=1)

    tk.Label(janela, text="Telefone").grid(row=3, column=0)
    telefone_var = tk.StringVar()
    tk.Entry(janela, textvariable=telefone_var).grid(row=3, column=1)

    tk.Label(janela, text="Endereço").grid(row=4, column=0)
    endereco_var = tk.StringVar()
    tk.Entry(janela, textvariable=endereco_var).grid(row=4, column=1)

    tk.Button(janela, text="Salvar", command=salvar).grid(row=5, columnspan=2)

# Função para remover um paciente do sistema.
def remover_paciente():
    def remover():
        cpf = cpf_var.get()# Captura o CPF informado pelo usuário.

        try:
            delete_paciente(cpf)# Remove o paciente utilizando a função utilitária.
            messagebox.showinfo("Sucesso", "Paciente removido com sucesso!")
            janela.destroy()# Fecha a janela atual. A janela referenciada por 'janela' é destruída.
        # Caso ocorra algum erro durante a execução do bloco anterior, captura a exceção e exibe uma mensagem de erro
        except Exception as e:
            # Exibe uma janela de mensagem de erro informando o problema ocorrido.
            messagebox.showerror("Erro", f"Erro ao remover paciente: {e}")

    # Cria a janela de remoção de pacientes.
    # Cria uma nova janela do tipo Toplevel, que é uma janela secundária (geralmente usada como uma nova tela ou diálogo).
    janela = tk.Toplevel()
    janela.title("Remover Paciente")

    tk.Label(janela, text="CPF").grid(row=0, column=0)
    cpf_var = tk.StringVar()
    tk.Entry(janela, textvariable=cpf_var).grid(row=0, column=1)
    
    tk.Button(janela, text="Remover", command=remover).grid(row=1, columnspan=2)

# Função para pesquisar informações de um paciente.
def pesquisar_paciente():
    def resultado():
        cpf = cpf_var.get()# Captura o CPF informado pelo usuário.

        try:
            paciente = get_paciente(cpf)# Busca o paciente no banco de dados.
            info = tk.Toplevel() # Cria uma nova janela para exibir as informações.
            
            # Exibe os dados do paciente na interface.
            nome = paciente[0][1]# Atribui à variável 'nome' o valor presente na segunda posição (índice 1) da sublista do primeiro paciente.
            data_nasc = paciente[0][2]# Atribui à variável 'data_nasc' o valor presente na terceira posição (índice 2) da sublista do primeiro paciente.
            telefone = paciente[0][4]# Atribui à variável 'telefone' o valor presente na quinta posição (índice 4) da sublista do primeiro paciente.
            endereco = paciente[0][5]# Atribui à variável 'endereco' o valor presente na sexta posição (índice 5) da sublista do primeiro paciente.

            tk.Label(info, text="Nome: ").grid(row=0, column=0)
            tk.Label(info, text=nome).grid(row=0, column=1)

            tk.Label(info, text="Data nascimento: ").grid(row=1, column=0)
            tk.Label(info, text=data_nasc).grid(row=1, column=1)

            tk.Label(info, text="CPF: ").grid(row=2, column=0)
            tk.Label(info, text=cpf).grid(row=2, column=1)

            tk.Label(info, text="telefone: ").grid(row=3, column=0)
            tk.Label(info, text=telefone).grid(row=3, column=1)

            tk.Label(info, text="endereço: ").grid(row=3, column=0)
            tk.Label(info, text=endereco).grid(row=3, column=1)

            janela.destroy()
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao procurar paciente: {e}")
    
    # Cria a janela de pesquisa de pacientes.
    janela = tk.Toplevel()
    janela.title("Pacientes")

    tk.Label(janela, text="CPF").grid(row=0, column=0)
    cpf_var = tk.StringVar()# Cria uma variável de controle (cpf_var) para armazenar o valor inserido no campo de entrada.
    tk.Entry(janela, textvariable=cpf_var).grid(row=0, column=1)
    # Cria e posiciona um botão (Button) na janela, com o texto "procurar".
    tk.Button(janela, text="procurar", command=resultado).grid(row=1, columnspan=2)

# Funções adicionais, como cadastrar médicos, consultas, etc., seguem a mesma estrutura.
def cadastrar_medico():
    def salvar():
        nome = nome_var.get()
        especialidade = especialidade_var.get()
        crm = crm_var.get()
        telefone = telefone_var.get()

        try:
            conn = sqlite3.connect("clinica.db")
            cursor = conn.cursor()
            cursor.execute("INSERT INTO medicos (nome, especialidade, crm, telefone) VALUES (?, ?, ?, ?)",
                           (nome, especialidade, crm, telefone))
            conn.commit()
            conn.close()
            messagebox.showinfo("Sucesso", "Médico cadastrado com sucesso!")
            janela.destroy()
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao cadastrar médico: {e}")

    janela = tk.Toplevel()
    janela.title("Cadastrar Médico")

    tk.Label(janela, text="Nome").grid(row=0, column=0)
    nome_var = tk.StringVar()
    tk.Entry(janela, textvariable=nome_var).grid(row=0, column=1)

    tk.Label(janela, text="Especialidade").grid(row=1, column=0)
    especialidade_var = tk.StringVar()
    tk.Entry(janela, textvariable=especialidade_var).grid(row=1, column=1)

    tk.Label(janela, text="CRM").grid(row=2, column=0)
    crm_var = tk.StringVar()
    tk.Entry(janela, textvariable=crm_var).grid(row=2, column=1)

    tk.Label(janela, text="Telefone").grid(row=3, column=0)
    telefone_var = tk.StringVar()
    tk.Entry(janela, textvariable=telefone_var).grid(row=3, column=1)

    tk.Button(janela, text="Salvar", command=salvar).grid(row=4, columnspan=2)

def remover_medico():
    def remover():
        crm = crm_var.get()

        try:
            delete_medico(crm)
            messagebox.showinfo("Sucesso", "Médico removido com sucesso!")
            janela.destroy()
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao remover médico: {e}")

    janela = tk.Toplevel()
    janela.title("Remover Médico")

    tk.Label(janela, text="CRM").grid(row=0, column=0)
    crm_var = tk.StringVar()
    tk.Entry(janela, textvariable=crm_var).grid(row=0, column=1)
    
    tk.Button(janela, text="Remover", command=remover).grid(row=1, columnspan=2)

def pesquisar_medico():
    def resultado():
        crm = crm_var.get()

        try:
            medico = get_medicos(crm)
            info = tk.Toplevel()
            
            nome = medico[0][1]
            especialidade = medico[0][2]
            telefone = medico[0][4]

            tk.Label(info, text="Nome: ").grid(row=0, column=0)
            tk.Label(info, text=nome).grid(row=0, column=1)

            tk.Label(info, text="Especialidade: ").grid(row=1, column=0)
            tk.Label(info, text=especialidade).grid(row=1, column=1)

            tk.Label(info, text="CRM: ").grid(row=2, column=0)
            tk.Label(info, text=crm).grid(row=2, column=1)

            tk.Label(info, text="telefone: ").grid(row=3, column=0)
            tk.Label(info, text=telefone).grid(row=3, column=1)

            janela.destroy()
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao procurar médico: {e}")
    
    janela = tk.Toplevel()
    janela.title("Medicos")

    tk.Label(janela, text="CRM").grid(row=0, column=0)
    crm_var = tk.StringVar()
    tk.Entry(janela, textvariable=crm_var).grid(row=0, column=1)
    
    tk.Button(janela, text="procurar", command=resultado).grid(row=1, columnspan=2)

def cadastrar_consulta():
    def salvar():
        id_paciente = id_paciente_var.get()
        id_medico = id_medico_var.get()
        data = data_var.get()
        horario = horario_var.get()

        try:
            insert_consulta(id_paciente, id_medico, data, horario)
            emitir_nota_fiscal(id_paciente, 300.00, data)  #valor fixo para a consulta

            messagebox.showinfo("Sucesso", "Consulta cadastrada com sucesso!")
            janela.destroy()
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao cadastrar consulta: {e}")

    janela = tk.Toplevel()
    janela.title("Cadastrar Consulta")

    tk.Label(janela, text="ID Paciente").grid(row=0, column=0)
    id_paciente_var = tk.StringVar()
    tk.Entry(janela, textvariable=id_paciente_var).grid(row=0, column=1)

    tk.Label(janela, text="ID Médico").grid(row=1, column=0)
    id_medico_var = tk.StringVar()
    tk.Entry(janela, textvariable=id_medico_var).grid(row=1, column=1)

    tk.Label(janela, text="Data").grid(row=2, column=0)
    data_var = tk.StringVar()
    tk.Entry(janela, textvariable=data_var).grid(row=2, column=1)

    tk.Label(janela, text="Horário").grid(row=3, column=0)
    horario_var = tk.StringVar()
    tk.Entry(janela, textvariable=horario_var).grid(row=3, column=1)

    tk.Button(janela, text="Salvar", command=salvar).grid(row=4, columnspan=2)

def remover_consulta():
    def remover():
        id = id_var.get()

        try:
            delete_consulta(id)
            messagebox.showinfo("Sucesso", "Consulta removido com sucesso!")
            janela.destroy()
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao remover consulta: {e}")

    janela = tk.Toplevel();
    janela.title("Remover Consulta")

    tk.Label(janela, text="ID Consulta").grid(row=0, column=0)
    id_var = tk.StringVar()
    tk.Entry(janela, textvariable=id_var).grid(row=0, column=1)
    
    tk.Button(janela, text="Remover", command=remover).grid(row=1, columnspan=2)

def pesquisar_consulta():
    def resultado():
        id_consulta = id_var.get()

        try:
            consulta = get_consulta(id_consulta)
            info = tk.Toplevel()

            id_paciente = consulta[0][1]
            id_medico = consulta[0][2]
            data = consulta[0][3]
            horario = consulta[0][4]

            tk.Label(info, text="ID paciente: ").grid(row=0, column=0)
            tk.Label(info, text=id_paciente).grid(row=0, column=1)

            tk.Label(info, text="ID médico: ").grid(row=1, column=0)
            tk.Label(info, text=id_medico).grid(row=1, column=1)

            tk.Label(info, text="Data: ").grid(row=2, column=0)
            tk.Label(info, text=data).grid(row=2, column=1)

            tk.Label(info, text="Hora: ").grid(row=3, column=0)
            tk.Label(info, text=horario).grid(row=3, column=1)

            janela.destroy()
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao pesquisar consulta: {e}")
    
    janela = tk.Toplevel();
    janela.title("Consultas")

    tk.Label(janela, text="ID Consulta").grid(row=0, column=0)
    id_var = tk.StringVar()
    tk.Entry(janela, textvariable=id_var).grid(row=0, column=1)
    
    tk.Button(janela, text="Pesquisar", command=resultado).grid(row=1, columnspan=2)

# Função principal que cria a janela principal do sistema.   
def MainWindow():
    root = tk.Tk()

    centralizar_janela(root, 800, 600)  # Centraliza a janela principal.
    root.option_add("*Font", "Helvetica 16")  # Define a fonte padrão.
    root.title("Sistema de Gerenciamento de Clínica")
    
    # Botões principais para acesso às funcionalidades do sistema.
    tk.Label(root, text="Bem-vindo ao Sistema!").pack()

    tk.Button(root, text="Cadastrar Paciente", command=cadastrar_paciente).pack(pady=5)
    tk.Button(root, text="Remover Paciente", command=remover_paciente).pack(pady=5)
    tk.Button(root, text="Procurar Paciente", command=pesquisar_paciente).pack(pady=5)

    tk.Button(root, text="Cadastrar Médico", command=cadastrar_medico).pack(pady=5)
    tk.Button(root, text="Remover Médico", command=remover_medico).pack(pady=5)
    tk.Button(root, text="Procurar Médico", command=pesquisar_medico).pack(pady=5)
    
    tk.Button(root, text="Cadastrar Consulta", command=cadastrar_consulta).pack(pady=5)
    tk.Button(root, text="Remover Consulta", command=remover_consulta).pack(pady=5)
    tk.Button(root, text="Procurar Consulta", command=pesquisar_consulta).pack(pady=5)
    
    #Repete as configurações toda vez que a janela principal é atualizada.
    root.mainloop()