

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from app.utils import *

class PacienteWindow:
    def __init__(self):
        self.janela = None
        self.abrir_janela()

    def obter_pacientes(self):
        conn = sqlite3.connect("app/database/clinica.db")
        cursor = conn.cursor()

        try:
            cursor.execute("SELECT pacientes.nome, pacientes.cpf, pacientes.data_nasc, pacientes.telefone, pacientes.email, pacientes.endereco FROM pacientes")
            registros = cursor.fetchall()
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao acessar o banco de dados: {e}")

        conn.close()

        return registros

    def abrir_janela(self):
        if self.janela is None or not self.janela.winfo_exists():
            self.janela = tk.Toplevel()
            self.janela.title("Gerenciar Pacientes")
            self.janela.geometry("1000x600")  # Tamanho da janela reduzido
            self.janela.grab_set()  # Faz a janela ficar na frente da principal
            self.criar_interface()
        else:
            self.janela.lift()

        # Atualiza a tabela ao abrir a janela
        self.atualizar_tabela()

    def atualizar_tabela(self):
        # Limpa a tabela atual
        for item in self.tabela_pacientes.get_children():
            self.tabela_pacientes.delete(item)

        # Recarrega os pacientes do banco de dados
        for paciente in self.obter_pacientes():
            self.tabela_pacientes.insert("", "end", values=paciente)

    def adicionar_paciente(self):
        nome = self.nome_entry.get()
        nascimento = self.nascimento_entry.get()
        cpf = self.cpf_entry.get()  # Alterado para cpf_entry
        contato = self.contato_entry.get()
        email = self.email_entry.get()
        endereco = self.endereco_entry.get()

        paciente = [nome, cpf, nascimento, contato, email, endereco]

        if nome and cpf and nascimento and contato and email and endereco:
            try:
                insert_paciente(nome, cpf, nascimento, contato, email, endereco)
                self.tabela_pacientes.insert('', tk.END, values=(paciente[0], paciente[1], paciente[2], paciente[3], paciente[4], paciente[5]))
                self.limpar_campos_paciente()
                messagebox.showinfo('Sucesso', f"Paciente {nome} adicionado com sucesso!")
            except Exception as e:
                messagebox.showerror("Erro", f"Erro ao adicionar paciente: {e}")
        else:
            messagebox.showwarning('Atenção', 'Preencha todos os campos!')

        # Mantém a janela na frente
        self.janela.lift()

    def limpar_campos_paciente(self):
        self.nome_entry.delete(0, tk.END)
        self.cpf_entry.delete(0, tk.END)  # Alterado para cpf_entry
        self.nascimento_entry.delete(0, tk.END)
        self.contato_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.endereco_entry.delete(0, tk.END)

        # Mantém a janela na frente
        self.janela.lift()

    def remover_paciente(self):
        selected_item = self.tabela_pacientes.selection()
        if selected_item:
            paciente = self.tabela_pacientes.item(selected_item)['values']
            cpf = paciente[1]  # CPF é o segundo valor na lista

            conn = sqlite3.connect("app/database/clinica.db")
            cursor = conn.cursor()

            try:
                cursor.execute("DELETE FROM pacientes WHERE cpf = ?", (cpf,))
                conn.commit()
                self.tabela_pacientes.delete(selected_item)
                messagebox.showinfo('Sucesso', f"Paciente {paciente[0]} removido com sucesso!")
            except Exception as e:
                messagebox.showerror("Erro", f"Erro ao remover paciente: {e}")
            finally:
                conn.close()
        else:
            messagebox.showwarning('Atenção', 'Selecione um paciente para remover!')

        # Mantém a janela na frente
        self.janela.lift()

    def criar_interface(self):
        frame = tk.Frame(self.janela, bg="white")
        frame.pack(fill=tk.BOTH, expand=True)

        tk.Label(frame, text="Nome do Paciente:", bg="white").grid(row=0, column=0, padx=5, pady=5)
        self.nome_entry = tk.Entry(frame)
        self.nome_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(frame, text="CPF:", bg="white").grid(row=1, column=0, padx=5, pady=5)
        self.cpf_entry = tk.Entry(frame)  # Alterado para cpf_entry
        self.cpf_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(frame, text="Data de Nascimento:", bg="white").grid(row=2, column=0, padx=5, pady=5)
        self.nascimento_entry = tk.Entry(frame)
        self.nascimento_entry.grid(row=2, column=1, padx=5, pady=5)

        tk.Label(frame, text="Contato:", bg="white").grid(row=3, column=0, padx=5, pady=5)
        self.contato_entry = tk.Entry(frame)
        self.contato_entry.grid(row=3, column=1, padx=5, pady=5)

        tk.Label(frame, text="E-mail:", bg="white").grid(row=4, column=0, padx=5, pady=5)
        self.email_entry = tk.Entry(frame)
        self.email_entry.grid(row=4, column=1, padx=5, pady=5)

        tk.Label(frame, text="Endereço:", bg="white").grid(row=5, column=0, padx=5, pady=5)
        self.endereco_entry = tk.Entry(frame, width=50)
        self.endereco_entry.grid(row=5, column=1, padx=5, pady=5)

        btn_add = tk.Button(frame, text="Adicionar", bg="blue", fg="white", command=self.adicionar_paciente)
        btn_add.grid(row=6, column=0, pady=5)

        btn_clear = tk.Button(frame, text="Limpar", bg="red", fg="white", command=self.limpar_campos_paciente)
        btn_clear.grid(row=6, column=1, pady=5)

        btn_remove = tk.Button(frame, text="Remover", bg="orange", fg="white", command=self.remover_paciente)
        btn_remove.grid(row=6, column=2, pady=5)

        colunas = ("Nome", "CPF", "Data de Nascimento", "Contato", "E-mail", "Endereço")
        self.tabela_pacientes = ttk.Treeview(frame, columns=colunas, show="headings")

        for col in colunas:
            self.tabela_pacientes.heading(col, text=col)
            self.tabela_pacientes.column(col, width=140)

        self.tabela_pacientes.grid(row=7, column=0, columnspan=3, pady=5)

        # Carregar pacientes existentes
        self.atualizar_tabela()