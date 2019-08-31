from enum import Enum


class StatusCode(Enum):
    SUCCESS = {'status': 'Ok'}
    ERR_NOT_ALLOWED = {'status': 'Error', 'message': 'Not allowed'}
    ERR_AUTH = {'status': 'Error', 'message': 'Wrong credentials'}
