import re

import connexion
from flask import g


from swagger_server.configuration.exceptions import Unauthorized
from swagger_server.configuration.signal import unauthorized_hook

chave_autenticacao = "x-api-key"





def before_request():
    g.username = ""

    allowed_urls = [
        "/v2/ui",
        "/v2/ui/",
        "/v2/swagger.json",
        "/v2/ping",
        "/v2/ping/",
    ]

    if connexion.request.method == 'OPTIONS':
        return

    print(f"Verificando se a url precisa de autorizacao")

    for allowed_url in allowed_urls:
        if re.match(allowed_url, connexion.request.path):
            print(f"Url nao precisa de autorizacao")
            return

    x_api_key = connexion.request.headers.get("x-api-key")
    if x_api_key is None or x_api_key!=chave_autenticacao:
        unauthorized_hook.send()
        raise Unauthorized


@unauthorized_hook.connect
def sinal_nao_autorizado(identity=None,**kwargs):
    return print("Sinal de LOGIN NAO AUTORIZADO enviado")
