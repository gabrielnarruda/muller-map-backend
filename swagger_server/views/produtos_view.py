from swagger_server.models.produtos_model import tb_produto
import json

from swagger_server.views.produtos_view_utils import query_filter_lista_de_produtos


def listar_produtos(black_friday=None):
    try:

        query = tb_produto.select()

        lista_de_produtos = query_filter_lista_de_produtos(query, black_friday)
        return lista_de_produtos
    except:
        raise


def listar_produto_por_id(id_produto):
    try:

        query = tb_produto.get(tb_produto.id == id_produto)

        produto = query.get()

        return json.loads(produto.json_data)
    except:
        raise
