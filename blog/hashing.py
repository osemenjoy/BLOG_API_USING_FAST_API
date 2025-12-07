from passlib.context import CryptContext

pwd_cxt = CryptContext(schemes=['argon2'], deprecated="auto")

class Hashing():
    def bcrypt(password: str):
        hashed_password = pwd_cxt.hash(password)

        return hashed_password
