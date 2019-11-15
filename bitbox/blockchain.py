import requests
import json
from .BITBOX import REST_URL

class Blockchain:
    def get_best_block_hash():
        response = requests.get(REST_URL+"blockchain/getBestBlockHash")
        return response.json()

    def get_block(blockhash, verbose=True):
        response = requests.get(REST_URL+"blockchain/getBlock/"+blockhash+"?verbose="+verbose)
        return response.json()

    def get_blockchain_info():
        response = requests.get(REST_URL+"blockchain/getBlockchainInfo")
        return response.json()

    def get_block_count():
        response = requests.get(REST_URL+"blockchain/getBlockCount")
        return response.json()

    def get_block_hash(height=1):
        response = requests.get(REST_URL+"blockchain/getBlockHash/"+height)
        return response.json()

    def get_block_header(_hash, verbose=True):
        if type(_hash) is str:
            response = requests.get(REST_URL+"blockchain/getBlockHeader/"+_hash+"?verbose="+verbose)
            return response.json()
        elif type(_hash) is list:
            response = requests.post(REST_URL+"blockchain/getBlockHeader", data={"hashes": _hash, "verbose": verbose})
            return response.json()
        else:
            raise TypeError("Input hash must be a string or array of strings.")

    def get_chain_tips():
        response = requests.get(REST_URL+"blockchain/getChainTips")
        return response.json()

    def get_difficulty():
        response = requests.get(REST_URL+"blockchain/getDifficulty")
        return response.json()

    def get_mempool_ancestors(txid, verbose=False):
        if type(txid) is not str:
            txid = json.dumps(txid)
        response = requests.get(REST_URL+"blockchain/getMempoolAncestors/"+txid+"?verbose="+verbose)
        return response.json()

    def get_mempool_descendants(txid, verbose=False):
        if type(txid) is not str:
            txid = json.dumps(txid)
        response = requests.get(REST_URL+"blockchain/getMempoolDescendants/"+txid+"?verbose="+verbose)
        return response.json()

    def get_mempool_entry(txid):
       if type(txid) is str:
           response = requests.get(REST_URL+"blockchain/getMempoolEntry/"+txid)
           return response.json()
       elif type(txid) is list:
           response = requests.post(REST_URL+"blockchain/getMempoolEntry", data={"txids": txid})
           return response.json()
       else:
           raise TypeError("Input must be a string or array of strings.")

    def get_mempool_info():
        response = requests.get(REST_URL+"blockchain/getMempoolInfo")
        return response.json()

    def get_raw_mempool(verbose=False):
        response = requests.get(REST_URL+"blockchain/getRawMempool?verbose="+verbose)
        return response.json()

    def get_tx_out(txid, n, include_mempool=True):
        response = requests.get(REST_URL+"blockchain/getTxOut/"+txid+"/"+str(n)+"?include_mempool="+include_mempool)
        return response.json()

    def get_tx_out_proof(txids):
        if type(txids) is str:
            response = requests.get(REST_URL+"blockchain/getTxOutProof/"+txids)
            return response.json()
        elif type(txids) is list:
            response = requests.post(REST_URL+"blockchain/getTxOutProof", data={"txids": txids})
            return response.json()
        else:
            raise TypeError("Input must be a string or array of strings.")

    def precious_block(blockhash):
        response = requests.get(REST_URL+"blockchain/preciousBlock/"+blockhash)
        return response.json()

    def prune_blockchain(height):
        response = requests.post(REST_URL+"blockchain/pruneBlockchain/"+str(height))
        return response.json()

    def verify_chain(checklevel=3, nblocks=6):
        response = requests.get(REST_URL+"blockchain/verifyChain?checklevel="+checklevel+"$nblocks="+nblocks)
        return response.json()

    def verify_tx_out_proof(proof):
        if type(proof) is str:
            response = requests.get(REST_URL+"blockchain/verifyTxOutProof/"+proof)
            return response.json()
        elif type(proof) is list:
            response = requests.post(REST_URL+"blockchain/verifyTxOutProof", data={"proofs": proof})
            return response.json()
        else:
            raise TypeError("Input must be a string or array of strings.")
