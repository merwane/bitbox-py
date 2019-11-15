import requests
from .BITBOX import REST_URL

class Control:
    def get_info():
        response = requests.get(REST_URL+"control/getInfo")
        return response.json()
    
    def get_network_info():
        response = requests.get(REST_URL+"control/getNetworkInfo")
        return response.json()
