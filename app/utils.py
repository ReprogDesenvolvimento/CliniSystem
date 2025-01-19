# Este arquivo contém funções utilitárias, como manipulação do banco de dados e centralização de janelas em Tkinter.

import sqlite3 # Biblioteca para conexão com bancos de dados SQLite.
from datetime import datetime # Biblioteca para manipulação de datas e horas.

# Caminho para o banco de dados.
db_path = "app/database/clinica.db"

#Manipulação tkinter
def centralizar_janela(janela, largura_janela, altura_janela):
    largura_tela = janela.winfo_screenwidth()  # Largura total da tela.
    altura_tela = janela.winfo_screenheight()  # Altura total da tela.
    pos_x = (largura_tela - largura_janela) // 2  # Cálculo da posição horizontal.
    pos_y = (altura_tela - altura_janela) // 2  # Cálculo da posição vertical.
    janela.geometry(f"{largura_janela}x{altura_janela}+{pos_x}+{pos_y}")


#Manipulação do Banco de Dados
def insert_paciente(nome, data_nasc, cpf, telefone, endereco):
    conn = sqlite3.connect(db_path)# Conexão com o banco de dados.
    cursor = conn.cursor()

    # Convertendo para um objeto datetime
    data_obj = datetime.strptime(data_nasc, "%d-%m-%Y")
    # Convertendo para o formato yyyy-mm-dd
    data_formatada = data_obj.strftime("%Y-%m-%d")

    cursor.execute("INSERT INTO pacientes (nome, data_nasc, cpf, telefone, endereco) VALUES (?, ?, ?, ?, ?)", (nome, data_formatada, cpf, telefone, endereco))
    
    conn.commit()
    conn.close()

# Função para excluir um paciente pelo CPF
def delete_paciente(cpf):
    conn = sqlite3.connect(db_path)# Conecta ao banco de dados
    cursor = conn.cursor()# Cria um cursor para executar comandos SQL
    cursor.execute("DELETE FROM pacientes WHERE cpf = ?", (cpf,)) # Exclui o paciente com o CPF fornecido
    conn.commit()  # Confirma a exclusão
    conn.close()# Fecha a conexão com o banco de dados

# Função para obter os dados de um paciente pelo CPF
def get_paciente(cpf):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()# Cria um cursor para executar comandos SQL

    cursor.execute("SELECT * FROM pacientes WHERE cpf = ?", (cpf,))# Consulta o paciente com o CPF fornecido

    return cursor.fetchall()# Retorna todos os dados encontrados para o paciente

# Função para inserir um novo médico no banco de dados
def insert_medico(nome, especialidade, crm, telefone):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO medicos (nome, especialidade, crm, telefone) VALUES (?, ?, ?, ?, ?)", (nome, especialidade, crm, telefone))  # Insere os dados do médico
    conn.commit()
    conn.close()

# Função para excluir um médico pelo CRM
def delete_medico(crm):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM medicos WHERE crm = ?", (crm,))
    conn.commit()
    conn.close()

# Função para obter os dados de um médico pelo CRM
def get_medicos(crm):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM medicos WHERE crm = ?", (crm,))
    return cursor.fetchall() # Retorna todos os dados encontrados para o médico

# Função para inserir uma nova consulta no banco de dados
def insert_consulta(id_paciente, id_medico, data, horario):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
     # Insere os dados da consulta
    cursor.execute("INSERT INTO consultas (id_paciente, id_medico, data, horario) VALUES (?, ?, ?, ?)", (id_paciente, id_medico, data, horario))
    
    conn.commit()
    conn.close()

# Função para excluir uma consulta pelo ID
def delete_consulta(id):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
     # Exclui a consulta com o ID fornecido
    cursor.execute("DELETE FROM consultas WHERE id_consulta = ?", (id,))
    conn.commit()
    conn.close()

# Função para obter os dados de uma consulta pelo ID
def get_consulta(id):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM consultas WHERE id_consulta = ?", (id,))

    return cursor.fetchall()# Retorna todos os dados encontrados para a consulta

# Função para inserir uma nova nota fiscal no banco de dados
def insert_nota_fiscal(id_paciente, valor, data_emissao):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
     # Insere os dados da nota fiscal
    cursor.execute("INSERT INTO notas_fiscais (id_paciente, valor, data_emissao) VALUES (?, ?, ?, ?)", (id_paciente, valor, data_emissao))
    
    conn.commit()
    conn.close()