import peewee

from swagger_server.models.base_model import BaseModel
from swagger_server.models.usuarios_model import tb_usuario


class tb_coordenadas(BaseModel):
    id = peewee.IntegerField()
    nm_local = peewee.TextField()
    lat = peewee.DecimalField()
    lon = peewee.DecimalField()
    indice_radiacao = peewee.DecimalField()
    id_usuario = peewee.ForeignKeyField(tb_usuario, 'id')
    created_at = peewee.DateField()