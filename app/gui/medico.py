import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from app.utils import *

class MedicoWindow:
    def __init__(self):
        self.janela = None
        self.abrir_janela()

    def obter_medicos(self):
        conn = sqlite3.connect("app/database/clinica.db")
        cursor = conn.cursor()

        try:
            cursor.execute("SELECT medicos.nome, medicos.especialidade, medicos.crm, medicos.telefone, medicos.email FROM medicos")
            registros = cursor.fetchall()
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao acessar o banco de dados: {e}")

        conn.close()

        return registros

    def abrir_janela(self):
        if self.janela is None or not self.janela.winfo_exists():
            self.janela = tk.Toplevel()
            self.janela.title("Gerenciar Médicos e Especializações")
            self.janela.geometry("1000x600")  # Tamanho da janela reduzido
            self.janela.grab_set()  # Faz a janela ficar na frente da principal
            self.criar_interface()
        else:
            self.janela.lift()

    def adicionar_medico(self):
        nome = self.nome_entry.get()
        especializacao = self.especializacao_entry.get()
        crm = self.crm_entry.get()
        contato = self.contato_entry.get()
        email = self.email_entry.get()

        medico = [nome, especializacao, crm, contato, email]

        if nome and especializacao and crm and contato and email:
            insert_medico(nome, especializacao, crm, contato, email)
            self.tabela_medicos.insert('', tk.END, values=(medico[0], medico[1], medico[2], medico[3], medico[4]))
            self.limpar_campos_medico()
            messagebox.showinfo('Sucesso', f"Médico {nome} adicionado com sucesso!")
        else:
            messagebox.showwarning('Atenção', 'Preencha todos os campos!')

    def limpar_campos_medico(self):
        self.nome_entry.delete(0, tk.END)
        self.especializacao_entry.delete(0, tk.END)
        self.crm_entry.delete(0, tk.END)
        self.contato_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)

    def remover_medico(self):
        selected_item = self.tabela_medicos.selection()
        if selected_item:
            medico = self.tabela_medicos.item(selected_item)['values']
            crm = medico[2]  # CRM é o terceiro valor na lista

            conn = sqlite3.connect("app/database/clinica.db")
            cursor = conn.cursor()

            try:
                cursor.execute("DELETE FROM medicos WHERE crm = ?", (crm,))
                conn.commit()
                self.tabela_medicos.delete(selected_item)
                messagebox.showinfo('Sucesso', f"Médico {medico[0]} removido com sucesso!")
            except Exception as e:
                messagebox.showerror("Erro", f"Erro ao remover médico: {e}")
            finally:
                conn.close()
        else:
            messagebox.showwarning('Atenção', 'Selecione um médico para remover!')

    def criar_interface(self):
        frame = tk.Frame(self.janela, bg="white")
        frame.pack(fill=tk.BOTH, expand=True)

        tk.Label(frame, text="Nome:", bg="white").grid(row=0, column=0, padx=5, pady=5)
        self.nome_entry = tk.Entry(frame)
        self.nome_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(frame, text="Especialização:", bg="white").grid(row=1, column=0, padx=5, pady=5)
        self.especializacao_entry = tk.Entry(frame)
        self.especializacao_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(frame, text="CRM:", bg="white").grid(row=2, column=0, padx=5, pady=5)
        self.crm_entry = tk.Entry(frame)
        self.crm_entry.grid(row=2, column=1, padx=5, pady=5)

        tk.Label(frame, text="Contato:", bg="white").grid(row=3, column=0, padx=5, pady=5)
        self.contato_entry = tk.Entry(frame)
        self.contato_entry.grid(row=3, column=1, padx=5, pady=5)

        tk.Label(frame, text="Email:", bg="white").grid(row=4, column=0, padx=5, pady=5)
        self.email_entry = tk.Entry(frame)
        self.email_entry.grid(row=4, column=1, padx=5, pady=5)

        btn_add = tk.Button(frame, text="Adicionar", bg="blue", fg="white", command=self.adicionar_medico)
        btn_add.grid(row=5, column=0, pady=5)

        btn_clear = tk.Button(frame, text="Limpar", bg="red", fg="white", command=self.limpar_campos_medico)
        btn_clear.grid(row=5, column=1, pady=5)

        btn_remove = tk.Button(frame, text="Remover", bg="orange", fg="white", command=self.remover_medico)
        btn_remove.grid(row=5, column=2, pady=5)

        colunas = ("Nome", "Especialização", "CRM", "Contato", "E-mail")
        self.tabela_medicos = ttk.Treeview(frame, columns=colunas, show="headings")

        for col in colunas:
            self.tabela_medicos.heading(col, text=col)
            self.tabela_medicos.column(col, width=140)

        self.tabela_medicos.grid(row=6, column=0, columnspan=3, pady=5)

        # Carregar médicos existentes
        for medico in self.obter_medicos():
            self.tabela_medicos.insert("", "end", values=medico)