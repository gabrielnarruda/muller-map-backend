import peewee

from swagger_server.models.base_model import BaseModel
from swagger_server.models.usuarios_model import tb_usuario


class tb_coordenadas(BaseModel):
    id = peewee.IntegerField()
    nm_local = peewee.TextField()
    lat = peewee.FloatField()
    lon = peewee.FloatField()
    indice_radiacao = peewee.FloatField()
    id_usuario = peewee.ForeignKeyField(tb_usuario, column_name='id_usuario')
    created_at = peewee.DateField()