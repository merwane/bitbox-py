import requests
from .BITBOX import REST_URL

class Transaction:
    def details(txid):
        if type(txid) is str:
            response = requests.get(REST_URL+"transaction/details/"+txid)
            return response.json()
        elif type(txid) is list:
            response = requests.post(REST_URL+"transaction/details", data={"txids": txid})
            return response.json()
        else:
            raise TypeError("Input txid must be a string or array of strings.")
