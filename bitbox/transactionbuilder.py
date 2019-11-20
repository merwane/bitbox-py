from bitcash import Key
from bitcash.exceptions import InsufficientFunds

class TransactionBuilder:
    def __init__(self, prkey):
        self.prkey = Key(prkey)

    def create(self, recipient, amount):
        key = self.prkey
        try:
            tx = key.send([(recipient, amount, 'satoshi')])
        except InsufficientFunds:
            tx = {"status": "error", "error": "Insufficient funds"}
        except ValueError:
            tx = {"status": "error"}
        return tx
