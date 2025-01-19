# Definição da classe 'paciente', que representa um paciente.
class paciente:
    # Método construtor (__init__) para inicializar os atributos da classe.
    def __init__(self, id_paciente, nome, data_nasc, cpf, telefone, endereco):
        self.id_paciente = id_paciente  # Atributo que armazena o ID único do paciente.
        self.nome = nome  # Atributo que armazena o nome do paciente.
        self.data_nasc = data_nasc  # Atributo que armazena a data de nascimento do paciente.
        self.cpf = cpf  # Atributo que armazena o CPF do paciente.
        self.telefone = telefone  # Atributo que armazena o telefone de contato do paciente.
        self.endereco = endereco  # Atributo que armazena o endereço do paciente.

    # Método que imprime as informações do paciente.
    def imprime_ficha(self):
        print("============================")  # Imprime uma linha para demarcar o início da ficha do paciente.
        print("ID do Paciente:", self.id_paciente)  # Exibe o ID do paciente.
        print("Nome:", self.nome)  # Exibe o nome do paciente.
        print("Data nascimento:", self.data_nasc)  # Exibe a data de nascimento do paciente.
        print("CPF:", self.cpf)  # Exibe o CPF do paciente.
        print("Telefone:", self.telefone)  # Exibe o telefone de contato do paciente.
        print("Endereço:", self.endereco)  # Exibe o endereço do paciente.
        print("============================")  # Imprime uma linha para demarcar o fim da ficha do paciente.
