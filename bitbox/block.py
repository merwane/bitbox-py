import requests
from .BITBOX import REST_URL

class Block:
    def details_by_height(_id):
        if type(_id) is int:
            response = requests.get(REST_URL+"block/detailsByHeight/"+str(_id))
            return response.json()
        elif type(_id) is list:
            response = requests.post(REST_URL+"block/detailsByHeight", data={"heights": _id})
            return response.json()
        else:
            raise TypeError("Input must be a number or array of numbers.")

    def details_by_hash(_hash):
        if type(_hash) is str:
            response = requests.get(REST_URL+"block/detailsByHash/"+_hash)
            return response.json()
        elif type(_hash) is list:
            response = requests.get(REST_URL+"block/detailsByHash", data={"hashes": _hash})
            return response.json()
        else:
            raise TypeError("Input must be a string or array of strings.")

