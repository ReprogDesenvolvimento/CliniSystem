-- Populando a tabela de pacientes
INSERT OR IGNORE INTO pacientes (nome, data_nasc, cpf, telefone, email, endereco)
VALUES 
    ("Amanda Lira", "10-08-1995", "22222222222", "88999999999", "email1@gmail.com",  "Rua Alta, 55"),
    ("Graziella Mendes", "15-05-2006", "11111111111", "88988888888", "email2@gmail.com", "Av. Brasil, 123"),
    ("Victor Anderson", "15-05-2004", "03071290390", "88988471374", "email3@gmail.com", "Rua Francisco Marcelino Santana, 209"),
    ("Jonas", "15-05-2004", "12345678910", "88988471879", "email4@gmail.com", "Travessa Assaré, 23");

-- Populando a tabela de médicos
INSERT OR IGNORE INTO medicos (nome, especialidade, crm, telefone, email)
VALUES 
    ("Dra. Fernanda Costa", "Nutricionista", "12345-CE", "88 3456-5647", "medico@gmail.com"),
    ("Dr. João Silva", "Cardiologista", "67890-CE", "88 3455-2100", "medico1@gmail.com"),
    ("Dr. Jonas Caetano", "Psiquiatra", "67833-CE", "88 3445-2120", "medico2@gmail.com");

-- Populando a tabela de consultas
INSERT OR IGNORE INTO consultas (id_paciente, id_medico, data, horario)
VALUES 
    (1, 1, "16/12/2024", "08:00"),
    (2, 2, "16/12/2024", "10:00");

-- Populando a tabela de notas fiscais
INSERT OR IGNORE INTO notas_fiscais (id_paciente, valor, data_emissao)
VALUES 
    (1, 300.00, "16/12/2024"),
    (2, 300.00, "17/12/2024");

-- Populando a tabela de notas fiscais
INSERT OR IGNORE INTO usuarios (Id, Username, Email, Senha, Confirma_Senha)
VALUES 
    (2, "admin", "victoranderson1575@gmail.com", "12345", "12345");