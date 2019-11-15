import hashlib
import secrets

class Crypto:
    def sha1(_str):
        data = hashlib.sha1(_str).digest()
        return data

    def sha256(_str):
        data = hashlib.sha256(_str).digest()
        return data

    def ripemd160(_str):
        data = hashlib.new('ripemd160', _str).digest()
        return data
    
    def hash256(_str):
        data = sha256(sha256(_str))
        return data

    def hash160(_str):
        data = ripemd160(sha256(_str))
        return data

    def random_bytes(number):
        data = secrets.token_bytes(number)
        return data
