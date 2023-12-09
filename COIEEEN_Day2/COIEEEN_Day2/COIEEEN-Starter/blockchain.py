import datetime
import requests
import json
from urllib.parse import urlparse
import requests
import hashlib

class Blockchain:

    def __init__(self):
        self.chain = []
        self.transactions = []
        self.create_block(proof=1 , previous_hash='0', block_hash='0')


    def create_block(self, proof, previous_hash, block_hash):
        block = {
            'index' : len(self.chain),
            'timestamp' : str(datetime.datetime.now()),
            'transactions' : self.transactions,
            'proof' : proof,
            'previous_hash':previous_hash,
            'block_hash' : block_hash,
        }
        self.transactions = []
        self.chain.append(block)
        return block

    def get_previous_block(self):
        return self.chain[-1]

    def add_transaction(self, sender, receiver, amount):
        self.transactions.append({'sender' : sender,
                                  'receiver' : receiver,
                                  'amount' : amount})
        previous_block = self.get_previous_block()
        return previous_block['index']+1

    def proof_of_work(self,previous_prof):
        new_proof=1
        check_proof=False
        while check_proof is False:
            hash_operation=hashlib.sha256(str(new_proof**2 - previous_prof**2).encode()).hexdigest()
            if hash_operation[:4]=='0000':
                check_proof=True
            else:
                new_proof+=1
            return new_proof

    def is_chain_valid(self,chain):
        previous_block=chain[0]
        block_index=1
        while block_index<len(chain):
            block=chain[block_index]
            if block['previous_hash']!= previous_block['block_hash']:
                return False

            previous_proof=previous_proof['proof']
            proof=block['proof']
            hash_operation=hashlib.sha256(str(proof**2- previous_proof**2).encode()).hexdigest()
            if hash_operation[:4]!='0000':
                return False

            previous_block=block
            block_index+=1
        return True


