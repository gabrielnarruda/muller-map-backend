from swagger_server.views.coordenadas_view import insert_nova_coordenada, listar_todas_coordenadas


def post_cria_coordenada(coordenada):
    id_coordenada = insert_nova_coordenada(coordenada)
    if type(id_coordenada) == int:
        coordenada['id'] = id_coordenada
        return coordenada
    else:
        return (f"Error>>> {id_coordenada}")

def get_lista_coordenadas():
    return listar_todas_coordenadas()