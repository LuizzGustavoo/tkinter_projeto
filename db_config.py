import mysql.connector
from mysql.connector import Error

def create_connection():
    """Cria uma conexão com o banco de dados MySQL"""
    try:
        connection = mysql.connector.connect(
            host='localhost',  # ou o endereço do seu servidor de banco de dados
            user='root',  # seu nome de usuário do banco de dados
            password='',  # sua senha do banco de dados
            database='cadastro-gustavo'  # nome do banco de dados
        )
        if connection.is_connected():
            print("Conexão com o banco de dados estabelecida com sucesso!")
            return connection
    except Error as e:
        print(f"Erro ao conectar ao MySQL: {e}")
        return None

def close_connection(connection):
    """Fecha a conexão com o banco de dados"""
    if connection.is_connected():
        connection.close()
        print("Conexão com o banco de dados fechada.")
