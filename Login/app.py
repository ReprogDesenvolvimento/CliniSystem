import customtkinter as ctk
from tkinter import * 
import sqlite3
from tkinter import messagebox

# Banco de dados
class BackEnd():
    # conexão com o banco
    def conecta_db(self):
        self.conn = sqlite3.connect("Sistema_Cadastros.db")
        self.cursor = self.conn.cursor()
        print("Banco de dados conectado")

    # desconexão
    def desconecta_db(self):
        self.conn.close()
        print("Banco de dados desconectado")

    # criação da tabela
    def criar_tabela(self):
        self.conecta_db()

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS Usuarios( 
                Id INTEGER PRIMARY KEY AUTOINCREMENT,
                Username TEXT NOT NULL,
                Email TEXT NOT NULL,
                Senha TEXT NOT NULL,
                Confirma_Senha TEXT NOT NULL
            );
        """)

        self.conn.commit()
        print("Tabela criada com sucesso!")
        self.desconecta_db()

    # cadastrar usuários
    def cadastrar_usuario(self):
        # Chamando as funções
        self.username_cadastro = self.username_cadastro_entry.get()
        self.email_cadastro = self.email_cadastro_entry.get()
        self.senha_cadastro = self.pass_cadastro_entry.get()
        self.confirma_senha_cadastro = self.confirma_senha_entry.get()

        self.conecta_db()

        # funções importantes que impõem regras na hora de fazer o cadastro
        try:
            if (self.username_cadastro == "" or self.email_cadastro == "" or self.senha_cadastro == "" or self.confirma_senha_cadastro == ""):
                messagebox.showerror(title="Sistema de login", message="ERRO!!!\nPor favor preencha todos os campos")
            elif (len(self.username_cadastro) < 4):
                messagebox.showwarning(title="Sistema de login", message="O nome de usuário deve ter no mínimo 4 caracteres.")
            elif (len(self.senha_cadastro) < 4):
                messagebox.showwarning(title="Sistema de login", message="A senha de usuário deve ter no mínimo 4 caracteres.")
            elif (self.senha_cadastro != self.confirma_senha_cadastro):
                messagebox.showerror(title="Sistema de login", message="ERRO!!!\nAs senhas não correspondem.")
            else:
                self.cursor.execute("""
                    INSERT INTO Usuarios (Username, Email, Senha, Confirma_Senha)
                    VALUES (?, ?, ?, ?)""", (self.username_cadastro, self.email_cadastro, self.senha_cadastro, self.confirma_senha_cadastro))
                self.conn.commit()
                messagebox.showinfo(title="Sistema de login", message=f"Parabéns {self.username_cadastro} \nOs seus dados foram cadastrados com sucesso!")
                self.limpa_cadastro()

        except Exception as e:
            messagebox.showerror(title="Sistema de login", message=f"Erro no processamento do seu cadastro!\nPor favor tente de novo.\n{e}")

        finally:
            self.desconecta_db()

    # Verificação do login
    def verifica_login(self):
        self.username_login = self.username_login_entry.get()
        self.senha_login = self.pass_login_entry.get()

        self.conecta_db()

        try:
            self.cursor.execute("""SELECT * FROM Usuarios WHERE (Username = ? AND Senha = ?)""", (self.username_login, self.senha_login))
            self.verifica_dados = self.cursor.fetchone()  # Percorrendo a tabela usuários

            # funções importantes que impõem regras na hora de fazer o login
            if (self.username_login == "" or self.senha_login == ""):
                messagebox.showwarning(title="Sistema de login", message="Por favor preencha todos os campos!")
            elif self.verifica_dados:
                messagebox.showinfo(title="Sistema de login", message=f"Parabéns {self.username_login} \nLogin feito com sucesso!")
                self.limpa_login()
            else:
                messagebox.showerror(title="Sistema de login", message="Erro!!!\nDados não encontrados no sistema.\nPor favor verifique seus dados ou cadastre-se no sistema!")

        except Exception as e:
            messagebox.showerror(title="Sistema de login", message=f"Erro ao verificar login.\n{e}")

        finally:
            self.desconecta_db()


class App(ctk.CTk, BackEnd):
    def __init__(self):
        super().__init__()
        self.configuracoes_janela_inicial()
        self.tela_de_login()
        self.criar_tabela()

    # Janela Principal
    def configuracoes_janela_inicial(self):
        self.geometry("700x400")
        self.title("Sistema de Login")
        self.resizable(False, False)

    def tela_de_login(self):
        # Carregar imagem com Pillow
        self.img = PhotoImage(file="Login/imagem1.png")
        self.lb_img = ctk.CTkLabel(self, text=None, image=self.img)
        self.lb_img.grid(row=3, column=0, padx=4)  
        
        # Título
        title_label = ctk.CTkLabel(self, text="Faça o seu login ou cadastre-se\nna nossa plataforma para acessar\nos nossos serviços!", font=("Century Gothic bold", 14))
        title_label.grid(row=0, column=0, pady=10, padx=10)

        # Frame do formulário de login
        self.frame_login = ctk.CTkFrame(self, width=350, height=380)
        self.frame_login.place(x=350, y=10)

        # Widgets
        self.lb_title = ctk.CTkLabel(self.frame_login, text="Faça o seu Login", font=("Century Gothic bold", 14))
        self.lb_title.grid(row=0, column=0, padx=10, pady=10)

        self.username_login_entry = ctk.CTkEntry(self.frame_login, width=300, placeholder_text="Seu nome de usuário...", font=("Century Gothic bold", 16), corner_radius=15, border_color="#005")
        self.username_login_entry.grid(row=1, column=0, pady=10, padx=10)

        self.pass_login_entry = ctk.CTkEntry(self.frame_login, width=300, placeholder_text="Sua senha...", font=("Century Gothic bold", 16), corner_radius=15, show="*", border_color="#005")
        self.pass_login_entry.grid(row=2, column=0, pady=10, padx=10)

        self.ver_senha = ctk.CTkCheckBox(self.frame_login, text="Clique para ver a senha", font=("Century Gothic bold", 12), corner_radius=20)
        self.ver_senha.grid(row=3, column=0, pady=10, padx=10)

        self.bnt_login = ctk.CTkButton(self.frame_login, width=300, fg_color="#11114E", hover_color="#005C6A", text="Fazer login".upper(), font=("Century Gothic bold", 14), corner_radius=15, command=self.verifica_login)
        self.bnt_login.grid(row=4, column=0, pady=10, padx=10)

        self.span = ctk.CTkLabel(self.frame_login, text="Se não tem conta, clique no botão abaixo para\ncadastrar-se no nosso sistema", font=("Century Gothic", 10))
        self.span.grid(row=5, column=0, pady=10, padx=10)

        self.bnt_cadastro = ctk.CTkButton(self.frame_login, width=300, fg_color="#11114E", hover_color="#005C6A", text="Fazer Cadastro".upper(), font=("Century Gothic bold", 14), corner_radius=15, command=self.tela_de_cadastro)
        self.bnt_cadastro.grid(row=6, column=0, pady=10, padx=10)

    def tela_de_cadastro(self):
        # Remoção da tela de login
        self.frame_login.place_forget()

        # Frame do formulário de login
        self.frame_cadastro = ctk.CTkFrame(self, width=350, height=380)
        self.frame_cadastro.place(x=350, y=10)

        # Título
        title_label = ctk.CTkLabel(self.frame_cadastro, text="Cadastre-se", font=("Century Gothic bold", 14))
        title_label.grid(row=0, column=0, pady=10, padx=10)

        # Widgets tela de cadastro
        self.username_cadastro_entry = ctk.CTkEntry(self.frame_cadastro, width=300, placeholder_text="Seu nome de usuário...", font=("Century Gothic bold", 16), corner_radius=15, border_color="#005")
        self.username_cadastro_entry.grid(row=1, column=0, pady=5, padx=10)

        self.email_cadastro_entry = ctk.CTkEntry(self.frame_cadastro, width=300, placeholder_text="Email do usuário...", font=("Century Gothic bold", 16), corner_radius=15, border_color="#005")
        self.email_cadastro_entry.grid(row=2, column=0, pady=5, padx=10)

        self.pass_cadastro_entry = ctk.CTkEntry(self.frame_cadastro, width=300, placeholder_text="Senha do usuário...", font=("Century Gothic bold", 16), corner_radius=15, show="*", border_color="#005")
        self.pass_cadastro_entry.grid(row=3, column=0, pady=5, padx=10)

        self.confirma_senha_entry = ctk.CTkEntry(self.frame_cadastro, width=300, placeholder_text="Confirme a senha do usuário...", font=("Century Gothic bold", 16), corner_radius=15, show="*", border_color="#005")
        self.confirma_senha_entry.grid(row=4, column=0, pady=5, padx=10)

        self.ver_senha = ctk.CTkCheckBox(self.frame_cadastro, text="Clique para ver a senha", font=("Century Gothic bold", 12), corner_radius=20)
        self.ver_senha.grid(row=5, column=0, pady=5, padx=10)

        self.bnt_cadastro = ctk.CTkButton(self.frame_cadastro, width=300, fg_color="#11114E", hover_color="#005C6A", text="Fazer Cadastro".upper(), font=("Century Gothic bold", 14), corner_radius=15, command=self.cadastrar_usuario)
        self.bnt_cadastro.grid(row=6, column=0, pady=5, padx=10)

        self.bnt_login_back = ctk.CTkButton(self.frame_cadastro, width=300, fg_color="#11114E", hover_color="#005C6A", text="Volte à tela de login".upper(), font=("Century Gothic bold", 14), corner_radius=15, command=self.tela_de_login)
        self.bnt_login_back.grid(row=7, column=0, pady=10, padx=10)

    # Limpa campo cadastro
    def limpa_cadastro(self):
        self.username_cadastro_entry.delete(0, END)
        self.email_cadastro_entry.delete(0, END)
        self.pass_cadastro_entry.delete(0, END)
        self.confirma_senha_entry.delete(0, END)

    # Limpa campo login
    def limpa_login(self):
        self.username_login_entry.delete(0, END)
        self.pass_login_entry.delete(0, END)


if __name__ == "__main__":
    app = App()
    app.mainloop()
