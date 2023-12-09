import datetime
import requests
import json
from urllib.parse import urlparse
import requests

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