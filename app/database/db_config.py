# Este arquivo é responsável por criar e configurar as tabelas do banco de dados SQLite para o sistema da clínica.

import sqlite3 # Biblioteca para manipulação do banco de dados SQLite.

def create_database():
    # Conecta ao banco de dados
    conn = sqlite3.connect("app/database/clinica.db")
    cursor = conn.cursor()
    
    # Cria a tabela 'pacientes' no banco de dados se ela não existir.
    # A tabela contém informações sobre os pacientes da clínica.
    #Adição cpf e substituição de idade por data de nascimento
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS pacientes (
        id_paciente INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        data_nasc DATE NOT NULL,
        cpf VARCHAR(11) NOT NULL UNIQUE,        
        telefone TEXT NOT NULL,
        endereco TEXT NOT NULL
    )
    ''')

    # Cria a tabela 'medicos' no banco de dados, se ela não existir.
    # A tabela contém informações sobre os médicos da clínica.
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS medicos (
        id_medico INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        especialidade TEXT NOT NULL,
        crm VARCHAR(10) NOT NULL UNIQUE,
        telefone TEXT NOT NULL
    )
    ''')
    # Cria a tabela 'consultas' no banco de dados, se ela não existir.
    # A tabela armazena informações sobre as consultas agendadas.
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS consultas (
        id_consulta INTEGER PRIMARY KEY AUTOINCREMENT,
        id_paciente INTEGER NOT NULL,
        id_medico INTEGER NOT NULL,
        data TEXT NOT NULL,
        horario TEXT NOT NULL,
        FOREIGN KEY (id_paciente) REFERENCES pacientes(id_paciente),
        FOREIGN KEY (id_medico) REFERENCES medicos(id_medico),
        UNIQUE (id_paciente, id_medico, data)
    )
    ''')
    # Cria a tabela 'notas_fiscais' no banco de dados, se ela não existir.
    # A tabela armazena informações sobre as notas fiscais emitidas para os pacientes.
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS notas_fiscais (
        id_nota INTEGER PRIMARY KEY AUTOINCREMENT,
        id_paciente INTEGER NOT NULL,
        valor REAL NOT NULL,
        data_emissao TEXT NOT NULL,
        FOREIGN KEY (id_paciente) REFERENCES pacientes(id_paciente),
        UNIQUE (id_paciente, valor, data_emissao)
    )
    ''')

    conn.commit() # Confirma todas as mudanças feitas no banco de dados.
    conn.close() # Fecha a conexão com o banco de dados.
