import requests
from .BITBOX import REST_URL

class RawTransactions:
    def decode_raw_transaction(_hex):
        if type(_hex) is str:
            response = requests.get(REST_URL+"rawtransactions/decodeRawTransaction/"+_hex)
            return response.json()
        elif type(_hex) is list:
            response = requests.post(REST_URL+"rawtransactions/decodeRawTransaction", data={"hexes": _hex})
            return response.json()
        else:
            raise TypeError("Input must be a string or array of strings.")

    def decode_script(script):
        if type(script) is str:
            response = requests.get(REST_URL+"rawtransactions/decodeScript/"+script)
            return response.json()
        elif type(script) is list:
            response = requests.post(REST_URL+"rawtransactions/decodeScript", data={"hexes": script})
            return response.json()
        else:
            raise TypeError("Input must be a string or array of strings.")

    def get_raw_transaction(txid, verbose=False):
        if type(txid) is str:
            response = requests.get(REST_URL+"rawtransactions/getRawTransaction/"+txid+"?verbose="+verbose)
            return response.json()
        elif type(txid) is list:
            response = requests.post(REST_URL+"rawtransactions/getRawTransaction", data={"txids": txid, "verbose": verbose})
            return response.json()
        else:
            raise TypeError("Input must be a string or array of strings.")

    def send_raw_transaction(_hex):
        if type(_hex) is str:
            response = requests.get(REST_URL+"rawtransactions/sendRawTransaction/"+_hex)
            if response.json() == "66: insufficient priority":
                print("""WARN: Insufficient Priority! This is likely due to a fee that is too low, or insufficient funds.
            Please ensure that there is BCH in the given wallet. If you are running on the testnet, get some
            BCH from the testnet faucet at https://developer.bitcoin.com/faucets/bch""")
            return response.json()
        elif type(_hex) is list:
            response = requests.post(REST_URL+"rawtransactions/sendRawTransaction", data={"hexes": _hex})
            return response.json()
        else:
            raise TypeError("Input hex must be a string or array of strings.")
