from passlib.context import CryptContext


class Hash():
    def bcrypt(password: str):
        return CryptContext(schemes=['bcrypt'], deprecated='auto').hash(password)
