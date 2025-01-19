# Definição da classe 'notafiscal', que representa uma nota fiscal emitida para um paciente.
class notafiscal:
    # Método construtor (__init__) para inicializar os atributos da classe.
    def __init__(self, id_nota, id_paciente, valor, data_emissao):
        self.id_nota = id_nota  # Atributo que armazena o ID único da nota fiscal.
        self.id_paciente = id_paciente  # Atributo que armazena o ID do paciente associado à nota fiscal.
        self.valor = valor  # Atributo que armazena o valor da nota fiscal.
        self.data_emissao = data_emissao  # Atributo que armazena a data de emissão da nota fiscal.

    # Método que simula a emissão de uma nota fiscal.
    def emitir(self):
        print("============================")  # Imprime uma linha para demarcar o início da mensagem.
        print("Nota fiscal emitida com sucesso!")  # Mensagem informando que a nota fiscal foi emitida.
        print("ID da Nota fiscal:", self.id_nota)  # Exibe o ID da nota fiscal emitida.
        print("ID do Paciente:", self.id_paciente)  # Exibe o ID do paciente para o qual a nota fiscal foi emitida.
        print("Valor: R$", self.valor)  # Exibe o valor da nota fiscal, formatado em moeda (R$).
        print("Data de Emissão:", self.data_emissao)  # Exibe a data de emissão da nota fiscal.
        print("============================")  # Imprime uma linha para demarcar o fim da mensagem.
