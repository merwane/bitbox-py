import requests
from .BITBOX import REST_URL

class CashAccounts:
    def lookup(account, number, collision):
        response = requests.get(REST_URL+"cashAccounts/lookup/"+account+"/"+str(number)+"/"+str(collision))
        return response.json()
    def check(account, number):
        response = requests.get(REST_URL+"cashAccounts/check/"+account+"/"+str(number))
        return response.json()
    def reverse_lookup(cashAddress):
        response = requests.get(REST_URL+"cashAccounts/reverseLookup/"+cashAddress)
        return response.json()
