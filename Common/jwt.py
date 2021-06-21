import jwt as jwt

from Common.key import sign_key


def decode(token):
    return jwt.decode(token, sign_key, None)