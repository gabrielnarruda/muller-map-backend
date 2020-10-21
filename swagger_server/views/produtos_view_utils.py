import json


def query_filter_lista_de_produtos(query, black_friday):
    lista_de_produtos = []
    if black_friday:
        for row in query:
            json_data = json.loads(row.json_data)
            if json_data.get('flag_blackfriday') == 1:
                produto = {
                    row.id: json_data
                }
                lista_de_produtos.append(produto)

            else:
                continue
    else:
        for row in query:
            json_data = json.loads(row.json_data)
            produto = {
                row.id: json_data
            }
            lista_de_produtos.append(produto)

    return lista_de_produtos
