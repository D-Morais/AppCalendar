import sqlite3 as sql
import pandas as pd


def connect():
    return sql.connect("vacation.db")


def init_db():
    conexao = connect()
    cursor = conexao.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS users(
            id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
            username VARCHAR(50) NOT NULL UNIQUE,
            password TEXT NOT NULL
        );
        """
    )

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS vacation(
            id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
            name TEXT NOT NULL UNIQUE,
            start_vacation TEXT NOT NULL,
            end_vacation TEXT NOT NULL
        );
        """
    )

    conexao.commit()
    conexao.close()


def add_user(name, hashed_password):
    conexao = connect()
    cursor = conexao.cursor()

    try:
        cursor.execute("""INSERT INTO users (username, password) VALUES (?, ?);""", (name, hashed_password))
        conexao.commit()
        return True

    except sql.IntegrityError:
        conexao.rollback()
        return False

    finally:
        conexao.close()


def add_vacation(name, start, end):
    conexao = connect()
    cursor = conexao.cursor()

    try:
        cursor.execute(
            """INSERT INTO vacation (name, start_vacation, end_vacation) VALUES (?, ?, ?);""", (name, start, end)
        )
        conexao.commit()
        return True

    except sql.IntegrityError:
        conexao.rollback()
        return False

    finally:
        conexao.close()


def get_users():
    conexao = connect()
    cursor = conexao.cursor()

    cursor.execute(
        """SELECT username FROM users;"""
    )

    list_users = cursor.fetchall()

    conexao.close()
    return list_users


def search_user(name):
    conexao = connect()
    cursor = conexao.cursor()

    cursor.execute("""SELECT username, password FROM users WHERE username = ?;""", (name, ))

    user = cursor.fetchone()
    conexao.close()

    return user


def rename_columns(df):
    df_updated = df.rename(columns={
        "name": "Nome",
        "start_vacation": "Inicio das férias",
        "end_vacation": "Fim da férias"
    })
    return df_updated


def load_ferias_from_db():
    conexao = connect()
    df = pd.read_sql_query("SELECT name, start_vacation, end_vacation FROM vacation;", conexao)
    df_updated = rename_columns(df)

    conexao.close()
    return df_updated


def fetch_data_by_date_range(start_date, end_date):
    conexao = connect()
    query = """
    SELECT name, start_vacation, end_vacation FROM vacation WHERE start_vacation BETWEEN ? AND ?;
    """

    df = pd.read_sql_query(query, conexao, params=[start_date, end_date])
    df_updated = rename_columns(df)

    conexao.close()
    return df_updated


def save_to_excel(df):
    df.to_excel("ferias.xlsx", index=False)


def remove_vacation(name):
    conexao = connect()
    cursor = conexao.cursor()

    try:
        cursor.execute(
            """DELETE FROM vacation WHERE name = ?""", (name, )
        )
        conexao.commit()
        return f"Usuário removido com sucesso."

    except sql.Error as er:
        conexao.rollback()
        return f"Erro ao remover o usuário: {er}"

    finally:
        conexao.close()


if __name__ == '__main__':
    init_db()
#    hash_teste = encrypt("teste123")
    add_user("Admin", "teste123")
