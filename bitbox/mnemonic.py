import os
import sys
import hashlib
import binascii
import hmac
import unicodedata
from pywallet import wallet
from bitcash import Key

def b58encode(v):
    alphabet = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"
    p, acc = 1, 0
    for c in reversed(v):
        if sys.version < "3":
            c = ord(c)
        acc += p * c
        p = p << 8

    string = ""
    while acc:
        acc, idx = divmod(acc, 58)
        string = alphabet[idx : idx + 1] + string
    return string

class Mnemonic:
    def __init__(self, language):
        self.radix = 2048
        with open("%s/%s.txt" % (self._get_directory(), language), "r", encoding="utf-8") as f:
            self.wordlist = [w.strip() for w in f.readlines()]
        if len(self.wordlist) != self.radix:
            raise ConfigurationError("Wordlist should contain %d words, but it contains %d words." % (self.radix, len(self.wordlist)))
    
    @classmethod
    def _get_directory(cls):
        return os.path.join(os.path.dirname(__file__), "wordlist")

    def generate(self, strength=128):
        if strength not in [128, 160, 192, 224, 256]:
            raise ValueError("Strength should be one of the following [128, 160, 192, 224, 256], but it is not (%d)." % strength)
        return self.to_mnemonic(os.urandom(strength // 8))

    def to_mnemonic(self, data):
        if len(data) not in [16, 20, 24, 28, 32]:
            raise ValueError("Data length should be one of the following: [16, 20, 24, 28, 32], but it is not (%d)." % len(data))
        h = hashlib.sha256(data).hexdigest()
        b = (
        bin(int(binascii.hexlify(data), 16))[2:].zfill(len(data) * 8)
        + bin(int(h, 16))[2:].zfill(256)[: len(data) * 8 // 32]
        )
        result = []
        for i in range(len(b) // 11):
            idx = int(b[i * 11 : (i + 1) * 11], 2)
            result.append(self.wordlist[idx])
        result_phrase = " ".join(result)
        return result_phrase
    
    @classmethod
    def normalize_string(cls, txt):
        if isinstance(txt, str if sys.version < "3" else bytes):
            utxt = txt.decode("utf-8")
        elif isinstance(txt, unicode if sys.version < "3" else str):
            utxt = txt
        else:
            raise TypeError("String value expected")
        return unicodedata.normalize("NFKD", utxt)

    @classmethod
    def to_seed(cls, mnemonic, passphrase=""):
        mnemonic = cls.normalize_string(mnemonic)
        passphrase = cls.normalize_string(passphrase)
        passphrase = "mnemonic"+passphrase
        mnemonic = mnemonic.encode("utf-8")
        passphrase = passphrase.encode("utf-8")
        stretched = hashlib.pbkdf2_hmac("sha512", mnemonic, passphrase, 2048)
        return stretched[:64]
    
    @classmethod
    def to_hd_master_key(cls, seed):
        if len(seed) != 64:
            raise ValueError("Provided seed should have length of 64")
        seed = hmac.new(b"Bitcoin seed", seed, digestmod=hashlib.sha512).digest()
        xprv = b"\x04\x88\xad\xe4"
        xprv += b"\x00" * 9
        xprv += seed[32:]
        xprv += b"\x00" + seed[:32]

        hashed_xprv = hashlib.sha256(xprv).digest()
        hashed_xprv = hashlib.sha256(hashed_xprv).digest()

        xprv += hashed_xprv[:4]

        # return base58
        return b58encode(xprv)

    @classmethod
    def to_key_pairs(cls, mnemonic):
        w = wallet.create_wallet(network="bch", seed=mnemonic, children=1)
        wif = w['wif']
        key = Key(wif)
        address = key.address
        keypair = {"private_key_WIF": wif, "address": address}
        return keypair
