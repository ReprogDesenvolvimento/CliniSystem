# Este é o ponto de entrada principal para executar o sistema da clínica.

from app.gui.main_screen import MainWindow  # Importa a interface gráfica principal.
from app.database.seed_db import seed_database  # Importa a função para popular o banco de dados.
from app.database.db_config import create_database  # Importa a função para criar/configurar o banco de dados.

def main():
    
    #Função principal que inicializa o banco de dados, popula com dados iniciais e abre a interface gráfica.
    
    create_database()  # Cria o banco de dados e as tabelas, caso não existam.
    seed_database()  # Popula o banco de dados com dados iniciais.
    MainWindow()  # Inicia a interface gráfica do sistema.

if __name__ == "__main__":
    main()  # Executa a função principal se este arquivo for o ponto de entrada.
