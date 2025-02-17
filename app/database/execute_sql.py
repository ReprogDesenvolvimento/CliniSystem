import sqlite3 # Biblioteca para manipulação do banco de dados SQLite.

def execute_sql(archive_path):
    # Conecta ao banco de dados
    conn = sqlite3.connect("app/database/clinica.db")
    cursor = conn.cursor()
    
    with open(archive_path, "r") as arquivo_sql:
        sql = arquivo_sql.read()

    cursor.executescript(sql)

    conn.commit() # Confirma todas as mudanças feitas no banco de dados.
    conn.close() # Fecha a conexão com o banco de dados.
