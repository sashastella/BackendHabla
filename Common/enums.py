from enum import Enum


class RequestType(Enum):
    POST = 1
    PUT = 2
    GET = 3
    DELETE = 4


class Status(Enum):
    ACTIVO = 1
    INACTIVO = 0