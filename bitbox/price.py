import requests

# current BCH prices in fiat
class Price:
    def current_price(currency):
        currency = currency.lower()
        try:
            price = requests.get('https://index-api.bitcoin.com/api/v0/cash/price/'+currency)
            return price.json()['price']
        except KeyError:
            raise KeyError("Invalid currency")

