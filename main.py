from app.gui.login import LoginScreen  # Interface de login.
from app.gui.main_screen import * # Interface gráfica principal.
from app.database.execute_sql import execute_sql  # Executa scripts SQL.
import tkinter as tk
from tkinter import ttk, messagebox

def conectar_banco():
    """ Garante que o banco de dados está criado antes de iniciar o sistema."""
    try:
        execute_sql("app/database/create_db.sql")  # Cria as tabelas.
        execute_sql("app/database/seed_db.sql")  # Popula com dados iniciais.
        print("Banco de dados inicializado com sucesso!")
    except Exception as e:
        print(f"Erro ao conectar ao banco de dados: {e}")

def main():
    conectar_banco()  # Conectar ao banco antes de iniciar a interface gráfica.
    
    login = LoginScreen()
    login.mainloop()

    app = Interface()

if __name__ == "__main__":
    main()
