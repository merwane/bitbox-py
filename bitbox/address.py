import cashaddress
import requests
from .BITBOX import REST_URL
import re

class Address:
    def to_legacy_address(address):
        if not "bitcoincash:" in address:
            if "bchtest:" in address:
                pass
            else:
                address = "bitcoincash:"+address
        converted = cashaddress.convert.to_legacy_address(address)
        return converted

    def to_cash_address(address):
        converted = cashaddress.convert.to_cash_address(address)
        return converted
    
    def is_legacy_address(address):
        legacy = re.match("^([13][a-km-zA-HJ-NP-Z1-9]{25,34})", address)
        tlegacy = re.match("^([2mn][1-9A-HJ-NP-Za-km-z]{26,35})", address)
        if any([legacy, tlegacy]):
            return True
        else:
            return False
    
    def is_cash_address(address):
        cash = re.match("^((bitcoincash|bchreg|bchtest):)?(q|p)[a-z0-9]{41}$", address)
        if any([cash]):
            return True
        else:
            return False
    
    def is_mainnet_address(address):
        cash = re.match("^((bitcoincash):)?(q|p)[a-z0-9]{41}$", address)
        legacy = re.match("^([13][a-km-zA-HJ-NP-Z1-9]{25,34})", address)
        if any([cash, legacy]):
            return True
        else:
            return False
    
    def is_testnet_address(address):
        cash = re.match("^((bchtest):)?(q|p)[a-z0-9]{41}$", address)
        legacy = re.match("^([2mn][1-9A-HJ-NP-Za-km-z]{26,35})", address)
        if any([cash, legacy]):
            return True
        else:
            return False
    
    def is_regtest_address(address):
        cash = re.match("^((bchreg):)?(q|p)[a-z0-9]{41}$", address)
        if any([cash]):
            return True
        else:
            return False
    
    def detect_address_format(address):
        cash = re.match("^((bitcoincash|bchreg|bchtest):)?(q|p)[a-z0-9]{41}$", address)
        legacy = re.match("^([13][a-km-zA-HJ-NP-Z1-9]{25,34})", address)
        tlegacy = re.match("^([2mn][1-9A-HJ-NP-Za-km-z]{26,35})", address)
        if any([cash]):
            return "cashaddr"
        elif any([legacy, tlegacy]):
            return "legacy"
    
    def detect_address_network(address):
        cash = re.match("^((bitcoincash):)?(q|p)[a-z0-9]{41}$", address)
        tcash = re.match("^((bchtest):)?(q|p)[a-z0-9]{41}$", address)
        legacy = re.match("^([13][a-km-zA-HJ-NP-Z1-9]{25,34})", address)
        tlegacy = re.match("^([2mn][1-9A-HJ-NP-Za-km-z]{26,35})", address)
        if any([cash, legacy]):
            return "mainnet"
        elif any([tcash, tlegacy]):
            return "testnet"
    
    def details(address):
        if type(address) is str:
            response = requests.get(REST_URL+"address/details/"+address)
            return response.json()
        elif type(address) is list:
            response = requests.post(REST_URL+"address/details", data={"addresses": address})
            return response.json()
        else:
            raise TypeError("Input address must be a string or array of strings.")

    def utxo(address):
        if type(address) is str:
            response = requests.get(REST_URL+"address/utxo/"+address)
            return response.json()
        elif type(address) is list:
            response = requests.post(REST_URL+"address/utxo", data={"addresses": address})
            return response.json()
        else:
            raise TypeError("Input address must be a string or array of strings")

    def unconfirmed(address):
        if type(address) is str:
            response = requests.get(REST_URL+"address/unconfirmed/"+address)
            return response.json()
        elif type(address) is list:
            response = requests.post(REST_URL+"address/unconfirmed", data={"addresses": address})
            return response.json()
        else:
            raise TypeError("Input address must be a string or array of strings")

    def transactions(address):
        if type(address) is str:
            response = requests.get(REST_URL+"address/transactions/"+address)
            return response.json()
        elif type(address) is list:
            response = requests.post(REST_URL+"address/transactions", data={"addresses": address})
            return response.json()
        else:
            raise TypeError("Input address must be a string or array of strings")

