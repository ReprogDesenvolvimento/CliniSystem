import customtkinter as ctk
from tkinter import * 


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.configuracoes_janela_inicial()
        self.tela_de_login()

    # Janela Principal
    def configuracoes_janela_inicial(self):
        self.geometry("700x400")
        self.title("Sistema de Login")
        self.resizable(False, False)

    def tela_de_login(self):
        # Carregar imagem com Pillow
        self.img = PhotoImage(file="imagem1.png")
        self.lb_img = ctk.CTkLabel(self, text=None, image=self.img)
        self.lb_img.grid(row=3, column=0, padx=4)  
        
        #Titulo
        title_label = ctk.CTkLabel(self, text="Faça o seu login ou cadastre-se\nna nossa plataforma para acessar\nos nossos serviços!", font=("Century Gothic bold", 14))
        title_label.grid(row=0, column=0, pady=10, padx=10)

        #Frame do formulario de login
        self.frame_login = ctk.CTkFrame(self, width=350, height=380)
        self.frame_login.place(x=350, y=10)

        #widgets
        self.lb_title = ctk.CTkLabel(self.frame_login, text="Faça o seu Login", font=("Century Gothic bold", 14))
        self.lb_title.grid(row=0, column=0, padx=10, pady=10)

        self.username_login = ctk.CTkEntry(self.frame_login, width=300, placeholder_text="Seu nome de usuario...", font=("Century Gothic bold", 16), corner_radius= 15, border_color="#005")
        self.username_login.grid(row=1, column=0, pady=10, padx= 10)

        self.pass_login = ctk.CTkEntry(self.frame_login, width=300, placeholder_text="Sua senha...", font=("Century Gothic bold", 16), corner_radius= 15, show = "*" , border_color="#005")
        self.pass_login.grid(row=2, column=0, pady=10, padx= 10)

        self.ver_senha = ctk.CTkCheckBox(self.frame_login, text="Clique para ver a senha", font=("Century Gothic bold", 12), corner_radius= 20)
        self.ver_senha.grid(row=3, column=0, pady=10, padx= 10)

        self.bnt_login = ctk.CTkButton(self.frame_login, width=300, fg_color="#11114E", hover_color="#005C6A", text="Fazer login".upper(), font=("Century Gothic bold", 14), corner_radius= 15)
        self.bnt_login.grid(row=4, column=0, pady=10, padx= 10)

        self.span = ctk.CTkLabel(self.frame_login, text="Se não tem conta, clique no botão abaixo para\ncadastrar-se no nosso sistema", font=("Century Gothic", 10))
        self.span.grid(row=5, column=0, pady=10, padx= 10)

        self.bnt_cadastro = ctk.CTkButton(self.frame_login, width=300, fg_color="#11114E", hover_color="#005C6A", text="Fazer Cadastro".upper(), font=("Century Gothic bold", 14), corner_radius= 15, command= self.tela_de_cadastro)
        self.bnt_cadastro.grid(row=6, column=0, pady=10, padx= 10)


    def tela_de_cadastro(self):
        #Remoção da tela de login
        self.frame_login.place_forget()

        #Frame do formulario de login
        self.frame_cadastro = ctk.CTkFrame(self, width=350, height=380)
        self.frame_cadastro.place(x=350, y=10)

        #Titulo
        title_label = ctk.CTkLabel(self.frame_cadastro, text="Cadastre-se", font=("Century Gothic bold", 14))
        title_label.grid(row=0, column=0, pady=10, padx=10)

        #widgets tela de cadastro
        self.username_cadastro_entry = ctk.CTkEntry(self.frame_cadastro, width=300, placeholder_text="Seu nome de usuario...", font=("Century Gothic bold", 16), corner_radius= 15, border_color="#005")
        self.username_cadastro_entry.grid(row=1, column=0, pady=5, padx= 10)

        self.email_cadastro_entry = ctk.CTkEntry(self.frame_cadastro, width=300, placeholder_text="Email do usuario...", font=("Century Gothic bold", 16), corner_radius= 15, border_color="#005")
        self.email_cadastro_entry.grid(row=2, column=0, pady=5, padx= 10)

        self.pass_cadastro_entry = ctk.CTkEntry(self.frame_cadastro, width=300, placeholder_text="Senha do usuario...", font=("Century Gothic bold", 16), corner_radius= 15, show = "*" , border_color="#005")
        self.pass_cadastro_entry.grid(row=3, column=0, pady=5, padx= 10)

        self.confirma_senha_cadastro = ctk.CTkEntry(self.frame_cadastro, width=300, placeholder_text="Confime senha do usuario...", font=("Century Gothic bold", 16), corner_radius= 15, show = "*", border_color="#005")
        self.confirma_senha_cadastro.grid(row=4, column=0, pady=5, padx= 10)

        self.ver_senha = ctk.CTkCheckBox(self.frame_cadastro, text="Clique para ver a senha", font=("Century Gothic bold", 12), corner_radius= 20)
        self.ver_senha.grid(row=5, column=0, pady=5, padx= 10)

        self.bnt_cadastro = ctk.CTkButton(self.frame_cadastro, width=300, fg_color="#11114E", hover_color="#005C6A", text="Fazer Cadastro".upper(), font=("Century Gothic bold", 14), corner_radius= 15)
        self.bnt_cadastro.grid(row=6, column=0, pady=5, padx= 10)

        self.bnt_login_back = ctk.CTkButton(self.frame_cadastro, width=300, fg_color="#11114E", hover_color="#005C6A", text="Volte a tela de login".upper(), font=("Century Gothic bold", 14), corner_radius= 15, command= self.tela_de_login)
        self.bnt_login_back.grid(row=7, column=0, pady=10, padx= 10)
    

if __name__ == "__main__":
    app = App()
    app.mainloop()
