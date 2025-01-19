# Definição da classe 'consulta', que representa uma consulta médica.
class consulta:
    # Método construtor (__init__) para inicializar os atributos da classe.
    def __init__(self, id_consulta, id_paciente, id_medico, data, horario):
        self.id_consulta = id_consulta  # Atributo que armazena o ID único da consulta.
        self.id_paciente = id_paciente  # Atributo que armazena o ID do paciente que agendou a consulta.
        self.id_medico = id_medico  # Atributo que armazena o ID do médico que atenderá a consulta.
        self.data = data  # Atributo que armazena a data da consulta.
        self.horario = horario  # Atributo que armazena o horário da consulta.

    # Método que simula o agendamento de uma consulta.
    def agendar(self):
        print("============================")  # Imprime uma linha para demarcar o início da mensagem.
        print("Consulta Agendada com Sucesso!")  # Mensagem informando que a consulta foi agendada.
        print("ID da Consulta:", self.id_consulta)  # Exibe o ID da consulta agendada.
        print("ID do Paciente:", self.id_paciente)  # Exibe o ID do paciente que agendou a consulta.
        print("ID do Médico:", self.id_medico)  # Exibe o ID do médico que realizará a consulta.
        print("Data:", self.data)  # Exibe a data da consulta agendada.
        print("Horário:", self.horario)  # Exibe o horário da consulta agendada.
        print("============================")  # Imprime uma linha para demarcar o fim da mensagem.
