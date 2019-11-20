import requests
import json
import base64
from .BITBOX import BITDB_URL

class BitDB:
    def __init__(self, bitdbURL = BITDB_URL):
        self.bitdbURL = bitdbURL

    def get(self, query):
        s = json.dumps(query)
        b64 = base64.b64encode(s.encode())
        
        url = self.bitdbURL+"q/"+str(b64, "utf-8")
        tokenres = requests.get(url)
        return tokenres.json()

