import os
import sys
import hashlib
import binascii
import unicodedata

class Mnemonic:
    def __init__(self, language):
        self.radix = 2048
        with open("./wordlist/%s.txt" % (language), "r", encoding="utf-8") as f:
            self.wordlist = [w.strip() for w in f.readlines()]
        if len(self.wordlist) != self.radix:
            raise ConfigurationError("Wordlist should contain %d words, but it contains %d words." % (self.radix, len(self.wordlist)))

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

