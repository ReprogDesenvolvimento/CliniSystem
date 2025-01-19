import sqlite3  # Importa a biblioteca sqlite3

def seed_database():
    # Conecta ao banco de dados 'clinica.db' localizado no diretório especificado.
    conn = sqlite3.connect("app/database/clinica.db")
    
    # Cria um objeto cursor para executar comandos SQL no banco de dados.
    cursor = conn.cursor()

    # Lista de pacientes para inserir na tabela 'pacientes'.
    pacientes = [
        ("Amanda Lira", "10-08-1995", "22222222222", "88999999999", "Rua Alta, 55"),
        ("Graziella Mendes", "15-05-2006", "11111111111", "88988888888", "Av. Brasil, 123"),
        ("Victor Anderson", "15-05-2004", "03071290390", "88988471374", "Rua Francisco Marcelino Santana, 209"),
        ("Jonas", "15-05-2004", "12345678910", "88988471879", "Travessa Assaré, 23")
    ]
    
    # Insere os dados de pacientes na tabela 'pacientes'. A cláusula 'OR IGNORE' impede erros caso o CPF já exista.
    cursor.executemany("INSERT OR IGNORE INTO pacientes (nome, data_nasc, cpf, telefone, endereco) VALUES (?, ?, ?, ?, ?)", pacientes)

    # Lista de médicos para inserir na tabela 'medicos'.
    medicos = [
        ("Dra. Fernanda Costa", "Nutricionista", "12345-CE", "88 3456-5647"),
        ("Dr. João Silva", "Cardiologista", "67890-CE", "88 3455-2100"),
        ("Dr. Jonas Caetano", "Psiquiatra", "67833-CE", "88 3445-2120")
    ]
    
    # Insere os dados de médicos na tabela 'medicos'. A cláusula 'OR IGNORE' impede erros caso o CRM já exista.
    cursor.executemany("INSERT OR IGNORE INTO medicos (nome, especialidade, crm, telefone) VALUES (?, ?, ?, ?)", medicos)

    # Lista de consultas para inserir na tabela 'consultas'.
    consultas = [
        (1, 1, "16/12/2024", "08:00"),  # Consulta de Amanda Lira com Dra. Fernanda Costa
        (2, 2, "16/12/2024", "10:00")   # Consulta de Graziella Mendes com Dr. João Silva
    ]
    
    # Insere os dados de consultas na tabela 'consultas'. A cláusula 'OR IGNORE' impede erros caso a consulta já exista.
    cursor.executemany("INSERT OR IGNORE INTO consultas (id_paciente, id_medico, data, horario) VALUES (?, ?, ?, ?)", consultas)

    # Lista de notas fiscais para inserir na tabela 'notas_fiscais'.
    notas = [
        (1, 300.00, "16/12/2024"),  # Nota fiscal de Amanda Lira no valor de 300.00
        (2, 300.00, "17/12/2024")   # Nota fiscal de Graziella Mendes no valor de 300.00
    ]
    
    # Insere as notas fiscais na tabela 'notas_fiscais'. A cláusula 'OR IGNORE' impede erros caso a nota já exista.
    cursor.executemany("INSERT OR IGNORE INTO notas_fiscais (id_paciente, valor, data_emissao) VALUES (?, ?, ?)", notas)

    # Confirma todas as alterações feitas no banco de dados.
    conn.commit()

    # Fecha a conexão com o banco de dados, liberando os recursos.
    conn.close()

    # Imprime uma mensagem no console indicando que o banco foi populado com sucesso.
    print("Banco populado!")
