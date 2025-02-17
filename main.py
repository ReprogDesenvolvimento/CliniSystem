from app.gui.login import LoginScreen  # Interface de login.
from app.gui.main_screen import * # Interface gráfica principal.
from app.database.execute_sql import execute_sql  # Executa scripts SQL.

def main():
    """ Garante que o banco de dados está criado antes de iniciar o sistema."""
    try:
        execute_sql("app/database/create_db.sql")  # Cria as tabelas.
        execute_sql("app/database/seed_db.sql")  # Popula com dados iniciais.
        print("Banco de dados inicializado com sucesso!")
    except Exception as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
    
    login = LoginScreen()
    login.mainloop()

if __name__ == "__main__":
    main()
