from swagger_server.configuration.data_mock import data
from swagger_server.views.produtos_view import listar_produtos, listar_produto_por_id


def get_produto_por_id(id_produto):  # noqa: E501
    """Retorna produto por ID

    Retorna produto por ID # noqa: E501

    :param id_produto: Busca por tabela_origem_dominio do domínio
    :type id_produto: int

    :rtype: Produto
    """
    return listar_produto_por_id(id_produto)


def get_lista_produtos(black_friday=None):  # noqa: E501
    """Retorna lista de produtos completa

    Retorna lista de produtos completa # noqa: E501

    :param black_friday: Busca por produtos que fazem parte da Black Friday
    :type black_friday: bool

    :rtype: ProdutoVO
    """
    return listar_produtos(black_friday)
