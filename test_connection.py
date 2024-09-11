from db_config import create_connection, close_connection

def test_database_connection():
    # Cria uma conexão com o banco de dados
    connection = create_connection()

    if connection:
        # Realize uma operação simples para testar a conexão, como listar os bancos de dados
        try:
            cursor = connection.cursor()
            cursor.execute("SHOW DATABASES;")
            databases = cursor.fetchall()
            print("Bancos de dados disponíveis:")
            for db in databases:
                print(db)
        except Exception as e:
            print(f"Erro ao executar consulta: {e}")
        finally:
            # Fecha o cursor e a conexão
            cursor.close()
            close_connection(connection)
    else:
        print("Não foi possível estabelecer a conexão com o banco de dados.")

if __name__ == "__main__":
    test_database_connection()
