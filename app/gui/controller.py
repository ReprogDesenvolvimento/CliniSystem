import tkinter as tk
from tkinter import ttk
#from app.gui.controller import CliniSystemController

class CliniSystemController:
    """
    Controlador central para gerenciar médicos, pacientes e consultas.
    """
    def __init__(self):
        self.medicos = []  # Lista de médicos
        self.pacientes = []  # Lista de pacientes
        self.consultas = []  # Lista de consultas
        self.especializacoes = []  # Lista de especializações

    def adicionar_medico(self, nome, especializacao, taxa, contato, email):
        medico = {"nome": nome, "especializacao": especializacao, "taxa": taxa, "contato": contato, "email": email}
        self.medicos.append(medico)
        return medico

    def adicionar_paciente(self, nome, genero, nascimento, contato, email, endereco):
        paciente = {"nome": nome, "genero": genero, "nascimento": nascimento, "contato": contato, "email": email, "endereco": endereco}
        self.pacientes.append(paciente)
        return paciente

    def adicionar_especializacao(self, especializacao):
        if especializacao not in self.especializacoes:
            self.especializacoes.append(especializacao)
        return especializacao

    def marcar_consulta(self, paciente, sintomas, especializacao, data, hora):
        consulta = {"paciente": paciente, "sintomas": sintomas, "especializacao": especializacao, "data": data, "hora": hora}
        self.consultas.append(consulta)
        return consulta

    def obter_consultas_do_dia(self, data_atual):
        return [consulta for consulta in self.consultas if consulta["data"] == data_atual]

    def obter_medicos(self):
        return self.medicos

    def obter_pacientes(self):
        return self.pacientes

    def obter_especializacoes(self):
        return self.especializacoes

    def obter_consultas(self):
        return self.consultas
