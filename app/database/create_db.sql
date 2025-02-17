CREATE TABLE IF NOT EXISTS pacientes (
    id_paciente INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    data_nasc DATE NOT NULL,
    cpf VARCHAR(11) NOT NULL UNIQUE,        
    telefone TEXT NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    endereco TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS medicos (
    id_medico INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    especialidade TEXT NOT NULL,
    crm VARCHAR(10) NOT NULL UNIQUE,
    telefone TEXT NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS consultas (
    id_consulta INTEGER PRIMARY KEY AUTOINCREMENT,
    id_paciente INTEGER NOT NULL,
    id_medico INTEGER NOT NULL,
    data TEXT NOT NULL,
    horario TEXT NOT NULL,
    FOREIGN KEY (id_paciente) REFERENCES pacientes(id_paciente),
    FOREIGN KEY (id_medico) REFERENCES medicos(id_medico),
    UNIQUE (id_paciente, id_medico, data)
);

CREATE TABLE IF NOT EXISTS notas_fiscais (
    id_nota INTEGER PRIMARY KEY AUTOINCREMENT,
    id_paciente INTEGER NOT NULL,
    valor REAL NOT NULL,
    data_emissao TEXT NOT NULL,
    FOREIGN KEY (id_paciente) REFERENCES pacientes(id_paciente),
    UNIQUE (id_paciente, valor, data_emissao)
);
       
CREATE TABLE IF NOT EXISTS usuarios( 
    Id INTEGER PRIMARY KEY AUTOINCREMENT,
    Username TEXT NOT NULL,
    Email TEXT NOT NULL,
    Senha TEXT NOT NULL,
    Confirma_Senha TEXT NOT NULL
);

