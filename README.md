
## Overview

Para construção da API foram utilizadas as seguintes tecnologias :
Flask, como WSGI (https://flask.palletsprojects.com/en/1.1.x/)
Connexion  como gerenciador de requests (https://connexion.readthedocs.io/en/latest/)
Sqlite como banco de dados (https://docs.python.org/3/library/sqlite3.html)
Peewee como ORM (http://docs.peewee-orm.com/en/latest/)
Blinker, como sinalizador broadcast (https://pythonhosted.org/blinker/)
Swagger, como estrutura de API (https://swagger.io/docs/specification/2-0/what-is-swagger/)

Para instalar os requirements do do projeto digite no console: pip install -r requirements.txt

A API conta com 2 recursos, cujo podem ser acompanhados através da url >>http://localhost:8080/v2/ui/<<, sendo eles:

/produtos
Nesta rota é possível retornar a listagem completa de todos os produtos cadastrados no banco de dados
Esta rota também aceita,opcionalmente, o parâmetro black_friday=True, retornando assim apenas os registros do banco que contém a flag_black_friday =1

/produtos/{id_produto)
 Nesta rota é possível buscar os produtos por um id específico (Os ids registrados no banco são :87400,85197,79936)

O Mock do banco de dados é realizado no Start da API, sendo inserido os registros das URLS enviadas no email anterior na instancia local SQLite. 

Para conseguir acessar os recursos é necessário passar no cabeçalho(headers) da requisição a seguinte chave de autenticação: {x-api-key:x-api-key}
Ao enviar uma requisição para o servidor, a API foi construída para acessar e validar o evento e checará o contexto da requisição que está sendo apresentada.
Caso a chave de autenticação esteja errada, ou não exista, a API cuidará de abortar a requisição e enviar um sinal (fictício) de notificação sobre a tentativa de requisição sem autenticação.


## Requirements
Python 3.5.2+

flask
#### API requirements
werkzeug==0.16.0
connexion==1.5.3
setuptools >= 21.0.0

#### DB requirements
peewee==3.13.3

#### webhook signal
blinker==1.4

## Usage
To run the server, please execute the following from the root directory:

```
pip install -r requirements.txt
python3 -m swagger_server
```

and open your browser to here:

```
http://localhost:8080/v2/ui/
```

Your Swagger definition lives here:

```
http://localhost:8080/v1/swagger.json
```


## Running with Docker

To run the server on a Docker container, please execute the following from the root directory:

```bash
# building the image
docker build -t swagger_server .

# starting up a container
docker run -p 8080:8080 swagger_server
```