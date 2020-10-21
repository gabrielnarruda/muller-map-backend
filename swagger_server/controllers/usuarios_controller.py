from swagger_server.views.usuarios_view import insert_novo_usuario


def post_cria_usuario(usuario):
    id_usuario = insert_novo_usuario(usuario)
    usuario['id']=id_usuario
    return usuario