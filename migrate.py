import json
import psycopg2

DB_NAME = "produtos"
DB_USER = "postgres"
DB_PASS = "JeFfSc123"
DB_HOST = "localhost"
DB_PORT = "5432"
JSON_FILE_PATH = "produtos.json"
TABLE_NAME = "produtos"

def migrar_json_para_postgres():
    """
    Lê um arquivo JSON e insere os dados em uma tabela do PostgreSQL.
    """
    # Carrega os dados do arquivo JSON
    try:
        with open(JSON_FILE_PATH, 'r', encoding='utf-8') as f:
            produtos = json.load(f)
        print(f"{len(produtos)} produtos carregados do arquivo JSON.")
    except FileNotFoundError:
        print(f"Erro: O arquivo {JSON_FILE_PATH} não foi encontrado.")
        return
    except json.JSONDecodeError:
        print(f"Erro: O arquivo {JSON_FILE_PATH} não é um JSON válido.")
        return

    conn = None
    try:
        # Conecta ao banco de dados
        conn = psycopg2.connect(
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASS,
            host=DB_HOST,
            port=DB_PORT
        )
        cur = conn.cursor()
        print("Conexão com o PostgreSQL bem-sucedida.")

        # Itera sobre cada produto e o insere no banco
        for produto in produtos:
            # Query SQL para inserção. Usamos %s para evitar SQL Injection.
            sql = f"""
                INSERT INTO {TABLE_NAME} (codigo, descricao, codigo_barras, referencia)
                VALUES (%s, %s, %s, %s);
            """
            # Executa o comando, passando os valores em uma tupla
            cur.execute(sql, (
                produto.get("codigo"),
                produto.get("descricao"),
                produto.get("codigoBarras"),
                produto.get("referencia")
            ))
        
        # Confirma as transações
        conn.commit()
        
        print(f"Sucesso! {len(produtos)} registros foram inseridos na tabela '{TABLE_NAME}'.")

    except psycopg2.Error as e:
        print(f"Erro na operação com o banco de dados: {e}")
        if conn:
            conn.rollback() # Desfaz as alterações em caso de erro

    finally:
        # Fecha a conexão
        if conn is not None:
            cur.close()
            conn.close()
            print("Conexão com o PostgreSQL fechada.")

# Executa a função de migração
if __name__ == "__main__":
    migrar_json_para_postgres()