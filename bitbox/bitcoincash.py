from bitcash.network import currency_to_satoshi, satoshi_to_currency

class BitcoinCash:
    def to_satoshi(coins):
        return currency_to_satoshi(coins, 'bch')
    
    def to_bitcoincash(coins):
        return satoshi_to_currency(coins, 'bch')
    
    def to_bits(coins):
        return satoshi_to_currency(coins, 'mbch')
    
    def from_bits(coins):
        return currency_to_satoshi(coins, 'mbch')

