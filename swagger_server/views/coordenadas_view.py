import json
import sqlite3
from datetime import datetime

from playhouse.shortcuts import model_to_dict

from swagger_server.__main__ import db_conn
from swagger_server.models.coordenadas_model import tb_coordenadas
from swagger_server.models.usuarios_model import tb_usuario


def insert_nova_coordenada(coordenada):
    try:
        sqlite_connection = sqlite3.connect(db_conn)
        cursor = sqlite_connection.cursor()

        nm_local = coordenada.get('nm_local'),
        lat = coordenada.get('lat'),
        lon = coordenada.get('lon'),
        indice_radiacao = coordenada.get('indice_radiacao'),
        id_usuario = coordenada.get('id_usuario'),
        created_at = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

        cursor.execute(
            "INSERT INTO tb_coordenadas(nm_local,lat,lon,indice_radiacao,id_usuario,created_at)VALUES(?,?,?,?,?,?)",
            (nm_local[0],
             lat[0],
             lon[0],
             indice_radiacao[0],
             id_usuario[0],
             created_at))
        sqlite_connection.commit()
        return cursor.lastrowid
    except sqlite3.Error as error:
        return sqlite3.Error("Error while executing sqlite script", error)
    finally:
        if (sqlite_connection):
            sqlite_connection.close()
            print("sqlite connection is closed")


def listar_todas_coordenadas():
    try:
        query = tb_coordenadas.select().join(tb_usuario, on=tb_coordenadas.id_usuario == tb_usuario.id).execute()
        lista_coordenadas = [coordenada for coordenada in query]
        coordenadas_json = []
        for coordenada in lista_coordenadas:
            orm_json = model_to_dict(coordenada)
            coordenadas_json.append(orm_json)

        return coordenadas_json
    except:
        raise
