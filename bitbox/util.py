import requests
from .BITBOX import REST_URL

# validate an address format
class Util:
    def validate_address(address):
        if type(address) is str:
            response = requests.get(REST_URL+"util/validateAddress/"+address)
            return response.json()
        elif type(address) is list:
            response = requests.post(REST_URL+"util/validateAddress", data={"addresses": address})
            return response.json()
        else:
            raise TypeError("Input must be a string or array of strings.")

