# Definição da classe 'medico', que representa um médico.
class medico:
    # Método construtor (__init__) para inicializar os atributos da classe.
    def __init__(self, id_medico, nome, especialidade, crm, telefone):
        self.id_medico = id_medico  # Atributo que armazena o ID único do médico.
        self.nome = nome  # Atributo que armazena o nome do médico.
        self.especialidade = especialidade  # Atributo que armazena a especialidade do médico.
        self.crm = crm  # Atributo que armazena o número do CRM (registro do médico).
        self.telefone = telefone  # Atributo que armazena o telefone de contato do médico.

    # Método que imprime as informações do médico.
    def imprime_ficha(self):
        print("============================")  # Imprime uma linha para demarcar o início da ficha do médico.
        print("ID do Médico:", self.id_medico)  # Exibe o ID do médico.
        print("Nome:", self.nome)  # Exibe o nome do médico.
        print("Especialidade:", self.especialidade)  # Exibe a especialidade do médico.
        print("CRM:", self.crm)  # Exibe o número de registro do médico (CRM).
        print("Telefone:", self.telefone)  # Exibe o telefone de contato do médico.
        print("============================")  # Imprime uma linha para demarcar o fim da ficha do médico.

