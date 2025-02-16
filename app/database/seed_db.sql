-- Populando a tabela de pacientes
INSERT OR IGNORE INTO pacientes (nome, data_nasc, cpf, telefone, endereco)
VALUES 
    ("Amanda Lira", "10-08-1995", "22222222222", "88999999999", "Rua Alta, 55"),
    ("Graziella Mendes", "15-05-2006", "11111111111", "88988888888", "Av. Brasil, 123"),
    ("Victor Anderson", "15-05-2004", "03071290390", "88988471374", "Rua Francisco Marcelino Santana, 209"),
    ("Jonas", "15-05-2004", "12345678910", "88988471879", "Travessa Assaré, 23");

-- Populando a tabela de médicos
INSERT OR IGNORE INTO medicos (nome, especialidade, crm, telefone)
VALUES 
    ("Dra. Fernanda Costa", "Nutricionista", "12345-CE", "88 3456-5647"),
    ("Dr. João Silva", "Cardiologista", "67890-CE", "88 3455-2100"),
    ("Dr. Jonas Caetano", "Psiquiatra", "67833-CE", "88 3445-2120");

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
    (1, "andizon", "victoranderson1575@gmail.com", "1234", "1234");