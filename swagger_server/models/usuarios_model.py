import peewee

from swagger_server.models.base_model import BaseModel


class tb_usuario(BaseModel):
    id = peewee.IntegerField()
    usuario = peewee.TextField()
    senha = peewee.TextField()
    nome = peewee.TextField()
    instituicao = peewee.TextField()
    email = peewee.TextField()
    created_at = peewee.DateField()
