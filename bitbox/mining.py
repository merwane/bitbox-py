import requests
from .BITBOX import REST_URL

class Mining:
    def get_block_template(template_request):
        response = requests.get(REST_URL+"mining/getBlockTemplate/"+template_request)
        return response.json()

    def get_mining_info():
        response = requests.get(REST_URL+"mining/getMiningInfo")
        return response.json()

    def get_network_hashps(nblocks=120, height=1):
        response = requests.get(REST_URL+"mining/getNetworkHashps?nblocks="+nblocks+"&height="+height)
        return response.json()

    def submit_block(_hex, parameters):
        path = REST_URL+"mining/submitBlock/"+_hex
        if parameters != None:
            path = path+"?parameters="+parameters
        response = requests.post(path)
        return response.json()
