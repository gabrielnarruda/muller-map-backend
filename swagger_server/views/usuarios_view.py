import sqlite3
from datetime import datetime

from swagger_server.__main__ import db_conn


def insert_novo_usuario(usuario):
    sqlite_connection = sqlite3.connect(db_conn)
    cursor = sqlite_connection.cursor()
    user = usuario.get('usuario'),
    senha = usuario.get('senha'),
    nome = usuario.get('nome'),
    instituicao = usuario.get('instituicao'),
    email = usuario.get('email'),
    created_at =datetime.now().strftime("%d-%m-%Y %H:%M:%S")

    cursor.execute("INSERT INTO tb_usuario(usuario,senha,nome,instituicao,email,created_at)VALUES(?,?,?,?,?,?)",
                   (user[0],
                    senha[0],
                    nome[0],
                    instituicao[0],
                    email[0],
                    created_at))
    sqlite_connection.commit()
    cursor.close()

    return cursor.lastrowid