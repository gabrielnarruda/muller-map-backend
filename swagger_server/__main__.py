#!/usr/bin/env python3

import connexion

from swagger_server.configuration.exceptions import generic_render, Unauthorized
# from swagger_server.configuration.logger import create_logger
from swagger_server.configuration.context_handler import before_request

db_conn = './db_produtos.db'


# logger = create_logger()

def main():
    app = connexion.FlaskApp(__name__, specification_dir='./swagger/')
    app.add_api('swagger.yaml')
    app.add_error_handler(Unauthorized, generic_render)
    app.app.before_request(before_request)
    app.run(port=8080)


if __name__ == '__main__':
    main()
