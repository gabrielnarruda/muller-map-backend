import json
from flask import Response


class ApiBaseException(Exception):
    status_code = 500
    message = None
    payload = None
    detail = None

    def __init__(self, message, detail=None, payload=None):
        Exception.__init__(self)
        self.message = message
        self.payload = payload
        self.detail = detail


def generic_render(exception: ApiBaseException):
    return Response(
        response=json.dumps(
            {"message": exception.message, "payload": exception.payload, "detail": exception.detail}
        ),
        status=exception.status_code,
        mimetype="application/json",
    )


class Unauthorized(ApiBaseException):
    status_code = 401
    message = "Não autorizado, token inválido ou inexistente"

    def __init__(self, message=None, payload=None):
        self.message = message if message is not None else self.message
        ApiBaseException.__init__(self, self.message, payload)
